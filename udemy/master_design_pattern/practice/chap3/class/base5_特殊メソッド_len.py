# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 60 特殊メソッド2 __len__
# Creat Date  : 2022/2/7
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜概要＞
# - 特殊メソッドはクラスに定型的な機能を持たせるために実装する
# - __len__はインスタンスにlen()が適用された際の振舞いを定義する


# ＜目次＞
# 1 クラス定義
# 2 __len__を実行する


# 1 クラス定義 ----------------------------------------------

# ＜ポイント＞
# - __len__はインスタンスにlen()が適用された場合の振舞いを定義する


# クラス定義
class Human:

    # コンストラクタ
    def __init__(self, name, age, phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number

    # len()が適用された場合に発動
    def __len__(self):
        #print('__len__が実行されました')
        return len(self.name)


# 2 __len__を実行する ----------------------------------------------

# ＜ポイント＞
# - __len__はインスタンスにif文が適用された場合に発動される


# インスタンス生成
man1 = Human(name='Taro', age=20, phone_number='08011111111')
man2 = Human(name='Taro2', age=18, phone_number='08011111111')

# nameの長さを取得
len(man1)
len(man2)
