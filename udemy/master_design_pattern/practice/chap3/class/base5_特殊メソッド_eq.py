# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 59 特殊メソッド1  __eq__
# Creat Date  : 2022/2/6
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜概要＞
# - 特殊メソッドはクラスに定型的な機能を持たせるために実装するメソッド
# - __eq__はインスタンス同士の一致比較の振舞いをカスタマイズする


# ＜目次＞
# 1 インスタンス同士の比較
# 2 __eq__による比較操作のカスタマイズ


# 1 インスタンス同士の比較 -----------------------------------------------

# ＜ポイント＞
# - 同じクラスのインスタンスでも別オブジェクトとして定義される
#   --- インスタンスを比較してもFalseとなる


# クラス定義
# --- 特殊メソッド(__eq__)を実装していないケース
class Human1:
    # コンストラクタ
    def __init__(self, name, age, phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number


# インスタンス生成
man_1 = Human1(name='Taro', age=20, phone_number='08011111111')
man_2 = Human1(name='Taro', age=20, phone_number='08011111111')

# 確認
# --- IDが異なるので別オブジェクト
print(man_1)
print(man_2)

# 一致確認
man_1 == man_2


# 2 __eq__による比較操作のカスタマイズ --------------------------------------

# ＜ポイント＞
# - __eq__でインスタンス同士の一致条件を定義する
#   --- 一致条件のもとでの判定である点に注意


# クラス定義
# --- 特殊メソッド(__eq__)を実装するケース
class Human2:
    # コンストラクタ
    def __init__(self, name, age, phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number

    def __eq__(self, ohter):
        return (self.name == ohter.name) and \
               (self.phone_number == ohter.phone_number)


# インスタンス生成
man_3 = Human2(name='Taro', age=20, phone_number='08011111111')
man_4 = Human2(name='Taro', age=18, phone_number='08011111111')

# 確認
# --- IDが異なるので別オブジェクト
print(man_3)
print(man_4)

# 一致確認
# --- 指定条件を満たしていればTrueを返す
print(man_3 == man_4)


# 不一致ケースの確認
man_5 = Human2(name='Jiro', age=20, phone_number='08011111111')
man_6 = Human2(name='Taro', age=18, phone_number='08011111111')
print(man_5 == man_6)
