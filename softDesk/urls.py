from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers

from project.views import ProjectViewSet
from contributor.views import ContributorViewset
from issue.views import IssueViewset
from comment.views import CommentViewset

router = routers.SimpleRouter()

router.register('projects', ProjectViewSet, basename='projects')
router.register('users', ContributorViewset, basename='users')
router.register('issues', IssueViewset, basename='issues')
router.register('comments', CommentViewset, basename='comments')

project_router = routers.NestedSimpleRouter(
    router,
    r'projects', 
    lookup='project'
    )

project_router.register(
    r'users', 
    ContributorViewset, 
    basename='user'
    )
project_router.register(
    r'issues',
    IssueViewset,
    basename='issue'
    )

issue_router = routers.NestedSimpleRouter(
    project_router,
    r'issues',
    lookup='issue'
    )

issue_router.register(
    r'comments',
    CommentViewset,
    basename='comment'
    )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('', include(router.urls)),
    path('', include(project_router.urls)),
    path('', include(issue_router.urls))
]
