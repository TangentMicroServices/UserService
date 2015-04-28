from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import routers, serializers, viewsets
from rest_framework.authentication import TokenAuthentication
from permissions import IsSelfOrDirector
from models import Profile, AppAuthorization, Role
from rest_framework.decorators import list_route, detail_route
import json
from datetime import datetime
from rest_framework.permissions import IsAuthenticated

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        exclude = ('user', 'id',)


class AppAuthorizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppAuthorization
        exclude = ('user',)


# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):

    profile = ProfileSerializer(read_only=True)
    authentications = AppAuthorizationSerializer(read_only=True, many=True)
    roles = serializers.RelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email',
                  'is_staff', 'is_superuser', 'profile', 'authentications', 'roles',)
        # read_only_fields = ('roles',)
        depth = 1


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = (IsSelfOrDirector,)
    permission_classes = (IsAuthenticated,)

    @list_route(methods=['get', 'post'])
    def me(self, request):

        # ensure they have permissions to see this user
        self.check_object_permissions(self.request, request.user)

        serializer = UserSerializer(request.user)
        response = json.dumps(serializer.data)

        return HttpResponse(response, content_type="application/json")

    #@detail_route(methods=['post'])
    #def grant(self, request):

    #    user_id = request.POST.get("id")
    #    role = request.POST.get("role")

    #@detail_route(methods=['post'])
    #def revoke(self, request):

     #   user_id = request.POST.get("id")
     #   role = request.POST.get("role")


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class AppAuthorizationViewSet(viewsets.ModelViewSet):
    queryset = AppAuthorization.objects.all()
    serializer_class = AppAuthorizationSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
# router.register(r'profiles', ProfileViewSet)
# router.register(r'apps', AuthenticationViewSet)