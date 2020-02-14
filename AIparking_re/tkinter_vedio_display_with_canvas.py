# coding:utf-8
__author__ = 'zhangsiqi'
__date__ = '2020/2/8 23:23'

import tkinter as tk
from PIL import Image, ImageTk
import cv2
import numpy as np
from hyperlpr import pipline as pp

cap = cv2.VideoCapture(0 + cv2.CAP_DSHOW)  # 摄像头


def close_window():
    global cap
    cap.release()
    cv2.destroyAllWindows()
    win.destroy()


def video_init():
    global cap
    cap.set(3, 640)
    cap.set(4, 480)
    return cap


def video_show():
    global cap
    cap = video_init()
    while True:
        ret, frame = cap.read()
        if ret:
            # 反转图片
            # frame = cv2.flip(frame, 1)
            # 将图像的通道顺序由BGR转换成RGB
            # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image, res, img_str = pp.SimpleRecognizePlate(frame)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # cv2.imshow("carPlate", image)
            if isinstance(image, np.ndarray):
                image = Image.fromarray(image.astype(np.uint8))
                print("进入is instances.")
            photo = ImageTk.PhotoImage(image=image)
            image_cvs.create_image([320, 240], image=photo)
            print(res, end="")
            print(img_str)
            win.update_idletasks()
            win.update()


if __name__ == '__main__':
    win = tk.Tk()
    image_cvs = tk.Canvas(win, width=640, height=480, bg='white')
    image_cvs.pack()

    # 点击界面右上角的关闭按钮时，会触发'WM_DELETE_WINDOW'消息
    # 我们在此截获该消息，并改变其行为
    win.protocol('WM_DELETE_WINDOW', close_window)

    win.after(200, video_show)
    win.mainloop()
