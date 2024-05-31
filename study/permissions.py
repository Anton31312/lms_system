from rest_framework.permissions import BasePermission


class IsStaff(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        
class IsOwner(BasePermission):

    def has_permission(self, request, view):
        if request.user == view.get_object().owner:
            return True
        