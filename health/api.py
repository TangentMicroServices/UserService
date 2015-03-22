from rest_framework import routers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.conf import settings

@api_view(['GET'])
@permission_classes((AllowAny,))
def health(request):

	json = {
		'version': settings.VERSION,
		'name': "UserService"
	}
	
	return Response(json)

router = routers.DefaultRouter()
