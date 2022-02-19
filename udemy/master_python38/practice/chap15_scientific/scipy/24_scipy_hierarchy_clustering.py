# ******************************************************************************
# Course      : Python3.8マスター講座
# Chapter     : 15 科学技術計算ライブラリ
# Theme       : Scipyによる階層クラスタリング
# Creat Date  : 2022/2/20
# Final Update:
# URL         : https://www.udemy.com/course/python-python/
# ******************************************************************************


# ＜概要＞
# - ScipyはNumpyをベースに作成されたライブラリで具体的なアルゴリズムが実装されている
# - ここでは階層クラスタリングを確認する


# ＜目次＞
# 0 準備
# 1 k-meansの適用
# 2 可視化


# 0 準備 ----------------------------------------------------------

# ライブラリ
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt


# データ読み込み
df = pd.read_csv('science_library/countries_position.csv')
print(df.head(10))


# 1 階層クラスタリング ---------------------------------------------

# データ抽出
longtitude_latitude = df.iloc[:, 1:]
linked = linkage(longtitude_latitude, 'ward')  # ウォード法

labels = list(df['country'])
print(labels)

dendrogram(linked, orientation='right', labels=labels)
plt.tight_layout()
plt.show()
