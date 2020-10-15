from rest_framework import serializers
from article.models import Article, ArticleTag, ArticleType, ArticleAlbum


class ArticleTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleTag
        fields = "__all__"


class ArticleAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleAlbum
        fields = "__all__"


class ArticleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleType
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(queryset=ArticleType.objects.all(), slug_field='name')
    album = serializers.SlugRelatedField(queryset=ArticleAlbum.objects.all(),  slug_field='name')
    tags = serializers.SlugRelatedField(queryset=ArticleTag.objects.all(), slug_field='name',many=True)
    class Meta:
        model = Article
        fields = (
            'pic',
            'title',
            'body',
            'share_at',
            'des',
            'update_at',
            'tags',
            'type',
            'album',
            'article_author',
            "get_content_type",
        )

        # type = serializers.SerializerMethodField()
        # tags = serializers.SerializerMethodField()
        # author = serializers.SerializerMethodField()
        # tags = ArticleTagSerializer()
        # album = ArticleAlbumSerializer()
        # type = ArticleTypeSerializer()
        # author = UserProfileSerializer()
        # author = serializers.SlugRelatedField(queryset=UserProfile.objects.all(), slug_field='user__username')
        # 'author',
        # 'article_type',
        # 'article_tags',
        # "article_album",
        # "article_comment")
        # fields = "__all__"
        # extra_kwargs = {
        #
        # }

    # def get_type(self,obj):
    #     return obj.type.name

    # def get_tags(self,obj):
    #     tags_obj_list = obj.tags.all()
    #     ret = []
    #     for item in tags_obj_list:
    #         ret.append({'name': item.name})
    #     return ret

    # def get_author(self,obj):
    #     return obj.author.user.username
