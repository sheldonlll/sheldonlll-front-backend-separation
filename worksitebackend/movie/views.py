from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from movie.models import Movie, MovieTag, MovieType, MovieAlbum, Actor, MovieLanguage
from movie.moviefilter import MoviesFilter
from movie.serializer import MovieSerializer, MovieTagSerializer, MovieTypeSerializer, MovieAlbumSerializer, \
    ActorSerializer, MovieLanguageSerializer


class MovieViewSet(ModelViewSet):
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter,]
    filterset_class = MoviesFilter
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    search_fields = ('title', )
    ordering_fields = ('share_at',)


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class MovieLanguageViewSet(ModelViewSet):
    queryset = MovieLanguage.objects.all()
    serializer_class = MovieLanguageSerializer

class MovieTypeViewSet(ModelViewSet):
    queryset = MovieType.objects.all()
    serializer_class = MovieTypeSerializer


class MovieAlbumViewSet(ModelViewSet):
    queryset = MovieAlbum.objects.all()
    serializer_class = MovieAlbumSerializer


class MovieTagViewSet(ModelViewSet):
    queryset = MovieTag.objects.all()
    serializer_class = MovieTagSerializer
