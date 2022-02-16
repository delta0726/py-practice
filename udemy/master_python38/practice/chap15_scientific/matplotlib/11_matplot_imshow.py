# ******************************************************************************
# Course      : Python3.8マスター講座
# Chapter     : 15 科学技術計算ライブラリ
# Theme       : 画像マップ
# Creat Date  : 2022/2/17
# Final Update:
# URL         : https://www.udemy.com/course/python-python/
# ******************************************************************************


# ＜概要＞
# - 画像マップは同じ値に同じ色を割り当ててマップを作成するもの


# ＜目次＞
# 0 準備
# 1 単純な画像マップ
# 2 連続値の画像マップ


# 0 準備 ----------------------------------------------------------

# ライブラリ
import matplotlib.pyplot as plt
import numpy as np


# 1 単純な画像マップ ------------------------------------------

# データ作成
z = np.array([[2, 2, 3, 4], [3, 4, 2, 1], [1, 2, 3, 4]])

# 画像表示
plt.imshow(z, origin='lower')
plt.colorbar()
plt.show()


# 2 連続値の画像マップ ----------------------------------------

# データ作成
z = np.random.rand(100, 100)

# 画像表示
plt.imshow(z, origin='lower')
plt.colorbar()
plt.show()
