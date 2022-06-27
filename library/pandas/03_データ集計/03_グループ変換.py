# ******************************************************************************
# Category  : Grammar of Pandas
# Chapter   : データ集計
# Title     : グループ変換
# Created by: Owner
# Created on: 2021/11/06
# ******************************************************************************


# ＜概要＞
# -
# - グループごとの統計情報を使ってすべての行を集計したい場合はtransformを使う


# ＜目次＞
# 0 準備
# 1 集計メソッドによるグループ演算
# 2 グループ演算のパターン
# 3 aggメソッドの活用
# 6 Pandas Groupオブジェクトのメソッド一覧

# 0 準備 ---------------------------------------------------------------------------

# ライブラリ
import pandas as pd
import numpy as np

# データ読み込み
# --- irisデータセット
fpath = "library/pandas/csv"
fname = "iris.csv"
iris = pd.read_csv(fpath + "/" + fname)




df1 = (iris.groupby(iris['Species']).sum().assign(sum = lambda x: x.sum(axis=1)))



# 1 複数列に計算を適用（データ全体） -------------------------------------------

# データ全体の集計
# --- 文字列の列が含まれないようにする
iris.select_dtypes("float").transform(lambda x: (x - x.mean()) / x.std())

iris.select_dtypes("float").transform(np.mean)


# 2 複数列に計算を適用（グループ単位） -----------------------------------------

# 関数
iris.groupby(['Species']).transform(np.mean)

# ラムダ式
iris.groupby(['Species']).transform(lambda x: (x - x.mean()) / x.std())

# カウント
iris.groupby(['Species']).transform(np.size)

# 順位
iris.groupby(['Species']).rank(method="dense")


# 3 単一列に計算を適用（グループ単位） ------------------------------------------

# 集計列を追加
iris['Sepal_Length_Gsum'] = iris.groupby(['Species'])['Sepal_Length'].transform(np.sum)


