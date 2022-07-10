# ******************************************************************************
# Category  : Grammar of Pandas
# Chapter   : 03 データ集計
# Title     : 列の集計
# Date      : 2022/07/10
# ******************************************************************************


# ＜目次＞
# 0 準備
# 1 全ての列を集計
# 2 カテゴリカルデータの列をカウント
# 3 パーセントランクに変換
# 4 連続データの離散化
# 5 列のデータ変換


# 0 準備 --------------------------------------------------------------------------

# ライブラリ
import numpy as np

import pandas as pd
from numpy import NaN


# ファイル読込
iris = pd.read_csv('library/pandas/csv/iris.csv')


# 1 全ての列を集計 ----------------------------------------------------------

# 集計関数を直接適用
# --- 数値は合計される
# --- 文字列は結合される（意図しない集計）
iris.sum()

# カウントは文字列でも可能
iris.count()

# 集計関数を直接適用
# --- 数値列のみ
iris.select_dtypes(exclude='object').sum()
iris.select_dtypes(exclude='object').mean()
iris.select_dtypes(exclude='object').var()
iris.select_dtypes(exclude='object').std()
iris.select_dtypes(exclude='object').max()
iris.select_dtypes(exclude='object').min()

# aggメソッドによる複数集計
# --- 結果はデータフレームで返される
iris.select_dtypes(exclude='object').agg([np.sum, np.mean, np.std])

# aggメソッドによる複数集計
# --- 辞書で集計方法を列ごとに指定する
iris.select_dtypes(exclude='object')\
    .agg({'Sepal_Length': [np.sum, np.std],
          'Sepal_Width': [np.sum, np.mean]})

# aggregateメソッドによる複数集計
# --- aggメソッドと同様
iris.select_dtypes(exclude='object')\
    .aggregate({'Sepal_Length': [np.sum, np.std],
                'Sepal_Width': [np.sum, np.mean]})


# 2 カテゴリカルデータの列をカウント -------------------------------------------

# カテゴリ変数のカウント
# --- グループ化しないでカウント
iris[['Species']].value_counts()

# 列ごとのユニーク要素数を一括カウント
iris.nunique()


# 3 パーセントランクに変換 ----------------------------------------------------

# ＜ポイント＞
#

# シリーズ
iris['Sepal_Length'].rank(pct=True)

# データフレーム
iris[['Sepal_Length']]\
    .assign(Pct_Rank=lambda x: x['Sepal_Length'].rank(pct=True))\
    .sort_values(by='Sepal_Length', ascending=True)


# ＜参考：Rankメソッド＞

# データフレーム作成
df = pd.DataFrame(data={'Animal': ['cat', 'penguin', 'dog', 'spider', 'snake'],
                        'legs': [4, 2, 4, 8, np.nan]})

# さまざまな順位
# --- デフォルトの順位計算方法はaverageになっている（一般的にmaxの方がイメージと合うか？）
# --- na_option引数でNAの処理方法を決めることができる
df.assign(default_rank=lambda x: x['legs'].rank(method='average'))\
    .assign(max_rank=lambda x: x['legs'].rank(method='max'))\
    .assign(NA_bottom=lambda x: x['legs'].rank(na_option='bottom'))\
    .assign(pct_rank=lambda x: x['legs'].rank(pct=True))


# 4 連続データの離散化 --------------------------------------------------------

# Seriesでビニング適用
# --- CategoricalDtypeとして格納
# --- 必要に応じて文字列変換
bins = pd.cut(iris['Sepal_Length'], 3, labels=['low', 'median', 'high'])
bins.dtype
bins.astype('str')

# 列のビニング適用
# --- 数値範囲が3分位となるように変換
iris[['Sepal_Length']]\
    .assign(price_group=lambda x: pd.cut(x['Sepal_Length'], bins=3))\
    .groupby('price_group')\
    .count()\
    .reset_index()

# 列のビニング適用
# --- 数値範囲が3分位となるように変換
iris[['Sepal_Length']]\
    .assign(price_group=lambda x: pd.qcut(x['Sepal_Length'], q=[0, 0.33, 0.66, 1], labels=['low', 'medium', 'high']))\
    .groupby('price_group')\
    .count()\
    .reset_index()


# 5 列のデータ変換 --------------------------------------------------------

# データ全体の集計
# --- 文字列の列が含まれないようにする
iris.select_dtypes("float")\
    .transform(lambda x: (x - x.mean()) / x.std())