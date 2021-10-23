from django.db import models
from django.conf import settings
from project.models import Project

ROLES = [('r1', 'r1'), ('r2', 'r2'), ('r3', 'r3')]
PERMS = [('ADMIN', 'admin'), ('CONTRIB', 'contrib')]


class Contributor(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='contributors', on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, related_name='contributors', on_delete=models.CASCADE)
    permission = models.CharField(choices=PERMS, default='p1', max_length=100)
    role = models.CharField(choices=ROLES, default='r1', max_length=100)

