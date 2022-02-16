# ******************************************************************************
# Course      : Python3.8マスター講座
# Chapter     : 15 科学技術計算ライブラリ
# Theme       : 棒グラフ
# Creat Date  : 2022/2/17
# Final Update:
# URL         : https://www.udemy.com/course/python-python/
# ******************************************************************************


# ＜概要＞
# - 棒グラフはカテゴリカルデータに対する集計値に対して作成する


# ＜目次＞
# 0 準備
# 1 簡単な棒グラフの作成
# 2 ラベルの追加


# 0 準備 ----------------------------------------------------------

# ライブラリ
import numpy as np
import matplotlib.pyplot as plt


# 1 簡単な棒グラフの作成 ---------------------------------------------

# データ作成
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]
labels = ['20-', '30-', '40-', '50-', '60-']

# パラメータ設定
# --- 系列インデックス
# --- 棒グラフの幅
x = np.arange(len(labels))
width = 0.35

# プロット作成
rect1 = plt.bar(x - width / 2, men_means, width, color='blue')
rect2 = plt.bar(x + width / 2, women_means, width)
plt.xticks(x, labels=labels)
plt.grid()
plt.ylabel('Score')
plt.title('Score by gender')
plt.show()


# 2 ラベルの追加 ---------------------------------------------------

# 関数定義
# --- 系列アノテーションの追加
def autoLabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.annotate('{}'.format(height), xy=(rect.get_x() + rect.get_width() / 2, height + 0.5), ha='center')

# プロット作成
rect1 = plt.bar(x - width / 2, men_means, width, color='blue')
rect2 = plt.bar(x + width / 2, women_means, width)
plt.xticks(x, labels=labels)
plt.grid()
plt.ylabel('Score')
plt.title('Score by gender')
autoLabel(rect1)
autoLabel(rect2)
plt.tight_layout()
plt.show()
