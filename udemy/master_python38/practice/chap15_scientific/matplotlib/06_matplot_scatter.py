# ******************************************************************************
# Course      : Python3.8マスター講座
# Chapter     : 15 科学技術計算ライブラリ
# Theme       : 散布図
# Creat Date  : 2022/2/17
# Final Update:
# URL         : https://www.udemy.com/course/python-python/
# ******************************************************************************


# ＜概要＞
# - 散布図は2系列の連続値で作成する


# ＜目次＞
# 0 準備
# 1 簡単な散布図の作成
# 2 散布図に3系列目を導入


# 0 準備 ----------------------------------------------------------

# ライブラリ
import numpy as np
import matplotlib.pyplot as plt


# 1 簡単な散布図の作成 -------------------------------------------------

# ＜ポイント＞
# - 散布図は2系列の連続値に対して作成する
# - 複数系列を1つのプロットに重ね書きすることができる


# データ作成
x1 = np.random.rand(100)
y1 = np.random.rand(100) - 0.5
x2 = np.random.rand(100)
y2 = np.random.rand(100) + 0.5

# プロット作成
# --- 重ね書き
plt.scatter(x1, y1, s=100, c='red')
plt.scatter(x2, y2, s=100, c='blue', marker='*')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot')
plt.show()


# 2 散布図に3系列目を導入 --------------------------------------------

# ＜ポイント＞
# - 散布図に3系列目のデータを反映させる
#  --- プロットの透明度や大きさに当てはめる
#  --- 透明度と大きさを異なる系列にすれば最大4系列まで可能


# データ作成
x = np.linspace(0, 10, 100) + np.random.rand(100)
y = np.linspace(0, 10, 100) + 5 * np.random.rand(100)
z = np.linspace(0, 10, 100)

# プロット作成
# --- プロットの透明度を値に応じて変更
plt.scatter(x, y, s=100, c=z, cmap='Blues')
plt.colorbar()
plt.show()
