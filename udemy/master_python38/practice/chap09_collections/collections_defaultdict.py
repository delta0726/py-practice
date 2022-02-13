# ******************************************************************************
# Course      : Python3.8マスター講座
# Chapter     : 9 標準ライブラリ（collections）
# Theme       : collections（defaultdictモジュール）
# Creat Date  : 2022/2/14
# Final Update:
# URL         : https://www.udemy.com/course/python-python/
# ******************************************************************************


# ＜概要＞
# - デフォルト値を持つ辞書（検索キーがない場合にデフォルト値が出力される）
#   --- キーエラーが発生しない


# ＜参考＞
# 公式ドキュメント
# https://docs.python.org/ja/3/library/collections.html


# ＜目次＞
# 0 準備
# 1 defaultdictオブジェクトの作成
# 2 defaultdictオブジェクトの操作


# 0 準備 ---------------------------------------------------

# ライブラリ
from collections import defaultdict


# 1 defaultdictオブジェクトの作成 ----------------------------

# 通常の辞書
# --- キーがなければKeyErrorとなる
s_dict = dict()
print(s_dict['A'])

# defaultdict
# --- キーがなくてもデフォルト値が返る（KeyErrorが発生しない）
d_dict = defaultdict(lambda: 0)
print(d_dict['A'])


# 2 defaultdictオブジェクトの操作 -----------------------------

# 値の変更
d_dict = defaultdict(lambda: 0)
print(d_dict['A'])
d_dict['A'] = 100
print(d_dict['A'])

# 値の変更
# --- 値を加算で変更
# --- デフォルト1に1を加算して2となる
d_dict = defaultdict(lambda: 1)
d_dict['B'] += 1
print(d_dict)

# 辞書型のメソッドは全て使用可能
d_dict.keys()
d_dict.values()
