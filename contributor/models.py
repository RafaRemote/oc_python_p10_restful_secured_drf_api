from django.db import models
from django.conf import settings
from project.models import Project

PERMS = [
    ('AUTHOR', 'author'),
    ('CONTRIBUTOR', 'contributor')
]

class Contributor(models.Model):
    user_id = models.ForeignKey(
                                settings.AUTH_USER_MODEL, 
                                related_name='contributors', 
                                on_delete=models.CASCADE
                                )
    project_id = models.ForeignKey(
                                   Project,
                                   related_name='contributors',
                                   on_delete=models.CASCADE,
                                   blank=True,
                                   null=True
                                   )
    permission = models.CharField(choices=PERMS,
                                  max_length=11,
                                  blank=True,
                                  null=True
                                  )
    role = models.CharField(
                            max_length=128,
                            blank=True,
                            null=True
                            )
