# ******************************************************************************
# Course      : Python3.8マスター講座
# Chapter     : 9 標準ライブラリ（collections）
# Theme       : collections（OrderedDictモジュール）
# Creat Date  : 2022/2/14
# Final Update:
# URL         : https://www.udemy.com/course/python-python/
# ******************************************************************************


# ＜概要＞
# - 要素の順番が保証された辞書
#   --- Python3.7以降は通常の辞書も順番の概念を持つようになった
#   --- 辞書はブレース({})で定義するが、OrderedDictはブラケット([])とパレンティス(())で定義する


# ＜参考＞
# 公式ドキュメント
# https://docs.python.org/ja/3/library/collections.html


# ＜目次＞
# 0 準備
# 1 OrderedDictの作成
# 2 OrderedDictの操作
# 3 比較の際の順序に対する振舞い


# 0 準備 ------------------------------------------------------------

# ライブラリ
from collections import OrderedDict


# 1 OrderedDictの作成 ------------------------------------------------

# OrderedDictの作成
o_dict = OrderedDict([('A', 100), ('B', 200)])

# 確認
print(o_dict, type(o_dict))


# 2 OrderedDictの操作 -----------------------------------------------

# 要素位置の変更
# --- 特定の要素を末尾に移動
o_dict = OrderedDict([('A', 100), ('B', 200), ('C', 300)])
o_dict.move_to_end('A', True)
print(o_dict)

# 要素位置の変更
# --- 特定の要素を末尾から移動
o_dict = OrderedDict([('A', 100), ('B', 200), ('C', 300)])
o_dict.move_to_end('C', False)
print(o_dict)


# 3 比較の際の順序に対する振舞い -------------------------------------------

# ＜ポイント＞
# - 通常の辞書型は要素が一致すれば順序の違いに関係なくTrueを返す
# - OrderedDictは要素と順序が一致している場合のみTrueを返す


# 通常の辞書型
# --- True
print({'A': 100, 'B': 200} == {'B': 200, 'A': 100})

# OrderedDict
# --- False
print(OrderedDict([('A', 100), ('B', 200)])
      == OrderedDict([('B', 200), ('A', 100)]))
