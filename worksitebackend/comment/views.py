from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from comment.commentfilter import CommentFilter
from comment.models import Comment
from comment.serializer import CommentSerializer


class CommentViewSet(ModelViewSet):
    filter_backends = [DjangoFilterBackend,]
    filterset_class = CommentFilter
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # search_fields = ('object_id', 'content_type',)


