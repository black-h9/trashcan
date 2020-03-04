from django.db import models

# Create your models here.

class User(models.Model):
    '''用户表'''

    gender = (
        ('male','男'),
        ('female','女'),
    )

#账号
    name = models.CharField(max_length=128,unique=True)

#密码
    password = models.CharField(max_length=256)

#邮箱
    email = models.EmailField(unique=True)

# 性别
    sex = models.CharField(max_length=32,choices=gender,default='男')

#个性签名
    selfdom =models.TextField()

#注册时间
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Ashbin(models.Model):

#垃圾桶的标题
    title = models.CharField(max_length=70)

#垃圾桶的内容
    body = models.TextField()

# 丢垃圾时间
    created_time = models.DateTimeField(auto_now=True)       #开始日期

# 丢的作者
    author = models.ForeignKey(User,on_delete=models.CASCADE) #作者


    def __str__(self):
        return self.title
