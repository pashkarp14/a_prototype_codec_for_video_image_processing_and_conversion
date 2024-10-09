##самый простой кодек видеообработки
#import shutil

#def encode_video(input_file, output_file):
#    # копируем исходное видеофайл
#    shutil.copyfile(input_file, output_file)

#def decode_video(input_file, output_file):
#    shutil.copyfile(input_file, output_file)

## пример использования
#encode_video('input_video.mp4', 'output_video_encoded.mp4')
#decode_video('output_video_encoded.mp4', 'output_video_decoded.mp4')






#+- рабочий вариант (видос получается без звука)
#from time import sleep
#from PIL import Image
#import os
#import imageio
#import numpy as np


#def encode_video(input_folder, output_folder):
#    # Проверяем, существует ли папка для выходных файлов
#    if not os.path.exists(output_folder):
#        os.makedirs(output_folder)

#    # Получаем список файлов в папке с видео
#    video_files = os.listdir(input_folder)

#    # Проходим по каждому файлу видео
#    for video_file in video_files:
#        # Проверяем, что файл является файлом видео (можно добавить проверку формата)
#        if video_file.endswith('.MP4'):
#            # Открываем видеофайл
#            video_path = os.path.join(input_folder, video_file)

#            # Создаем папку для текущего видео
#            video_output_folder = os.path.join(output_folder, video_file[:-4])
#            os.makedirs(video_output_folder, exist_ok=True)

#            # Считываем кадры видео и сохраняем их как изображения
#            with imageio.get_reader(video_path) as reader:
#                for i, frame in enumerate(reader):
#                    frame_img = Image.fromarray(frame)
#                    frame_path = os.path.join(video_output_folder, f'frame_{i}.jpg')
#                    frame_img.save(frame_path, quality=100)  # Устанавливаем качество JPEG

#def decode_video(input_folder, output_file):
#    # Получаем список папок с кадрами видео
#    video_folders = os.listdir(input_folder)

#    # Сортируем папки по именам
#    video_folders.sort()

#    # Создаем список для хранения кадров
#    frames = []

#    # Проходим по каждой папке с кадрами видео
#    for video_folder in video_folders:
#        frame_files = os.listdir(os.path.join(input_folder, video_folder))
#        frame_files.sort()

#        # Считываем и добавляем каждый кадр в список кадров
#        for frame_file in frame_files:
#            frame_path = os.path.join(input_folder, video_folder, frame_file)
#            frame = Image.open(frame_path)
#            frames.append(np.array(frame))

#    # Создаем видео из списка кадров
#    height, width, layers = frames[0].shape
#    writer = imageio.get_writer(output_file, fps=30)
#    for frame in frames:
#        writer.append_data(frame)
#    writer.close()


## Пример использования
#encode_video('input_videos_2', 'output_frames_2')
#decode_video('output_frames_2', 'output_video_encoded_2.mp4')


#не лагает видео, тоже без звука
#from PIL import Image
#import os
#import imageio
#import numpy as np
#from moviepy.editor import *

#def encode_video(input_folder, output_folder):
#    # Проверяем, существует ли папка для выходных файлов
#    if not os.path.exists(output_folder):
#        os.makedirs(output_folder)

#    # Получаем список файлов в папке с видео
#    video_files = os.listdir(input_folder)

#    # Проходим по каждому файлу видео
#    for video_file in video_files:
#        # Проверяем, что файл является файлом видео (можно добавить проверку формата)
#        if video_file.endswith('.MP4'):
#            # Открываем видеофайл
#            video_path = os.path.join(input_folder, video_file)

#            # Создаем папку для текущего видео
#            video_output_folder = os.path.join(output_folder, video_file[:-4])
#            os.makedirs(video_output_folder, exist_ok=True)

#            # Считываем кадры видео и сохраняем их как изображения
#            with imageio.get_reader(video_path) as reader:
#                for i, frame in enumerate(reader):
#                    frame_img = Image.fromarray(frame)
#                    frame_path = os.path.join(video_output_folder, f'frame_{i}.jpg')
#                    frame_img.save(frame_path, quality=100)  # Устанавливаем качество JPEG

