# Monkey patching is a way to add additional functionality to the user module

# pylint: disable=E1101
# pylint: disable=C0111

from django.contrib.auth.models import User
from models import Role
from rest_framework.authtoken.models import Token


