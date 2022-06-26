# ******************************************************************************
# Category : Grammar of Pandas
# Chapter  : データ加工
# Title    : 列の選択
# Date     : 2022/06/27
# ******************************************************************************


# ＜目次＞
# 0 準備
# 1 列名によるSeries選択
# 2 列名によるDataFrame選択
# 3 番号によるSeries/DataFrame選択
# 4 列名の一部から選択(ラムダ式)
# 5 データ型による列選択
# 6 内包表記による選択
# 7 列名を指定して並び替え
# 8 別のデータフレームの順番に並び替える
# 9 特定列を先頭にして並び替える
# 10 複数列を先頭にして並び替える


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


# 1 列名によるSeries選択 ---------------------------------------------------------

# ＜ポイント＞
# - PandasSeriesとして列を選択する場合はブラケットで個別要素を指定する
# - locプロパティでも列を選択することができる

# ブラケットによる選択
# --- ブラケットで個別を指定（一重のブラケット）
iris['Sepal_Length']

# locによる選択
iris.loc[:, 'Sepal_Length']


# 2 列名によるDataFrame選択 -------------------------------------------------------

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


# 3 番号によるSeries/DataFrame選択 ------------------------------------------------------

# ＜ポイント＞
# - 列番号で列を選択する場合はilocプロパティを使う
# - 数値の場合はSeries / リストの場合はDataFrame


# ilocで番号による選択
# --- Series
# --- DataFrame
iris.iloc[:, 1]
iris.iloc[:, [0, 2, 4]]


# 4 列名の一部から選択 -------------------------------------------------------

# ＜ポイント＞
# - ラムダ式を用いる方法とfilterメソッドを用いる方法がある
#   --- ラムダ式はstringモジュールを使って文字列を選択して列取得
#   --- fitlterメソッドは正規表現で文字列を選択して列取得


# 先頭一致
iris.loc[:, lambda x: x.columns.str.startswith("Sepal")]
iris.filter(regex="^Sepal")

# 後方一致
iris.loc[:, lambda x: x.columns.str.endswith("Width")]
iris.filter(regex="Width$")

# 部分一致
iris.loc[:, lambda x: x.columns.str.contains("Wid")]
iris.filter(like="Wid")


# 5 データ型による列選択 ---------------------------------------------------------

# ＜ポイント＞
# - select_dtypeメソッドを使うと選択する列をデータ型で指定することができる


# 数値列の選択
iris.select_dtypes(include=float)

# 文字列の選択
iris.select_dtypes(include=object)

# 参考：データ型の確認
iris.dtypes


# 6 内包表記による選択 -----------------------------------------------------------

# ＜ポイント＞
# - リスト内包表記を使うことで列選択することも可能
#   --- 多くの場合は上記の方法で列選択が可能なのでユースケースは多くない

iris.loc[:, lambda x: [c.startswith('Sepal') for c in x.columns]]


# 7 列名を指定して並び替え -------------------------------------------------------

# ＜ポイント＞
# - データフレームの列を並び替える方法は以下の2種類がある
#   --- 単純に列名を選択
#   --- メソッドによる並び替え


# 列名取得
iris.columns

# 単純に列名を選択
iris[['Species', 'Sepal_Width', 'Petal_Width', 'Sepal_Length', 'Petal_Length']]
iris.loc[:, ['Species', 'Sepal_Width', 'Petal_Width', 'Sepal_Length', 'Petal_Length']]

# メソッドによる並び替え
iris.reindex(columns=['Species', 'Sepal_Width', 'Petal_Width', 'Sepal_Length', 'Petal_Length'])


# 8 別のデータフレームの順番に並び替える ------------------------------------------------

# ＜ポイント＞
# - 特定のデータフレームの列順序を参照して並び替える


# 指定したデータフレームの列順にソート
iris.reindex(columns=['Species', 'Sepal_Width', 'Petal_Width', 'Sepal_Length', 'Petal_Length']).\
    reindex_like(iris)

# 列が存在しない場合はNaNとなる
iris.reindex(columns=['Species', 'Sepal_Width', 'Sepal_Length']).\
    reindex_like(iris)\
    .dropna(axis=1)

# 必要に応じてNaN列を削除する
iris.reindex(columns=['Species', 'Sepal_Width', 'Sepal_Length']).\
    reindex_like(iris)\
    .dropna(axis=1)


# 9 特定列を先頭にして並び替える -------------------------------------------------------

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


# 10 複数列を先頭にして並び替える ------------------------------------------------------

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
