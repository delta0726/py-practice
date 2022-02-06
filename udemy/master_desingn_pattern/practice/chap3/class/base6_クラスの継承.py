# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       :
# Creat Date  : 2022//
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜概要＞
# - クラス継承はオブジェクト指向の要素の1つ
#   --- オブジェクト指向の3要素とは｢継承｣｢ポリモーフィズム｣｢カプセル化｣をいう


# ＜継承＞
# - ある別のクラスを参照することで参照先のプロパティやメソッドを引き継ぐこと
#   --- 参照先をスーパークラス、実装先をサブクラスという


# ＜ポリモーフィズム＞
# - 複数作成したサブクラス間でメソッド名を統一させること
#   --- ユーザーはサブクラスごとの実装の違いを意識せずに使うことができる


# ＜メソッドの上書き＞
# - オーバーライド： 親クラスと同じ名前のメソッドを定義すること
# - オーバーロード： 親クラスと同じ名前のメソッドだが、引数や戻り値の異なるものを定義すること
#                  ⇒オーバーロードはPythonではできない


# ＜目次＞
# 1 スーパークラスの定義
# 2 サブクラスの定義
# 3 クラスの実行


# 1 スーパークラスの定義 ---------------------------------------------------

# ＜ポイント＞
# - スーパークラス自体は通常のクラス
#   --- インスタンスを生成して単独で用いることも可能


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greeting(self):
        print('hello {}'.format(self.name))
    
    def say_age(self):
        print('{} years old'.format(self.age))


# 2 サブクラスの定義 --------------------------------------------------------

# ＜ポイント＞
# - サブクラスはスーパークラス(Person)を継承している
#   --- コンストラクタでsuper().__init__()を実行する


class Employee(Person):

    def __init__(self, name, age, number):
        super().__init__(name, age)
        self.number = number

    # サブクラス独自の実装
    def say_number(self):
        print('my number is = {}'.format(self.number))

    # オーバライド
    # --- 親クラスに存在するものを上書きする
    def greeting(self):
        super().greeting()
        print('I\'m employee phone_number = {}'.format(self.number))

    # オーバロード
    # --- 親クラスの実装に引数を追加している
    # def greeting(self, age):
    #     print('オーバーロード')


# 3 クラスの実行 ----------------------------------------------------------

# インスタンス生成（サブクラス）
man = Employee(name='Tonegawa', age=45, number='08011111111')

# メソッドの実行
# --- サブクラスでオーバーライド
man.greeting()

# メソッドの実行
# --- スーパークラスのみで実行
man.say_age()

# メソッドの実行
# --- サブクラスのみで実行
man.say_number()
