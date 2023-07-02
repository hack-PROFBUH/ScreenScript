import cv2
import os


def generate_screenshots(video_path, screenshot_interval=10):

    video = cv2.VideoCapture(video_path)
    fps = video.get(cv2.CAP_PROP_FPS)
    frame_count = 0

    output_folder = "screenshots"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    while video.isOpened():
        success, frame = video.read()

        # Если фреймов больше нет, то выходим из цикла
        if not success:
            break

        # Если текущий фрейм кратен числу кадров в интервале, то сохраняем его как скриншот
        if frame_count % (fps * screenshot_interval) == 0:
            cv2.imwrite(os.path.join(output_folder,
                        f'screenshot_{frame_count // fps}.png'), frame)

        frame_count += 1

    video.release()


# использование функции
generate_screenshots('video.mp4', screenshot_interval=10)
