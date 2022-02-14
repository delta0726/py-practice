# ******************************************************************************
# Course      : Python3.8マスター講座
# Chapter     : 9 標準ライブラリ（collections）
# Theme       : collections（dataclassモジュール）
# Creat Date  : 2022/2/14
# Final Update:
# URL         : https://www.udemy.com/course/python-python/
# ******************************************************************************


# ＜概要＞
# - Cの構造体に似たオブジェクトを生成する
#   --- Python3.7以降


# ＜参考＞
# 公式ドキュメント
# https://docs.python.org/ja/3/library/collections.html


# ＜目次＞
# 0 準備
# 1 オブジェクトの作成
# 2 主なメソッド


# 0 準備 ---------------------------------------------------

# dataclasses(3.7以降)
from dataclasses import dataclass


# 1 オブジェクトの作成 ----------------------------------------

@dataclass
class Student:
    name: str
    age: int
    grade: int


# インスタンス生成
taro = Student('Taro', 12, 3)

# 確認
print(taro.name)
print(taro.age)

# 値の変更
taro.grade = 4
print(taro)


jiro = Student('Taro', 12, 4)
print(taro == jiro)
