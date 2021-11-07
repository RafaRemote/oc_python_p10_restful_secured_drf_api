from rest_framework.viewsets import ModelViewSet
from .serializers import ProjectSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Project
from custom_permissions.permissions import IsObjOwner
from django.shortcuts import get_object_or_404


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsObjOwner, )

    def get_queryset(self):
        print(self.request.user.id)
        queryset = Project.objects.filter(author_user_id=self.request.user.id)
        return queryset

    def perform_create(self, serializer):
        serializer.save(author_user_id=self.request.user)

    def destroy(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.kwargs['pk'])
        project.delete()
        return Response(
            {"status": f"success: the {self.__class__.__name__.replace('ViewSet', '')} does no more exist"},
            status=status.HTTP_204_NO_CONTENT
            )
