# ******************************************************************************
# Category  : Grammar of Pandas
# Chapter   : 02 データ加工
# Title     : データ結合
# Created by: Owner
# Created on: 2021/11/03
# ******************************************************************************


# ＜目次＞
# 0 準備
# 1 データ結合(行の結合)
# 2 データ結合(列の結合)
# 3 テーブル結合（merge）
# 4 テーブル結合(join)


# 0 準備 --------------------------------------------------------------------------

# ライブラリ
import numpy as np

import pandas as pd
from numpy import NaN


# パス指定
fpath = "library/pandas/csv"

# ファイル名
fname1 = "iris.csv"

# ファイル読込
iris = pd.read_csv(fpath + "/" + fname1)


# 1 データ結合(行の結合) -----------------------------------------------------------

# ＜ポイント＞
# - 同一形式のデータセットを行方向で結合する
#   --- ｢列名｣｢データ型｣が一致していることを前提とする


# 列名が同じデータ ---------------------------------------

# 準備
iris_1 = iris.query('Species == "setosa"').head()
iris_2 = iris.query('Species == "versicolor"').head()
iris_3 = iris.query('Species == "virginica"').head()

# データ結合
# --- 全ての列を結合
pd.concat([iris_1, iris_2, iris_3])

# データ結合
# --- インデックスをリセット
pd.concat([iris_1, iris_2, iris_3], ignore_index=True)


# 列名が異なるデータ -------------------------------------

# 準備
iris_1 = iris.query('Species == "setosa"').rename(columns={'Species': 'Species1'}).head()
iris_2 = iris.query('Species == "versicolor"').rename(columns={'Species': 'Species2'}).head()
iris_3 = iris.query('Species == "virginica"').rename(columns={'Species': 'Species3'}).head()

# データ結合
# --- 全ての列を結合
pd.concat([iris_1, iris_2, iris_3])

# データ結合
# --- 一致列のみ結合
pd.concat([iris_1, iris_2, iris_3], join='inner')



# 2 データ結合(列の結合) -----------------------------------------------------------

# ＜ポイント＞
# - 同一形式のデータセットを列方向で結合する
#   --- インデックスが一致していることを前提とする


# インデックスが同じデータ -------------------------------------------------

# 準備
iris_sl = iris[['Sepal_Length']]
iris_sw = iris[['Sepal_Width']]
iris_pl = iris[['Petal_Length']]
iris_pw = iris[['Petal_Width']]

# データ結合
# --- 全ての行を結合
pd.concat([iris_sl, iris_sw, iris_pl, iris_pw], axis=1)


# インデックスが異なるデータ -------------------------------------------------

# 準備
iris_sl = iris[['Sepal_Length']].iloc[0:5, :]
iris_sw = iris[['Sepal_Width']].iloc[5:10, :]
iris_pl = iris[['Petal_Length']].iloc[10:15, :]
iris_pw = iris[['Petal_Width']].iloc[15:20, :]

# データ結合
# --- 全ての行を結合
pd.concat([iris_sl, iris_sw, iris_pl, iris_pw], axis=1)


# インデックスが一部共通するデータ ----------------------------------------------

# 準備
iris_sl = iris[['Sepal_Length']].iloc[0:5, :]
iris_sw = iris[['Sepal_Width']].iloc[0:10, :]
iris_pl = iris[['Petal_Length']].iloc[0:15, :]
iris_pw = iris[['Petal_Width']].iloc[0:20, :]

# データ結合
# --- 全ての行を結合
pd.concat([iris_sl, iris_sw, iris_pl, iris_pw], axis=1)

# データ結合
# --- 一致行のみ結合
pd.concat([iris_sl, iris_sw, iris_pl, iris_pw], axis=1, join='inner')


# 3 テーブル結合（merge）------------------------------------------------------------------

# ＜ポイント＞
# - 列に同じ要素を持つ2つのデータセットを結合する
#   --- インデックスは使用しない


# 列名が一致する場合 --------------------------------------------------------------

# 準備
ab = pd.DataFrame({'a': ['a_1', 'a_2', 'a_3'],
                   'b': ['b_1', 'b_2', 'b_3']})
ac = pd.DataFrame({'a': ['a_1', 'a_2', 'a_4'],
                   'c': ['c_1', 'c_2', 'c_4']})

# メソッドによる結合
# --- 内部結合
ab.merge(ac, on='a')

