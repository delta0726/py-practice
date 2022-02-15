# ******************************************************************************
# Course      : Python3.8マスター講座
# Chapter     : 15 科学技術計算ライブラリ
# Theme       : サブプロット
# Creat Date  : 2022/2/16
# Final Update:
# URL         : https://www.udemy.com/course/python-python/
# ******************************************************************************


# ＜概要＞
# - matpllotlibでサブプロットを作成する
#   --- プロットを並べるだけでファセットではない点に注意


# ＜目次＞
# 0 準備
# 1 複数プロットの表示
# 2 サブプロットの作成
# 3 サブプロットの装飾
# 4 サブプロットを4つに拡張


# 0 準備 ----------------------------------------------------------

# ライブラリ
import numpy as np
import matplotlib.pyplot as plt


# 1 複数系列のプロットの表示 ------------------------------------------

# ＜参考＞
# [Matplotlib] 線の種類、色と太さの設定
# https://python.atelierkobato.com/linestyle/


# データ作成
x = np.arange(10)
y = x

# 系列の作成
# --- カラーやスタイルは引数で個別に指定可能
plt.plot(x, y, color=(255 / 255, 127 / 255, 80 / 255, 0.3), linestyle='--')
plt.plot(x, y + 1, 'ko:')
plt.plot(x, y - 1, 'c<-')
plt.plot(x, y - 2, 'y>-')

# プロット表示
plt.show()


# 2 サブプロットの作成 -----------------------------------------------

# ＜ポイント＞
# - subplot(行数, 列数, 表示番号)で構成と出力位置を決定する


# プロット1
plt.subplot(2, 1, 1)
x = np.arange(10)
y = x
plt.plot(x, y, color=(255 / 255, 127 / 255, 80 / 255, 0.3), linestyle='--')
plt.plot(x, y + 1, 'ko:')
plt.plot(x, y - 1, 'c<-')
plt.plot(x, y - 2, 'y>-')

# プロット2
plt.subplot(2, 1, 2)
x = np.arange(100)
y = np.random.randint(0, 10, 100)
plt.plot(x, y)

# プロット表示
plt.show()


# 3 サブプロットの装飾 ----------------------------------------------------

# プロット1
ax = plt.subplot(2, 1, 1)
x = np.arange(10)
y = x
plt.plot(x, y, color=(255 / 255, 127 / 255, 80 / 255, 0.3), linestyle='--')
plt.plot(x, y + 1, 'ko:')
plt.plot(x, y - 1, 'c<-')
plt.plot(x, y - 2, 'y>-')

# プロット1の装飾
ax.grid()
ax.set_ylabel('Y label - chart1')
ax.set_xlabel('X label - chart1')
ax.set_title('Title - chart1')
ax.legend(['y'], loc='best')

# プロット2
ax = plt.subplot(2, 1, 2)
x = np.arange(100)
y = np.random.randint(0, 10, 100)
plt.plot(x, y)

# プロット2の装飾
ax.grid()
ax.set_ylabel('Y label - chart2')
ax.set_xlabel('X label - chart2')
ax.set_title('Title - chart2')
ax.legend(['y'], loc='best')

# プロット表示
plt.show()


# 4 サブプロットを4つに拡張 -----------------------------------------------

# ＜ポイント＞
# - サブプロットを(2, 2)で指定して1から順にプロットを作成して格納していく


# プロット1
ax = plt.subplot(2, 2, 1)
x = np.arange(10)
y = x
plt.plot(x, y, color=(255 / 255, 127 / 255, 80 / 255, 0.3), linestyle='--')
plt.plot(x, y + 1, 'ko:')
plt.plot(x, y - 1, 'c<-')
plt.plot(x, y - 2, 'y>-')

# プロット2
ax = plt.subplot(2, 2, 2)
x = np.arange(100)
y = np.random.randint(0, 10, 100)
plt.plot(x, y)

# プロット3
ax = plt.subplot(2, 2, 3)
x = np.arange(100)
y = np.random.randint(0, 10, 100)
plt.plot(x, y, color='k', linestyle='--', linewidth=2.0,
         marker='o', markerfacecolor='b', markeredgecolor='r',
         markeredgewidth=2.0, markersize=6)

# プロット4
ax = plt.subplot(2, 2, 4)
x = np.linspace(0, 10 * np.pi, 100)
y = np.sin(x)
ax.set_title('sin')
plt.plot(x, y)
plt.tight_layout()

# プロット保存
plt.savefig('png/test2.jpg')

# プロット表示
plt.show()

