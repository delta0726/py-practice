# ******************************************************************************
# Course      : Python3.8マスター講座
# Chapter     : 15 科学技術計算ライブラリ
# Theme       : 近似
# Creat Date  : 2022/2/18
# Final Update:
# URL         : https://www.udemy.com/course/python-python/
# ******************************************************************************


# ＜概要＞
# - データ分布の近似式の作成方法を確認する


# ＜目次＞
# 0 準備
# 1 1次式による近似
# 2 3次式による近似


# 0 準備 ----------------------------------------------------------

# ライブラリ
import numpy as np
import matplotlib.pyplot as plt


# 1 1次式による近似 ----------------------------------------------

# データ作成
x = np.random.rand(100) * 2 - 1
noise = np.random.rand(100) * 5
y = x * 2 + noise
print(np.corrcoef(x, y))

# プロット
# --- 正の相関を持つ散布図
plt.scatter(x, y)
plt.show()

# 1次式で近似
# --- 切片と傾きを取得
a, b = np.polyfit(x, y, 1)

# 近似式の作成
test_x = np.linspace(np.min(x), np.max(x), 100)
test_y = a * test_x + b
plt.scatter(x, y)
plt.plot(test_x, test_y)
plt.show()


# 2 3次式による近似 ----------------------------------------------

# データ作成
x = np.random.rand(100) * 2 - 1
noise = np.random.rand(100)
y = x ** 3 - 0.25 * x ** 2 + noise

# プロット
plt.scatter(x, y)
plt.show()

# 3次式で近似
# --- 切片と3つの傾きを取得
a, b, c, d = np.polyfit(x, y, 3)

# 近似式の作成
test_x = np.linspace(np.min(x), np.max(x), 100)
test_y = a* test_x **3 + b * test_x **2 + c * test_x + d
plt.scatter(x, y)
plt.plot(test_x, test_y)
plt.show()

# 近似式の簡単な作成
func = np.poly1d(np.polyfit(x, y, 3))
plt.scatter(x, y)
plt.plot(test_x, func(test_x))
plt.show()
