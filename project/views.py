from rest_framework.viewsets import ModelViewSet
from .serializers import ProjectSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Project
from custom_permissions.permissions import IsProjectOwner
from django.shortcuts import get_object_or_404


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsProjectOwner, )

    def get_queryset(self):
        queryset = Project.objects.filter(author_user_id=self.request.user.id)
        return queryset

    def perform_create(self, serializer):
        serializer.save(author_user_id=self.request.user)

    def destroy(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.kwargs['pk'])
        project.delete()
        return Response({"status": "success: the project does no more exist"}, status=status.HTTP_204_NO_CONTENT)
