from .models import Project
from .serializers import ProjectSerializer
from rest_framework import generics
from rest_framework import permissions


class CreateProject(generics.ListCreateAPIView):
    pass


class ReadProjects(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ReadProject(generics.ListCreateAPIView):
    pass


class UpdateProject(generics.ListCreateAPIView):
    pass


class DeleteProject(generics.ListCreateAPIView):
    pass
