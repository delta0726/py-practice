# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 59 特殊メソッド1  __str__
# Creat Date  : 2022/2/6
# Final Update: 2022/3/2
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜概要＞
# - 特殊メソッドはクラスに定型的な機能を持たせるために実装するメソッド
# - __str__はインスタンスのprintの出力値をカスタマイズする


# ＜目次＞
# 1 クラス定義
# 2 __str__で定義したオブジェクトの出力


# 1 クラス定義 ----------------------------------------------

# クラス定義
class Human:

    # コンストラクタ
    def __init__(self, name, age, phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number

    # 文字列変換
    def __str__(self):
        return 'name = {}, age = {}, phone_number: {}'.format(self.name, self.age, self.phone_number)


# 2 __str__で定義したオブジェクトの出力 ------------------------------------

# ＜ポイント＞
# - インスタンスをprint()すると通常はメモリアドレスが返される
#   --- __str__を付けると出力方法を設定することができる


# インスタンス生成
woman = Human(name='Elsa', age=20, phone_number='08011111111')

# 確認
# --- __str__で設定した出力定義に基づいて出力される
# --- 通常だとクラス情報が出力される（<__main__.Human object at 0x000001C92D438AC0>）
print(woman)
