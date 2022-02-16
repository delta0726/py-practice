# ******************************************************************************
# Course      : Python3.8マスター講座
# Chapter     : 15 科学技術計算ライブラリ
# Theme       : 行列操作
# Creat Date  : 2022/2/17
# Final Update:
# URL         : https://www.udemy.com/course/python-python/
# ******************************************************************************


# ＜概要＞
# - numpyオブジェクトと基本操作を確認する


# ＜目次＞
# 0 準備
# 1 行列の基本操作


# 0 準備 ----------------------------------------------------------

# ライブラリ
import numpy as np


# 1 行列の基本操作 --------------------------------------------------

# データ作成
# --- ベクトル
x = np.arange(6)

# 行列変換
print(x.reshape(2, 3))

# ベクトルからの行列作成
x = np.arange(8).reshape(2, 4)
print(x)

# 行列のベクトル変換
# --- 参照渡し：ravel関数
x = np.arange(8).reshape(2, 4)
y = np.ravel(x)
print(y)
x[0, 0] = 100
print(y)


# 行列のベクトル変換
# --- コピー渡し：flattenメソッド
x = np.arange(8).reshape(2, 4)
y = x.flatten()
print(y)
x[0, 0] = 100
print(y)

# ベクトルの結合
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print(np.stack((x, y), axis=1))
print(np.hstack((x, y)))
print(np.vstack((x, y)))
print(np.dstack((x, y)))


# 行列の分割
# --- 行方向に分割
x = np.arange(9).reshape(3, 3)
a, b, c = np.split(x, 3)
print(a, b, c)

# 行列の分割
# --- 列方向に分割
x = np.arange(9).reshape(3, 3)
a, b, c = np.hsplit(x, 3)
print(a)
print(b)
print(c)

# 行列の回転
# --- 上下左右反転
# --- 上下反転
# --- 左右反転
x = np.arange(16).reshape(4, 4)
print(x)
print(np.flip(x))
print(np.flip(x, axis=0))
print(np.flip(x, axis=1))

# 行列の回転2
# --- 90度反時計回り回転
x = np.arange(16).reshape(4, 4)
print(x)
print(np.roll(x, 5))
print(np.rot90(x, 3))
