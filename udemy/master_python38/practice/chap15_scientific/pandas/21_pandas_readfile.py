# ******************************************************************************
# Course      : Python3.8マスター講座
# Chapter     : 15 科学技術計算ライブラリ
# Theme       : ファイルからの読み込み
# Creat Date  : 2022/2/20
# Final Update:
# URL         : https://www.udemy.com/course/python-python/
# ******************************************************************************


# ＜概要＞
# - Pandas DataFrameの読込と操作方法を確認する


# ＜目次＞
# 0 準備
# 1 データの操作
# 2 データ集計
# 3 データの抽出
# 4 データのグループ化


# 0 準備 ----------------------------------------------------------

# ライブラリ
import pandas as pd


# 読み込み
df = pd.read_csv('csv/people.csv')
print(df)


# 1 データの操作-----------------------------------------------

# 先頭/末尾
print(df.head(3))
print(df.tail(3))

# 列確認
print(df.columns)

# 特定範囲のデータ抽出
# --- 列と行を指定
print(df[['first_name', 'last_name']][0:5])

# 行番号でデータを取得
# --- 2-4行目, 6-11列目
print(df.iloc[1:4, 5:10])

# データの並び替え
print(df.sort_values(['first_name', 'last_name'], ascending=[1, 0]). \
      head(20)[['first_name', 'last_name']])


# 2 データ集計-----------------------------------------------

# 集計
print(df.describe())
print(df.age.sum())
print(df.age.min())
print(df.age.agg(['sum', 'max', 'mean']))


# 3 データの抽出 ----------------------------------------------

# データのフィルタ
# --- 条件指定で抽出
print(df.loc[df['first_name'] == 'Michael'])

# 絞り込み
# --- MIを含むか
# --- MIを含まないか
print(df.loc[df['first_name'].str.contains('Mi')])
print(df.loc[~df['first_name'].str.contains('Mi')])

# 文字列で抽出
# --- 正規表現を利用
print(df.loc[df['first_name'].str.contains('William|Richard')])
print(df.loc[df['first_name'].str.contains('^A[a-z]*')])
print(df.loc[df['first_name'].str.contains('^A[a-z]*a$')])

# 複数条件で抽出
df.loc[df['country'] == 'Japan', 'nationality'] = 'Japanese'
print(df.loc[df['country'] == 'Japan'])
print(df.head(3))


# 4 データのグループ化 ---------------------------------------

# グループ化
print(df.groupby(['country']).mean().sort_values('age'))
