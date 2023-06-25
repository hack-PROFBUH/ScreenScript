import numpy as np
import os
iimport cv2


def mse(imageA, imageB):
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err


def generate_screenshots(video_path, screenshot_interval=10, mse_threshold=500):

    video = cv2.VideoCapture(video_path)
    fps = video.get(cv2.CAP_PROP_FPS)
    frame_count = 0

    output_folder = "screenshots"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    previous_frame = None
    while video.isOpened():
        success, frame = video.read()

        # Если фреймов больше нет, то выходим из цикла
        if not success:
            break

        # Если текущий фрейм кратен числу кадров в интервале, то проверяем его на схожесть с предыдущим
        if frame_count % (fps * screenshot_interval) == 0:
            if previous_frame is not None and mse(previous_frame, frame) < mse_threshold:
                cv2.imwrite(os.path.join(output_folder,
                            f'screenshot_{frame_count // fps}.png'), frame)
            previous_frame = frame

        frame_count += 1

    video.release()

generate_screenshots('video.mp4', screenshot_interval=30)
