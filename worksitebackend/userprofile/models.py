from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,help_text='用户')
    phone = models.CharField(max_length=15,help_text='电话',blank=True,null=True)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-create_at"]

    def __str__(self):
        return self.user.username

    @property
    def user_name(self):
        return self.user.username

    @property
    def user_email(self):
        return self.user.email
