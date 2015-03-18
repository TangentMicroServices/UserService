from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):

	help = "Create default users"

	def handle(self, *args, **options):
	
		#clear all data
		for user in User.objects.all():
			user.delete()

		admin_users = ['admin']

		User.objects.create_user(** {
			'email': 'admin@tangentsolutions.co.za',
			'password': 'tangentsolutions',
			'first_name': 'Tangent',
			'last_name': 'Solutions',
			'username': admin_users[0]
		})

		for user in User.objects.all():
			if user.username in admin_users:
				user.is_superuser = True
				user.is_staff = True

			user.save()
			
		print('created user admin')
