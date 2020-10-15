from rest_framework import serializers

from comment.models import Comment


class CommentChildSerializer(serializers.ModelSerializer):
    reply_count = serializers.SerializerMethodField()
    content_object_url = serializers.SerializerMethodField()
    replies = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = [
            "id",
            "content_type",
            "object_id",
            "body",
            "author",
            "create_at",
            "comment_author",
            "root",
            "parent",
            "replies",
            "content_object_url",
            "reply_count",
            "get_content_type",
            "is_parent"
        ]

    def get_content_object_url(self, obj):
        try:
            return obj.content_object.get_api_url()
        except:
            return None

    def get_replies(self, obj):
        if obj.is_parent:
            return CommentChildSerializer(obj.children(), many=True).data
        return None

    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        return 0

class CommentSerializer(serializers.ModelSerializer):
    reply_count = serializers.SerializerMethodField()
    content_object_url = serializers.SerializerMethodField()
    replies = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = (
            "id",
            "content_type",
            "object_id",
            "author",
            "body",
            "create_at",
            "comment_author",
            "root",
            "parent",
            "reply_to",
            "replies",
            "content_object_url",
            "reply_count",
            "get_content_type",
            "is_parent")

    def get_content_object_url(self, obj):
        try:
            return obj.content_object.get_api_url()
        except:
            return None

    def get_replies(self, obj):
        if obj.is_parent:
            return CommentChildSerializer(obj.children(), many=True).data
        return None

    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        return 0
