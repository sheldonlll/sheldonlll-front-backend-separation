from django.shortcuts import render
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from userprofile.models import UserProfile
from userprofile.serializer import UserProfileSerializer


class UserProfileViewSet(ModelViewSet):
    filter_backends = [SearchFilter, ]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    search_fields = ('id', )


