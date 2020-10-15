from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from userprofile.models import UserProfile


class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,help_text='评论对象model')
    object_id = models.PositiveIntegerField(help_text='评论对象ID')
    content_object = GenericForeignKey('content_type', 'object_id')

    body = models.TextField(max_length=200, help_text='内容')
    create_at = models.DateTimeField(auto_now_add=True, help_text='创建')
    author = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE, help_text='用户')

    root = models.ForeignKey(
        'self',
        related_name='root_comment',
        null=True,
        blank=True,
        on_delete=models.CASCADE, help_text='根评论')
    parent = models.ForeignKey(
        'self',
        related_name='parent_comment',
        null=True,
        blank=True,
        on_delete=models.CASCADE, help_text='父评论')
    reply_to = models.ForeignKey(
        UserProfile,
        related_name="replies",
        null=True,
        blank=True,
        on_delete=models.CASCADE, help_text='回复给')

    class Meta:
        ordering = ['-create_at']

    def __str__(self):
        return self.body

    def children(self): #replies
        return Comment.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True

    @property
    def comment_author(self):
        return self.author.user.username

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type.id


