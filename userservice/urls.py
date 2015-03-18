from django.conf.urls import patterns, include, url
from api.api import router
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^', include(router.urls)),
	url(r'^api-token-auth/',
	   'rest_framework.authtoken.views.obtain_auth_token'),

	url(r'^api-explorer/', include('rest_framework_swagger.urls')),

	# url(r'^$', 'userService.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	url(r'^admin/', include(admin.site.urls)),
	)
