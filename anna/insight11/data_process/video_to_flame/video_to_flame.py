import cv2
import os
import shutil

# 设置输入文件夹和输出文件夹的路径
input_folder = '/home/ljh/v8/yolov8_tracking/datasets/tumor'
output_folder = '/home/ljh/v8/anna/insight11/output/tumor_images'

# 遍历输入文件夹中的所有视频文件
for file_name in os.listdir(input_folder):
    if file_name.endswith('.mp4') or file_name.endswith('.avi'):

        # 创建输出文件夹
        output_path = os.path.join(output_folder, file_name[:-4])
        os.makedirs(output_path, exist_ok=True)

        # 打开视频文件
        cap = cv2.VideoCapture(os.path.join(input_folder, file_name))

        # 获取视频的帧率和总帧数
        fps = cap.get(cv2.CAP_PROP_FPS)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        # 循环遍历视频的每一帧
        for i in range(total_frames):
            ret, frame = cap.read()

            # 如果成功读取一帧，就将它保存到输出文件夹中
            if ret:
                frame_path = os.path.join(output_path, f'frame_{i:06d}.jpg')
                cv2.imwrite(frame_path, frame)
            else:
                break

        # 释放视频对象
        cap.release()

        # 将输出文件夹移动到更大的文件夹中
        shutil.move(output_path, os.path.join(output_folder, file_name[:-4]))
