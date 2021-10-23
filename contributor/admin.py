from django.contrib import admin
from .models import Contributor


class ContributorAdmin(admin.ModelAdmin):

    list_display = ['user_id', 'project_id', 'permission', 'role']


admin.site.register(Contributor, ContributorAdmin)
