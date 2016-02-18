#from django.conf.urls import patterns, include, url
from django.conf.urls import url, include, patterns
from api.api import router
from django.contrib import admin
from health import api
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
	url(r'^api/v1/', include(router.urls)),
	url(r'^api-token-auth/','rest_framework.authtoken.views.obtain_auth_token'),
	url(r'^api-explorer/', include('rest_framework_swagger.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^', api.health),
)

if settings.DEBUG is True:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


