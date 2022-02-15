# ******************************************************************************
# Course      : Python3.8マスター講座
# Chapter     : 15 科学技術計算ライブラリ
# Theme       : 円グラフ
# Creat Date  : 2022/2/16
# Final Update:
# URL         : https://www.udemy.com/course/python-python/
# ******************************************************************************


# ＜概要＞
# - matpllotlibで円グラフを作成する
#   --- 円グラフはカテゴリごとの単一の出力値に対してプロットを作成する


# ＜目次＞
# 0 準備
# 1 円グラフの作成
# 2 円グラフの装飾


# 0 準備 ----------------------------------------------------------

# ライブラリ
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# 1 円グラフの作成 --------------------------------------------------

# データ作成
generations = ['10-', '20-', '30-', '40-', '50-']
numbers = [20, 30, 35, 40, 20]
explode = (0, 0.1, 0, 0.1, 0)

# プロット作成
plt.pie(numbers, labels=generations, autopct='%1.2f%%')

# 凡例設定
plt.legend(generations, title='Age', bbox_to_anchor=(1, 1))

# プロット表示
plt.show()


# 2 円グラフの装飾 ---------------------------------------------------

# 関数定義
# --- autopctの設定値
def func_pct(pct, numbers):
    number = int(round(pct / 100 * np.sum(numbers)))
    return '{:.2f}%\n{}'.format(pct, number)

# カラー設定
colors = ['#ffeedd', 'red', 'blue', '#aa1133', 'yellow']

# プロット定義
plt.pie(numbers, labels=generations, explode=explode, colors=colors,
        counterclock=False, startangle=90,
        autopct=lambda pct: func_pct(pct, numbers))

# 凡例設定
plt.legend(generations, title='Age', bbox_to_anchor=(1, 1))

# プロット表示
plt.show()
