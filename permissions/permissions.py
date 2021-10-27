from rest_framework import permissions
from contributor.models import Contributor


class ProjectPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        object_id = view.kwargs.get("pk")
        try:
            if obj.author_user_id == request.user:
                return True
            elif Contributor.objects.get(user_id=request.user, project=object_id):
                return request.method in ["GET"]
            else:
                return False
        except:
            return False
