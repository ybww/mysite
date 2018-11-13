from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class BlogType(models.Model):#博文分类
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name

class Blog(models.Model):#博文 继承Model模型
    title = models.CharField(max_length=50)#标题
    blog_type = models.ForeignKey(BlogType,on_delete=models.DO_NOTHING)#关联到上面的博客类型
    content = models.TextField()#内容
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING)#作者
    created_time = models.DateTimeField(auto_now_add=True)#创建时间
    last_updated_time = models.DateTimeField(auto_now=True)#最后修改时间

    def __str__(self):
        return "<Blog: %s>" % self.title