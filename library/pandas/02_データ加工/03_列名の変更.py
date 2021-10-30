# ******************************************************************************
# Category  : Grammar of Pandas
# Chapter   : データ加工
# Title     : 列名の変更
# Created by: Owner
# Created on: 2021/10/23
# ******************************************************************************


# ＜目次＞
# 0 準備
# 1 列を指定して列名変更
# 2 列名のパターン変更
# 3 列名の再定義


# 0 準備 --------------------------------------------------------------------------

# ライブラリ
import pandas as pd


# パスの指定
fpath = "library/pandas/csv"

# ファイル名
fname1 = "iris.csv"
fname2 = "iris_dot.csv"

# ファイル読込
iris = pd.read_csv(fpath + "/" + fname1)
iris_dot = pd.read_csv(fpath + "/" + fname2)


# 1 列を指定して列名変更 ------------------------------------------------------------

# ＜ポイント＞
# - renameメソッドを使って辞書形式で{'旧名称':'新名称'}を指定する
# - dict()を用いることもできるが、列名にドット(.)が含まれるとエラーになる

# 単一列の列名変更
# --- 列名にドットが含まれない場合
iris.rename(columns={'Sepal_Length':'SL'})
iris.rename(columns=dict(Sepal_Length='SL'))

# 単一列の列名変更
# --- 列名にドットが含まれる場合（dict()は使えない）
iris_dot.rename(columns={'Sepal.Length':'SL'})
# iris_dot.rename(columns=dict('Sepal.Length'='SL'))

# 複数列の列名変更
# --- 演算子で辞書を作成
iris.rename(columns={'Sepal_Length':'SL', 'Sepal_Width':'SW',
                     'Petal_Length':'PL', 'Petal_Width':'PW'})

# 複数列の列名変更
# --- dict()で辞書を作成
iris.rename(columns=dict(Sepal_Length='SL', Sepal_Width='SW',
                         Petal_Length='PL', Petal_Width='PW'))


# 2 列名のパターン変更 -------------------------------------------------------------

# ＜ポイント＞
# - 文字列のメソッドを活用して列名を変更することが可能


# 列名を大文字に変換
iris.rename(columns=str.upper)
iris.rename(columns=lambda x: x.upper())

# 列名の一部を置換
iris.rename(columns=lambda x: x.replace('.', '_').title())
iris.rename(columns=lambda x: x.replace(".", "_"))


# 3 列名の再定義 -------------------------------------------------------------------

# ＜ポイント＞
# - 元の列名を指定する必要がない
# - 列数と同じ要素数のリストが必要

# 列名を再定義
iris.set_axis(['SL', 'SW', 'PL', 'PW', 'SPE'], axis=1)
