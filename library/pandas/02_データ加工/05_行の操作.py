# ******************************************************************************
# Category  : Grammar of Pandas
# Chapter   : 02 データ加工
# Title     : 行の操作
# Created by: Owner
# Created on: 2022/07/09
# ******************************************************************************


# ＜目次＞
# 0 準備
# 1 インデックスの操作
# 2 行番号による抽出
# 3 行のフィルタ(loc)
# 4 行のフィルタ(query)
# 5 行のフィルタ(isin)
# 6 ランダムサンプリング
# 7 欠損値の削除
# 8 レコードの並び替え
# 9 重複レコードのユニーク化
# 10 数字の大きさでレコード抽出


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
fname3 = "iris_na.csv"
fname4 = "iris_index.csv"

# ファイル読込
iris = pd.read_csv(fpath + "/" + fname1)
iris_dot = pd.read_csv(fpath + "/" + fname2)
iris_na = pd.read_csv(fpath + "/" + fname3)
iris_idx = pd.read_csv(fpath + "/" + fname4)


# 1 インデックスの操作 -------------------------------------------------------------

# ＜ポイント＞
# - 既存列をインデックスとして割り当てることができる
# - インデックスは必ずしも一意の制約はない
#   --- マルチインデックスを活用するなどしてレコード抽出など一意にしておいた方が便利

# インデックスの設定
iris_idx.set_index('Species')

# マルチインデックスの設定
iris_idx.set_index(['Species', 'No'])

# インデックスの解除
iris_idx.set_index('Species').reset_index()


# 2 行番号による抽出/削除 --------------------------------------------------------

# ＜ポイント＞
# - 行番号による抽出はilocプロパティで行う
# - 行の削除はdropメソッドで行う（フィルタと削除は同一操作）


# 行番号で抽出
iris.iloc[0:3, :]

# 1行とばしで抽出
iris.iloc[::2]

# 複数範囲の抽出
iris.iloc[pd.np.r_[10:12, 25:28]]

# 行指定で削除
iris.drop([1, 3, 5], axis=0)

# 先頭行/末尾行の取得
iris.head(10)
iris.tail(10)


# 3 行のフィルタ(loc) -------------------------------------------------------------

# ＜ポイント＞
# - locプロパティを用いるとフィルタを行うことが可能
#   --- ラムダ式の使用が前提となる


# 基本フィルタ ----------------------------------------------

# 単一条件の抽出
iris.loc[lambda x: x["Species"] == "virginica"]

# 複数条件の抽出
# --- AND条件
# --- OR条件
iris.loc[lambda x: (x["Species"] == 'virginica') & (x["Sepal_Length"] >= 7)]
iris.loc[lambda x: (x["Species"] == 'virginica') | (x["Sepal_Length"] >= 7)]

# NOT抽出
iris.loc[lambda x: x["Species"] != "virginica"]
iris.loc[lambda x: ~(x["Species"] == "virginica")]

# 範囲抽出
iris.loc[lambda x: (6.5 <= x["Sepal_Length"]) & (x["Sepal_Length"] <= 7.2)]


# 文字列フィルタ -----------------------------------------

# 先頭一致の抽出
iris.loc[lambda x: x["Species"].str.startswith('vir')]

# 後方一致の抽出
iris.loc[lambda x: x["Species"].str.endswith('ica')]

# 部分一致の抽出
iris.loc[lambda x: x["Species"].str.contains('irginic')]

# 正規表現による抽出
iris.loc[lambda x: x.species.str.match('.*i.*a')]


# その他のフィルタ -----------------------------------------

# 重複行のみ抽出
iris.loc[lambda x: x.loc[:,:].duplicated(keep=False),:]

# 重複行の削除
iris.drop_duplicates()

# 重複行の削除
iris.drop_duplicates(subset=['Species'])


# 4 行のフィルタ(query) -----------------------------------------------------------

# ＜ポイント＞
# - queryメソッドでフィルタ操作を行う
#   --- 条件は文字列で指定する（変数操作も可能）
#   --- locプロパティと違ってラムダ式なしで記述することができる


# 数値のフィルタ
iris.query('Sepal_Length >= 5')

# 文字列のフィルタ
iris.query('Species == "setosa"')

# 列比較のフィルタ
# --- 該当レコードがないため生成
iris.assign(Sepal_Length = lambda x: x["Sepal_Length"] - 1.5)\
    .query('Sepal_Width >= Sepal_Length')

