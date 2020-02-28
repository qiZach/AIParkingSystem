# coding = utf-8
__author__ = 'zhangsiqi'
__date__ = '2020/2/28 19:07'

import os
import threading
from playsound import playsound


def play():
    path = os.path.abspath('../../resources/welcome.wav')
    print(path)
    playsound(path)


def main():
    threading.Thread(target=play).start()
    print('hello world!')
    print('接着进行处理')


if __name__ == '__main__':
    main()
