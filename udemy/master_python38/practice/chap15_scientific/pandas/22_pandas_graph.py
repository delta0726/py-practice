# ******************************************************************************
# Course      : Python3.8マスター講座
# Chapter     : 15 科学技術計算ライブラリ
# Theme       : グラフ表示
# Creat Date  : 2022/2/20
# Final Update:
# URL         : https://www.udemy.com/course/python-python/
# ******************************************************************************


# ＜概要＞
# - Pandasでグラフを作成する


# ＜目次＞
# 0 準備
# 1 散布図の作成
# 2 棒グラフの作成
# 3 ヒストグラムの作成
# 4 折れ線グラフの作成


# 0 準備 ----------------------------------------------------------

# ライブラリ
import pandas as pd
import matplotlib.pyplot as plt


# データ準備
df = pd.read_csv('csv/people_salary.csv')
print(df.columns)
print(df.head(5))

# プロット設定
# fig, axes = plt.subplots(nrows=2, ncols=2)


# 1 散布図の作成 -----------------------------------------------------

# プロット作成
pd_plt = df.plot(kind='scatter', x='age', y='salary')
pd_plt.set_ylabel('Saraly')
pd_plt.set_xlabel('Age')
pd_plt.set_title('Scatter Plot')

# プロット表示
plt.show()


# 2 棒グラフの作成 ----------------------------------------------------

# データ集計
average_by_countries = df.groupby(['country']).mean()
average_by_countries.head(5)

# プロット作成
average_by_countries\
    .plot(kind='bar', y='salary', title='Average Saraly per Country', color='red')

# プロット表示
plt.show()


# 3 ヒストグラムの作成 -----------------------------------------------

# データ抽出
engineer_in_japan = df.loc[(df['country'] == 'Japan') \
                           & (df['job'] == 'Engineer')]

# ヒストグラム
engineer_in_japan['age']\
    .plot(kind='hist', title='Histogram of Age')

# プロット表示
plt.show()


# 4 折れ線グラフの作成 -----------------------------------------------

# データ抽出
engineer_in_japan = df \
    .loc[(df['country'] == 'Japan') & (df['job'] == 'Engineer')]\
    .groupby(['age'])\
    .mean()

# 折れ線グラフ
engineer_in_japan\
    .groupby(['age'])\
    .mean()\
    .plot(kind='line', y='salary')

# プロット表示
plt.show()
