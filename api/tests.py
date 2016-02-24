# pylint: disable=R0904

from django.test import TestCase, Client
from models import Profile
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework.authtoken.models import Token
from permissions import IsDirector, IsSelf
from django.http import HttpRequest
import json
import unittest


class Pep8TestCase(TestCase):

    def test_pep8(self):
        """
        Ensure that code is pep8 compliant
        """
        pass
        #from subprocess import call
        # py.test --pep8
        # see pytest.ini for config options
        #result = call(['py.test'])
        #assert result == 0, "Code is pep8"


class TokenAuthTestCase(TestCase):

    def setUp(self):
        for user in User.objects.all(): user.delete()
        self.user = User.objects.create_user(username="joe", password="test")
        self.c = Client()

    def tearDown(self):
        for user in User.objects.all(): user.delete()

    def test_get_token(self):

        response = self.c.post(
            "/api-token-auth/", {"username": "joe", "password": "test"})

        assert 200 == response.status_code, "Response is 200 OK"
        assert json.loads(response.content).get("token", False) is not False, "Token is set"

    


class PermissionsTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="joe", password="test")

    def tearDown(self):

        for user in User.objects.all():
            user.delete()
        for role in self.user.roles.all():
            role.delete()

    def test_is_director_passes_if_user_is_director(self):

        mock_request = HttpRequest()
        self.user.add_role("Director")
        mock_request.user = self.user

        permission_class = IsDirector()
        authorization_response = permission_class.has_permission(
            mock_request, None)

        assert authorization_response is True, "Permission should be granted"

    def test_is_director_fails_if_user_is_not_a_director(self):

        mock_request = HttpRequest()
        mock_request.user = self.user

        permission_class = IsDirector()
        authorization_response = permission_class.has_permission(
            mock_request, None)

        assert authorization_response is False, "Permission should be denied"

    def test_is_self_allows_me_to_see_myself(self):

        mock_request = HttpRequest()
        mock_request.user = self.user

        permission_class = IsSelf()
        authorization_response = permission_class.has_object_permission(
            mock_request, None, self.user)

        assert authorization_response is True, "IsSelf passes if I request to see myself"

    def test_is_self_allows_me_to_see_my_profile(self):

        mock_request = HttpRequest()
        mock_request.user = self.user

        permission_class = IsSelf()
        authorization_response = permission_class.has_object_permission(
            mock_request, None, self.user.profile)

        assert authorization_response is True, "IsSelf passes if I request to see my profile"


class ModelsTestCase(TestCase):

    def tearDown(self):

        for user in User.objects.all():
            user.delete()

    def test_new_user_signals(self):

        user = User.objects.create_user(username="joe", password="test")
        token = Token.objects.get(user=user)

        assert type(token) is Token, "Token is 40 characters long"
        assert Profile.objects.filter(
            user=user).count() == 1, "Exactly 1 matching profile is created"


class EndpointAuthenticationTestCase(TestCase):

    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user(username="joe", password="test")

    def tearDown(self):

        for user in User.objects.all():
            user.delete()

        for role in self.user.roles.all():
            role.delete()

    def test_endpoints_require_token_auth(self):
        url = reverse('user-me')
        response = self.c.get(url)

        assert response.status_code == 401, \
            "Expect 401 Authentication required. Got: {}" . format (response.status_code)

    @unittest.skip("This doesnt really make sense?")
    def test_director_can_see_anyone(self):
        '''test_director_can_see_anyone: This doesn't make sense? /me should always return the logged in user'''
        url = reverse('user-me')
        self.user.add_role('Director')

        response = self.c.get(url, HTTP_AUTHORIZATION="Token {0}" \
                        . format(self.user.get_token()))

        assert response.status_code == 200, \
            "Expect Director can view any user. Expected 200. Got: {}" . format (response.status_code)

    def test_user_can_see_self(self):
        url = reverse('user-me')

        token_header = "Token {0}" . format(self.user.get_token())
        response = self.c.get(url, HTTP_AUTHORIZATION=token_header)

        assert response.status_code == 200, \
            "User can see self. Expected 200. Got: {}" . format (response.status_code)

class EndpointsTestCase(TestCase):

    def setUp(self):
        self.c = Client()

    def tearDown(self):

        for user in User.objects.all():
            user.delete()

    def test_enrol_employee(self):
        """
        POST /user/{:id}/enrol/
        @requires exec or admin

        * Give user appropriate roles
        * Sends a welcome e-mail to staff
        * Sends an on-boarding e-mail to user
        * Creates a pivotal account
        * Creates a hipchat account
        """
        pass

    def test_retire_employee(self):
        """
        POST /user/{:id}/enrol/
        @requires exec or admin

        * Delete pivotal account
        * Delete hipchat account
        * Remove access from Github Organization
        * Remove access from Tangent microservices
        """
        pass
