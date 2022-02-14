# ******************************************************************************
# Course      : Python3.8マスター講座
# Chapter     : 9 標準ライブラリ（collections）
# Theme       : collections（namedtupleモジュール）
# Creat Date  : 2022/2/14
# Final Update:
# URL         : https://www.udemy.com/course/python-python/
# ******************************************************************************


# ＜概要＞
# - リストと似たオブジェクトだが処理時間が速いのが特徴


# ＜参考＞
# 公式ドキュメント
# https://docs.python.org/ja/3/library/collections.html


# ＜目次＞
# 0 準備
# 1 オブジェクトの作成
# 2 主なメソッド


# 0 準備 ---------------------------------------------------

# ライブラリ
from collections import namedtuple



# 1 オブジェクトの作成 --------------------------------------

# オブジェクト定義
# ---- クラス定義のイメージ
S = namedtuple('Student', ['name', 'age', 'grade'])

# インスタンス生成
taro = S('Taro', 12, 3)

# 確認
print(taro.name)
print(taro[0])
print(taro[1])
print(taro[2])

# 要素の置換
taro = taro._replace(name='Jiro')
print(taro.name)

# 辞書からの作成
dict_b = {'name': 'John', 'age': 20, 'grade': 2}
john = S(**dict_b)
print(john)


# 2 主なメソッド --------------------------------------------------

# オブジェクト定義
S = namedtuple('Student', ['name', 'age', 'grade'])
taro = S('Taro', 12, 3)

# 辞書に変換
print(taro._asdict())

# キー一覧
print(taro._fields)

# _makeメソッドによる作成
paul = S._make(['Paul', 15, 2])
print(paul)