# 列名にドットを含む場合のフィルタ
# --- カラム名をバッククォート(`)で囲む
# --- pandas 0.24.0以前ではエラー
iris_dot.query('`Sepal.Length` >= 5')

# 複数条件のフィルタ
# --- 基本
# --- 数値範囲
iris.query('Sepal_Length > 5 and Species == "setosa"')
iris.query('3 < Sepal_Length < 5')

# NaNの行を操作
# --- NaNを抽出
# --- NaNを除外
iris_na.query('Sepal_Length != Sepal_Length')
iris_na.query('Sepal_Length == Sepal_Length')

# IN演算子による抽出
# --- 対象のみ抽出
# --- 対象を除外
iris.query('Species not in ("setosa", "virginica")')

# 変数を利用した条件抽出
# --- 単一条件
# --- 複数条件
x1 = "setosa"
x2 = ["setosa", "virginica"]
iris.query('Species == @x1')
iris.query('Species in @x2')

# 文字列メソッドを活用した抽出
# --- 前方一致
# --- 後方一致
# --- 部分一致
iris.query('Species.str.startswith("se")', engine='python')
iris.query('Species.str.endswith("ca")', engine='python')
iris.query('Species.str.contains("to")', engine='python')


# 5 行のフィルタ(isin) ------------------------------------------------------------

# isinの動作
# --- シリーズに対して含まれているかどうかを判定
# --- チルダ(~)で判定を反転させることも可能
iris['Species'].isin(['setosa', 'virginica'])
~iris['Species'].isin(['setosa', 'virginica'])

# 判定情報をもとに抽出
iris[iris['Species'].isin(['setosa', 'virginica'])]


# 6 ランダムサンプリング -----------------------------------------------------------

# ＜ポイント＞
# - 絶対数と比率でサンプリングが可能
# - 引数により復元方法やランダムシードの指定が可能


# サンプル数を指定
iris.sample(n=5)

# 全レコード数に対する割合を指定
iris.sample(frac=0.05)

# ランダムシードを指定
iris.sample(frac=0.05, random_state=0)


# 7 欠損値の削除 ------------------------------------------------------------------

# ＜ポイント＞
# - 欠損値の削除はdropnaメソッドで行う
#  --- 欠損値の処理方法と組み合わせて使用を検討する必要がある


# 全ての列のNaNを削除
iris_na.dropna()

# 指定列のNaNを削除
iris_na.dropna(subset=['Sepal_Length','Sepal_Width'])


# 8 レコードの並び替え --------------------------------------------------------------

# 基本的なソート ----------------------------------------

# ＜ポイント＞
# - ソートは基本的にロング型に対して行う


# インデックスでソート
iris.sort_index(axis=0, ascending=True)
iris.sort_index(axis=0, ascending=False)

# 単一キーでソート
iris.sort_values(by='Sepal_Length', ascending=True)

# 複数キーでソート
# --- リストでキーを指定
iris.sort_values(by=['Sepal_Length', 'Sepal_Width'], ascending=[True, False])

# ランダムソート
# --- ランダムサンプリングで全て残す
iris.sample(frac=1, random_state=0)


# 列方向のソート -----------------------------------------

# ＜ポイント＞
# - ワイド型のデータセットに対して使用する
#   --- 基本的にソートはロング型で行うほうが分かりやすい


# 列の並び替え
iris.sort_index(axis=1, ascending=False)


# 任意の順番にソート --------------------------------------

# ＜ポイント＞
# - 集計列を使用してソートしてから集計列を削除する


# サンプルデータ作成
df_species = pd.DataFrame({'Species': pd.Series(['setosa', 'versicolor', 'virginica'])})

# オーダー指定
order = {'versicolor': 0, 'setosa': 1, 'virginica': 2}

# 任意の順番にソート
df_species\
    .assign(order = lambda x: x['Species'].map(order))\
    .sort_values(by='order', ascending=True)\
    .drop('order', axis=1)\
    .reset_index(drop=True)


# 9 重複レコードのユニーク化 ----------------------------------------------------

# 複数行のユニーク化
iris[['Species', 'Petal_Width']].drop_duplicates()

# シリーズのユニーク化
iris['Species'].unique()
iris['Species'].value_counts()


# 10 数字の大きさでレコード抽出 -------------------------------------------------

# 数字の大きさでレコード抽出
# --- 上位Nレコード
# --- 下位Nレコード
iris.nlargest(n=10, columns=['Sepal_Length'])
iris.nsmallest(n=10, columns=['Sepal_Length'])
