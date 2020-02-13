# coding:utf-8

import numpy as np
import cv2
from hyperlpr import pipline as pp

# 调用笔记本内置摄像头，所以参数为0，如果有其他的摄像头可以调整参数为1，2

camera_number = 0
# 不可缺少 cv2.CAP_DSHOW 少了就读取不了了，CAP_DSHOW 是微软特有的。
# PS：opencv-python 4.2.0版本 使用cap = cv2.VideoCapture(camera_number, cv2.CAP_DSHOW)
cap = cv2.VideoCapture(camera_number + cv2.CAP_DSHOW)

if cap.isOpened():
    print('Yes opened.')
while True:
    # print('从摄像头读取图片')
    success, img = cap.read()
    if success:
        # print('显示摄像头')
        image, res, img_str = pp.SimpleRecognizePlate(img)
        cv2.imshow("carPlate", image)
        # print("**********img_str = {0}****************".format(img_str))
        # 显示车牌小图
        if img_str.strip() != "":
            cv2.imshow("image_gray", cv2.imread(img_str))
        print(res)
        # 保持画面的持续。
        k = cv2.waitKey(1)
        if k == 27:
            # 通过esc键退出摄像
            cv2.destroyAllWindows()
            break
        elif k == ord("s"):
            # 通过s键保存图片，并退出。
            cv2.imwrite("image2.jpg", img)
            cv2.destroyAllWindows()
            break
    else:
        print("Fail!")
        break
# 关闭摄像头
cap.release()
print("Yes closed.")
