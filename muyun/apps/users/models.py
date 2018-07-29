from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name='昵称', default='')
    avatar = models.ImageField(upload_to='image/%Y/%m', default=u'image/default.png', max_length=100, verbose_name='用户头像')
    signature = models.CharField(max_length=100, verbose_name='个性签名', default='')
    archives_counts = models.IntegerField(verbose_name='日志总数', default=0)
    categories_counts = models.IntegerField(verbose_name='分类数', default=0)
    tags_counts = models.IntegerField(verbose_name='标签数', default=0)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
