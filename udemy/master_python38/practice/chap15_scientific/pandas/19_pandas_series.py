# ******************************************************************************
# Course      : Python3.8マスター講座
# Chapter     : 15 科学技術計算ライブラリ
# Theme       : Pandas Seriesの使い方
# Creat Date  : 2022/2/19
# Final Update:
# URL         : https://www.udemy.com/course/python-python/
# ******************************************************************************


# ＜概要＞
# - PandasのSeriesオブジェクトの基本操作を確認する


# ＜目次＞
# 0 準備
# 1 Seriesの作成
# 2 インデックスの指定
# 3 オブジェクトの基本操作
# 4 基本的な統計演算


# 0 準備 ----------------------------------------------------------

# ライブラリ
import pandas as pd
import numpy as np


# 1 Seriesの作成 --------------------------------------------------

# Seriesの作成
sr1 = pd.Series(['A', 'B', 'C', 'D'])
print(sr1)

# 他のオブジェクトに変換
# --- リストに変換
# --- タプルに変換
print(list(sr1))
print(tuple(sr1))


# 2 インデックスの指定 --------------------------------------

# Seriesの作成
# --- インデックス引数を指定する
sr = pd.Series([23, 24, 22, 21], index=['Taro', 'Jiro', 'Hanako', 'Yoshiko'])
print(sr)

# Seriesの作成
# --- 辞書からSeriesを作成する（キーインデックスとなる）
sr = pd.Series({'Taro': 23, 'Jiro': 24, 'Hanako': 22, 'Yoshiko': 21})
print(sr)

# Seriesの作成
# --- Numpyオブジェクトから作成
sr = pd.Series(np.random.randint(0, 10, 10))
print(sr)


# 3 オブジェクトの基本操作 --------------------------------------

# 要素の追加
sr1 = pd.Series({'Taro': 23, 'Jiro': 24, 'Hanako': 22, 'Yoshiko': 21})
sr2 = pd.Series({'Saburo': 20})
sr = sr1.append(sr2)
print(sr)

# 要素の抽出
# --- 値だけ取り出す
# --- インデックスだけ取り出す
sr = pd.Series({'Taro': 23, 'Jiro': 24, 'Hanako': 22, 'Yoshiko': 21})
print(sr.values)
print(sr.index)

# 演算子で抽出
# --- 指定した値より大きいものだけ取り出す
sr = pd.Series({'Taro': 23, 'Jiro': 24, 'Hanako': 22, 'Yoshiko': 21})
filter = sr > 22
print(sr[filter])

# 名前を付ける
# --- オブジェクトに名前を付ける（変数名ではない）
# --- インデックスに名前を付ける
sr = pd.Series({'Taro': 23, 'Jiro': 24, 'Hanako': 22, 'Yoshiko': 21})
print(sr)
sr.name = '年齢'
sr.index.name = '名前'
print(sr)

# 重複要素を削除
sr1 = pd.Series(np.random.randint(0, 10, 10))
print(sr1.unique())

# 要素数のカウント
# --- Rのtable())に相当
sr1 = pd.Series(np.random.randint(0, 10, 10))
print(sr1.value_counts())

# 掛け算
# --- 要素数が同じ長さの必要がある
sr1 = pd.Series(np.random.randint(0, 10, 10))
sr2 = pd.Series(np.random.randint(0, 10, 10))
print(sr1 * sr2)

# 要素の上書き
# --- 追加位置を指定
sr1 = pd.Series(['A', 'B', 'C', 'D'])
sr1[1:] = ['E', 'F', 'G']
print(sr1)

# 要素の削除
# --- インデックスの1が歯抜けになっている点に注意
sr1 = pd.Series(['A', 'B', 'C', 'D'])
sr2 = sr1.drop(1)
print(sr2)

# インデックスの張り直し
sr1 = pd.Series(['A', 'B', 'C', 'D'])
sr2 = sr1.drop(1).reset_index(drop=True)
print(sr2)

# NAの追加
sr1 = pd.Series(np.random.randint(0, 10, 10))
print(sr1)
sr1[5] = pd.NA
print(sr1)

# 判定関数を用いた抽出
sr1 = pd.Series(np.random.randint(0, 10, 10))
sr1[5] = pd.NA
print(sr1[sr1.isna()])
print(sr1[~sr1.isna()])


# 4 基本的な統計演算 -----------------------------------------

# データ作成
sr1 = pd.Series(np.random.randint(0, 10, 10))
sr1[5] = pd.NA
print(sr1)

# カウント
# --- 欠損値を除く数
print(sr1.count())

# 平均値
print(sr1.mean())

# 最大値/最小値
print(sr1.max())
print(sr1.min())

# 分散/標準偏差
print(sr1.var())
print(sr1.std())

# パーセンタイル点の取得
# --- 昇順に並べて80%地点の値
print(sr1.quantile(0.8))

# 基本統計量
print(sr1.describe())
