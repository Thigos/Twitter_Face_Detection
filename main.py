import firefox_downloader as fox_downloader
import twitter_scraping
import cv2
import argparse
import os
from unidecode import unidecode

args = argparse.ArgumentParser()
args.add_argument('-p', '--path', nargs='?', const='', default='query.txt')

FACE_CASCADE = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')


def save_frame(frame, path, nameImage):
    if not os.path.exists(path):
        os.mkdir(path)

    saved = cv2.imwrite(path + nameImage, frame)

    if saved:
        print("File Saved!", path + nameImage)
    else:
        print("File Save Status", saved, path + nameImage)


def video_read(cap, key):
    count = 0
    key = unidecode(key.replace(' ', '_'))
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = FACE_CASCADE.detectMultiScale(gray)

        contains_face_in_image = False

        for i, (x, y, w, h) in enumerate(faces):
            tl = (x, y)  # TOP LEFT
            br = (x + w, y + h)  # BOTTOM RIGHT

            cv2.rectangle(frame, tl, br, (80, 47, 245), 2)

            cv2.imshow("Video_face_cropped", frame[y:y + h, x:x + w])

            save_frame(frame[y:y + h, x:x + w], "data/" + key + "_face_crop", "/frame_("+str(count)+")_face_" + str(i) + ".png")

            contains_face_in_image = True

        count += 1

        if contains_face_in_image:
            save_frame(frame, "data/" + key, "/frame_" + str(count) + ".png")

        cv2.imshow("Video", frame)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    cap.release()


def main():
    fox_downloader.install()
    list_videos = twitter_scraping.start(args.parse_args().path)

    for key in list_videos:
        print(key)
        cap = cv2.VideoCapture(list_videos[key])

        video_read(cap, key)


cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
