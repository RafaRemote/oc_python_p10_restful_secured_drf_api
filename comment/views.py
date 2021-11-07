from rest_framework.viewsets import ModelViewSet
from .serializers import CommentSerializer
from django.shortcuts import get_object_or_404
from .models import Comment
from issue.models import Issue
from rest_framework.response import Response
from rest_framework import status
from custom_permissions.permissions import IsProjectOnwerOrContributor, IsObjOwner


class CommentViewSet(ModelViewSet):

    serializer_class = CommentSerializer
    permission_classes = (IsProjectOnwerOrContributor, IsObjOwner, )

    def get_queryset(self):
        queryset = Comment.objects.filter(issue_id=self.kwargs['issue_pk'])
        return queryset

    def create(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=self.request.parser_context['kwargs']['issue_pk'])
        request.POST._mutable = True
        request.data["author_user_id"] = request.user.id
        request.data["issue_id"] = issue.id
        request.POST_mutable = False
        return super(CommentViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        comment = self.get_object()
        serializer = self.get_serializer(comment, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        project = get_object_or_404(Comment, pk=self.kwargs['pk'])
        project.delete()
        return Response(
            {"status": f"success: the {self.__class__.__name__.replace('ViewSet', '')} does no more exist"},
            status=status.HTTP_204_NO_CONTENT
            )
