from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('articles', views.ArticleViewSet)
router.register('articletags', views.ArticleTagViewSet)
router.register('articletypes', views.ArticleTypeViewSet)
router.register('articlealbums', views.ArticleAlbumViewSet)

urlpatterns = [
    path('', include(router.urls)),
]