from rest_framework.viewsets import ModelViewSet
from .serializers import ProjectSerializer
from .models import Project
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.http import HttpResponse


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [
                          IsAuthenticated
                         ]

    def get_object(self):
        obj = get_object_or_404(
                                self.get_queryset(),
                                pk=self.kwargs["pk"],
                                author_user_id=self.request.user.id)
        return obj

    def perform_create(self, serializer):
        serializer.save(author_user_id=self.request.user)
