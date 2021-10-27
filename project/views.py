from rest_framework.viewsets import ModelViewSet
from .serializers import ProjectSerializer
from .models import Project
from rest_framework.permissions import IsAuthenticated


class ProjectViewset(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [
                          IsAuthenticated  
                         ]

    def perform_create(self, serializer):
        serializer.save(author_user_id=self.request.user)
