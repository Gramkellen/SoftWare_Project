from django.db import models

# Create your models here.

#创建数据库案例：
class detectPicture(models.Model):
    user = models.CharField(max_length=64)    #标识了用户
    photo = models.ImageField(upload_to='photos', default='user1.jpg')   #设置了图片的上传路径，没有图片默认user1.jpg
