# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 59 特殊メソッド1 __bool__
# Creat Date  : 2022/2/6
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜概要＞
# - 特殊メソッドはクラスに定型的な機能を持たせるために実装する
# - __bool__はインスタンスにif文が適用された場合の振舞いを定義する


# ＜目次＞
# 1 クラス定義
# 2 __bool__を実行する


# 1 クラス定義 ----------------------------------------------

# ＜ポイント＞
# - __bool__はインスタンスにif文が適用された場合の振舞いを定義する


# クラス定義
class Human:

    # コンストラクタ
    def __init__(self, name, age, phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number

    # if文が適用された場合に発動
    # --- True/Falseの条件を記述
    def __bool__(self):
        print('__bool__が実行されました')
        return True if self.age >= 20 else False



# 2 __bool__を実行する ----------------------------------------------

# ＜ポイント＞
# - __bool__はインスタンスにif文が適用された場合に発動される


# インスタンス生成
man1 = Human(name='Taro', age=20, phone_number='08011111111')
man2 = Human(name='Taro', age=18, phone_number='08011111111')

# 確認
if man1:
    print('ageが20以上')
else:
    print('ageが20以下')

# if文
if man2:
    print('ageが20以上')
else:
    print('ageが20以下')
