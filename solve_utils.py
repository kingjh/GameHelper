#!/usr/bin/python
# -*- coding: utf-8 -*-
# 穷举搜索答案
import json


def mix_idioms(riddles, chars):
    with open("./idioms.json", 'r', encoding='utf8') as f:
        idioms = json.loads(f.readlines()[0])

        # 找出有谜面的成语作为备选成语集
        tmp_anrss = {}
        for riddle in riddles:
            tmp_anrs = []
            for idiom in idioms:
                pos = idiom.find(riddle)
                if pos != -1:
                    tmp_anrs.append([idiom, idiom[0: pos] + idiom[pos + 1:]])

            tmp_anrss[riddle] = tmp_anrs

        anrss = []
        for riddle in tmp_anrss.keys():
            anrs = []
            for tmp_anr in tmp_anrss[riddle]:
                cnt = 0
                tmp_str = tmp_anr[1]
                for char in chars:
                    pos = tmp_str.find(char)
                    if pos != -1:
                        tmp_str = tmp_str[0: pos] + tmp_str[pos + 1:]
                        cnt += 1

                if cnt == 3:
                    anrs.append(tmp_anr[0])

            anrss.append(anrs)

        anrss.append(['！以下为备选字能组成的成语：'])
        for idiom in idioms:
            anrs = []
            cnt = 0
            tmp_str = idiom
            for char in chars:
                pos = tmp_str.find(char)
                if pos != -1:
                    tmp_str = tmp_str[0: pos] + tmp_str[pos + 1:]
                    cnt += 1

            if cnt == 4:
                anrs.append(idiom)

            anrss.append(anrs)

        return anrss
