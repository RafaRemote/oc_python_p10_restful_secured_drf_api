from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):

    list_display = [
                    'id',
                    'author_user_id',
                    'title',
                    'type',
                    'description'
                    ]

admin.site.register(Project, ProjectAdmin)
