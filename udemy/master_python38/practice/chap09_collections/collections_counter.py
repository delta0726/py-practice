# ******************************************************************************
# Course      : Python3.8マスター講座
# Chapter     : 9 標準ライブラリ（collections）
# Theme       : collections（Counterモジュール）
# Creat Date  : 2022/2/14
# Final Update:
# URL         : https://www.udemy.com/course/python-python/
# ******************************************************************************


# ＜概要＞
# - 要素数をカテゴリごとにカウントする機能を持つオブジェクト


# ＜参考＞
# 公式ドキュメント
# https://docs.python.org/ja/3/library/collections.html


# ＜目次＞
# 0 準備
# 1 Counterオブジェクトの作成
# 2 Counterオブジェクトの操作


# 0 準備 ---------------------------------------------------

# ライブラリ
from collections import Counter
from random import randint, seed


# 1 Counterオブジェクトの作成 ---------------------------------

# データ作成
# --- 整数の乱数
seed(1)
list_a = [randint(0, 5) for _ in range(20)]

# カウンターオブジェクトの作成
cnt = Counter(list_a)

# 確認
# --- 辞書風に要素数がカウントされている
# --- 元のリスト
print(cnt, type(cnt))
print(list_a)


# 2 Counterオブジェクトの操作 ---------------------------------

# 0の数
print(cnt[0])

# リスト形式で出力
print(list(cnt.elements()))

# 要素数の多い順に並び替え
# --- リスト+タプルで表現
print(cnt.most_common())

# 要素数をコントロールする
# --- most_commonの結果に対して加減算を行う
cnt = Counter(list_a)
print(cnt.most_common())
cnt.subtract({2: 20, 3: -5})
print(cnt.most_common())
