# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 6 デザインパターン講座
# Theme       : 構造に関するパターン（Decorator）
# Creat Date  : 2022/2/28
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜Decoratorパターン＞
# - 別のクラスが持っている特定の機能を別のクラスに追加する
#   --- 互いに関連したクラスの処理をクラスをまたいで追加していきたい場合に用いられる


# ＜目的＞
# - 複数の機能を1つのクラスにまとめる


# ＜仕組み＞
# - Componentを継承したConcreteComponent , Decoratorを作成する
# - DecoratorはComponentをプロパティに持つ。
# - Decoratorを継承したConcreteDecoratorを作成する
# - 利用する際にプロパティにConcreteComponentを設定する


# ＜構成要素＞
# Component         : 機能を追加する際の中核となるクラス
# ConcreteComponent : 追加する処理を記載したComponentを継承したクラス
# Decorator         : Componentを継承したクラスで、プロパティにComponentを持つ
# ConcreteDecorator : Decoratorの処理を具体的に記述したクラス


# ＜目次＞
# 0 準備
# 1 Componentの定義
# 2 ConcreteComponentの定義
# 3 Decoratorの定義
# 4 ConcreteDecoratorの定義
# 5 動作確認


# 0 準備 ----------------------------------------------------------------

# ライブラリ
from abc import ABC, abstractmethod


# 1 Componentの定義 ------------------------------------------------------

class Component(ABC):

    @abstractmethod
    def operation(self):
        pass


# 2 ConcreteComponentの定義 -----------------------------------------------

class ShowCharComponent(Component):

    def __init__(self, char):
        self.__char = char

    def operation(self):
        print(self.__char * 20)


# 3 Decoratorの定義 -------------------------------------------------

class ShowDecorator(Component, ABC):

    def __init__(self, component: Component):
        self._component = component


class WriteDecorator(Component, ABC):

    def __init__(self, component: Component, file_name, msg):
        self._component = component
        self._file_name = file_name
        self._msg = msg


# 4 ConcreteDecoratorの定義 --------------------------------------------------

class ShowMessage(ShowDecorator):

    def __init__(self, component: Component, msg):
        super().__init__(component)
        self.__msg = msg

    def operation(self):
        self._component.operation()  # Componentのメソッド
        print(self.__msg)  # ShowMessageクラスのメソッド
        self._component.operation()


class WriteMessage(WriteDecorator):

    def operation(self):
        self._component.operation()
        with open(self._file_name, mode='w') as fh:
            fh.write(self._msg)


# 5 動作確認 -----------------------------------------------------------------

show_component = ShowCharComponent('-')

# show_component.operation()
show_message = ShowMessage(show_component, 'Hello World')

# show_message.operation()
write_message = WriteMessage(show_message, 'practice/chap6/構造に関するパターン/output/tmp2.txt', 'Write Message')
write_message.operation()
