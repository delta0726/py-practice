# ******************************************************************************
# Course      : Python3.8マスター講座
# Chapter     : 15 科学技術計算ライブラリ
# Theme       : ヒストグラム作成
# Creat Date  : 2022/2/17
# Final Update:
# URL         : https://www.udemy.com/course/python-python/
# ******************************************************************************


# ＜概要＞
# - ヒストグラムは連続値の系列の分布状況を示す


# ＜目次＞
# 0 準備
# 1 ヒストグラムの作成
# 2 2次元のヒストグラム(ヒートマップ)


# 0 準備 ----------------------------------------------------------

# ライブラリ
import matplotlib.pyplot as plt
import numpy as np


# 1 ヒストグラムの作成 ---------------------------------------------

# データ作成
x = np.random.randn(100)

# プロット作成
plt.hist(x, bins=20)
plt.show()


# 2 2次元のヒストグラム(ヒートマップ) --------------------------------

# データ作成
x = np.random.normal(3, 4, 10000)
y = np.random.normal(3, 4, 10000)

# プロット作成
plt.hist2d(x, y, bins=100, cmap='plasma')
print(dir(plt.cm))
plt.colorbar()
plt.show()
