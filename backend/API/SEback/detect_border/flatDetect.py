import subprocess
import os
import cv2
import matplotlib.pyplot as plt
import flat


def run_inference(image_path, save_dir):
    # 提取文件名（不包含扩展名）
    base_filename = os.path.splitext(os.path.basename(image_path))[0]

    # 构建结果保存路径
    result_path = os.path.join(save_dir, f"{base_filename}.png")

    # 构建推理命令
    command = f"python /root/code/SoftWare_Project/backend/API/SEback/detect_border/deploy/python/infer.py --config /root/code/SoftWare_Project/backend/API/SEback/detect_border/inference_model/deploy.yaml --image_path {image_path} --save_dir {save_dir}"

    try:
        subprocess.run(command, shell=True, check=True)
        print("Inference completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during inference: {e}")

    # 返回结果保存路径
    return result_path

# 结构胶检测及平整度检测
def border_flat_detect(image_path, save_dir="output"):
    # 结构胶检测
    
    result_path = run_inference(image_path, save_dir)
    print("ssss")
    # 平整度检测
    original_image, overlay_result_on_original, marked_image, horizontal_parallel, vertical_parallel = flat.detect(
        image_path, result_path)

    # 返回原始图像，结构胶检测图像，边缘拟合后的图像，水平方向直线平行关系和竖直方向直线平行关系
    return original_image, overlay_result_on_original, marked_image, horizontal_parallel, vertical_parallel


# 测试部分
# if __name__ == "__main__":
#     # 设置图片路径和存储路径
#     image_path = "2023_200003.jpg"
#     # save_dir = "output"

#     # 结构胶检测及平整度检测
#     original_image, overlay_result_on_original, marked_image, horizontal_parallel, vertical_parallel = \
#         border_flat_detect(image_path)

#     # 显示检测结果
#     fig, axs = plt.subplots(1, 3, figsize=(15, 5))

#     # 显示原始图像
#     axs[0].imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
#     axs[0].set_title("origin image")
#     axs[0].axis('off')

#     # 显示结构胶检测的图像
#     axs[1].imshow(cv2.cvtColor(overlay_result_on_original, cv2.COLOR_BGR2RGB))
#     axs[1].set_title("detected image")
#     axs[1].axis('off')

#     # 显示边缘拟合后图像
#     axs[2].imshow(cv2.cvtColor(marked_image, cv2.COLOR_BGR2RGB))
#     axs[2].set_title("marked image")
#     axs[2].axis('off')

#     # 在图像下方添加横向和竖向线条是否平行的检测结果
#     fig.text(0.5, 0.1, f'Horizontal Parallel: {horizontal_parallel}   |   Vertical Parallel: {vertical_parallel}',
#              ha='center', va='center')

#     plt.tight_layout()
#     plt.show()
