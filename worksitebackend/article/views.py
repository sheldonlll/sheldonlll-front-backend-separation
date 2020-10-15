from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from article.articlefilter import ArticlesFilter
from article.models import Article, ArticleTag, ArticleType, ArticleAlbum
from article.serializer import ArticleSerializer, ArticleTagSerializer, ArticleTypeSerializer, ArticleAlbumSerializer



class ArticleViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ArticlesFilter
    queryset = Article.objects.all()
    search_fields = ('title', 'body')
    serializer_class = ArticleSerializer



class ArticleTypeViewSet(ModelViewSet):
    queryset = ArticleType.objects.all()
    serializer_class = ArticleTypeSerializer


class ArticleAlbumViewSet(ModelViewSet):
    queryset = ArticleAlbum.objects.all()
    serializer_class = ArticleAlbumSerializer


class ArticleTagViewSet(ModelViewSet):
    queryset = ArticleTag.objects.all()
    serializer_class = ArticleTagSerializer
