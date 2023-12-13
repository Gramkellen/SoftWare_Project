from django.shortcuts import render, HttpResponse
from django.db import models
# Create your views here.

from django.core.files.base import ContentFile


def updateinfo(request):
    if request.method == 'POST':
        #如果请求是POST，就创建一个新的模型对象，同时将数据文件保存在数据库当中
        new_img = models.detectPicture(
            photo=request.FILES.get('photo'),  # 拿到图片
            user=request.FILES.get('photo').name # 拿到图片的名字
        )
        new_img.save()  # 保存图片
        return HttpResponse('上传成功！')  

    return HttpResponse('一次尝试')