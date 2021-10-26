from rest_framework import permissions
from contributor.models import Contributor


class ProjectPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        query_project = view.kwargs.get("pk")
        try:
            if obj.author_user_id == request.user:
                return True
            elif Contributor.objects.get(user_id=request.user, project=query_project):
                return request.method in ["GET"]
            else:
                return False
        except:
            return False


# from rest_framework import viewsets, permissions
# from .models import Projects
# from .serializers import ProjectSerializer
# from .permission import ProjectPermission


# class ProjectViewSet(viewsets.ModelViewSet):

#     permission_classes = [permissions.IsAuthenticated & ProjectPermission]
#     queryset = Projects.objects.all()
#     serializer_class = ProjectSerializer

#     def perform_create(self, serializer):
#         serializer.save(author_project=self.request.user)

