from django.db import models
from django.utils import timezone
# from DjangoUeditor.models import UEditorField

# Create your models here.
'''
class Student(models.Model):
    st_name = models.CharField(max_length=10, verbose_name='学生姓名',)
    st_sex = models.BooleanField(default=1)
    st_age = models.IntegerField(default=0)
    st_address = models.CharField(max_length=10, verbose_name='地址')
    st_email = models.EmailField(verbose_name='邮箱地址')

    class Meta:
        db_table = 'students'
        ordering = ['-st_age']
'''

##  文章标签类
class Tag(models.Model):
    t_name = models.CharField(max_length=255, verbose_name='文章标签名')
    t_info = models.CharField(max_length=50, verbose_name='标签简介')
    t_createtime = models.DateTimeField(default=timezone.now, db_index=True, verbose_name='创建时间')
    def __str__(self):
        return self.t_name
    class Meta:
        verbose_name_plural = '标签'
        db_table = 'tag'
        ordering = ['-t_createtime']




## 文章类
class Art(models.Model):
    a_title = models.CharField(max_length=255 ,verbose_name='文章标题')
    a_info = models.CharField(max_length=300, verbose_name='文章描述')
    a_content = models.TextField(verbose_name='文章内容')
    '''
    a_content = UEditorField(verbose_name="文章内容", width=1000, height=600,
                             imagePath="arts_ups/ueditor/", filePath="arts_ups/ueditor/",
                             blank=True, toolbars="full", default='')
    '''
    a_img = models.ImageField(null=True, blank=True, upload_to="arts_ups/%Y/%m", verbose_name='封面')
    a_createtime = models.DateTimeField(default=timezone.now, db_index=True, verbose_name='创建时间')
    a_updatetime = models.DateTimeField(default=timezone.now, verbose_name='更新时间')
    a_tag = models.ForeignKey(to=Tag, verbose_name='关联标签')
    def __str__(self):
        return self.a_title
    class Meta:
        verbose_name_plural = '文章'
        db_table = 'art'
        ordering = ['-a_createtime']


#
    # def __unicode__(self):
    #     return self.a_title,self.a_content