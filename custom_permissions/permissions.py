"""Custom permissions"""

from rest_framework.permissions import BasePermission
from project.models import Project
from issue.models import Issue
from comment.models import Comment
from contributor.models import Contributor
from django.shortcuts import get_object_or_404


class IsProjectOwner(BasePermission):
    """Checks if the User is the Project's Owner"""

    def has_permission(self, request, view):
        """Gives permission to Project's author

        Searches the Project concerned by the request.
        Checks if the request.user is the owner of the Project.

        Returns:
            Boolean.
        """

        project = get_object_or_404(Project, pk=view.kwargs['project_pk'])
        if request.user == project.author_user_id:
            return True
        else:
            return False


class IsProjectOnwerOrContributor(BasePermission):
    """Checks if the User is the Project's Owner or Contributor"""

    def has_permission(self, request, view):
        """Gives permission to access objects



        Returns:
            Boolean.
        """

        allowed_actions = ['create', 'list']
        if view.action in allowed_actions and view.basename == 'projects':
            return True

        allowed_actions = ['list', 'create', 'retrieve']
        alllowed_basenames = ['issue', 'comment', 'user', 'projects']

        if view.action in allowed_actions and view.basename in alllowed_basenames:
            try:
                project = get_object_or_404(Project, pk=view.kwargs['project_pk'])
            except KeyError:
                project = get_object_or_404(Project, pk=view.kwargs['pk'])
            request_user_projects = [project for project in Project.objects.filter(author_user_id=request.user)]
            contributors = [i.user_id for i in Contributor.objects.filter(project_id=project.pk)]
            if project in request_user_projects or request.user in contributors:
                return True
            else:
                return False

        allowed_actions = ['create', 'list']
        if view.action in allowed_actions and view.basename == 'projects':
            try:
                project = get_object_or_404(Project, pk=view.kwargs['project_pk'])
            except KeyError:
                project = get_object_or_404(Project, pk=view.kwargs['pk'])
            if request.user == project.author_user_id:
                return True
            else:
                return False
        elif view.basename == 'issue':
            issue = get_object_or_404(Issue, pk=view.kwargs['pk'])
            if request.user == issue.assignee_user_id:
                return True
            else:
                return False
        else:
            comment = get_object_or_404(Comment, pk=view.kwargs['pk'])
            if request.user == comment.author_user_id:
                return True
            else:
                return False
