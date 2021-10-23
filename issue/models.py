from django.db import models
from django.conf import settings
from project.models import Project

TAGS = [('BUG', 'bug'), ('IMPROVEMENT', 'improvement'), ('TASK', 'task')]
PRIORITIES = [('LOW', 'low'), ('AVERAGE', 'average'), ('HIGH', 'high')]
STATUSES = [('TO_DO', 'to_do'), ('IN_PROGRESS', 'in_progress'), ('DONE', 'done')]


class Issue(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    tag = models.CharField(choices=TAGS, default=None, max_length=100)
    priority = models.CharField(choices=PRIORITIES, default=None, max_length=100)
    status = models.CharField(choices=STATUSES, default=None, max_length=100)
    project_id = models.ForeignKey(Project, related_name='issues', on_delete=models.CASCADE)
    assignee_user_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='issues', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
