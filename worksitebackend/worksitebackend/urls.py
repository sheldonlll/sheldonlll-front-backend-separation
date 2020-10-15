"""worksitebackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.documentation import include_docs_urls

from MyUtils.tokenobtain import MyTokenObtainPairView
from worksitebackend import settings

from rest_framework_simplejwt.views import (
    # TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # DRF文档
    path('docs/', include_docs_urls(title='DRF文档')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('api-token-auth/', obtain_auth_token),  # drf token获取的url
    path('api/v1/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),  # simplejwt认证接口
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # simplejwt认证接口

    path('api/v1/a/',include('article.urls')),
    # path('api/v1/m/',include('movie.urls')),
    # path('api/v1/m2/', include('music.urls')),
    path('api/v1/u/', include('userprofile.urls')),
    path('api/v1/c/', include('comment.urls')),
    # path('api/v1/l/', include('like.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
