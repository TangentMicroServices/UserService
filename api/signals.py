from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from models import Profile
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=User)
def new_user_created(sender, instance, **kwargs):

    if kwargs.get("created", False):
        token = Token.objects.create(user=instance)
        Profile.objects.create(user=instance)

        # put a message on the queue

    
