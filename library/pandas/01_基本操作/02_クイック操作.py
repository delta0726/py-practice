# ******************************************************************************
# Category  : Grammar of Pandas
# Chapter   : 01 基本操作
# Title     : 02 クイック操作
# Created by: Owner
# Created on: 2020/12/20
# ******************************************************************************


# ＜概要＞
# - 普段の操作でよく使うものをピックアップ


# ＜目次＞
# 0 準備
# 1 データフレームの構造
# 2 データフレームの概要
# 3 データ確認
# 4 欠損値の確認
# 5 シリーズの抽出
# 6 クイック分析
# 7 クリップボード操作


# 0 準備 ------------------------------------------------------------------------------------

# ライブラリ
import os
import pandas as pd

# データ読み込み
# --- irisデータセット（NAなし）
fpath = "library/pandas/csv"
fname = "iris.csv"
iris = pd.read_csv(fpath + "/" + fname)

# データ読み込み
# --- irisデータセット（NAあり）
fpath = "library/pandas/csv"
fname = "iris_na.csv"
iris_na = pd.read_csv(fpath + "/" + fname)

# データフレーム定義
# --- 空のデータフレーム
df_empty = pd.DataFrame()


# 1 データフレームの構造-------------------------------------------------------------------------

# Pandas DataFrame
type(iris)
type(iris).mro()

# Pandas Series
type(iris['Species'])
type(iris['Species']).mro()

# Numpy Array
type(iris['Species'].values)
type(iris['Species'].values).mro()


# 2 データフレームの概要-------------------------------------------------------------------------

# データフレームの構造
iris.info()

# 列ごとのデータ型
iris.dtypes

# インデックス取得
iris.index

# 列名取得
iris.columns

# 行列数
iris.shape
iris.shape[0]
iris.shape[1]

# 次元数
iris.ndim

# 全要素数
iris.size

# メモリ使用量
iris.memory_usage()


# 3 データ確認 ---------------------------------------------------------------------------------

# 先頭行の確認
iris.head(n=5)

# 末尾行の確認
iris.tail(n=5)

# データ部分の抽出
# --- NumpyのArray
iris.values

# ユニークデータの確認
iris['Species'].unique()

# ユニークデータごとのレコード数を確認
iris['Species'].value_counts()


# 4 欠損値の確認 -------------------------------------------------------------------------------

# 有効データ数のカウント
iris_na.count()

# 欠損値のカウント
iris_na.isnull().sum()

# 欠損値がないか判定
iris_na.isnull().any()

# データフレームが空かどうかを判定
df_empty.empty
iris.empty
iris_na.empty


# 5 系列データの抽出 ------------------------------------------------------------------------

# シリーズで抽出
# --- pandas.Series
iris.Species
iris["Species"]
iris.loc[:, "Species"]

# データフレームで抽出
iris[["Species"]]
iris.loc[:, ["Species"]]

# Numpy配列に変換
# --- numpy.ndarray
iris.Species.to_numpy()


# 6 クイック分析 -----------------------------------------------------------------------------

# 基本統計量
iris_na.describe()

# 相関分析
iris_na.corr()


# 7 クリップボード操作 -------------------------------------------------------------------------

# クリップボード出力
# --- エクセルやRで確認する際に便利
iris.to_clipboard()

# クリップボード入力
# --- 簡単に外部からデータ取得
iris2 = pd.read_clipboard()
