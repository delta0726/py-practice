# ******************************************************************************
# Category  : Grammar of Pandas
# Chapter   : 02 データ加工
# Title     : 列の追加
# Created by: Owner
# Created on: 2021/10/29
# ******************************************************************************


# ＜目次＞
# 0 準備
# 1 列の追加
# 2 NaNの列を追加
# 3 条件文に基づく追加
# 4 複数列を結合して列追加
# 5 文字列分割による列追加
# 6 スペースやドットを含む列の扱い
# 7 行列の転置
# 8 データ型の変換
# 9 データの置換


# 0 準備 --------------------------------------------------------------------------

# ライブラリ
import numpy as np

import pandas as pd
from numpy import NaN


# パス指定
fpath = "library/pandas/csv"

# ファイル名
fname1 = "iris.csv"
fname2 = "iris_dot.csv"

# ファイル読込
iris = pd.read_csv(fpath + "/" + fname1)
iris_dot = pd.read_csv(fpath + "/" + fname2)


# 1 列の追加 -------------------------------------------------------------------

# ＜ポイント＞
# - 列の追加はassignメソッドで行う


# 演算列の追加
iris.assign(SL2 = lambda x: x["Sepal_Length"] * 2)

# 固定値の列を追加
iris.assign(Name = "iris")

# 演算列の追加
iris.assign(length_sum = lambda x: x["Sepal_Length"] + x["Petal_Length"])

# 既存列の更新
iris.assign(Sepal_Length = lambda x: x["Sepal_Length"].mean())

# 複数列の更新
iris.loc[:, ["Sepal_Length", "Sepal_Width"]]\
    .assign(Pct_Sepal_Length = lambda x: x["Sepal_Length"] / x["Sepal_Length"].sum() * 100,
            Pct_Sepal_Width  = lambda x: x["Sepal_Width"] / x["Sepal_Width"].sum() * 100)

# 辞書を活用した更新
iris.loc[:, ["Sepal_Length", "Sepal_Width"]]\
    .assign(**{'Pct_Sepal_Length': lambda x: x["Sepal_Length"] / x["Sepal_Length"].sum(),
               'Pct_Sepal_Width': lambda x: x["Sepal_Width"] / x["Sepal_Width"].sum()})


# 2 NaNの列を追加 --------------------------------------------------------------

# ＜ポイント＞
# - 空の列を定義する場合はNaNを追加する


# 明示的にNaNを追加
iris.assign(NA = NaN)

# 新しい列名の定義
# --- set_axis()は新規列の追加の場合は使えないので注意
now_col = iris.columns.tolist() + ["NA"]
iris.reindex(now_col, axis=1)


# 3 条件文に基づく追加 ----------------------------------------------------------

# ＜ポイント＞
# - 条件文を用いて列を定義する


# np.whereによる追加
iris.assign(flg = lambda x: np.where(x["Sepal_Length"] >= 5, 1, 0))

# map関数による追加
iris.assign(flg = lambda x: x["Sepal_Length"].map(lambda x: 1 if x >= 5 else 0 ))

# リスト内包表記による追加
iris.assign(flg = [1 if x >= 5 else 0 for x in iris["Sepal_Length"]])


# 4 複数列を結合して列追加 ------------------------------------------------------

# ＜ポイント＞
# - 複数の文字列を結合して新しい列を追加する


# 準備
iris_sep = iris.assign(test = "test")

#  演算子による結合
iris_sep.assign(cat = lambda x: x["Species"] + "_" + x["test"])

# str.catによる結合
iris_sep.assign(cat = lambda x: x["Species"].str.cat(x.test, sep='_'))


# 5 文字列分割による列追加 ------------------------------------------------------

# ＜ポイント＞
# - セパレータで区切られた文字列を分割したものを新しい列として追加する


# 準備
iris_cat = iris.assign(Species = lambda x: x["Species"] + "_test")

# ＜方法1＞
# 文字列を分解して列追加
iris_cat\
    .assign(col1 = lambda x: x["Species"].str.split("_").str[0],
            col2 = lambda x: x["Species"].str.split("_").str[1])

# ＜方法2＞
# 分割対象列をあらかじめ分割しておく
x_split = \
    iris_cat.loc[:,'Species']\
        .str.split("_", expand=True)\
        .rename({0: 'col1', 1: 'col2'}, axis=1)

# 元のデータと結合
iris_cat.join(x_split, how='left')


# 6 スペースやドットを含む列の扱い -------------------------------------------

# ＜ポイント＞
# - スペースやドットを含む列を新しく追加する際には辞書型で定義する
#   --- assignメソッドだと列名定義の際にエラーとなる
#   --- 本来は列名にスペースやドットを含むべきではない


# 既存列の更新
iris_dot.assign(**{'Sepal.Length': (lambda x: x["Sepal.Length"].mean())})


# 7 行列の転置 -----------------------------------------------------------

# ＜ポイント＞
# - データフレームの転置はメソッドやプロパティで行うことができる


# メソッドによる転置
iris.head().transpose()

# プロパティによる転置
iris.head().T


# 8 データ型の変換 --------------------------------------------------------

# ＜ポイント＞
# - データ型はデータ全体と列単位で変換することができる

# ＜参考＞
# pandasのデータ型dtype一覧とastypeによる変換（キャスト）
# https://note.nkmk.me/python-pandas-dtype-astype/


# 単一列のデータ変換
iris.astype({'Sepal_Length': str}).dtypes

# 複数列のデータ変換
iris.astype({'Sepal_Length': 'str',
             'Sepal_Width': 'int',
             'Species': 'category'}).dtypes

# データフレーム全体のデータ変換
iris.astype(str).dtypes

# 参考：ラムダ式を用いる方法
# --- 冗長になるので特段の理由がなければ避ける
iris.assign(Sepal_Length = lambda x: x["Sepal_Length"].astype(str)).dtypes


# 9 データの置換 --------------------------------------------------------

# ＜ポイント＞
# - replaceメソッドの中で辞書形式で置換パターンを指定する


# 単一要素の置換
iris.replace({"Species": {'setosa': 'setosa2'}})

# 複数要素の置換
iris\
    .replace({"Species": {'setosa': 'setosa2',
                          'versicolor': 'versicolor2',
                          'virginica': 'virginica2'}})

# データフレーム全体を置換
iris\
    .assign(Species2 = lambda x: x["Species"])\
    .replace({'setosa': 'setosa2'})

# 参考：ラムダ式を用いる方法
# --- 冗長になるので特段の理由がなければ避ける
iris.assign(Species = lambda x: x["Species"].replace('setosa', 'setosa2'))

