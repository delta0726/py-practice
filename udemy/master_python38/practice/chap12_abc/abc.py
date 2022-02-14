# ******************************************************************************
# Course      : Python3.8マスター講座
# Chapter     : 12 抽象基底クラス（abc）
# Theme       : abcモジュール
# Creat Date  : 2022/2/16
# Final Update:
# URL         : https://www.udemy.com/course/python-python/
# ******************************************************************************


# ＜概要＞
# - 主に他のクラスに継承されることによって利用されるクラス
# - ポリモーフィズムを実装する際に用いられる
#   --- 抽象プロパティと抽象メソッドを継承先のクラスで実装する


# ＜参考＞
# 公式ドキュメント
# https://docs.python.org/ja/3/library/abc.html


# ＜目次＞
# 0 準備
# 1 クラス定義


# 0 準備 ------------------------------------------------------------

# 抽象基底クラス
from abc import (
    abstractproperty, abstractmethod, abstractclassmethod,
    abstractstaticmethod, ABC, ABCMeta
)



# 1 abstractpropertyの使い方 ------------------------------------------

# ＜ポイント＞
# - スーパークラスで@abstractpropertyを指定するとサブクラスで定義がない場合にエラーとなる
#   --- ABCクラスを継承する


# スーパークラス
class BaseAbstracClass(ABC):

    @abstractproperty
    def value(self):
        return 'Read Only Property'


# サブクラス
class MyClass(BaseAbstracClass):

    _value = 'Default Value'

    @property
    def value(self):
        return self._value

    def print_a(self):
        print('A')


# クラス定義
a = MyClass()
print(a.value)


# 2 ABCmetaの使い方 ------------------------------------------

# ＜ポイント＞
# - スーパークラスで@abstractpropertyを指定するとサブクラスで定義がない場合にエラーとなる
#   --- metaclassにABCMetaクラスを指定する

# スーパークラス
class BaseAbstracClass(metaclass=ABCMeta):

    @abstractproperty
    def value(self):
        return 'Read Only Property'


# サブクラス
class MyClass(BaseAbstracClass):

    _value = 'Default Value'

    @property
    def value(self):
        return self._value

    def print_a(self):
        print('A')


# クラス定義
a = MyClass()
print(a.value)


# 3 抽象クラスのメソッド ----------------------------------------------------

# ＜ポイント＞
# - ポリモーフィズムではスーパークラスで定義した各種メソッドはサブクラスで実装する
#   --- サブクラスで実装が無ければエラーとなる


class BaseAbstractClass(metaclass=ABCMeta):

    @abstractproperty
    def value(self):
        return 'Read Only property'

    @abstractmethod
    def print_value(self):
        pass

    @abstractclassmethod
    def write_value(cls, value):
        pass

    @abstractstaticmethod
    def print_static():
        pass


class MyClass(BaseAbstractClass):
    _value = 'Default Value'

    @property
    def value(self):
        return self._value

    def print_value(self):
        print('value = {}'.format(self.value))

    @classmethod
    def write_value(cls, value):
        with open('txt/tmp.txt', mode='w', encoding='utf-8') as fh:
            fh.write(value)

    @staticmethod
    def print_static():
        print('staticメソッド')

    def print_a():
        print('A')


# インスタンス生成
a = MyClass()
print(a.value)

# メソッド実行
a.print_value()
MyClass.write_value('抽象クラスの演習')
# a.print_static()
