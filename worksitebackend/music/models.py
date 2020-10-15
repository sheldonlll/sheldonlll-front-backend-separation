from django.contrib.contenttypes.models import ContentType
from django.db import models

from MyUtils.fields import RestrictedFileField
from userprofile.models import UserProfile


class MusicType(models.Model):
    name = models.CharField(max_length=10, help_text='类型')
    create_at = models.DateTimeField(auto_now_add=True, help_text='创建')
    class Meta:
        ordering = ['-create_at']
    def __str__(self):
        return self.name


class MusicTag(models.Model):
    name = models.CharField(max_length=10, help_text='标签')
    create_at = models.DateTimeField(auto_now_add=True, help_text='创建')
    class Meta:
        ordering = ['-create_at']
    def __str__(self):
        return self.name


class MusicLanguage(models.Model):
    name = models.CharField(max_length=10, help_text='语种')
    create_at = models.DateTimeField(auto_now_add=True, help_text='创建')
    class Meta:
        ordering = ['-create_at']
    def __str__(self):
        return self.name


class Singer(models.Model):
    name = models.CharField(max_length=20, help_text='歌手')
    des = models.TextField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-create_at']
    def __str__(self):
        return self.name


class MusicAlbum(models.Model):
    name = models.CharField(max_length=20, help_text='专辑')
    des = models.TextField(max_length=200)
    release_at = models.DateField(null=True, help_text='发布')
    create_at = models.DateTimeField(auto_now_add=True)
    cover = RestrictedFileField(
        upload_to='music/album',
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


class Music(models.Model):
    author = models.ForeignKey(UserProfile,on_delete=models.CASCADE,default=1)
    album = models.ForeignKey(MusicAlbum,on_delete=models.CASCADE,help_text='专辑',null=True,blank=True)
    language = models.ForeignKey(
        MusicLanguage,
        on_delete=models.CASCADE,
        help_text='语种')
    tags = models.ManyToManyField(MusicTag, help_text='标签')
    type = models.ForeignKey(
        MusicType,
        on_delete=models.CASCADE,
        help_text='类型')
    title = models.CharField(max_length=20, help_text='歌名')
    lyrics = models.TextField(help_text='歌词')
    release_at = models.DateField(null=True, help_text='发布')
    share_at = models.DateTimeField(auto_now_add=True, help_text='创建')
    singer = models.ForeignKey(Singer, help_text='歌手',on_delete=models.CASCADE)
    cover = RestrictedFileField(
        upload_to='music/pic',
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
        upload_to='music/file/songs',
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
        help_text='file',
    )
    mv = RestrictedFileField(
        upload_to='music/file/mv',
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
        null=True,
        help_text='MV',
        blank=True
    )

    class Meta:
        ordering = ["-share_at"]

    def __str__(self):
        return self.title


    @property
    def music_type(self):
        return self.type.name

    @property
    def music_author(self):
        return self.author.user.username

    @property
    def music_album(self):
        return self.album.name

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type.id

    @property
    def music_language(self):
        return self.language.name

    @property
    def music_tags(self):
        return self.tags.values('name').all()

    @property
    def music_singer(self):
        return self.singer.name
