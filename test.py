'''
-*- coding: utf-8 -*-
@Author  : Meet
@Time    : 2020/6/27 12:28
@Software: PyCharm
@File    : 8.matplotlib极坐标系.py
'''



import numpy as np
import matplotlib.pyplot as mp

t = np.linspace(0, 4 * np.pi, 1000)
r = 0.8 * t

x = np.linspace(0, 6 * np.pi, 1000)
y = 3 * np.sin(6 * x)
mp.figure('Polar')
mp.gca(projection='polar')
mp.plot(t, r)
mp.plot(x, y)
mp.show()
