from django.contrib.contenttypes.models import ContentType
from django.db import models

from MyUtils.fields import RestrictedFileField
from userprofile.models import UserProfile


class MovieType(models.Model):
    name = models.CharField(max_length=10,help_text='类型')
    create_at = models.DateTimeField(auto_now_add=True,help_text='创建')
    class Meta:
        ordering = ['-create_at']
    def __str__(self):
        return self.name


class MovieTag(models.Model):
    name = models.CharField(max_length=10,help_text='标签')
    create_at = models.DateTimeField(auto_now_add=True,help_text='创建')
    class Meta:
        ordering = ['-create_at']
    def __str__(self):
        return self.name


class MovieLanguage(models.Model):
    name = models.CharField(max_length=10,help_text='语种')
    create_at = models.DateTimeField(auto_now_add=True,help_text='创建')
    class Meta:
        ordering = ['-create_at']
    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=20,help_text='演员')
    des = models.TextField(max_length=200,help_text='简介')
    create_at = models.DateTimeField(help_text='创建')
    class Meta:
        ordering = ['-create_at']
    def __str__(self):
        return self.name


class MovieAlbum(models.Model):
    name = models.CharField(max_length=20, help_text='专题')
    des = models.TextField(max_length=200)
    release_at = models.DateField(null=True, help_text='发布')
    create_at = models.DateTimeField(auto_now_add=True)
    cover = RestrictedFileField(
        upload_to='movie/album',
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
        help_text='封面',
    )
    class Meta:
        ordering = ['-create_at']
    def __str__(self):
        return self.name


class Movie(models.Model):
    author = models.ForeignKey(UserProfile,on_delete=models.CASCADE,default=1)
    album = models.ForeignKey(MovieAlbum,on_delete=models.CASCADE,help_text='专题',null=True,blank=True)
    language = models.ForeignKey(MovieLanguage,on_delete=models.CASCADE,help_text='语种')
    tags = models.ManyToManyField(MovieTag,help_text='标签')
    type = models.ForeignKey(MovieType,on_delete=models.CASCADE,help_text='类型')
    title = models.CharField(max_length=20,help_text='片名')
    des = models.TextField(help_text='简介')
    dialogue = models.TextField(help_text='台词')
    release_at = models.DateField(null=True,help_text='发布')
    share_at = models.DateTimeField(auto_now_add=True,help_text='创建')
    actors = models.ManyToManyField(Actor,help_text='演员表', blank=True)
    cover = RestrictedFileField(
        upload_to='movie/pic',
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
        help_text='封面',
    )
    file = RestrictedFileField(
        upload_to='movie/file',
        content_types=[
            'audio/wave',
            'audio/wav',
            'audio/x-wav',
            'audio/x-pn-wav',
            'audio/webm',
            'video/webm',
            'audio/ogg',
            'video/ogg',
            'application/ogg',
            'application/json',
            'video/mp4'],
        max_upload_size=3221225472,
        help_text='视频'
    )

    class Meta:
        ordering = ["-share_at"]

    def __str__(self):
        return self.title

    @property
    def movie_type(self):
        return self.type.name

    @property
    def movie_author(self):
        return self.author.user.username

    @property
    def movie_album(self):
        return self.album.name

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type.id

    @property
    def movie_language(self):
        return self.language.name

    @property
    def movie_tags(self):
        return self.tags.values('name').all()

    @property
    def movie_actors(self):
        return self.actors.values('name').all()
