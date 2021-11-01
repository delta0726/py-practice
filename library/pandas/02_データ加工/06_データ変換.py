# ******************************************************************************
# Category  : Grammar of Pandas
# Chapter   : 02 データ加工
# Title     : データ変換
# Created by: Owner
# Created on: 2021/11/02
# ******************************************************************************


# ＜目次＞
# 0 準備
# 1 ロング型に変換(インデックスなし)
# 2 ロング型に変換(インデックス使用)
# 3 ワイド型に変換(インデックスをなし)
# 4 ワイド型に変換(インデックスを使用)


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


# 1 ロング型に変換(インデックスなし) ---------------------------------------------------

# meltによる変換
# --- インデックスを使わない
iris.melt(id_vars = "Species", var_name = "Key", value_name = "Value")


# 2 ロング型に変換(インデックス使用) ---------------------------------------------------

# stackによる変換
# --- キーがインデックスとなる
iris.set_index(["Species"]).stack()

# stackによる変換
# --- インデックスを解除する
iris.set_index(["Species"])\
    .stack()\
    .reset_index()\
    .set_axis(["Species", "Key", "Value"], axis=1)


# 3 ワイド型に変換(インデックスをなし) -------------------------------------------------

# ＜ポイント＞
# - ロングデータで列番号を保持しておかないとワイドデータに再変換できない


# 準備：ロングデータの作成
# --- ワイド変換のため列番号を保持しておく（reset_index）
iris_melt = iris\
    .reset_index()\
    .melt(id_vars = ["index", "Species"], var_name = "Key", value_name = "Value")

# ワイドデータに変換
iris_melt\
    .pivot(index=["index", "Species"], columns= "Key", values="Value")\
    .reset_index()


# 4 ワイド型に変換(インデックスを使用) ----------------------------------------------------

# ＜ポイント＞
# - unstackを行う際には予めキーをインデックスにしておく


# 全ての列をロング/ワイド変換 --------------------------------

# 準備：ロングデータの作成
iris_stack = iris.stack()

# ワイドデータに変換
iris_stack.unstack()


# 指定列をキーとして保持 -----------------------------------

# 準備：ロング型データの作成
# --- 列番号となっているインデックスもunstackの際に使用する
iris_stack = iris.set_index("Species").stack()

# インデックスの確認
# --- 既存インデックスである列番号も保持されている
iris_stack.index

# ワイド型データに変換
iris_stack.unstack()
