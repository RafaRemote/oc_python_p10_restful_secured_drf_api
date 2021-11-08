from rest_framework.viewsets import ModelViewSet
from .serializers import ProjectSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Project
from contributor.models import Contributor
from custom_permissions.permissions import IsProjectOnwerOrContributor
from django.shortcuts import get_object_or_404


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsProjectOnwerOrContributor, )

    def get_queryset(self):
        contributings = [i.project_id for i in Contributor.objects.filter(user_id=self.request.user)]
        queryset = Project.objects.filter(author_user_id=self.request.user.id)
        if len(queryset) > 0:
            return queryset
        else:
            return contributings

    def retrieve(self, request, *args, **kwargs):
        print('on cherche:', kwargs['pk'])
        project = get_object_or_404(Project, id=kwargs['pk'])

        return Response(ProjectSerializer(project).data)

    def perform_create(self, serializer):
        serializer.save(author_user_id=self.request.user)

    def destroy(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.kwargs['pk'])
        project.delete()
        return Response(
            {"status": f"success: the {self.__class__.__name__.replace('ViewSet', '')} does no more exist"},
            status=status.HTTP_204_NO_CONTENT
            )
