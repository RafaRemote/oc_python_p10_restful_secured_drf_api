from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):

    list_display = ['description', 'author_user_id', 'issue_id', 'created_time']


admin.site.register(Comment, CommentAdmin)
