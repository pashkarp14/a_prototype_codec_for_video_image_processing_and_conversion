##����� ������� ����� ��������������
#import shutil

#def encode_video(input_file, output_file):
#    # �������� �������� ���������
#    shutil.copyfile(input_file, output_file)

#def decode_video(input_file, output_file):
#    shutil.copyfile(input_file, output_file)

## ������ �������������
#encode_video('input_video.mp4', 'output_video_encoded.mp4')
#decode_video('output_video_encoded.mp4', 'output_video_decoded.mp4')






#+- ������� ������� (����� ���������� ��� �����)
#from time import sleep
#from PIL import Image
#import os
#import imageio
#import numpy as np


#def encode_video(input_folder, output_folder):
#    # ���������, ���������� �� ����� ��� �������� ������
#    if not os.path.exists(output_folder):
#        os.makedirs(output_folder)

#    # �������� ������ ������ � ����� � �����
#    video_files = os.listdir(input_folder)

#    # �������� �� ������� ����� �����
#    for video_file in video_files:
#        # ���������, ��� ���� �������� ������ ����� (����� �������� �������� �������)
#        if video_file.endswith('.MP4'):
#            # ��������� ���������
#            video_path = os.path.join(input_folder, video_file)

#            # ������� ����� ��� �������� �����
#            video_output_folder = os.path.join(output_folder, video_file[:-4])
#            os.makedirs(video_output_folder, exist_ok=True)

#            # ��������� ����� ����� � ��������� �� ��� �����������
#            with imageio.get_reader(video_path) as reader:
#                for i, frame in enumerate(reader):
#                    frame_img = Image.fromarray(frame)
#                    frame_path = os.path.join(video_output_folder, f'frame_{i}.jpg')
#                    frame_img.save(frame_path, quality=100)  # ������������� �������� JPEG

#def decode_video(input_folder, output_file):
#    # �������� ������ ����� � ������� �����
#    video_folders = os.listdir(input_folder)

#    # ��������� ����� �� ������
#    video_folders.sort()

#    # ������� ������ ��� �������� ������
#    frames = []

#    # �������� �� ������ ����� � ������� �����
#    for video_folder in video_folders:
#        frame_files = os.listdir(os.path.join(input_folder, video_folder))
#        frame_files.sort()

#        # ��������� � ��������� ������ ���� � ������ ������
#        for frame_file in frame_files:
#            frame_path = os.path.join(input_folder, video_folder, frame_file)
#            frame = Image.open(frame_path)
#            frames.append(np.array(frame))

#    # ������� ����� �� ������ ������
#    height, width, layers = frames[0].shape
#    writer = imageio.get_writer(output_file, fps=30)
#    for frame in frames:
#        writer.append_data(frame)
#    writer.close()


## ������ �������������
#encode_video('input_videos_2', 'output_frames_2')
#decode_video('output_frames_2', 'output_video_encoded_2.mp4')


#�� ������ �����, ���� ��� �����
#from PIL import Image
#import os
#import imageio
#import numpy as np
#from moviepy.editor import *

#def encode_video(input_folder, output_folder):
#    # ���������, ���������� �� ����� ��� �������� ������
#    if not os.path.exists(output_folder):
#        os.makedirs(output_folder)

#    # �������� ������ ������ � ����� � �����
#    video_files = os.listdir(input_folder)

#    # �������� �� ������� ����� �����
#    for video_file in video_files:
#        # ���������, ��� ���� �������� ������ ����� (����� �������� �������� �������)
#        if video_file.endswith('.MP4'):
#            # ��������� ���������
#            video_path = os.path.join(input_folder, video_file)

#            # ������� ����� ��� �������� �����
#            video_output_folder = os.path.join(output_folder, video_file[:-4])
#            os.makedirs(video_output_folder, exist_ok=True)

#            # ��������� ����� ����� � ��������� �� ��� �����������
#            with imageio.get_reader(video_path) as reader:
#                for i, frame in enumerate(reader):
#                    frame_img = Image.fromarray(frame)
#                    frame_path = os.path.join(video_output_folder, f'frame_{i}.jpg')
#                    frame_img.save(frame_path, quality=100)  # ������������� �������� JPEG

