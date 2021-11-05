from django.db import models
from user.models import User


class Project(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    author_user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f' id: {self.id}, {self.__class__.__name__}: {self.title}, author:{self.author_user_id}'
