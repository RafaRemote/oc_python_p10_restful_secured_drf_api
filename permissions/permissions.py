from rest_framework import permissions


class ObjectPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, obj):
        try:
            if obj.author_user_id == request.user:
                return True
        except:
            return False
