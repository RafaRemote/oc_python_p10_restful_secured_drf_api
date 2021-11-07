from rest_framework.permissions import BasePermission
from project.models import Project
from contributor.models import Contributor
from django.shortcuts import get_object_or_404


class IsProjectOwner(BasePermission):

    def has_permission(self, request, view):
        if view.basename == "projects" and view.action == "create":
            return True
        elif view.basename == 'projects' and view.action == "list":
            return True
        try:
            project = get_object_or_404(Project, pk=request.parser_context['kwargs']['project_pk'])
            return project.author_user_id == request.user
        except KeyError:
            project = get_object_or_404(Project, pk=request.parser_context['kwargs']['pk'])
            return project.author_user_id == request.user

    def has_object_permission(self, request, view, obj):
        return bool(obj.author_user_id == request.user)


class IsProjectOnwerOrContributor(BasePermission):

    def has_permission(self, request, view):
        project = get_object_or_404(Project, pk=request.parser_context['kwargs']['project_pk'])
        contributors = [i.user_id for i in Contributor.objects.filter(project_id=project.id)]
        return bool(request.user in contributors or project.author_user_id == request.user)

    def has_object_permission(self, request, view, obj):
        if view.basename == "projects" and view.action == "create":
            return True
        if view.basename == 'comments' and view.action == "retrieve":
            return True
        if view.basename == "issue":
            return bool(obj.assignee_user_id == request.user)
        return bool(obj.author_user_id == request.user)
