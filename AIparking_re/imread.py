# -*- coding:utf-8 -*-
import cv2
from hyperlpr import pipline as pp

from hyperlpr import pipline as pp
import cv2

# 自行修改文件名
image = cv2.imread("./car/car1.jpg")
img, res, img_str = pp.SimpleRecognizePlate(image)
cv2.imshow("carPlate", img)
print(res)
cv2.waitKey()
cv2.destroyAllWindows()
