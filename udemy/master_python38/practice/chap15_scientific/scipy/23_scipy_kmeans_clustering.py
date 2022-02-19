# ******************************************************************************
# Course      : Python3.8マスター講座
# Chapter     : 15 科学技術計算ライブラリ
# Theme       : Scipyによるk-meansクラスタリング
# Creat Date  : 2022/2/20
# Final Update:
# URL         : https://www.udemy.com/course/python-python/
# ******************************************************************************


# ＜概要＞
# - ScipyはNumpyをベースに作成されたライブラリで具体的なアルゴリズムが実装されている
# - ここではk-meansを確認する


# ＜目次＞
# 0 準備
# 1 k-meansの適用
# 2 可視化


# 0 準備 ----------------------------------------------------------

# ライブラリ
import matplotlib.pyplot as plt
from numpy import vstack, array
from numpy.random import rand
from scipy.cluster.vq import kmeans, vq


# データ生成
data = vstack((rand(150, 2), (rand(150, 2) + array([0.5, 0.5]))))
data[1:10, ]

# データ確認
plt.scatter(data[:,0], data[:,1])
plt.show()


# 1 k-meansの適用 -------------------------------------------------

# 2つに分類
# --- 2つに分類した際の重心と重心からの距離の平均値
centroids, distortion = kmeans(data, 2)
print(centroids)
print(distortion)

# クラスに分類
codes, distances = vq(data, centroids)
print(codes)


# 2 可視化 --------------------------------------------------------

# codesが0のものを散布図に表示
plt.scatter(data[(codes == 0), 0], data[(codes == 0), 1], label='ClassA')

# codesが1のものを散布図に表示
plt.scatter(data[(codes == 1), 0], data[(codes == 1), 1], label='ClassB')
plt.scatter(centroids[:, 0], centroids[:, 1], label='Center')
plt.legend()

new_values = rand(10, 2) + array([0.25, 0.25])
new_codes, _ = vq(new_values, centroids)
for i, code in enumerate(new_codes):
    class_value = 'ClassA' if code == 0 else 'ClassB'
    print('x: ' + str(new_values[i][0]) + ' y: ' + str(new_values[i][1])
          + ' : ' + class_value)

plt.show()
