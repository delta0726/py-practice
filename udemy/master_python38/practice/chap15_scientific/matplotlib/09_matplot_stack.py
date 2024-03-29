# ******************************************************************************
# Course      : Python3.8マスター講座
# Chapter     : 15 科学技術計算ライブラリ
# Theme       : 積み上げグラフ
# Creat Date  : 2022/2/17
# Final Update:
# URL         : https://www.udemy.com/course/python-python/
# ******************************************************************************


# ＜概要＞
# - 積み上げグラフは2つのカテゴリの集計値などを可視化する場合に用いる


# ＜目次＞
# 0 準備
# 1 積み上げ棒グラフの作成


# 0 準備 ----------------------------------------------------------

# ライブラリ
import matplotlib.pyplot as plt
import numpy as np


# 1 積み上げ棒グラフの作成 ------------------------------------------

# データ作成
x = np.arange(10)
y1 = x
y2 = 2 * x
y3 = 3 * x

# プロット
plt.stackplot(x, y1, y2, y3, colors=['blue', 'green', 'yellow'])
plt.show()
