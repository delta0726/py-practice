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
# 8 特定列を先頭にする
# 9 複数列を先頭にする


# 0 準備 --------------------------------------------------------------------

# ライブラリ
import pandas as pd


# パス指定
fpath = "library/pandas/csv"

# ファイル名
fname1 = "iris.csv"
fname2 = "iris_dot.csv"
fname3 = "iris_na.csv"

# ファイル読込
iris = pd.read_csv(fpath + "/" + fname1)
iris_dot = pd.read_csv(fpath + "/" + fname2)
iris_na = pd.read_csv(fpath + "/" + fname3)


# 1 Seriesによる選択 ---------------------------------------------------------

# ＜ポイント＞
# - PandasSeriesとして列を選択する場合はブラケットで個別要素を指定する
# - locプロパティでも列を選択することができる

# ブラケットによる選択
# --- ブラケットで個別を指定（一重のブラケット）
iris['Sepal_Length']

# locによる選択
iris.loc[:, 'Sepal_Length']


# 2 列名による選択 ------------------------------------------------------------

# ＜ポイント＞
# - locプロパティを使って列選択を行うのが一般的（Pythonではlocを列選択に使う人が多い）
# - SQLではfilterは行選択だが、Pandasでは列選択なので注意
# - ブラケットでデータフレームとして抽出する場合は列をリストで指定する


# locによる選択
iris.loc[:, ['Sepal_Length', 'Petal_Width', 'Species']]

# filterによる選択
iris.filter(['Sepal_Length', 'Petal_Width', 'Species'])

# ブラケットによる選択
# --- ブラケットでリストを指定（二重のブラケット）
iris[['Sepal_Length', 'Petal_Width', 'Species']]


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


# 8 特定列を先頭にする -----------------------------------------------------------

# 特定列を先頭にする
# --- リストのアンパックによる操作
col_list = iris.columns.tolist()
col_list.remove('Species')
iris[['Species', *col_list]]

# 参考：アンパックの動作
# --- アンパックなし（リストが維持される）
# --- アンパックあり（リストが解除される）
['Species', col_list]
['Species', *col_list]


# 9 複数列を先頭にする -----------------------------------------------------------

# 単純な方法
col_lst = iris.columns.tolist()
col_lst.remove('Petal.Length')
col_lst.remove('Petal.Width')
iris[['Petal.Length', 'Petal.Width', *col_lst]]

# 内包表記の活用
col_lst = df.columns.tolist()
cols_to_front = ['model', 'category_1', 'category_2']
l2 = [col for col in col_lst if col not in cols_to_front]
df[[*cols_to_front, *l2]]
