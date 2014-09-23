from rest_framework import permissions

class HasRolePermission(permissions.BasePermission):

	def has_permission(self, request, view):	

		if request.user.is_authenticated():	
			return (self.required_role,) in request.user.roles.all().values_list("role_name")
		else:
			return False

class IsDirector(HasRolePermission):
    required_role = 'Director'

class IsAdministrator(HasRolePermission):
    required_role = 'Administrator'

class IsDeveloper(HasRolePermission):
    required_role = 'Developer'

class IsEmployee(HasRolePermission):
    required_role = 'Employee'


class IsSelf(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        
    	if request.user.is_authenticated():

	        if obj.__class__.__name__ == 'User':
	        	return obj.pk == request.user.pk
	        else:

	        	user_id = getattr(obj,"user_id",False)
	        	if user_id:
	        		return user_id == request.user.pk

      	return False

