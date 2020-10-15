from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from like.models import LikeRecord, LikeCount
from like.serializer import LikeRecordSerializer, LikeCountSerializer


class LikeRecordViewSet(ModelViewSet):
    queryset = LikeRecord.objects.all()
    serializer_class = LikeRecordSerializer

class LikeCountViewSet(ModelViewSet):
    queryset = LikeCount.objects.all()
    serializer_class = LikeCountSerializer

