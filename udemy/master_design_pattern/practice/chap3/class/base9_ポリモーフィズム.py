# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 66 ポリモーフィズム
# Creat Date  : 2022/2/8
# Final Update: 2022/3/2
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜概要＞
# - ｢ポリモーフィズム｣を実現するための手段として｢抽象クラス｣を用いる


# ＜抽象クラスとは＞
# - クラス自体は実装を持たず、メソッドの名前と体系のみを抽象的に定義するクラス
#   --- スーパークラスで定義されるもので、継承の概念の中で使用される
# -- 抽象クラスで抽象化を指定したメソッドは｢抽象メソッド｣と呼ばれる
#   --- 抽象メソッドはサブクラスでの実装が強制される


# ＜ポリモーフィズムとは＞
# - サブクラスを複数作成し、同じメソッドを定義して呼び出す際にどのクラスかを意識せずに呼び出すこと
#   --- 同じ名称のメソッドを定義するので、事前に選択されるクラスが分からなくても動作する


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


# スーパークラスの定義
# --- 抽象メソッドには@abstractmethodをつける（pass文のみを記述して実装は行わない）
class Human(metaclass=ABCMeta):

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

    def say_dummy(self):
        print('女性: 名まえは={}'.format(self.name))

    def say_something(self):
        print('女性: 名まえは={}'.format(self.name))


class Man(Human):

    def say_something(self):
        print('男性: 名まえは={}'.format(self.name))


class Woman_Err(Human):
    pass


# エラー確認
# --- Womanクラスにsay_something()を含めないで定義するとエラーとなる
# --- TypeError: Can't instantiate abstract class Woman with abstract methods say_something
human = Woman(name='Hanako')


# 3 ポリモーフィズム -----------------------------------------------

# ＜ポイント＞
# - humanクラスは入力値によってManクラスかWomanクラスが作られる（事前にクラスが分からない）
# - しかし、以下のプログラムはどちらか分からなくても実行できる
#   --- 抽象クラスを介して同じ名称のメソッドが実装されているため


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
