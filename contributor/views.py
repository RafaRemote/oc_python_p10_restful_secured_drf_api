from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from custom_permissions.permissions import IsProjectOwner
from .serializers import ContributorSerializer
from .models import Contributor
from project.models import Project
from django.shortcuts import get_object_or_404


class ContributorViewSet(ModelViewSet):

    serializer_class = ContributorSerializer
    permission_classes = (IsProjectOwner, )

    def get_queryset(self):
        queryset = Contributor.objects.filter(project_id=self.kwargs['project_pk'])
        return queryset

    def create(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.kwargs['project_pk'])
        if int(request.POST['user_id']) == request.user.id:
            request.POST._mutable = True
            request.data["permission"] = 'AUTHOR'
            request.data["project_id"] = project.id
            request.POST_mutable = False
        else:
            request.POST._mutable = True
            request.data["permission"] = 'CONTRIBUTOR'
            request.data["project_id"] = project.id
            request.POST._mutable = False
        project_contributors = Contributor.objects.filter(project_id=request.POST['project_id'])
        project_contributors_id = [i.user_id.id for i in project_contributors]
        if int(request.POST['user_id']) in project_contributors_id:
            return Response(
                            {"status": "this contributor already exists for this project"},
                            status=status.HTTP_400_BAD_REQUEST
                            )
        return super(ContributorViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        project = get_object_or_404(Contributor, pk=self.kwargs['pk'])
        project.delete()
        return Response(
            {"status": f"success: the {self.__class__.__name__.replace('ViewSet', '')} does no more exist"},
            status=status.HTTP_204_NO_CONTENT
            )
