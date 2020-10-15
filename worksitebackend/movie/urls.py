from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('movies', views.MovieViewSet)
router.register('movietags', views.MovieTagViewSet)
router.register('movietypes', views.MovieTypeViewSet)
router.register('moviealbums', views.MovieAlbumViewSet)
router.register('movielanguages', views.MovieLanguageViewSet)
router.register('actors',views.ActorViewSet)


urlpatterns = [
    path('', include(router.urls)),
]