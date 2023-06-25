import cv2
import numpy as np
import os


def generate_screenshots(video_path, threshold=1000000):

    video = cv2.VideoCapture(video_path)
    ret, frame = video.read()

    output_folder = "screenshots"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    frame_count = 0
    while video.isOpened():
        ret, next_frame = video.read()

        # Если фреймов больше нет, то выходим из цикла
        if not ret:
            break

        diff = cv2.absdiff(frame, next_frame)
        non_zero_count = np.count_nonzero(diff)

        if non_zero_count > threshold:
            cv2.imwrite(os.path.join(output_folder,
                        f'screenshot_{frame_count}.png'), frame)

        frame = next_frame
        frame_count += 1

    video.release()


# использование функции
generate_screenshots('video.mp4', threshold=1000000)
