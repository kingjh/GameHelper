#!/usr/bin/python
# -*- coding: utf-8 -*-
import time

import imutils
import win32con
import win32gui
import config
import cv2
import numpy as np
from PIL import ImageGrab


def get_window_pos(name):
    name = name
    handle = win32gui.FindWindow(0, name)
    # 获取窗口句柄
    if handle == 0:
        return None
    else:
        # 返回坐标值和handle
        return win32gui.GetWindowRect(handle), handle


# 识别文字
def crop():
    (x1, y1, x2, y2), handle = get_window_pos('成语中状元')
    win32gui.SendMessage(handle, win32con.WM_SYSCOMMAND, win32con.SC_RESTORE, 0)
    # 发送还原最小化窗口的信息
    win32gui.SetForegroundWindow(handle)
    # 等待窗口前置
    time.sleep(1)
    img = ImageGrab.grab((x1, y1, x2, y2))
    img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
    # 转换图像为灰度图像，需要image和cv2.COLOR_BGR2GRAY标志
    gray_img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
    # 所有灰度值<180的像素点设置为255（白色）—— 文字
    # 灰度值>=180且<=255的像素点设置为0（黑色）—— 背景
    # 实测180时效果最好
    gray_img = cv2.threshold(gray_img, 180, 255, cv2.THRESH_BINARY_INV)[1]
    # 在图像中找到前景物体的轮廓
    cnts = cv2.findContours(gray_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    # 循环绘制轮廓
    for c in cnts:
        # 以10宽度的黄色线条绘制方框轮廓，否则会把方框识别为“口”
        cv2.drawContours(img, [c], -1, (0, 255, 255), 10)
    img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
    # 转换图像为灰度图像，需要image和cv2.COLOR_BGR2GRAY标志
    # 裁剪图像
    # 截取谜题和可选字，[y0: y1, x0: x1]
    arr_riddles = img[config.RIDDLES_AREA_UPPER: config.RIDDLES_AREA_UPPER + config.RIDDLES_AREA_HEIGHT, 0: config.WIDTH]
    arr_chars = img[config.CHARS_AREA_UPPER: config.CHARS_AREA_UPPER + config.CHARS_AREA_HEIGHT, 0: config.WIDTH]
    return arr_riddles, arr_chars