# 関数による結合
# --- 内部結合
pd.merge(ab, ac, on='a')


# 列名が一致しない場合 -------------------------------------------------------------

# 準備
ab = pd.DataFrame({'a': ['a_1', 'a_2', 'a_3'],
                   'b': ['b_1', 'b_2', 'b_3']})
aac = pd.DataFrame({'aa': ['a_1', 'a_2', 'a_4'],
                    'c': ['c_1', 'c_2', 'c_4']})

# メソッドによる結合
# --- 内部結合
ab.merge(aac, left_on='a', right_on='aa')

# 関数による結合
# --- 内部結合
pd.merge(ab, aac, left_on='a', right_on='aa')


# 結合方法の指定 -------------------------------------------------------------------

# 準備
ab = pd.DataFrame({'a': ['a_1', 'a_2', 'a_3'],
                   'b': ['b_1', 'b_2', 'b_3']})
ac = pd.DataFrame({'a': ['a_1', 'a_2', 'a_4'],
                   'c': ['c_1', 'c_2', 'c_4']})

# 内部結合
pd.merge(ab, ac, on='a', how='inner')

# 外部結合
pd.merge(ab, ac, on='a', how='outer')

# Left結合
pd.merge(ab, ac, on='a', how='left')


# 複数キーでの結合 ----------------------------------------------------------------

# 準備
axb = pd.DataFrame({'a': ['a_1', 'a_2', 'a_3'],
                    'x': ['x_2', 'x_2', 'x_3'],
                    'b': ['b_1', 'b_2', 'b_3']})
axc = pd.DataFrame({'a': ['a_1', 'a_2', 'a_4'],
                    'x': ['x_1', 'x_2', 'x_2'],
                    'c': ['c_1', 'c_2', 'c_4']})

# 複数キーで結合
# --- 冗長性なし
pd.merge(axb, axc, on=['a', 'x'])

# 単一キーで結合
# --- xに冗長性が残る
pd.merge(axb, axc, on='a')


# 4 テーブル結合（join）------------------------------------------------------------------

# ＜ポイント＞
# - インデックスを用いて同じ要素を持つ2つのデータセットを結合する


# 列名が一致する場合 --------------------------------------------------------------

# 準備
ab = pd.DataFrame({'a': ['a_1', 'a_2', 'a_3'],
                   'b': ['b_1', 'b_2', 'b_3']}).set_index('a')
ac = pd.DataFrame({'a': ['a_1', 'a_2', 'a_4'],
                   'c': ['c_1', 'c_2', 'c_4']}).set_index('a')

# メソッドによる結合
ab.join(ac, on='a')


# 列名が一致しない場合 -------------------------------------------------------------

# 準備
ab = pd.DataFrame({'a': ['a_1', 'a_2', 'a_3'],
                   'b': ['b_1', 'b_2', 'b_3']}).set_index('a')
aac = pd.DataFrame({'aa': ['a_1', 'a_2', 'a_4'],
                    'c': ['c_1', 'c_2', 'c_4']}).set_index('aa')

# メソッドによる結合
ab.join(aac, on='a')


# 結合方法の指定 -------------------------------------------------------------------

# 準備
ab = pd.DataFrame({'a': ['a_1', 'a_2', 'a_3'],
                   'b': ['b_1', 'b_2', 'b_3']}).set_index('a')
ac = pd.DataFrame({'a': ['a_1', 'a_2', 'a_4'],
                   'c': ['c_1', 'c_2', 'c_4']}).set_index('a')

# 内部結合
ab.join(aac, on='a', how='inner')

# 外部結合
ab.join(aac, on='a', how='outer')

# Left結合
ab.join(aac, on='a', how='left')


# 複数キーでの結合 ----------------------------------------------------------------

# 準備
axb = pd.DataFrame({'a': ['a_1', 'a_2', 'a_3'],
                    'x': ['x_2', 'x_2', 'x_3'],
                    'b': ['b_1', 'b_2', 'b_3']}).set_index(['a', 'x'])
axc = pd.DataFrame({'a': ['a_1', 'a_2', 'a_4'],
                    'x': ['x_1', 'x_2', 'x_2'],
                    'c': ['c_1', 'c_2', 'c_4']}).set_index(['a', 'x'])

# 複数キーで結合
# --- mergeと異なりインデックスは全て指定しなければならない
axb.join(axc, on=['a', 'x'])
