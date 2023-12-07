from argparse import _ActionsContainer
import io
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from backend.models import Image
from rest_framework import status
from backend.serializers import ImageSerializer
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.conf import settings

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import os
import csv
import numpy as np
import torch
import cv2
import sys
# 模块路径添加到 sys.path
#sys.path.append('/root/StudyOnCurtainWall/backend')
from backend.segment_anything import sam_model_registry, SamAutomaticMaskGenerator


class GetImg(GenericViewSet):
    serializer_class = ImageSerializer

    @action(methods=['post'], detail=False)
    def save_image(self, request):
        file_path = './media/' # 指定保存文件的文件夹路径
        # 若文件夹不存在则新建
        if not os.path.exists(file_path):
            os.makedirs(file_path)

        if request.POST.get('func')  == 'A':

            file_path = os.path.join(file_path,'segmentaion')
            fs = FileSystemStorage(location=file_path)
            try:
                uploaded_file = request.FILES['image']  # 获取上传的图像文件
                FileSystemStorage(location=file_path)
                filename = fs.save(uploaded_file.name, uploaded_file)

                #返回图片先写死为原图片
                result_url = request.build_absolute_uri('/media/segmentation/' + filename)
                print(result_url)
                return Response({'message': 'Image Saving complete.',
                                 'total': 13,  #结果图片数量
                                 'pictures': [   #结果图片url
                                     {'url': result_url},
                                     {'url': result_url},
                                     {'url': result_url},
                                     {'url': result_url}, 
                                     {'url': result_url},
                                     {'url': result_url},
                                     {'url': result_url},
                                     {'url': result_url},
                                     {'url': result_url},
                                     {'url': result_url},
                                     {'url': result_url},
                                     {'url': result_url},
                                     {'url': result_url},
                                 ]}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e),'message': 'Image uploading fail.'}, status=status.HTTP_400_BAD_REQUEST)

                # 开始图像分割的操作————————————————————————————
                # 以下代码由严文昊小组填充修改———————————————————
                # 取消代码逻辑，后续用连接代替

            #     # 读取上传的图像文件并转换为numpy数组
            #     image_data = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)

            #     # 调用图像分割函数进行处理
            #     #segment_image(image_data)

            #     image_list = []  # 用于存储图片路径的列表
            #     valid_extensions = ['.png', '.jpg', '.jpeg', '.gif']  # 允许的图片文件扩展名列表
    
            #     # 遍历文件夹中的所有文件和子文件夹
            #     for root, dirs, files in os.walk('./backend/media/segged'):
            #         for file in files:
            #             file_extension = os.path.splitext(file)[1].lower()  # 获取文件扩展名并转换为小写
            #             if file_extension in valid_extensions:
            #                 image_path = request.build_absolute_uri('/media/segged/' + file)
            #                 image_list.append(image_path)
     
            #     return Response({'message': 'Image processing complete.',
            #                      'total': len(image_list),  #结果图片数量
            #                      'pictures':image_list},
            #                      status=status.HTTP_200_OK)
            # except Exception as e:
            #     print(e)
            #     # 处理异常情况
            #     return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        elif request.POST.get('func')  == 'B':
            file_path = os.path.join(file_path,'explosion_identify')
            if not os.path.exists(file_path):
                os.makedirs(file_path)
            fs = FileSystemStorage(location=file_path)

            try:
                uploaded_file = request.FILES['image']  # 获取上传的图像文件
                filename = fs.save(uploaded_file.name, uploaded_file)


                 # 开始识别玻璃内爆的操作—————————————————————————
                 # 以下代码由邓丁熙小组填充修改———————————————————


                #返回图片先写死为原图片
                result_url = request.build_absolute_uri('/media/explosion_identify/' + filename)
                return Response({'message': 'Image Saving complete.',
                                 'total': 13,  #结果图片数量
                                 'pictures': [   #结果图片url
                                     {'url': result_url},
                                     {'url': result_url},
                                     {'url': result_url},
                                     {'url': result_url},
                                     {'url': result_url},
                                     {'url': result_url},
                                     {'url': result_url},
                                     {'url': result_url},
                                     {'url': result_url},
                                     {'url': result_url},
                                     {'url': result_url},
                                     {'url': result_url},
                                     {'url': result_url},
                                 ]}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e),'message': 'Image uploading fail.'}, status=status.HTTP_400_BAD_REQUEST)

