# ******************************************************************************
# Category  : Grammar of Pandas
# Chapter   : データ加工
# Title     : 列の選択
# Created by: Owner
# Created on: 2021/10/23
# ******************************************************************************


# ＜目次＞
# 0 準備
# 1 Seriesによる選択
# 2 列名による選択
# 3 番号による選択
# 4 列名の一部から選択
# 5 正規表現による選択
# 6 データ型による選択
# 7 内包表記による選択


# 0 準備 --------------------------------------------------------------------

# ライブラリ
import pandas as pd


# データ読み込み
# --- irisデータセット（NAなし）
fpath = "library/pandas/csv"
fname1 = "iris.csv"
iris = pd.read_csv(fpath + "/" + fname1)

# データ読み込み
# --- irisデータセット（NAなし）
fname2 = "iris_na.csv"
iris_na = pd.read_csv(fpath + "/" + fname2)

# データ読み込み
# --- irisデータセット（列名アンダースコア）
fname3 = "iris_col.csv"
iris_col = pd.read_csv(fpath + "/" + fname3)


# 1 Seriesによる選択 ---------------------------------------------------------

# ＜ポイント＞
# - PandasSeriesとして列を選択する場合は演算子を用いる
# - パイプによる選択は直感的だがエラーを起こすケースがある（列名にドットを含む場合）

# 演算子による選択
iris['Sepal.Length']

# locによる選択
iris.loc[:, 'Sepal.Length']

# パイプによる選択
# --- 列名に"."が含まれるとエラーになる
iris.Sepal.Length
iris_col.Sepal_Length


# 2 列名による選択 ------------------------------------------------------------

# ＜ポイント＞
# - locプロパティを使って列選択を行うのが一般的（Pythonではlocを列選択に使う人が多い）
# - SQLではfilterは行選択だが、Pandasでは列選択なので注意

# locによる選択
iris.loc[:, ['Sepal.Length', 'Petal.Width', 'Species']]

# filterによる選択
iris.filter(['Sepal.Length', 'Petal.Width', 'Species'])

# 演算子による選択
iris[['Sepal.Length', 'Petal.Width', 'Species']]


# 3 番号による選択 ------------------------------------------------------------

# ＜ポイント＞
# - 列番号で列を選択する場合はilocプロパティを使う

# ilocで番号による選択
iris.iloc[:, [0, 2, 4]]


# 4 列名の一部から選択 ---------------------------------------------------------

# ＜ポイント＞
# - 列名パターンからの選択はstrクラスの関数でTRUE/FALSEの情報に変換して選択する


# 先頭一致
iris.loc[:, lambda x: x.columns.str.startswith("Sepal")]

# 後方一致
iris.loc[:, lambda x: x.columns.str.endswith("Width")]

# 部分一致
# --- locプロパティ
# --- filterメソッド
iris.loc[:, lambda x: x.columns.str.contains("Wid")]
iris.filter(like="Wid")


# 5 正規表現による選択 ---------------------------------------------------------

# ＜ポイント＞
# - filterメソッドを用いるとで正規表現によるパターン検索の列選択が可能となる

# 先頭一致
iris.filter(regex="^Sepal")

# 後方一致
iris.filter(regex="Width$")


# 6 データ型による選択 ---------------------------------------------------------

# ＜ポイント＞
# - select_dtypeメソッドを使うと選択する列をデータ型で指定することができる

# 数値列の選択
iris.select_dtypes(include=float)

# 文字列の選択
iris.select_dtypes(include=object)

# 参考：データ型の確認
iris.dtypes


# 7 内包表記による選択 -----------------------------------------------------------

# ＜ポイント＞
# - リスト内包表記を使うことで列選択することも可能
#   --- 多くの場合は上記の方法で列選択が可能なのでユースケースは多くない

iris.loc[:, lambda x: [c.startswith('Sepal') for c in x.columns]]