#def decode_video(input_folder, output_file):
#    # �������� ������ ����� � ������� �����
#    video_folders = os.listdir(input_folder)

#    # ��������� ����� �� ������
#    video_folders.sort()

#    # ������� ������ ��� �������� ������
#    frames = []

#    # �������� �� ������ ����� � ������� �����
#    for video_folder in video_folders:
#        frame_files = os.listdir(os.path.join(input_folder, video_folder))

#        # ��������� ����� ������ ������ �� ��������� �������� ������ �����
#        frame_files.sort(key=lambda x: int(x.split('_')[1].split('.')[0]))

#        # ��������� � ��������� ������ ���� � ������ ������
#        for frame_file in frame_files:
#            frame_path = os.path.join(input_folder, video_folder, frame_file)
#            frame = Image.open(frame_path)
#            frames.append(np.array(frame))

#    # ������� ����� �� ������ ������
#    height, width, layers = frames[0].shape
#    writer = imageio.get_writer(output_file, fps=30)

#    # ���������, ���� �� �����
#    if len(frames) == 0:
#        print("No frames found.")
#        return

#    # ���������� ����� � �����
#    for frame in frames:
#        writer.append_data(frame)
#    writer.close()
#    print(f'Decoding finished. Video saved to {output_file}')  # ������� ���������� � ���������� �������������

## ������ �������������
#encode_video('input_videos_2', 'output_frames_2')
#decode_video('output_frames_2', 'output_video_encoded_with_audio_2.mp4') 


#������ �������� ���� � �����
#import cv2
#import os
#import imageio
#import numpy as np
#from moviepy.editor import *
#from PIL import Image


#def encode_video(input_folder, output_folder):
#    # ���������, ���������� �� ����� ��� �������� ������
#    if not os.path.exists(output_folder):
#        os.makedirs(output_folder)

#    # �������� ������ ������ � ����� � �����
#    video_files = os.listdir(input_folder)

#    # �������� �� ������� ����� �����
#    for video_file in video_files:
#        # ���������, ��� ���� �������� ������ ����� (����� �������� �������� �������)
#        if video_file.endswith('.MP4'):
#            # ��������� ���������
#            video_path = os.path.join(input_folder, video_file)

#            # ������� ����� ��� �������� �����
#            video_output_folder = os.path.join(output_folder, video_file[:-4])
#            os.makedirs(video_output_folder, exist_ok=True)

#            # ��������� ����� ����� � ��������� �� ��� �����������
#            with imageio.get_reader(video_path) as reader:
#                for i, frame in enumerate(reader):
#                    frame_img = Image.fromarray(frame)
#                    frame_path = os.path.join(video_output_folder, f'frame_{i}.jpg')
#                    frame_img.save(frame_path, quality=100)  # ������������� �������� JPEG

#def decode_video(input_folder, output_file):
#    # �������� ������ ����� � ������� �����
#    video_folders = os.listdir(input_folder)

#    # ��������� ����� �� ������
#    video_folders.sort()

#    # ������� ������ ��� �������� ������
#    frames = []

#    # �������� �� ������ ����� � ������� �����
#    for video_folder in video_folders:
#        frame_files = os.listdir(os.path.join(input_folder, video_folder))

#        # ��������� ����� ������ ������ �� ��������� �������� ������ �����
#        frame_files.sort(key=lambda x: int(x.split('_')[1].split('.')[0]))

#        # ��������� � ��������� ������ ���� � ������ ������
#        for frame_file in frame_files:
#            frame_path = os.path.join(input_folder, video_folder, frame_file)
#            frame = Image.open(frame_path)
#            frames.append(np.array(frame))

#    # ������� ����� �� ������ ������
#    height, width, layers = frames[0].shape
#    writer = imageio.get_writer(output_file, fps=30)

#    # ���������, ���� �� �����
#    if len(frames) == 0:
#        print("No frames found.")
#        return

#    # ���������� ����� � �����
#    for frame in frames:
#        writer.append_data(frame)
#    writer.close()
#    print(f'Decoding finished. Video saved to {output_file}')  # ������� ���������� � ���������� �������������

#def add_audio(input_video, output_video):
#    # ��������� ����� �� ��������� �����
#    audio = AudioFileClip(input_video)
    
