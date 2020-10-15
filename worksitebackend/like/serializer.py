from rest_framework import serializers

from like.models import LikeRecord, LikeCount


class LikeRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeRecord
        fields = "__all__"

class LikeCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeCount
        fields = "__all__"


