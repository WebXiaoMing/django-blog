from datetime import datetime

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Tags(models.Model):
    tag_name = models.CharField(verbose_name='标签名', max_length=20)
    count = models.IntegerField(verbose_name='关联的博客数', default=0)
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tag_name


class Categories(models.Model):
    name = models.CharField(verbose_name='类别名', unique=True, max_length=20)
    count = models.IntegerField(verbose_name='关联的博客数', default=0)
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)

    class Meta:
        verbose_name = '类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Years(models.Model):
    name = models.CharField(verbose_name='年份', unique=True, max_length=20)
    count = models.IntegerField(verbose_name='关联的博客数', default=0)
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)

    class Meta:
        verbose_name = '年份'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Blogs(models.Model):
    title = models.CharField(verbose_name='博客标题', max_length=100)
    categories = models.ForeignKey(Categories, to_field='name', verbose_name='类别', on_delete=models.DO_NOTHING)
    year = models.ForeignKey(Years, to_field='name', verbose_name='归档年份', on_delete=models.DO_NOTHING)
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)
    tags = models.ManyToManyField(Tags, verbose_name='标签')
    short_text = models.CharField(verbose_name='简介', max_length=500)

    class Meta:
        verbose_name = '博客'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Detail(models.Model):
    detail = RichTextUploadingField('博客内容')
    blog = models.ForeignKey(Blogs, verbose_name='所属博客', on_delete=models.DO_NOTHING)
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)

    class Meta:
        verbose_name = '博客内容'
        verbose_name_plural = verbose_name

    def _getDetail_(self):
        return {
            'blog': self.blog,
            'detail': self.detail,
            'add_time': self.add_time
        }