#    # ������� ����� ��������� �����
#    cap = cv2.VideoCapture(output_video)
#    fps = cap.get(cv2.CAP_PROP_FPS)
#    frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    
#    # ������� ������ VideoWriter ��� ������ ����� � �����
#    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#    out = cv2.VideoWriter(output_video[:-4] + '_with_audio.mp4', fourcc, fps, frame_size)
    
#    # ���������� ����� � �����
#    while True:
#        ret, frame = cap.read()
#        if not ret:
#            break
#        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # OpenCV ������ � BGR, � moviepy ������� RGB
#        out.write(frame)

#    # ��������� ����� � �����
#    audio.write_audiofile(output_video[:-4] + '_audio.wav')
#    out.release()
#    cap.release()

## ������ �������������
#encode_video('input_videos_2', 'output_frames_2')
#decode_video('output_frames_2', 'output_video_encoded_with_audio_2.mp4')
#add_audio('input_videos_2/input_video.MP4', 'output_video_encoded_with_audio_2.mp4')






#������� ���

import os
import imageio
import numpy as np
from moviepy.editor import *
from PIL import Image


def encode_video(input_folder, output_folder):
    # ���������, ���������� �� ����� ��� �������� ������
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # �������� ������ ������ � ����� � �����
    video_files = os.listdir(input_folder)

    # �������� �� ������� ����� �����
    for video_file in video_files:
        # ���������, ��� ���� �������� ������ ����� (����� �������� �������� �������)
        if video_file.endswith('.MP4'):
            # ��������� ���������
            video_path = os.path.join(input_folder, video_file)

            # ������� ����� ��� �������� �����
            video_output_folder = os.path.join(output_folder, video_file[:-4])
            os.makedirs(video_output_folder, exist_ok=True)

            # ��������� ����� ����� � ��������� �� ��� �����������
            with imageio.get_reader(video_path) as reader:
                for i, frame in enumerate(reader):
                    frame_img = Image.fromarray(frame)
                    frame_path = os.path.join(video_output_folder, f'frame_{i}.jpg')
                    frame_img.save(frame_path, quality=100)  # ������������� �������� JPEG

def decode_video(input_folder, output_file):
    # �������� ������ ����� � ������� �����
    video_folders = os.listdir(input_folder)

    # ��������� ����� �� ������
    video_folders.sort()

    # ������� ������ ��� �������� ������
    frames = []

    # �������� �� ������ ����� � ������� �����
    for video_folder in video_folders:
        frame_files = os.listdir(os.path.join(input_folder, video_folder))

        # ��������� ����� ������ ������ �� ��������� �������� ������ �����
        frame_files.sort(key=lambda x: int(x.split('_')[1].split('.')[0]))

        # ��������� � ��������� ������ ���� � ������ ������
        for frame_file in frame_files:
            frame_path = os.path.join(input_folder, video_folder, frame_file)
            frame = Image.open(frame_path)
            frames.append(np.array(frame))

    # ������� ����� �� ������ ������
    height, width, layers = frames[0].shape
    writer = imageio.get_writer(output_file, fps=30)

    # ���������, ���� �� �����
    if len(frames) == 0:
        print("No frames found.")
        return

    # ���������� ����� � �����
    for frame in frames:
        writer.append_data(frame)
    writer.close()
    print(f'Decoding finished. Video saved to {output_file}')  # ������� ���������� � ���������� �������������

def add_audio(input_video, output_video):
    # ��������� ����� �� ��������� �����
    audio = AudioFileClip(input_video)
    
    # ������� ������ VideoFileClip ��� �����
    video = VideoFileClip(output_video)
    
    # ���������� ����� � �����
    final_clip = video.set_audio(audio)
    
    # ��������� ������������ ����
    final_clip.write_videofile(output_video[:-4] + '_with_audio.mp4', codec='libx264', audio_codec='aac')

# ������ �������������
encode_video('input_videos_2', 'output_frames_2')
decode_video('output_frames_2', 'output_video_encoded_with_audio_2.mp4')
add_audio('input_videos_2/input_video.MP4', 'output_video_encoded_with_audio_2.mp4')


