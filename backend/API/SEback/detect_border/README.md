# 结构胶检测

## 1 环境要求

我使用的conda创建的虚拟环境：

```
conda create -n paddleseg python=3.10
conda activate paddleseg
```

我是在上述paddleseg环境中配置的环境，也可以直接配置。

#### 1.1 安装PaddlePaddle

安装链接：https://www.paddlepaddle.org.cn/install/quick

这里我使用的2.5的gpu版本

```
python -m pip install paddlepaddle-gpu==2.5.2.post120 -f https://www.paddlepaddle.org.cn/whl/windows/mkl/avx/stable.html
```

#### 1.2 安装PaddlePaddle

执行如下命令，安装发布的PaddleSeg包。

```
pip install paddleseg
```

## 2 运行程序

有两种运行程序的方式：可以通过cmd运行，也可以通过我写的python文件运行。

#### 2.1 命令行运行

在上面创建的paddleseg虚拟环境中，在detect_border根目录，执行以下命令进行检测：

```
python deploy/python/infer.py \
    --config inference_model/deploy.yaml \
    --image_path <图片路径> \
    --save_dir <存储路径> 
```

可以使用我提供的2023_200003.jpg图片进行测试，将结果保存在output文件夹中：

```
python deploy/python/infer.py --config inference_model/deploy.yaml --image_path 2023_200003.jpg --save_dir output
```

#### 2.2 python文件运行

可以使用run.py文件运行检测程序，python解释器需要选择上面创建的paddleseg虚拟环境。

直接运行run.py文件会使用我提供的2023_200003.jpg图片进行测试，结果保存在output文件夹中。

可以在run.py文件内修改图片路径和存储路径。

------

## 运行更新

调用run.py中的`border_flat_detect(image_path, save_dir="output")`函数就可以直接执行结构胶检测和平整度检测。

参数说明：

- image_path：图片路径。由你给出
- save_dir：结构胶检测结果图片保存路径。默认值为save_dir = "output"，即结果图片将保存在当前文件夹下的output文件夹中。如果不指定将直接使用默认值，可以参考代码中测试部分的使用方法。

返回值说明：

- original_image：原始图像
- overlay_result_on_original：结构胶检测的图像
- marked_image：边缘拟合后图像
- horizontal_parallel：水平方向直线平行关系
- vertical_parallel：竖直方向直线平行关系

其中`original_image`、`overlay_result_on_original`、`marked_image` 是 NumPy 数组，相当于`cv2.imread()` 读取图像后返回的结果。

如果需要保存图像可以调用完该函数再对相关图片进行保存；或者在`border_flat_detect`函数进行保存，将返回值修改为图像对应的保存路径。**这里请根据后端图像存储及传输需求自行修改。**

`horizontal_parallel`和 `vertical_parallel`是bool值，即为True或False。

#### 补充说明

直接运行run.py会显示我给出的测试结果，即`if __name__ == "__main__"`下的内容。如果只是调用`border_flat_detect`函数将不会运行测试内容。