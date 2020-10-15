from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from userprofile.models import UserProfile


class LikeCount(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,help_text='点赞对象model')
    object_id = models.PositiveIntegerField(help_text='点赞对象ID')
    content_object = GenericForeignKey('content_type', 'object_id')
    liked_num = models.IntegerField(default=0,help_text='点赞数')

    class Meta:
        ordering = ["-liked_num"]

    def __str__(self):
        return str(self.liked_num)


class LikeRecord(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,help_text='点赞对象model')
    object_id = models.PositiveIntegerField(help_text='点赞对象ID')
    content_object = GenericForeignKey('content_type', 'object_id')

    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE,help_text='用户')
    create_at = models.DateTimeField(auto_now_add=True,help_text='点赞时间')

    class Meta:
        ordering = ["-create_at"]

    def __str__(self):
        return self.author.user.username
