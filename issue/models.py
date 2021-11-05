from django.db import models
from django.conf import settings
from project.models import Project


class Issue(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    tag = models.CharField(max_length=100, blank=True, null=True)
    priority = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    project_id = models.ForeignKey(Project, related_name='issues', on_delete=models.CASCADE, blank=True, null=True)
    assignee_user_id = models.ForeignKey(settings.AUTH_USER_MODEL,
                                         related_name='issues',
                                         on_delete=models.CASCADE,
                                         blank=True,
                                         null=True
                                         )
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        msg = (
              f'id:{self.id}, project:{self.project_id.id}-{self.__class__.__name__}:'
              f'{self.title}, author:{self.assignee_user_id}'
              )
        return msg
