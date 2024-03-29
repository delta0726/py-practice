# ******************************************************************************
# Course      : Python3.8マスター講座
# Chapter     : 15 科学技術計算ライブラリ
# Theme       : 統計量
# Creat Date  : 2022/2/18
# Final Update:
# URL         : https://www.udemy.com/course/python-python/
# ******************************************************************************


# ＜概要＞
# - 基本的な統計演算を確認する


# ＜目次＞
# 0 準備
# 1 基本統計量
# 2 行列ごとの統計量
# 3 パーセンタイルの計算
# 4 データでヒストグラムの作成


# 0 準備 ----------------------------------------------------------

# ライブラリ
import numpy as np


# データ準備
a = np.random.randint(0, 10, 10)
print(a)


# 1 基本統計量 ------------------------------------------------------

# 中央値
print(np.median(a))

# 平均値
print(np.mean(a))

# 標準偏差
print(np.std(a))

# 分散
print(np.var(a))


# 2 行列ごとの統計量 -----------------------------------------------

# データ作成
a = np.random.randint(0, 10, (2, 5))
print(a)

# 平均値
print(np.average(a, axis=0, weights=[1, 10]))
print(np.average(a, axis=1, weights=[1, 1, 1, 1 ,1]))

# 合計値
print(np.sum(a, axis=0))
print(np.sum(a, axis=1))


# 3 パーセンタイルの計算 ------------------------------------------

# パーセンタイル
# --- (25%くらいの値、75％くらいの値)
a = np.random.rand(100)
lower, upper = np.percentile(a, [25, 75])

# データ抽出
# --- 外れ値の処理などに利用
print(a[(a > lower) & (a < upper)])


# 4 データでヒストグラムの作成 -------------------------------------

# ＜ポイント＞
# - 階級値と頻度を配列で表示する


# ヒストグラム
a = np.array([0, 1, 1, 1, 2, 2, 3, 3, 4, 5, 5, 5, 5, 6, 10])
print(np.histogram(a, bins=20))