#def decode_video(input_folder, output_file):
#    # Получаем список папок с кадрами видео
#    video_folders = os.listdir(input_folder)

#    # Сортируем папки по именам
#    video_folders.sort()

#    # Создаем список для хранения кадров
#    frames = []

#    # Проходим по каждой папке с кадрами видео
#    for video_folder in video_folders:
#        frame_files = os.listdir(os.path.join(input_folder, video_folder))

#        # Сортируем имена файлов кадров по числовому значению номера кадра
#        frame_files.sort(key=lambda x: int(x.split('_')[1].split('.')[0]))

#        # Считываем и добавляем каждый кадр в список кадров
#        for frame_file in frame_files:
#            frame_path = os.path.join(input_folder, video_folder, frame_file)
#            frame = Image.open(frame_path)
#            frames.append(np.array(frame))

#    # Создаем видео из списка кадров
#    height, width, layers = frames[0].shape
#    writer = imageio.get_writer(output_file, fps=30)

#    # Проверяем, есть ли кадры
#    if len(frames) == 0:
#        print("No frames found.")
#        return

#    # Записываем кадры в видео
#    for frame in frames:
#        writer.append_data(frame)
#    writer.close()
#    print(f'Decoding finished. Video saved to {output_file}')  # Выводим информацию о завершении декодирования

## Пример использования
#encode_video('input_videos_2', 'output_frames_2')
#decode_video('output_frames_2', 'output_video_encoded_with_audio_2.mp4') 


#выдает отдельно звук и видео
#import cv2
#import os
#import imageio
#import numpy as np
#from moviepy.editor import *
#from PIL import Image


#def encode_video(input_folder, output_folder):
#    # Проверяем, существует ли папка для выходных файлов
#    if not os.path.exists(output_folder):
#        os.makedirs(output_folder)

#    # Получаем список файлов в папке с видео
#    video_files = os.listdir(input_folder)

#    # Проходим по каждому файлу видео
#    for video_file in video_files:
#        # Проверяем, что файл является файлом видео (можно добавить проверку формата)
#        if video_file.endswith('.MP4'):
#            # Открываем видеофайл
#            video_path = os.path.join(input_folder, video_file)

#            # Создаем папку для текущего видео
#            video_output_folder = os.path.join(output_folder, video_file[:-4])
#            os.makedirs(video_output_folder, exist_ok=True)

#            # Считываем кадры видео и сохраняем их как изображения
#            with imageio.get_reader(video_path) as reader:
#                for i, frame in enumerate(reader):
#                    frame_img = Image.fromarray(frame)
#                    frame_path = os.path.join(video_output_folder, f'frame_{i}.jpg')
#                    frame_img.save(frame_path, quality=100)  # Устанавливаем качество JPEG

#def decode_video(input_folder, output_file):
#    # Получаем список папок с кадрами видео
#    video_folders = os.listdir(input_folder)

#    # Сортируем папки по именам
#    video_folders.sort()

#    # Создаем список для хранения кадров
#    frames = []

#    # Проходим по каждой папке с кадрами видео
#    for video_folder in video_folders:
#        frame_files = os.listdir(os.path.join(input_folder, video_folder))

#        # Сортируем имена файлов кадров по числовому значению номера кадра
#        frame_files.sort(key=lambda x: int(x.split('_')[1].split('.')[0]))

#        # Считываем и добавляем каждый кадр в список кадров
#        for frame_file in frame_files:
#            frame_path = os.path.join(input_folder, video_folder, frame_file)
#            frame = Image.open(frame_path)
#            frames.append(np.array(frame))

#    # Создаем видео из списка кадров
#    height, width, layers = frames[0].shape
#    writer = imageio.get_writer(output_file, fps=30)

#    # Проверяем, есть ли кадры
#    if len(frames) == 0:
#        print("No frames found.")
#        return

#    # Записываем кадры в видео
#    for frame in frames:
#        writer.append_data(frame)
#    writer.close()
#    print(f'Decoding finished. Video saved to {output_file}')  # Выводим информацию о завершении декодирования

#def add_audio(input_video, output_video):
#    # Извлекаем аудио из исходного видео
#    audio = AudioFileClip(input_video)
    
