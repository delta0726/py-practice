# ******************************************************************************
# Course      : Python3.8マスター講座
# Chapter     : 15 科学技術計算ライブラリ
# Theme       : Pandas DataFrameの使い方
# Creat Date  : 2022/2/20
# Final Update:
# URL         : https://www.udemy.com/course/python-python/
# ******************************************************************************


# ＜概要＞
# - PandasのSeriesオブジェクトの基本操作を確認する


# ＜目次＞
# 0 準備
# 1 データフレームの作成
# 2 データフレームの操作


# 0 準備 ----------------------------------------------------------

# ライブラリ
import pandas as pd
import numpy as np


# 1 データフレームの作成 --------------------------------------------

# データフレームの作成
df = pd.DataFrame([[1, 2, 3], [4, 5, 6]])
print(df)

# データフレームの作成
# --- 列名とインデックスあり
df = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=['A', 'B', 'c'], index=['index1', 'index2'])
print(df)


# データフレームの転置
df = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=['A', 'B', 'c'], index=['index1', 'index2'])
print(df.T)

# データの確認
df = pd.DataFrame(np.random.randint(0, 10, 9).reshape(3, 3))
print(df)
print(df.head(1))
print(df.tail(1))


# 2 データフレームの操作 ----------------------------------------------

# データフレームの作成
df = pd.DataFrame([['Taro', 21, 'Man', 175],
                   ['Jiro', 20, 'Man', 160],
                   ['Hanako', 19, 'Woman', 155],
                   ['Yoshiko', 18, 'Woman', 160]],
                  columns=['名前', '年齢', '性別', '身長'])

# 単一列の抽出
print(df['名前'])
print(df.名前)

# 複数列の抽出
print(df[['名前', '年齢']])

# 行の追加
new_member = pd.DataFrame([['Saburo', 17, 'Man', 180], ], columns=df.columns)
df = df.append(new_member).reset_index()
print(df)

# 列の追加
df['体重'] = np.random.randint(50, 80, 5)
df['BMI'] = df['体重'] / (df['身長'] * 0.01) ** 2
print(df)

# Numpy配列に変換
print(df.to_numpy())

# 統計値
print(df.describe())
print(df.mean())
print(df.max())
print(df.min())
print(df.var())
print(df.std())
print(df.count())
print(df.quantile(0.8))
