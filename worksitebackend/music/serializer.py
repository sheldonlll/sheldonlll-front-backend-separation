from rest_framework import serializers

from music.models import Music, MusicType, MusicTag, Singer, MusicLanguage, MusicAlbum


class MusicTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicType
        fields = "__all__"


class MusicTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicTag
        fields = "__all__"


class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = "__all__"


class MusicLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicLanguage
        fields = "__all__"


class MusicAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicAlbum
        fields = "__all__"


class MusicSerializer(serializers.ModelSerializer):
    # type = serializers.SerializerMethodField()
    # singer = SingerSerializer()
    # tags = serializers.SerializerMethodField()
    # author = serializers.SerializerMethodField()

    class Meta:
        model = Music
        fields = (
            "title",
            "lyrics",
            "release_at",
            "share_at",
            "cover",
            "file",
            "mv",
            'music_type',
            "music_author",
            "music_language",
            "music_tags",
            "music_singer",
            'music_album',
            "get_content_type",
        )
    #
    # def get_type(self, obj):
    #     return obj.type.name
    #
    # def get_tags(self, obj):
    #     tags_obj_list = obj.tags.all()
    #     ret = []
    #     for item in tags_obj_list:
    #         ret.append({'name': item.name})
    #     return ret
    # def get_author(self,obj):
    #     return obj.author.user.username
