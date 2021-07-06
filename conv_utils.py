#!/usr/bin/python
# -*- coding: utf-8 -*-
import config
import img_utils
from aip import AipOcr
import cv2
client = AipOcr(config.APP_ID, config.API_KEY, config.SECRET_KEY)


def get_chars():
    # 裁剪
    arr_riddles, arr_chars = img_utils.crop()
    # 识别文字
    res = client.basicGeneral(cv2.imencode('.jpg', arr_riddles)[1].tobytes(), {'language_type': 'CHN_ENG'})
    print(res)
    riddles = []
    for obj in res['words_result']:
        # 字符有可能被识别为乱码，所以要判断是否为汉字
        for char in obj['words']:
            if '\u4e00' <= char <= '\u9fa5':
                riddles.append(char)

    res = client.basicGeneral(cv2.imencode('.jpg', arr_chars)[1].tobytes())
    chars = []
    for obj in res['words_result']:
        # 字符有可能被识别为乱码，所以要判断是否为汉字
        for char in obj['words']:
            if '\u4e00' <= char <= '\u9fa5':
                chars.append(char)

    return riddles, chars
