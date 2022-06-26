# ******************************************************************************
# Category  : Grammar of Pandas
# Chapter   : データ加工
# Title     : 列の削除
# Created by: Owner
# Created on: 2021/10/23
# ******************************************************************************


# ＜目次＞
# 0 準備
# 1 列名を指定して列削除
# 2 列名パターンで列削除
# 3 データ型で列削除
# 4 全てNaNの列を削除


# 0 準備 ---------------------------------------------------------------------------

# ライブラリ
import pandas as pd
import numpy as np


# データ読み込み
# --- irisデータセット（NAなし）
fpath = "library/pandas/csv"
fname1 = "iris.csv"
iris = pd.read_csv(fpath + "/" + fname1)


# 1 列名を指定して列削除 ------------------------------------------------------------

# ＜ポイント＞
# - 列名を指定する場合はdropメソッドを使用する


# 単一列の削除
iris.drop("Species", axis=1)

# 複数列の削除
iris.drop(["Sepal_Length", "Species"], axis=1)


# 2 列名パターンで列削除 ------------------------------------------------------------

# ＜ポイント＞
# - パターン検索する場合はチルダ(~)を用いて真偽を反転させて選択する
# - 正規表現を用いると｢含まない｣も柔軟に表現できる


# 先頭不一致
# --- 真偽の反転を活用
iris.loc[:, lambda x: ~x.columns.str.startswith("Sepal")]

# 後方不一致
iris.loc[:, lambda x: ~x.columns.str.startswith("Width")]

# 部分不一致
iris.loc[:, lambda x: ~x.columns.str.contains("Wid")]


# 3 データ型で列削除 ----------------------------------------------------------------

# 数値列を削除
iris.select_dtypes(exclude=float)

# 文字列を削除
iris.select_dtypes(exclude=object)

# 参考：データ型の確認
iris.dtypes


# 4 全てNaNの列を削除 ---------------------------------------------------------------

# ＜ポイント＞
# - 全てNaNの列を削除する場合はdropna()のaxis引数を1にして適用する


# 準備：全てNaNの列を作成
iris_na = iris.assign(Col_NaN = np.nan)

# 全てNaNの列を削除
iris_na.dropna(axis=1)
