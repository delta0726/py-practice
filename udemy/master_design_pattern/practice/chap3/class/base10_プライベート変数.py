# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 67 プライベート変数
# Creat Date  : 2022/2/8
# Final Update: 2022/3/3
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜概要＞
# - クラス変数やインスタンス変数は外部からアクセスして値を書き換えることが可能
# - プライベート変数はアクセスできない変数のことをいう
#   --- アンダースコア2つ(__)を変数名の前に付ける
#   --- 厳密にはアクセス可能であり、Pythonでは厳密なプライベート変数はない
# - プライベート変数であっても外部から値の変更は可能
#   --- アクセスコントロールする手段としてgetterとsetterがある（後述）


# ＜目次＞
# 1 クラス定義(通常の変数)
# 2 クラス定義(プライベート変数)


# 1 クラス定義(通常の変数) ------------------------------------------

# ＜ポイント＞
# - プライベート変数と動作比較してみる


# クラス定義
class Human1:

    class_val = 'Human'

    def __init__(self, name, age):
        # インスタンス変数として定義
        self.name = name
        self.age = age

    def print_msg(self):
        print('name = {}, age = {}'.format(self.name, self.age))


# インスタンス生成
human1 = Human1(name='Taro', age=15)

# 変数へのアクセス（外部からもアクセス可能）
# --- クラス変数
# --- インスタンス変数
human1.class_val
human1.name
human1.age

# メソッドの実行
# --- クラス内でもアクセス可能
human1.print_msg()


# 2 クラス定義(プライベート変数) ------------------------------------------

# ＜ポイント＞
# - プライベート変数は外部からアクセスすることが禁止されている
# - クラス内では通常どおり使用することが可能


# クラス定義
class Human2:
    # クラス変数
    # --- プライベート変数の定義
    __class_val = 'Human'

    def __init__(self, name, age):
        # インスタンス変数
        # --- プライベート変数として定義
        self.__name = name
        self.__age = age

    def print_msg(self):
        print('name = {}, age = {}'.format(self.__name, self.__age))


# インスタンス生成
human2 = Human2(name='Taro', age=15)

# 変数アクセス
# --- 外部からはアクセス不可（エラー）
human2.__name
human2.__age

# メソッドの実行
# --- クラス内からはアクセス可能
human2.print_msg()

# ＜参考＞
# 厳密には以下の方法で変数にアクセス可能
# human2._Human2__name
