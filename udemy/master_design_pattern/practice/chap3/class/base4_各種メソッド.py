# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 各種メソッド（インスタンスメソッド / クラスメソッド /スタティックメソッド）
# Creat Date  : 2022/2/6
# Final Update: 2022/3/2
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜概要＞
# - メソッドには以下の3種類のメソッドがある
#   --- インスタンスメソッド
#   --- クラスメソッド
#   --- スタティックメソッド


# ＜インスタンスメソッド＞
# - クラス内に定義される一般的なメソッド（第1引数は必ず｢self｣となる）
# - クラス変数とインスタンス変数の両方にアクセス可能


# ＜クラスメソッド＞
# - インスタンス化せずに使えるメソッド
# - メソッド名にはデコレータ(@classmethod)を付け、第1引数は必ず｢cls｣となる
# - クラス変数のみにアクセス可能（インスタンス生成を前提としないので、インスタンス変数は使えない）


# ＜スタティックメソッド＞
# - クラス内に定義されている点を除けば、単なる関数に近い
# - メソッド名にはデコレータ(@staticmethod)を付ける（第1引数に制約はない）
# - クラス変数もインスタンス変数もアクセス不可
# - クラス変数やインスタンス変数に全くアクセスする必要がない場合にそれを明示するために使用する


# ＜目次＞
# 1 クラス定義
# 2 インスタンスメソッドの実行
# 3 クラスメソッドの実行
# 4 スタティックメソッドの実行


# 1 クラス定義 ----------------------------------------------

# ＜ポイント＞
# - 3種類のメソッドを持つクラスを定義して各メソッドの振舞いの違いを確認する


class Human:
    # クラス変数
    class_name = "Human"

    # コンストラクタ
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # インスタンスメソッド
    # --- 第1引数がselfとなる
    # --- クラス変数とインスタンス変数の両方にアクセスすることができる
    def print_name_age(self):
        print('インスタンスメソッド実行')
        print('name = {}, age = {}'.format(self.name, self.age))

    # クラスメソッド
    # --- デコレータを付けて第1引数をclsとする
    # --- クラス変数にアクセスすることができる（インスタンスがないのでインスタンス変数のアクセスは不可）
    @classmethod
    def print_class_name(cls, msg):
        print('クラスメソッド実行')
        print(cls.class_name)
        print(msg)

    # スタティックメソッド
    @staticmethod
    def print_msg(msg):
        print('スタティックメソッド実行')
        print(msg)


# 2 インスタンスメソッドの実行 ---------------------------------------------

# ＜ポイント＞
# - インスタンスを生成してから実行する
# - クラス変数とインスタンス変数の両方にアクセス可能


# インスタンス生成
man = Human(name='桜木', age=18)

# メソッド実行
# --- クラス変数とインスタンス変数にアクセス
man.print_name_age()


# 3 クラスメソッドの実行 ---------------------------------------------------

# ＜ポイント＞
# - クラスからメソッドを直接呼び出す（インスタンス生成なしに実行できる）
# - クラス変数のみアクセス可能（インスタンスを生成しないためインスタンス変数はアクセス不可）
# - クラスメソッドが持つ引数に値を与えることは可能


# メソッド実行
# --- クラスからメソッドを直接呼び出す
Human.print_class_name(msg='こんにちは')


# 4 スタティックメソッドの実行 --------------------------------------------

# ＜ポイント＞
# - スタティックメソッドはインスタンスからもクラスからも実行可能
#   --- メソッドを関数的な使い方をするためのものなのでインスタンスを生成しないほうが自然
#   --- @staticmethodのデコレータで関数的に使用するメソッドであることを明示できる


# インスタンス生成
man = Human(name='桜木', age=18)

# メソッド実行
# --- インスタンスから実行
# --- クラスから実行
man.print_msg('hello static')
Human.print_msg('hello static')
