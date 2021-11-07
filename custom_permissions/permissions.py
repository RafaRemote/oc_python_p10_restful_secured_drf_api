"""Custom permissions"""

from rest_framework.permissions import BasePermission
from project.models import Project
from contributor.models import Contributor
from django.shortcuts import get_object_or_404


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

        return True

    def has_object_permission(self, request, view, obj):
        """Gives permission if the User is the owner of the object
        
        Returns:
            Boolean.
        """
        print('IsObjOwner', obj, obj.author_user_id == request.user)
        return bool(obj.author_user_id == request.user)


class IsProjectOnwerOrContributor(BasePermission):
    """Checks if the User is the Project's Owner or Project's Contributor"""

    def has_permission(self, request, view):
        """Gives permission to authenticated User 
        
        The main condition to consume the API is to be auhtenticated.
        This condition is set as default for the whole project in softDesk.settings.AUTH_USER_MODEL.
        Therefore, this methode returns always True.

        Returns:
            Boolean.
        """

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
        contributors = [i.user_id for i in Contributor.objects.filter(project_id=project.id)]
        print('IsProjectOwnerOrContributor', obj, bool(request.user in contributors or project.author_user_id == request.user))
        return bool(request.user in contributors or project.author_user_id == request.user)
