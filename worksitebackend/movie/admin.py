from django.contrib import admin

from movie.models import Movie, MovieType, MovieTag, MovieAlbum, Actor, MovieLanguage

admin.site.register(Movie)
admin.site.register(MovieType)
admin.site.register(MovieTag)
admin.site.register(MovieAlbum)
admin.site.register(MovieLanguage)

admin.site.register(Actor)