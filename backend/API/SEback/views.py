from django.shortcuts import render, HttpResponse
from . import models
from django.http import JsonResponse
# Create your views here.
import sys
sys.path.append(r'/root/code/SoftWare_Project/backend/API/SEback/detect_border') #添加上绝对路径
import flatDetect
from . import algo
from django.core.files.base import ContentFile

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
        #print("A")
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

def flatinfo(request):
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
        print(new_img.user)
        print(new_img.photo)
        original_image, overlay_result_on_original, marked_image, horizontal_parallel, vertical_parallel = \
        flatDetect.border_flat_detect(photo_url,"/root/code/SoftWare_Project/backend/API/SEback/detect_border/output")
        #图像保存
        print("图像保存：")
        originURL = algo.saveImage(original_image,"original-"+new_img.user)
        overlayURL = algo.saveImage(overlay_result_on_original,"overlay-" + new_img.user)
        markedURL = algo.saveImage(marked_image,"marked-" + new_img.user)
        # result = flatDetect.border_flat_detect(photo_url)
        print(markedURL)
        stat = "玻璃平整"
        if horizontal_parallel and vertical_parallel :
            stat = "玻璃平整"
        elif horizontal_parallel and not vertical_parallel:
            stat = "玻璃水平平整，垂直不平整"
        elif vertical_parallel and not horizontal_parallel:
            stat = "玻璃水平不平整，垂直平整"
        else:
            stat = "玻璃水平垂直均不平整"
        print(stat)
        #这里返回 JsonRespose 格式出错了
        return JsonResponse({'status': stat, 'original': originURL,'overlay': overlayURL,'marked': markedURL})
    else:
        return HttpResponse('请使用 POST 请求进行上传！')