# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 66 ポリモーフィズム
# Creat Date  : 2022/2/8
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜概要＞
# - サブクラスを複数作成し、同じメソッドを定義して呼び出す際にどのクラスかを意識せずに呼び出すこと


# ＜目次＞
# 0 準備
# 1 スーパークラスの定義
# 2 サブクラスの定義
# 3 ポリモーフィズム


# 0 準備 -----------------------------------------------------------

# ライブラリ
from abc import abstractmethod, ABCMeta


# 1 スーパークラスの定義 --------------------------------------------

# ＜ポイント＞
# - 抽象メソッドはスーパークラスのメソッドに記述する（中身は定義しない）


class Human(metaclass=ABCMeta):  # 親クラス

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def say_something(self):
        pass

    def say_name(self):
        print(self.name)


# 2 サブクラスの定義 ----------------------------------------------

# ＜ポイント＞
# - スーパークラスで抽象メソッドとしたメソッドが実装されている必要がある
#   --- 実装がない場合は明示的にエラーが返される


class Woman(Human):

    def say_something(self):
        print('女性: 名まえは={}'.format(self.name))


class Man(Human):

    def say_something(self):
        print('男性: 名まえは={}'.format(self.name))


# 3 ポリモーフィズム -----------------------------------------------

# ＜ポイント＞
# - humanクラスは入力値によってManクラスかWomanクラスか分からない
# - しかし、以下のプログラムはどちらか分からなくても実行できる
#   --- 同じメソッドが抽象クラスで実装されているため


# 数値入力
num = input('0か1を入力してください')

# インスタンス生成
if num == '0':
    human = Man('Taro')
elif num == '1':
    human = Woman('Hanako')
else:
    print('入力が間違っています')

# メソッド実行
# --- ポリモーフィズムの考え方
human.say_something()
