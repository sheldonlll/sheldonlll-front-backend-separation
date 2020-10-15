from rest_framework import serializers

from movie.models import Movie, MovieAlbum, MovieType, MovieTag, MovieLanguage, Actor


class MovieTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieType
        fields = "__all__"


class MovieTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieTag
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"


class MovieLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguage
        fields = "__all__"


class MovieAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieAlbum
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    # type = serializers.SerializerMethodField()
    # tags = serializers.SerializerMethodField()
    # actors = serializers.SerializerMethodField()
    # author = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = (
            'title',
            'des',
            'dialogue',
            'release_at',
            'share_at',
            'cover',
            'file',
            'movie_type',
            'movie_author',
            'movie_tags',
            'movie_language',
            'movie_actors',
            'movie_album',
            "get_content_type",
        )

    #
    # def get_type(self,obj):
    #     return obj.type.name
    #
    # def get_tags(self, obj):
    #     tags_obj_list = obj.tags.all()
    #     ret = []
    #     for item in tags_obj_list:
    #         ret.append({'name': item.name})
    #     return ret
    #
    # def get_actors(self, obj):
    #     actors_obj_list = obj.actors.all()
    #     ret = []
    #     for item in actors_obj_list:
    #         ret.append({'name': item.name})
    #     return ret
    #
    # def get_author(self,obj):
    #     return obj.author.user.username
