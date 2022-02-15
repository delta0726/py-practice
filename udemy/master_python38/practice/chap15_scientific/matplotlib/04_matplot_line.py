# ******************************************************************************
# Course      : Python3.8マスター講座
# Chapter     : 15 科学技術計算ライブラリ
# Theme       : 折れ線グラフ（基本）
# Creat Date  : 2022/2/16
# Final Update:
# URL         : https://www.udemy.com/course/python-python/
# ******************************************************************************


# ＜概要＞
# - matpllotlibで折れ線グラフを作成する


# ＜目次＞
# 0 準備
# 1 簡単な折れ線グラフの作成
# 2 プロットの装飾


# 0 準備 ----------------------------------------------------------

# ライブラリ
import numpy as np
import matplotlib.pyplot as plt


# 1 簡単な折れ線グラフの作成 -----------------------------------------

# データ定義
a = [1, 2, 3, 4, 5]
b = [2, 3, 4, 5, 6]

# プロット作成
# --- 'o'：点のみ
# --- 'o-'：点＋線
# --- 'o--'：点＋点線
plt.plot(a, b, 'o--')
plt.show()


# 2 プロットの装飾 --------------------------------------------------

# データ作成
x = np.arange(10)

# プロット作成
# --- 複数系列の表示
plt.plot(x, x ** 2, x, x ** 3, x, x ** 4)

# プロット装飾
plt.grid()
plt.title('Line Chart Example')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.legend(['x**2', 'x**3', 'x**4'], loc='upper center')
plt.xlim([2, 6])
plt.ylim([0, 1000])

# プロット保存
plt.savefig('png/test.png')

# プロット表示
plt.show()
