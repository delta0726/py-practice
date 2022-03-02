# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 60 特殊メソッド2 __bool__
# Creat Date  : 2022/2/6
# Final Update: 2022/3/2
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜概要＞
# - 特殊メソッドはクラスに定型的な機能を持たせるために実装するメソッド
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
#   --- 定義した基準に基づいてTrue/Falseを返す


# インスタンス生成
man1 = Human(name='Taro', age=20, phone_number='08011111111')
man2 = Human(name='Taro', age=18, phone_number='08011111111')

# 確認
# --- インスタンスのageに対して判定をおっこなう
print('ageが20以上') if man1 else print('ageが20以下')
print('ageが20以上') if man2 else print('ageが20以下')
