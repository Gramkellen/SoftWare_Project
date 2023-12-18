#构建整个流程尝试
import cv2
from matplotlib import pyplot as plt
import torch
from torchvision.models import resnet18
from torchvision import transforms
import torch.nn as nn
import os
import glob
from PIL import Image

def Classify(filename):
     #--------------------进行幕墙分割---------------------#
    # cv2.imread()用于读取图片文件
    filename = os.path.normpath(filename)
    image = cv2.imread(filename)

    # cv2.COLOR_BGR2GRAY 将BGR格式转换成灰度图片
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # otsu图像分割为前景和背景
    ret1, th1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
    
    # 提取前景部分 - glass graph
    glassphoto = cv2.bitwise_and(image, image, mask=th1)
    #添加绘制，可删除后期
    # plt.imshow(glassphoto, cmap='gray'), plt.title('Glass')
    # plt.show()
    #--------------------进行幕墙检测---------------------#
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    #device = torch.device('cpu')
    img_size = 224
    class_names = ["class_0", "class_1"]
    model = resnet18()
    channel_in = model.fc.in_features
    
    model.fc = nn.Sequential(nn.Linear(channel_in,2))
    model.to(device)

    #这里加载已经训练好的模型出错的了：
    #model.load_state_dict(torch.load("./resnet18-2Class.pth")) #路径需要修改
    print("1111")
    #/root/code/SoftWare_Project/backend/API/SEback/New-resnet18-2Class.pth
    model.load_state_dict(torch.load("/root/code/SoftWare_Project/backend/API/SEback/New-resnet18-2Class.pth")) #路径需要修改
    #这里需要Debug
    #下面部分没有问题
    print("pppppppppppppppppppppppppppp")
    model.eval()
    print("ccc")
    with torch.no_grad():
        tf = transforms.Compose([
                    lambda x: x.convert('RGB'),
                    transforms.Resize((img_size, img_size)),
                    transforms.ToTensor(),
                    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                         std=[0.229, 0.224, 0.225])
                ])
        #将openCV的照片格式转化成为PIL中IMAGE的照片形式
        image_rgb = cv2.cvtColor(glassphoto, cv2.COLOR_BGR2RGB)
        image_pil = Image.fromarray(image_rgb)
        img = tf(image_pil).unsqueeze(0)
        pred = model(img.to(device))
        cls_id = pred.argmax(dim=1).item()
        print("pred: ", pred, "\ncls: ", cls_id)
        if(cls_id == 0):
            print("完整玻璃\n")
            return True
        else:
             print("碎玻璃\n")
             return False