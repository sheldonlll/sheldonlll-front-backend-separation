from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('users', views.UserProfileViewSet)


urlpatterns = [
    path('', include(router.urls)),
]