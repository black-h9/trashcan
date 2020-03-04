from django.contrib import admin
from . import models
# Register your models here.


class User_U(admin.ModelAdmin):
    list_display = ['id','name','password','email','sex','selfdom','c_time']

class Ashbin_A(admin.ModelAdmin):
    list_display = ['id','title','body','created_time','author']

admin.site.register(models.User,User_U)
admin.site.register(models.Ashbin,Ashbin_A)