# 上传CSV振动数据文件
class UploadCsv(GenericViewSet):
    serializer_class = ImageSerializer

    @action(methods=['post'], detail=False)
    def save_csv(self,request):
        file_path = './backend/media/' # 指定保存文件的文件夹路径

        file_path = os.path.join(file_path,'vibration/')
        # 若文件夹不存在则新建
        if not os.path.exists(file_path):
            os.makedirs(file_path)

        try:
            uploaded_file = request.FILES['csv']  # 获取上传的图像文件
            print(uploaded_file)
            # building = request.POST['building']
            # equipment = request.POST['equipment']
            # start_time = request.POST['start_time']
            # end_time = request.POST['end_time']
            #
            # print(uploaded_file.name,building,equipment,start_time,end_time)

            # 判断文件是否存在
            if os.path.exists(file_path + uploaded_file.name):
                #文件已存在
                print("该文件已上传过")
            else:
                #文件尚不存在
                # 创建文件系统存储对象
                fs = FileSystemStorage(location=file_path)
                fs.save(uploaded_file.name, uploaded_file)

            # 从保存的.csv文件中读取数据并返回前端
            x_data=[]
            y_data=[]
            z_data=[]

            with open(file_path + uploaded_file.name,'r') as file:
                reader =csv.reader(file,delimiter=',')
                for i,row in enumerate(reader):
                    x_data.append(float(row[0].strip()))
                    y_data.append(float(row[1].strip()))
                    z_data.append(float(row[2].strip()))

            parts = 3600
            x_data = data_smoothing(x_data,parts)
            y_data = data_smoothing(y_data,parts)
            z_data = data_smoothing(z_data,parts)

            return Response({
                'yData':{
                    'x':x_data,
                    'y':y_data,
                    'z':z_data,
                },
                'csv_url': file_path + uploaded_file.name,
            },status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            # 处理异常情况
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


# 异常值筛选
class FilterOutlier(GenericViewSet):
    serializer_class = ImageSerializer

    @action(methods=['post'], detail=False)
    def filter_outlier(self,request):
        file_path = os.path.join('./backend/media/','vibration/')
        try:
            min = request.POST['min']
            max = request.POST['max']
            file_url = request.POST['csv_url']
            min = float(min)
            max = float(max)

            print(file_url)

            # 从保存的.csv文件中读取数据并返回前端
            x_data=[]
            y_data=[]
            z_data=[]

            with open(file_url,'r') as file:
                reader =csv.reader(file,delimiter=',')
                for i,row in enumerate(reader):
                    x_data.append(float(row[0].strip()))
                    y_data.append(float(row[1].strip()))
                    z_data.append(float(row[2].strip()))

            # 筛选异常值
            x_abnormal = [ x for x in x_data if x < min or x > max]
            y_abnormal = [ y for y in y_data if y < min or y > max]
            z_abnormal = [ z for z in z_data if z < min or z > max]

            return Response({
                'yData':{
                    'x':x_abnormal,
                    'y':y_abnormal,
                    'z':z_abnormal,
                },
            },status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            # 处理异常情况
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

def data_smoothing(data, num_parts):
    n = len(data)
    chunk_size = n // num_parts  # 每份大小
    result = []
    for i in range(0, n, chunk_size):
        chunk = data[i:i + chunk_size]
        average = sum(chunk) / len(chunk)
        result.append(average)
    return result

# 条件搜索：数据库数据
class ConditionSearch(GenericViewSet):
    serializer_class = ImageSerializer

    @action(methods=['post'], detail=False)
    def condition_search(self,request):
        try:
            building = request.POST['building']
            equipment = request.POST['equipment']
            start_time = request.POST['start_time']
            end_time = request.POST['end_time']
            pageNo = request.POST['pageNo']
            pageSize = request.POST['pageSize']

            #数据库查找

            return Response({
                'total': 34,
                'records':[
                    {
                        'date': '2023-1-23-12:12',
                        'id': '1',
                        'building': 'A楼',
                        'equipment': 'Device230EF3',
                        'x': -0.001,
                        'y': 0.023,
                        'z': 0.3,
                    },
                    {
                        'date': '2023-1-23-12:12',
                        'id': '1',
                        'building': 'A楼',
                        'equipment': 'Device230EF3',
                        'x': -0.001,
                        'y': 0.023,
                        'z': 0.3,
                    },
                    {
                        'date': '2023-1-23-12:12',
                        'id': '1',
                        'building': 'A楼',
                        'equipment': 'Device230EF3',
                        'x': -0.001,
                        'y': 0.023,
                        'z': 0.3,
                    },
                    {
                        'date': '2023-1-23-12:12',
                        'id': '1',
                        'building': 'A楼',
                        'equipment': 'Device230EF3',
                        'x': -0.001,
                        'y': 0.023,
                        'z': 0.3,
                    }
                ]
            },status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            # 处理异常情况
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


# 发送邮件到指定邮箱
class SendMail(GenericViewSet):
    serializer_class = ImageSerializer

    @action(methods=['post'], detail=False)
    def send_mail(self,request):
        info = request.data;
        sender_address = 'curtainwall2023@163.com'
        receiver_address = info['address']
        subject = '异常数据报告'

        x_str = ';  '.join(str(x) for x in info['data']['x']) if info['data']['x'] else ''
        y_str = ';  '.join(str(y) for y in info['data']['y']) if info['data']['y'] else ''
        z_str = ';  '.join(str(z) for z in info['data']['z']) if info['data']['z'] else ''

        message = f"异常范围：[{info['min']},{info['max']}]\n" \
                 f"传感器编号：{info['device']} \n" \
                 f" x方向:\n {x_str} \n\n" \
                 f" y方向:\n {y_str} \n\n" \
                 f" z方向:\n {z_str} "

        # 创建邮件内容
        msg = MIMEMultipart()
        msg['From'] = sender_address
        msg['To'] = receiver_address
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        try:
            # #连接SMTP服务器并发送邮件
            smtp_server = 'smtp.163.com'
            port = 25
            username = 'curtainwall2023@163.com'
            password = 'ZFTHMXDLEOEZDJTS'

            with smtplib.SMTP(smtp_server, port) as server:
                server.login(username, password)
                server.sendmail(sender_address, receiver_address, msg.as_string())

            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            # 处理异常情况
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


# def segment_image(input_image_data, output_dir='/root/StudyOnCurtainWall/backend/media/segged', sam_checkpoint="backend\sam_vit_h_4b8939.pth", model_type="vit_h"):
#     # Check if CUDA is available
#     if torch.cuda.is_available():
#         device = "cuda"
#     else:
#         device = "cpu"
#     # Create the output directory if it doesn't exist
#     os.makedirs(output_dir, exist_ok=True)
#     print("here")
#
#     # Load the SAM model
#     sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
#     sam.to(device=device)
#     mask_generator = SamAutomaticMaskGenerator(sam)
#
#     # Process the input image data
#     image = cv2.cvtColor(input_image_data, cv2.COLOR_BGR2RGB)
#     width = int(image.shape[1] * 25 / 100)
#     height = int(image.shape[0]* 25 / 100)
#     size = width * height
#     image = cv2.resize(image, (width, height))
#     masks = mask_generator.generate(image)
#
#     def generate_anns(anns, image, size):
#         original_image = image
#         if len(anns) == 0:
#             return
#
#         sorted_anns = sorted(anns, key=(lambda x: x['area']), reverse=True)
#         img = np.ones((sorted_anns[0]['segmentation'].shape[0], sorted_anns[0]['segmentation'].shape[1], 4))
#         img[:, :, 3] = 0
#
#         for index, ann in enumerate(sorted_anns):
#             m = ann['segmentation']
#             if ann['area'] > size / 24 and ann['area'] < size / 2:
#                 img_tosave = np.where(m[..., None] == 1, original_image, 255)
#                 img_tosave = cv2.cvtColor(img_tosave, cv2.COLOR_BGR2RGB)
#                 output_filename = f"{index}_saved.png"
#                 output_path = os.path.join(output_dir, output_filename)
#                 cv2.imwrite(output_path, img_tosave)
#
#     generate_anns(masks, image, size)


# 数据平滑处理

