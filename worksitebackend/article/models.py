from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

from MyUtils.fields import RestrictedFileField
from userprofile.models import UserProfile


class ArticleType(models.Model):
    name = models.CharField(max_length=10,help_text='类型')
    create_at = models.DateTimeField(auto_now_add=True,help_text='创建')
    class Meta:
        ordering = ['-create_at']
    def __str__(self):
        return self.name


class ArticleTag(models.Model):
    name = models.CharField(max_length=10,help_text='标签')
    create_at = models.DateTimeField(auto_now_add=True,help_text='创建')
    class Meta:
        ordering = ['-create_at']
    def __str__(self):
        return self.name


class ArticleAlbum(models.Model):
    name = models.CharField(max_length=10,help_text='专栏')
    des = models.TextField(max_length=200,help_text='简介')
    create_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-create_at']
    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(UserProfile,on_delete=models.CASCADE,default=1)
    album = models.ForeignKey(ArticleAlbum,on_delete=models.CASCADE,help_text='专栏',null=True,blank=True)
    tags = models.ManyToManyField(ArticleTag,help_text='标签')
    type = models.ForeignKey(ArticleType,on_delete=models.CASCADE,help_text='类型')
    title = models.CharField(max_length=20,help_text='标题')
    body = models.TextField(help_text='内容')
    share_at = models.DateTimeField(auto_now_add=True,help_text='创建')
    update_at = models.DateTimeField(auto_now=True,help_text='修改')
    des = models.CharField(max_length=200,help_text='简介',blank=True,null=True)
    comments = GenericRelation(to='comment.Comment')

    pic = RestrictedFileField(
        upload_to='article/pic',
        content_types=[
            'image/gif',
            'image/png',
            'image/svg+xml',
            'image/jpeg',
            'image/bmp',
            'image/webp',
            'image/x-icon',
            'image/vnd.microsoft.icon'],
        max_upload_size=104857600,
        null=True,
        help_text='图片',
        blank=True
    )

    class Meta:
        ordering = ['-share_at']

    def __str__(self):
        return self.title

    @property
    def article_type(self):
        return self.type.name

    # @property
    # def article_comment(self):
    #     return self.comments.values().all()

    @property
    def article_album(self):
        return self.album.name


    @property
    def article_author(self):
        return self.author.user.username

    @property
    def article_tags(self):
        return self.tags.values('name').all()
    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type.id
