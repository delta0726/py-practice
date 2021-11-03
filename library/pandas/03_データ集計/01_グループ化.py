# ******************************************************************************
# Category  : Grammar of Pandas
# Chapter   : データ集計
# Title     : グループ化
# Created by: Owner
# Created on: 2021/11/04
# ******************************************************************************


# ＜目次＞
# 0 準備
# 1 グループ化
# 2 グループ属性の確認
# 3 グループフィルタ
# 4 グループデータの抽出


# 0 準備 ---------------------------------------------------------------------------

# ライブラリ
import pandas as pd
import numpy as np

# データ読み込み
# --- irisデータセット（NAなし）
fpath = "library/pandas/csv"
fname1 = "iris.csv"
iris = pd.read_csv(fpath + "/" + fname1)


# 1 グループ化 ---------------------------------------------------------------------

# グループ化
# --- 独自のオブジェクトが生成される（データは出力されない）
iris.groupby(['Species'])

# データ型の確認
# --- pandas.core.groupby.generic.DataFrameGroupBy
type(iris.groupby(['Species']))

# 元データの抽出
# --- グループ化する前のデータにアクセス
iris.groupby(['Species']).obj

# グループ化の解除
iris.groupby(['Species']).apply(lambda x: x.reset_index(drop=True))


# 2 グループ属性の確認 ---------------------------------------------------------------

# グループ数
iris.groupby(['Species']).ngroups

# グループごとのレコード数
# --- グループ別
# --- 特定要素を抽出
iris.groupby(['Species']).size()
iris.groupby(['Species']).size()['versicolor']

# データタイプ
# ---グループ要素ごとのデータ型
iris.groupby(['Species']).dtypes

# インデックス情報
# --- グループごとのインデックスを辞書形式で取得
# --- グループごとのインデックスをNumpyのArray形式で取得
iris.groupby(['Species']).groups
iris.groupby(['Species']).indices

# グループキーの取得
iris.groupby(['Species']).groups.keys()


# 3 グループフィルタ ---------------------------------------------------------------

# グループ名で抽出
iris.groupby(['Species']).get_group('versicolor')

# 複数グループの抽出
# --- get_groupでの抽出はできない
iris.loc[lambda x: x['Species'].isin(['setosa', 'versicolor'])]


# 4 グループデータの抽出 ---------------------------------------------------------------

# 先頭/末尾データの抽出
iris.groupby(['Species']).head()
iris.groupby(['Species']).tail()

# サンプリング
iris.groupby(['Species']).sample(5)

# 条件抽出
# --- 比較対象が固定値
iris.groupby(['Species'])\
    .filter(lambda x: x['Sepal_Length'].max() >= 6)

# グループ集計
# --- 比較対象も集計値
iris.groupby(['Species'])\
    .apply(lambda x: x[x['Sepal_Length'] >= x['Sepal_Length'].mean()])
