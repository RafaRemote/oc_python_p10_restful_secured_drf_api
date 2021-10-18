from django.contrib import admin
from snippets.models import Contributor, Project, Issue, Comment


class ContributorAdmin(admin.ModelAdmin):

    list_display = ['user_id', 'role', 'permission']


class ProjectAdmin(admin.ModelAdmin):

    list_display = ['title', 'type', 'author_user_id']


class IssueAdmin(admin.ModelAdmin):

    list_display = ['project_id', 'title', 'assignee_user_id', 'tag', 'priority', 'status']

    # @admin.display(description='Category')
    # def category(self, obj):
    #     return obj.product.category

class CommentAdmin(admin.ModelAdmin):

    list_display = ['issue_id', 'author_user_id', 'created_time']


admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(Comment, CommentAdmin)