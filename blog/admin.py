from django.contrib import admin
from .models import BlogType,Blog
# Register your models here.

@admin.register(BlogType)#注册下
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id','type_name')#显示列表

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','blog_type','author','created_time','last_updated_time')

