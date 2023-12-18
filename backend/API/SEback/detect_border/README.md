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