from rest_framework import serializers

from userprofile.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("id", "phone","create_at","user_name","user_email")


