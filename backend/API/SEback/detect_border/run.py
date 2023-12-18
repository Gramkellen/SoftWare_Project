import subprocess


def run_inference(image_path, save_dir):
    command = f"python deploy/python/infer.py --config inference_model/deploy.yaml --image_path {image_path} --save_dir {save_dir}"

    try:
        subprocess.run(command, shell=True, check=True)
        print("Inference completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during inference: {e}")


if __name__ == "__main__":
    # 设置图片路径和存储路径
    image_path = "2023_200003.jpg"
    save_dir = "output"

    run_inference(image_path, save_dir)
