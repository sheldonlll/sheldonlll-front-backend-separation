from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('musics', views.MusicViewSet)
router.register('musictags', views.MusicTagViewSet)
router.register('musictypes', views.MusicTypeViewSet)
router.register('musicalbums', views.MusicAlbumViewSet)
router.register('musiclanguages', views.MusicLanguageViewSet)
router.register('singers',views.SingerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]