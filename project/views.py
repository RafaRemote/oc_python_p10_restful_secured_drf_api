from .models import Project
from .serializers import ProjectSerializer
from rest_framework import generics
from rest_framework import permissions
# from rest_framework import get_queryset


class CreateProject(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer


class ReadProjects(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReadProject(generics.ListCreateAPIView):
    pass


class UpdateProject(generics.ListCreateAPIView):
    pass


class DeleteProject(generics.ListCreateAPIView):
    pass
