#!/usr/bin/python
# -*- coding: utf-8 -*-

import conv_utils
import solve_utils

riddles, chars = conv_utils.get_chars()
print(riddles, chars)
anrss = solve_utils.mix_idioms(riddles, chars)
list(map(lambda anrs: list(map(print, anrs)), anrss))