#    # Считаем кадры конечного видео
#    cap = cv2.VideoCapture(output_video)
#    fps = cap.get(cv2.CAP_PROP_FPS)
#    frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    
#    # Создаем объект VideoWriter для записи видео с аудио
#    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#    out = cv2.VideoWriter(output_video[:-4] + '_with_audio.mp4', fourcc, fps, frame_size)
    
#    # Записываем кадры с аудио
#    while True:
#        ret, frame = cap.read()
#        if not ret:
#            break
#        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # OpenCV читает в BGR, а moviepy требует RGB
#        out.write(frame)

#    # Добавляем аудио к видео
#    audio.write_audiofile(output_video[:-4] + '_audio.wav')
#    out.release()
#    cap.release()

## Пример использования
#encode_video('input_videos_2', 'output_frames_2')
#decode_video('output_frames_2', 'output_video_encoded_with_audio_2.mp4')
#add_audio('input_videos_2/input_video.MP4', 'output_video_encoded_with_audio_2.mp4')






#работая фул

import os
import imageio
import numpy as np
from moviepy.editor import *
from PIL import Image


def encode_video(input_folder, output_folder):
    # Проверяем, существует ли папка для выходных файлов
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Получаем список файлов в папке с видео
    video_files = os.listdir(input_folder)

    # Проходим по каждому файлу видео
    for video_file in video_files:
        # Проверяем, что файл является файлом видео (можно добавить проверку формата)
        if video_file.endswith('.MP4'):
            # Открываем видеофайл
            video_path = os.path.join(input_folder, video_file)

            # Создаем папку для текущего видео
            video_output_folder = os.path.join(output_folder, video_file[:-4])
            os.makedirs(video_output_folder, exist_ok=True)

            # Считываем кадры видео и сохраняем их как изображения
            with imageio.get_reader(video_path) as reader:
                for i, frame in enumerate(reader):
                    frame_img = Image.fromarray(frame)
                    frame_path = os.path.join(video_output_folder, f'frame_{i}.jpg')
                    frame_img.save(frame_path, quality=100)  # Устанавливаем качество JPEG

def decode_video(input_folder, output_file):
    # Получаем список папок с кадрами видео
    video_folders = os.listdir(input_folder)

    # Сортируем папки по именам
    video_folders.sort()

    # Создаем список для хранения кадров
    frames = []

    # Проходим по каждой папке с кадрами видео
    for video_folder in video_folders:
        frame_files = os.listdir(os.path.join(input_folder, video_folder))

        # Сортируем имена файлов кадров по числовому значению номера кадра
        frame_files.sort(key=lambda x: int(x.split('_')[1].split('.')[0]))

        # Считываем и добавляем каждый кадр в список кадров
        for frame_file in frame_files:
            frame_path = os.path.join(input_folder, video_folder, frame_file)
            frame = Image.open(frame_path)
            frames.append(np.array(frame))

    # Создаем видео из списка кадров
    height, width, layers = frames[0].shape
    writer = imageio.get_writer(output_file, fps=30)

    # Проверяем, есть ли кадры
    if len(frames) == 0:
        print("No frames found.")
        return

    # Записываем кадры в видео
    for frame in frames:
        writer.append_data(frame)
    writer.close()
    print(f'Decoding finished. Video saved to {output_file}')  # Выводим информацию о завершении декодирования

def add_audio(input_video, output_video):
    # Извлекаем аудио из исходного видео
    audio = AudioFileClip(input_video)
    
    # Создаем объект VideoFileClip для видео
    video = VideoFileClip(output_video)
    
    # Объединяем видео и аудио
    final_clip = video.set_audio(audio)
    
    # Сохраняем объединенный клип
    final_clip.write_videofile(output_video[:-4] + '_with_audio.mp4', codec='libx264', audio_codec='aac')

# Пример использования
encode_video('input_videos_2', 'output_frames_2')
decode_video('output_frames_2', 'output_video_encoded_with_audio_2.mp4')
add_audio('input_videos_2/input_video.MP4', 'output_video_encoded_with_audio_2.mp4')


