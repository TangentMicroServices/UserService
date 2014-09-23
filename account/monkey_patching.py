from django.contrib.auth.models import User 
from account.models import Role
from rest_framework.authtoken.models import Token

def add_role(self, role_name):

    if self.is_authenticated():
        role, created = Role.objects.get_or_create(role_name=role_name)
        self.roles.add(role)

def get_token(self):

    if self.is_authenticated():
        return Token.objects.get(user=self).key
    return None
    

User.add_to_class("add_role",add_role)
User.add_to_class("get_token",get_token)