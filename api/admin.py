from django.contrib import admin
from models import Role, Profile, AppAuthorization

class RoleAdmin(admin.ModelAdmin):
    pass

class ProfileAdmin(admin.ModelAdmin):
    pass

class AppAuthorizationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Role, RoleAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(AppAuthorization, AppAuthorizationAdmin)