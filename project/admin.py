from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):

    list_display = [
                    'title',
                    'description',
                    'type',
                    'author_user_id',
                    'created_time'
                    ]


admin.site.register(Project, ProjectAdmin)
