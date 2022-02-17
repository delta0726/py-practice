# ******************************************************************************
# Course      : Python3.8マスター講座
# Chapter     : 15 科学技術計算ライブラリ
# Theme       : 数学関数
# Creat Date  : 2022/2/18
# Final Update:
# URL         : https://www.udemy.com/course/python-python/
# ******************************************************************************


# ＜概要＞
# - 基本的な数学関数を確認する


# ＜目次＞
# 0 準備
# 1 三角関数
# 2 対数関数
# 3 指数関数


# 0 準備 ----------------------------------------------------------

# ライブラリ
import numpy as np
import matplotlib.pyplot as plt


# 1 三角関数 -------------------------------------------------------

# 円周率の定義
low = -np.pi
high = np.pi

# パラメータ設定
N = 50

# データ作成
x = np.linspace(low, high, N)
print(x)

# sin関数
y = np.sin(x)
plt.plot(x, y)

# cos関数
y = np.cos(x)
plt.plot(x, y)

# tan関数
y = np.tan(x)
plt.plot(x, y)

# プロット作成
plt.ylim([-10, 10])
plt.show()


# 2 対数関数 --------------------------------------------------

# パラメータ設定
N = 50

# データ作成
# --- 整数数列
# --- 自然対数(log)
# --- 常用対数(log10X)
x = np.linspace(1, 10, N)
y = np.log(x)
plt.plot(x, y)
y = np.log10(x)
plt.plot(x, y)
plt.show()


# 3 指数関数 ---------------------------------------------------

# データ作成
x = np.arange(10)

# eのx乗
y = np.exp(x)

# 2のx乗
y = np.exp2(x)

# プロット作成
plt.plot(x, y, 'o--')
plt.show()
