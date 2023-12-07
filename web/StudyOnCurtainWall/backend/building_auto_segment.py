import numpy as np
import torch
import matplotlib.pyplot as plt
import cv2
import os
from segment_anything import sam_model_registry, SamAutomaticMaskGenerator

# config
image_dir = 'media/img'  # 存放图片的目录
output_dir = 'segged'  # 存放输出图片的目录
sam_checkpoint = "sam_vit_h_4b8939.pth"
model_type = "vit_h"
if(torch.cuda.is_available()):
    device = "cuda"
else:
    device = "cpu"

# read the image
os.makedirs(output_dir, exist_ok=True)
# image = cv2.imread(image_path)
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_files = [f for f in os.listdir(image_dir) if (f.endswith('.jpg') or f.endswith('.JPG'))]

# use the model
sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
sam.to(device=device)
# mask_generator = SamAutomaticMaskGenerator(
#     model=sam,
#     points_per_side=20,
#     # pred_iou_thresh=0.86,
# )
mask_generator = SamAutomaticMaskGenerator(sam)

# generate segmented images
def generate_anns(anns, image, size):
    original_image = image
    if len(anns) == 0:
        return
    sorted_anns = sorted(anns, key=(lambda x: x['area']), reverse=True)     # 按照 area 大小排序，从大到小
    ax = plt.gca()
    ax.set_autoscale_on(False)

    img = np.ones((sorted_anns[0]['segmentation'].shape[0], sorted_anns[0]['segmentation'].shape[1], 4))        # 先开一个四个通道全是 True 的数组，长宽分别为原矩阵
    img[:,:,3] = 0  # set the alpha channel to 0
    
    for index, ann in enumerate(sorted_anns):

        m = ann['segmentation']     # m 是一个矩阵，里面有 True 和 False
        print(ann['area'])
        if ann['area'] > size / 24 and ann['area'] < size / 2:
            # 把原来的图片根据掩码 复制到 img_tosave 中
            img_tosave = np.where(m[..., None] == 1, original_image, 255)
            img_tosave = cv2.cvtColor(img_tosave, cv2.COLOR_BGR2RGB)
            output_filename = f"{os.path.splitext(image_file)[0]}_{index}_saved.png"  # 构建输出文件名
            output_path = os.path.join(output_dir, output_filename)  # 构建输出文件路径
            cv2.imwrite(output_path, img_tosave)

        # color_mask = np.concatenate([np.random.random(3), [0.35]])  # concatenate 拼接通道，0.35作为透明度，这样直接覆盖在原图上
        # img[m] = color_mask     # 布尔索引法，也即通过 True 和 False 来对指定像素点应用颜色


for image_file in image_files:  # 通常做法就是遍历文件名之后拼接
    image_path = os.path.join(image_dir, image_file)
    # 读取图像
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    width = int(image.shape[1] * 25 / 100)
    height = int(image.shape[0] * 25 / 100)

    size = width * height
    image  = cv2.resize(image, (width, height))
    masks = mask_generator.generate(image)
    generate_anns(masks, image, size)
