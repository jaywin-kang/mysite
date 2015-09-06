from django.db import models
from django.contrib import admin
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 150) #������Ŀ
    category = models.CharField(max_length = 50,blank = True) #���ͱ�ǩ
    date_time = models.DateTimeField(auto_now_add = True) #����ʱ���
    content = models.TextField(blank = True,null = True) #��������
    def __unicode__(self):
        return self.title
    class Meta:
        ordering = ['-date_time']