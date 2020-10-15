from django.contrib import admin

from music.models import Music, MusicType, MusicTag, MusicAlbum, Singer, MusicLanguage

admin.site.register(Music)
admin.site.register(MusicType)
admin.site.register(MusicTag)
admin.site.register(MusicAlbum)
admin.site.register(MusicLanguage)
admin.site.register(Singer)