# ******************************************************************************
# Category  : Grammar of Pandas
# Chapter   : データ集計
# Title     : グループ集計
# Date      : 2022/07/10
# ******************************************************************************


# ＜目次＞
# 0 準備
# 1 集計メソッドによるグループ演算
# 2 グループ演算のパターン
# 3 aggメソッドによる集計
# 4 applyメソッドによる集計
# 5 Pandasの集計メソッド


# 0 準備 ---------------------------------------------------------------------------

# ライブラリ
import pandas as pd
import numpy as np

# データ読み込み
# --- irisデータセット（複数グループ）
iris = pd.read_csv('library/pandas/csv/iris.csv')
iris_group = pd.read_csv('library/pandas/csv/iris_group.csv')


# 1 集計メソッドによるグループ演算 -----------------------------------------------------

# ＜ポイント＞
# - グループ化したオブジェクトに対してメソッドを適用することで集計結果を返す
# - グループ化に適用したキーはインデックスとして扱われる


# 単一グループでの集計
iris.groupby(['Species']).mean()

# 複数グループでの集計
iris_group.groupby(['Species', 'Type']).mean()

# グループをインデックスから解除
iris.groupby(['Species']).mean().reset_index()
iris.groupby(['Species'], as_index=False).mean()


# 2 グループ集計のパターン ------------------------------------------------------------

# ＜ポイント＞
# - グループ集計は集計メソッド/agg()/apply()を使って行うことができる
# - 集計はデータが一意に定義される演算によって実現される


# 集計メソッド
# --- 1つの値に集計される演算
iris.groupby(['Species']).mean()

# aggメソッド
# --- 外部関数を使用
iris.groupby(['Species']).agg(np.mean)

# applyメソッド
# --- 外部関数を使用
iris.groupby(['Species']).apply(np.mean)

# 独自関数
# --- ラムダ式
iris.groupby(['Species']).agg(lambda x: np.max(x) - np.min(x))

# 独自関数
# --- 関数定義
def calc_range(x):
    return (np.max(x) - np.min(x))

iris.groupby(['Species']).agg(calc_range)


# 3 aggメソッドによる集計 --------------------------------------------------------

# ＜ポイント＞
# - agg())は引数として与えた関数を指定列に適用して集計する
#   --- agg()はaggregate()のエイリアス


# 全ての列を集計
# --- 単一の関数で集計
# --- 複数の関数で集計
iris.groupby(['Species']).agg(np.mean)
iris.groupby(['Species']).agg([np.mean, np.std])

# 指定列を集計（メソッド）
# --- 辞書で適用列ごとにメソッドを指定
iris.groupby(['Species'])\
    .agg({'Sepal_Length':'mean',
          'Sepal_Width':'sum'})

# 指定列を集計（関数）
# --- 辞書で適用列ごとに関数を指定
iris.groupby(['Species'])\
    .agg({'Sepal_Length': np.mean,
          'Sepal_Width': np.sum})

# 指定列を集計（ミックス）
# --- 辞書で適用列ごとにメソッド/関数/ラムダ式を指定
def my_range(x):
    return(np.max(x) - np.min(x))

iris.groupby(['Species'])\
    .agg({'Sepal_Length':['max', 'min', 'mean', 'median',
                          np.sum,
                          my_range,
                          lambda x: np.percentile(x, q=20)]})

# ＜参考＞
# 同じ列を複数の関数で集計した場合は最後の演算が適用される
iris.groupby(['Species'])\
    .agg({'Sepal_Length':'min',
          'Sepal_Length':'sum'})


# 4 applyメソッドによる集計 ----------------------------------------------------

# ＜ポイント＞
# - グループオブジェクトの集計はapply()を使って行うこともできる
# - applyメソッドはパフォーマンスが劣る可能性が指摘される
#   --- 集計イテレーションごとに関数を呼び出しているため

# 全ての列を集計
# --- 単一の関数で集計
iris.groupby(['Species']).apply(np.mean)


# 5 Pandasの集計メソッド   -------------------------------------------

# 基本統計量
iris.groupby(['Species']).sum()
iris.groupby(['Species']).mean()
iris.groupby(['Species']).median()
iris.groupby(['Species']).min()
iris.groupby(['Species']).max()
iris.groupby(['Species']).skew()
iris.groupby(['Species']).mad()
iris.groupby(['Species']).std()
iris.groupby(['Species']).var()

# クイック集計
# --- 相関係数行列
# --- 分散共分散行列
# --- 基本統計量
iris.groupby(['Species']).corr()
iris.groupby(['Species']).cov()
iris.groupby(['Species']).describe()
