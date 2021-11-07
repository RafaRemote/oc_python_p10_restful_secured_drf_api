"""Custom permissions"""

from rest_framework.permissions import BasePermission
from project.models import Project
from contributor.models import Contributor
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status


class IsObjOwner(BasePermission):
    """Checks if the User is the Project's Owner"""

    def has_permission(self, request, view):
        """Gives permission to authenticated User 
        
        The main condition to consume the API is to be auhtenticated.
        This condition is set as default for the whole project in softDesk.settings.AUTH_USER_MODEL.
        Therefore, this methode returns always True.

        Returns:
            Boolean.
        """
        print(view.action)
        print(view.basename)

        if view.action == 'create' and view.basename == 'projects':
            return True
        allowed_actions = ['list', 'retrieve']
        if view.action in allowed_actions and view.basename == 'projects':
            projects = [i.author_user_id for i in Project.objects.filter(author_user_id=request.user)]
            if request.user in projects:
                return True
            else:
                return Response()

        allowed_actions = ['list', 'create', 'retrieve']
        alllowed_basenames = ['issue', 'comment', 'user']
        if view.action in allowed_actions and view.basename in alllowed_basenames:
            project = get_object_or_404(Project, pk=request.parser_context['kwargs']['project_pk'])
            if request.user == project.author_user_id:
                return True
            else:
                return False
        
        if view.action == 'destroy':
            try:
                project = get_object_or_404(Project, pk=request.parser_context['kwargs']['project_pk'])
            except KeyError:
                project = get_object_or_404(Project, pk=request.parser_context['kwargs']['pk'])
            if project.author_user_id == request.user:
                return True
            else:
                return False

        # allowed_actions = ['list', 'create']
        # if view.action in allowed_actions and view.basename == 'users':
        #     project = get_object_or_404(Project, pk=request.parser_context['kwargs']['project_pk'])
        #     if request.user == project.author_user_id:
        #         return True

        return True

    def has_object_permission(self, request, view, obj):
        print('h_o_p')
        """Gives permission if the User is the owner of the object
        
        Returns:
            Boolean.
        """

        if view.basename == 'issue':
            return bool(obj.assignee_user_id == request.user)
        else:
            return bool(obj.author_user_id == request.user)


class IsProjectOnwerOrContributor(BasePermission):
    """Checks if the User is the Project's Owner or Contributor"""

    def has_permission(self, request, view):
        """Gives permission to Project Owner or Contributor 

        Returns:
            Boolean.
        """
        print(view.action)
        print(view.basename)
        print(request.user)

        allowed_actions = ['list', 'create', 'retrieve']
        alllowed_basenames = ['issue', 'comment', 'user']

        if view.action in allowed_actions and view.basename in alllowed_basenames:
            project = get_object_or_404(Project, pk=request.parser_context['kwargs']['project_pk'])
            contributors = [i.user_id for i in Contributor.objects.filter(project_id=project.id)]
            print(request.user == project.author_user_id or request.user in contributors)
            if request.user == project.author_user_id or request.user in contributors:
                return True
            else:
                return False
        
        if view.action == 'destroy':
            try:
                project = get_object_or_404(Project, pk=request.parser_context['kwargs']['project_pk'])
            except KeyError:
                project = get_object_or_404(Project, pk=request.parser_context['kwargs']['pk'])
            if project.author_user_id == request.user:
                return True
            else:
                return False

        return True

    def has_object_permission(self, request, view, obj):
        """Gives permission to Project's Contributor or the Owner of the object
        
        Returns:
            Boolean.
        """

        try:
            project = get_object_or_404(Project, pk=request.parser_context['kwargs']['project_pk'])
        except KeyError:
            project = get_object_or_404(Project, pk=request.parser_context['kwargs']['pk'])
        return bool(request.user == project.author_user_id)
