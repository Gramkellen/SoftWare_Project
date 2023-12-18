from django.shortcuts import render, HttpResponse
from . import models
# Create your views here.

from django.core.files.base import ContentFile
from . import algo

def updateinfo(request):
    if request.method == 'POST':
        #如果请求是POST，就创建一个新的模型对象，同时将数据文件保存在数据库当中
           # 确保文件是图片文件
        new_img = models.detectPicture(
            #这里前端需要设置好key为photo
            photo=request.FILES.get('photo'),  # 拿到图片
            user =request.FILES.get('photo').name # 拿到图片的名字
        )
        new_img.save()  # 保存图片
        photo_url = "/root/code/SoftWare_Project/backend/API/media/photos/" + new_img.user
        result = algo.Classify(photo_url)
        #result = True
        if result:
            return HttpResponse('完整玻璃')
        else :
            return HttpResponse("玻璃破碎")
    else:
        return HttpResponse('没有接收到图片文件！')
    return HttpResponse('请使用 POST 请求进行上传！')