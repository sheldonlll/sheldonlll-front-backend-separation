from django.contrib import admin

# Register your models here.
from article.models import Article, ArticleType, ArticleTag, ArticleAlbum

admin.site.register(Article)
admin.site.register(ArticleType)
admin.site.register(ArticleTag)
admin.site.register(ArticleAlbum)