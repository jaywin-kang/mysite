from django.db import models
from django.contrib import admin
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 150) #博客题目
    category = models.CharField(max_length = 50,blank = True) #博客标签
    date_time = models.DateTimeField(auto_now_add = True) #博客时间戳
    content = models.TextField(blank = True,null = True) #博客正文
    def __unicode__(self):
        return self.title
    class Meta:
        ordering = ['-date_time']
