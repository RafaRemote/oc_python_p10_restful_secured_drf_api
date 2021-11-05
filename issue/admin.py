from django.contrib import admin
from .models import Issue


class IssueAdmin(admin.ModelAdmin):

    list_display = [
                    'id',
                    'title',
                    'description',
                    'tag',
                    'priority',
                    'status',
                    'project_id',
                    'assignee_user_id',
                    'created_time'
                    ]


admin.site.register(Issue, IssueAdmin)
