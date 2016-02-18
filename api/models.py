from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from rest_framework.authtoken.models import Token

class Role(models.Model):

    def __unicode__(self):
        return self.role_name

    user = models.ManyToManyField(User, related_name='roles')
    role_name = models.CharField(
        max_length=20, help_text='Describes a role that this user has',
        choices=settings.USER_ROLES)


class Profile(models.Model):

    """
    Additional data about a user
    """

    user = models.OneToOneField(User)
    # token = models.CharField(max_length=36, default=str(uuid.uuid4()))
    contact_number = models.CharField(max_length=20)
    status_message = models.CharField(
        max_length=144, help_text='Twitter style status message', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)


class AppAuthorization(models.Model):

    """
    Collection of authentication tokens/keys for various services
    """

    user = models.ForeignKey(User, related_name='authentications')
    service_name = models.CharField(
        max_length=20, help_text='Service such as pivotal, hipchat, .. etc')
    key = models.CharField(max_length=200, blank=True, null=True,
                           help_text='Optional, typically your API_KEY value')
    token = models.CharField(
        max_length=200, blank=True, null=True, help_text='Optional, this is your token or secret')


## monkey patching:
def add_role(self, role_name):

    if self.is_authenticated():
        role, created = Role.objects.get_or_create(
            role_name=role_name)  # pylint: disable=W0612
        self.roles.add(role)


def has_role(self, role_name):

    if self.is_authenticated():

        return (role_name,) in self.roles.all().values_list("role_name")

    return False


def get_token(self):

    if self.is_authenticated():
        return Token.objects.get(user=self).key
    return None


User.add_to_class("add_role", add_role)
User.add_to_class("has_role", has_role)
User.add_to_class("get_token", get_token)


from signals import new_user_created
