from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContributorSerializer
from django.shortcuts import get_object_or_404
from .models import Contributor


class ContributorViewset(ModelViewSet):

    serializer_class = ContributorSerializer

    def get_queryset(self):
        queryset = Contributor.objects.all()
        return queryset

    # def post(self, request):
    #     serializer = ProjectSerializer(data=request.data) #first we create a serializer object from the request.data using ProjectSerializer created previously.
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    #     else:
    #         return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

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

    # def delete(self, request, id=None):
    #     item = get_object_or_404(Project, id=id)
    #     item.delete()
    #     return Response({"status": "success", "data": "Item Deleted"})
