from django.test import TestCase, Client
from django.conf import settings

import requests 
import responses


def mock_auth_success():

	url = '/health/'	
	responses.add(responses.GET, url,
              status=200,
              content_type='application/json')


class HealthTestCase(TestCase):

	def test_health_returns_useful_information(self):

		response = self.client.get('/health/')
		self.assertEqual(response.data, {"name": "UserService", "explorer_url": "/api-explorer/","version": settings.VERSION})