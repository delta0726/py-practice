# ******************************************************************************
# Course      : Python3.8マスター講座
# Chapter     : 15 科学技術計算ライブラリ
# Theme       : 行列表現
# Creat Date  : 2022/2/17
# Final Update:
# URL         : https://www.udemy.com/course/python-python/
# ******************************************************************************


# ＜概要＞
# - numpyで扱う基本的な数値表現と行列を確認する


# ＜目次＞
# 0 準備
# 1 さまざまな数値表現
# 2 さまざまな行列表現


# 0 準備 ----------------------------------------------------------

# ライブラリ
import numpy as np


# 1 さまざまな数値表現 ----------------------------------------------

# 無限大
print(np.inf)

# マイナスの無限大
print(np.NINF)

# 非数
print(np.NAN)

# 負の0
print(np.NZERO)

# 正の0
print(np.PZERO)

# ネイピア数
print(np.e)

# 円周率
print(np.pi)


# 2 さまざまな行列表現 ---------------------------------------------

# 行列作成
mat = np.arange(1, 10).reshape(3, 3)
print(mat)

# 転置行列
print(mat.T)

# 行列の初期化
# --- 全ての要素がゼロの行列
x = np.empty([3, 3])
print(x)

# 単位行列
# --- 対角成分が1の行列
# --- identityは正方行列のみに対応
print(np.eye(5))
print(np.identity(3))

# さまざまな単位行列
print(np.eye(3, 2))
print(np.eye(5, 5, 1))
print(np.eye(5, 5, -2))

# 特定の要素の行列を作成
# --- 全ての要素が1
# --- 全ての要素が0
# --- 全ての要素が指定値
print(np.ones((3, 3, 5)))
print(np.zeros((3, 3, 2)))
print(np.full((3, 3, 3), fill_value=3))

# 三角行列
x1 = np.tri(3, 3, k=0)
x2 = np.tri(3, 3, k=-1)
x3 = np.tri(3, 3, k=+1)
print(x1)
print(x2)
print(x3)

# 三角行列で抽出
# --- 元の行列の作成
# --- 下三角行列を取得
# --- 上三角行列を取得
mat = np.arange(1, 26).reshape(5, 5)
print(mat)
print(np.tril(mat, k=0))
print(np.triu(mat, k=0))
