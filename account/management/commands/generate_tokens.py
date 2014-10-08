from django.core.management.base import BaseCommand, CommandError
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class Command(BaseCommand):
    args = '<>'
    help = 'Generals new tokens for all users'

    def handle(self, *args, **options):
        users = User.objects.all()
        for user in users:
            token = Token.objects.create(user=user)
