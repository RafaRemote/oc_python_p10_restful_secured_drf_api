from django.urls import path
from .views import CreateProject, ReadProjects, ReadProject, UpdateProject, DeleteProject


urlpatterns = [
    path('projects/', ReadProjects.as_view()), #3 - GET - get all the projects of the connected user
    path('projects/', CreateProject.as_view()), #4 - POST - create a project
    path('projects/<int:pk>/', ReadProject.as_view()), #5 -GET - details of a project
    path('projects/<int:pk>/', UpdateProject.as_view()), #6 - PUT - update a project
    path('projects/<int:pk>/', DeleteProject.as_view()) #7 - DELETE - delete a project
]

# from rest_framework.urlpatterns import format_suffix_patterns
# urlpatterns = format_suffix_patterns(urlpatterns)
