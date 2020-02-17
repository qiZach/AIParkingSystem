# coding:utf-8
__author__ = 'zhangsiqi'
__date__ = '2020/2/8 17:42'

import cv2
import time
import webbrowser
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import *
from PIL import Image, ImageTk
from collections import Counter
import threading
from hyperlpr import pipline as pp


class Surface(ttk.Frame):
    camera = None
    camera_flag = False
    is_running = True
    list = []
    block_list = []
    count = 50
    EdgePath = r'C:\Users\zhangsiqi\AppData\Local\Microsoft\Edge\Application\msedge.exe'

    def __init__(self, window):
        ttk.Frame.__init__(self, window)
        # 左边显示图片框架
        frame_left = ttk.Frame(self)
        # 右边定位框架
        frame_right1 = ttk.Frame(self)
        # 右边按钮框架
        frame_right2 = ttk.Frame(self)
        window.title("车牌识别")
        window.minsize(750, 600)
        # 将窗口放在屏幕中央
        self.center_window()
        self.pack(fill=tk.BOTH, expand=tk.YES, padx="10", pady="10")
        # 左侧摄像头，右侧： right1 定位车牌及车牌号  right2 按钮位置
        frame_left.pack(side=LEFT, expand=1)
        frame_right1.pack(side=TOP, expand=1, fill=tk.Y)
        frame_right2.pack(side=RIGHT, expand=0)

        # 创建左侧摄像头画布
        self.image_ctl = tk.Canvas(frame_left, width=640, height=480,
                                   bg='white')
        self.image_ctl.pack()

        # 车牌识别结果
        ttk.Label(frame_right1, text='定位识别结果：').grid(column=0, row=2,
                                                     sticky=tk.W)
        self.r_ctl = ttk.Label(frame_right1, text="", font=('Times', '20'))
        self.r_ctl.grid(column=0, row=3, sticky=tk.W)

        # 车牌定位图片
        ttk.Label(frame_right1, text='定位车牌位置：').grid(column=0, row=0,
                                                     sticky=tk.W)
        self.roi_ctl = ttk.Label(frame_right1)
        self.roi_ctl.grid(column=0, row=1, sticky=tk.W)

        # 控制按钮
        from_video_time = ttk.Button(frame_right2, text="开关摄像头实时识别", width=20,
                                     command=self.from_video)
        from_video_time.pack(anchor="se", pady="5")

    def center_window(self):
        screenwidth = win.winfo_screenwidth()
        screenheight = win.winfo_screenheight()
        win.update()
        width = win.winfo_width()
        height = win.winfo_height()
        size = '+%d+%d' % (
            (screenwidth - width) / 2, (screenheight - height) / 2)
        win.geometry(size)

    def from_video(self):
        # 摄像头打开就关掉
        if self.camera_flag:
            self.close_video()
            return
        # 摄像头
        self.camera = cv2.VideoCapture(0 + cv2.CAP_DSHOW)
        self.camera_flag = True
        # 初始化时打开清空屏蔽名单
        threading.Thread(target=self.clear_block_list).start()
        while self.camera_flag:
            ret, frame = self.camera.read()
            if ret:
                image, res, img_str = pp.SimpleRecognizePlate(frame)
                self.add_res_to_list(res)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                if isinstance(image, np.ndarray):
                    image = Image.fromarray(image.astype(np.uint8))
                photo = ImageTk.PhotoImage(image=image)
                self.image_ctl.create_image([320, 240], image=photo)
                win.update_idletasks()
                win.update()
                # 显示车牌小图
                if img_str.strip() != "":
                    im = Image.open(str(img_str))
                    img_read = ImageTk.PhotoImage(im)
                    self.roi_ctl.configure(image=img_read)
                self.r_ctl.configure(text=res)

    def close_video(self):
        self.camera.release()
        self.camera_flag = FALSE
        self.roi_ctl.configure(image=None)
        self.r_ctl.configure(text="")
        # 关闭清空线程
        self.is_running = False

    def add_res_to_list(self, res):
        if len(self.list) < self.count:
            if len(res) > 0:
                print("res: {0} and res[0]:{1}".format(res, res[0]))
                self.list.append(res[0])
        else:
            self.send_request()

    def send_request(self):
        # list够了找出出现次数最多的车牌号
        str_count = Counter(self.list)
        str = str_count.most_common(1)
        if str not in self.block_list:
            # 发送请求,并添加到屏蔽列表
            print("--------------------------发送请求啦： "
                  "{0}-----{1}-------{2}-----{3}-------{4}---------"
                  "-".format(str, type(str), type(str[0]), type(str[0][0]),
                             str[0][0]))
            # 发送后端请求
            webbrowser.register('EDGE', None,
                                webbrowser.BackgroundBrowser(self.EdgePath))
            webbrowser.get('EDGE').open(
                '127.0.0.1:8000/identify/?car_plate={0}'.format(str[0][0]),
                new=1, autoraise=True)
            self.block_list.append(str)
            self.list.clear()

    def clear_block_list(self):
        while self.is_running:
            time.sleep(120)
            if len(self.block_list) > 0:
                print("--------clear_block_list thread 清空 block_list--------")
                # 防止list提前攒满了，清空block瞬间发出请求,所以先清空
                self.list.clear()
                self.block_list.clear()


def close_window():
    print("destroy")
    cv2.destroyAllWindows()
    win.destroy()


if __name__ == '__main__':
    win = tk.Tk()

    surface = Surface(win)
    # close,退出输出destroy
    win.protocol('WM_DELETE_WINDOW', close_window)
    # 进入消息循环
    win.mainloop()
