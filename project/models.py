from django.db import models
from django.conf import settings

TYPES = [('TYPE_1', 'type_1'), ('TYPE_2', 'type_2'), ('TYPE_3', 'type_3')]

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    type = models.CharField(choices=TYPES, max_length=100)
    author_user_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='projects', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f' {self.__class__.__name__}:  {self.title}'
