from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from music.models import Music, MusicTag, MusicType, MusicAlbum, Singer, MusicLanguage
from music.musicsfilter import MusicsFilter
from music.serializer import MusicSerializer, MusicTagSerializer, MusicTypeSerializer, MusicAlbumSerializer, \
    SingerSerializer, MusicLanguageSerializer


class MusicViewSet(ModelViewSet):
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter,]
    filterset_class = MusicsFilter
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    search_fields = ('title', )
    ordering_fields = ('share_at',)

class SingerViewSet(ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

class MusicLanguageViewSet(ModelViewSet):
    queryset = MusicLanguage.objects.all()
    serializer_class = MusicLanguageSerializer

class MusicTypeViewSet(ModelViewSet):
    queryset = MusicType.objects.all()
    serializer_class = MusicTypeSerializer


class MusicAlbumViewSet(ModelViewSet):
    queryset = MusicAlbum.objects.all()
    serializer_class = MusicAlbumSerializer


class MusicTagViewSet(ModelViewSet):
    queryset = MusicTag.objects.all()
    serializer_class = MusicTagSerializer
