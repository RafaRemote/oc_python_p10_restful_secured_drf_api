from rest_framework import serializers
from .models import Project
from user.models import User
from user.serializers import UserSerializer


# class ProjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Project
#         fields = "__all__"

#     def create(self, validated_data):
#         """
#         Create and return a new `Project` instance, given the validated data.
#         """
#         return Project.objects.create(**validated_data)
 

class ProjectSerializer(serializers.ModelSerializer):
    author_user_id = UserSerializer(read_only=True)

    class Meta:
        model = Project
        fields = "__all__"