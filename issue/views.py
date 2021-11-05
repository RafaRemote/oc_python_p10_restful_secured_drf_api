from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializers import IssueSerializer
from django.shortcuts import get_object_or_404
from .models import Issue
from project.models import Project
from custom_permissions.permissions import IsProjectOnwerOrContributor


class IssueViewSet(ModelViewSet):

    serializer_class = IssueSerializer
    permission_classes = (IsProjectOnwerOrContributor, )

    def get_queryset(self):
        print('wvw;vnmwv;m')
        print('wvw;vnmwv;m')
        print('wvw;vnmwv;m')
        project = get_object_or_404(Project, pk=self.request.parser_context['kwargs']['project_pk'])
        print(project.id)
        queryset = Issue.objects.filter(project_id=project.id)
        return queryset

    def create(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.request.parser_context['kwargs']['project_pk'])
        issue = Issue.objects.filter(
                                     title=request.POST['title'],
                                     project_id=project.id
                                     )
        if len(issue) == 0:
            request.POST._mutable = True
            request.data["project_id"] = project.id
            request.data["assignee_user_id"] = request.user.id
            request.POST_mutable = False
            return super(IssueViewSet, self).create(request, *args, **kwargs)
        else:
            return Response(
                            {"status": "An issue with the same title for the same project does already exist"},
                            status=status.HTTP_400_BAD_REQUEST
                            )
