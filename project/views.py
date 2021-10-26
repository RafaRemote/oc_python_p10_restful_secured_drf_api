from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProjectSerializer
from django.shortcuts import get_object_or_404
from .models import Project
from contributor.models import Contributor
from rest_framework.exceptions import NotFound 


class ProjectViewset(ModelViewSet):

    serializer_class = ProjectSerializer

    # def list(self, request):
    #     queryset = Project.objects.all()
    #     serializer = ProjectSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = Project.objects.all()
    #     project = get_object_or_404(queryset, pk=pk)
    #     serializer = ProjectSerializer(project)
    #     return Response(serializer.data)


    def get_queryset(self):
        queryset = Project.objects.filter(author_user_id=self.request.user)
        # if len(queryset) == 0:
        #     raise NotFound('not found found')
        return queryset

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author_user_id=request.user)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        project = Project.objects.get()
        data = request.data
        project.title = data['title']
        project.description = data['description']
        project.type = data['type']
        project.author_user_id = data['author_user_id']

        project.save()

        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    # def destroy(self, request, id=None):
    #     item = get_object_or_404(Project, id=id)
    #     item.delete()
    #     return Response({"status": "success", "data": "Item Deleted"})


    # def get(self, request, id=None):
    #     if id:
    #         project = Project.objects.get(id=id)
    #         serializer = ProjectSerializer(project)
    #         return Response({"stauts":"success", "data": serializer.data}, status=status.HTTP_200_OK)
    #     projects = Project.objects.all()
    #     serializer = ProjectSerializer(projects, many=True)
    #     return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    # def put(self, request, id=None):
    #     try:
    #         project = Project.objects.get(id=id)
    #     except Exception:
    #         return  Response({"error": "object not found in the database"}, status=status.HTTP_404_NOT_FOUND)
    #     serializer = ProjectSerializer(project, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    #     else:
    #         return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

  