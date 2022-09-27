from rest_framework.authentication import BaseAuthentication

class CustomPermission(BaseAuthentication):
    
    def has_permission(self,request,view):
        user = request.user
        if request.method == "GET" or request.method == "POST":
            if user.is_superuser:
                return True
        return False