from django.contrib import admin

from like.models import LikeRecord, LikeCount

admin.site.register(LikeRecord)
admin.site.register(LikeCount)