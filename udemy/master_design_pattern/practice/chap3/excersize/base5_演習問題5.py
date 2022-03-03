# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 演習問題5
# Creat Date  : 2022/3/2
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜概要＞
# - 継承とポリモーフィズムを用いてAnimalクラスにspeakという抽象メソッドを定義する


# ＜実装＞
# - Animalクラスにspeakという抽象メソッドを定義する
# - Dogクラス   : speakメソッドを実行すると｢わん｣
# - Catクラス   : speakメソッドを実行すると｢にゃー｣
# - Sheepクラス : speakメソッドを実行すると｢めー｣
# - Otherクラス : speakメソッドを実行すると｢そんな動物いない｣


# ＜目次＞
# 0 準備
# 1 スーパークラスの定義
# 2 サブクラスの定義
# 3 動作確認


# 0 準備 --------------------------------------------------------------

# ライブラリ
from abc import abstractmethod, ABCMeta


# 1 スーパークラスの定義 -------------------------------------------------

# ＜ポイント＞
# - 抽象クラスとして定義してspeakメソッドを抽象メソッドとする
#   --- メソッド名を定義するだけで実装は行わない(pass文のみ)


class Animals(metaclass=ABCMeta):

    @abstractmethod
    def speak(self):
        pass


# 2 サブクラスの定義 -------------------------------------------------------

# ＜ポイント＞
# - Animalクラスを継承してspeakメソッドを実装する
#   --- speakメソッドを定義しないとTypeErrorとなる


class Dog(Animals):

    def speak(self):
        print('わん')


class Cat(Animals):

    def speak(self):
        print('にゃー')


class Sheep(Animals):

    def speak(self):
        print('めー')


class Other(Animals):

    def speak(self):
        print('そんな動物いない')


# 3 動作確認 ------------------------------------------------------------

# ＜ポイント＞
# - 抽象メソッドを定義したことでポリモーフィズムが実現できている
#   --- 生成されるクラスに関わらず同一のメソッドが使用可能


# インスタンス生成
number = input('好きな動物は？ 1: 犬、2: 猫, 3:羊')

# インスタンス生成
# --- 入力値に応じて生成するクラスが異なる
if number == '1':
    animal = Dog()
elif number == '2':
    animal = Cat()
elif number == '3':
    animal = Sheep()
else:
    animal = Other()

# メソッドの実行
# --- ポリモーフィズムを実現しているたspeakメソッドが共通して使用可能
animal.speak()
