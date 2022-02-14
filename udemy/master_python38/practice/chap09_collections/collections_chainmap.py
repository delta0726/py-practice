# ******************************************************************************
# Course      : Python3.8マスター講座
# Chapter     : 9 標準ライブラリ（collections）
# Theme       : collections（ChainMapモジュール）
# Creat Date  : 2022/2/14
# Final Update:
# URL         : https://www.udemy.com/course/python-python/
# ******************************************************************************


# ＜概要＞
# - ChainMapとは複数の辞書をつなげたオブジェクトのことをいう


# ＜参考＞
# 公式ドキュメント
# https://docs.python.org/ja/3/library/collections.html


# ＜目次＞
# 0 準備
# 1 オブジェクトの作成
# 2 新しい辞書の追加
# 3 メソッドの実行


# 0 準備 ---------------------------------------------------

# ライブラリ
from collections import ChainMap


# 1 オブジェクトの作成 ----------------------------------------

# ＜ポイント＞
# - ChainMapとは複数の辞書をつなげたオブジェクトのことをいう
# - 指定したキーが複数の辞書にある場合は最初のものが取得される


# オブジェクトの定義
# --- 複数の辞書を入れる
c_map = ChainMap({'key1': 1, 'key2': 2}, {'key3': 3, 'key2': 4})

# 値の取得
# --- key2は最初の2が取得される
print(c_map['key1'])
print(c_map['key2'])
print(c_map['key3'])

# キーの追加
# --- 最初の辞書に追加される
c_map['key4'] = 4
print(c_map)


# 2 新しい辞書の追加 ------------------------------------------

# オブジェクトの定義
c_map = ChainMap({'key1': 1, 'key2': 2}, {'key3': 3, 'key2': 4})

# 新しい辞書の追加
c_map = c_map.new_child({'key5': 5, 'key1': 100})

# 確認
print(c_map)
print(c_map['key5'])
print(c_map['key1'])


# 3 メソッドの実行 ----------------------------------------------

# キーの取得
print(list(c_map.keys()))

# 値の取得
print(list(c_map.values()))
