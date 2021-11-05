from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers

from project.views import ProjectViewSet
from contributor.views import ContributorViewSet
from issue.views import IssueViewSet
from comment.views import CommentViewSet

router = routers.SimpleRouter()

router.register('projects', ProjectViewSet, basename='projects')
router.register('users', ContributorViewSet, basename='users')
router.register('issues', IssueViewSet, basename='issues')
router.register('comments', CommentViewSet, basename='comments')

project_router = routers.NestedSimpleRouter(
    router,
    r'projects', 
    lookup='project'
    )

project_router.register(
    r'users', 
    ContributorViewSet, 
    basename='user'
    )
project_router.register(
    r'issues',
    IssueViewSet,
    basename='issue'
    )

issue_router = routers.NestedSimpleRouter(
    project_router,
    r'issues',
    lookup='issue'
    )

issue_router.register(
    r'comments',
    CommentViewSet,
    basename='comment'
    )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('', include(router.urls)),
    path('', include(project_router.urls)),
    path('', include(issue_router.urls))
]
