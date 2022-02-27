# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 6 デザインパターン講座
# Theme       : 生成に関するパターン（prototype）
# Creat Date  : 2022/2/27
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜prototypeパターン＞
# - あるインスタンスから同じクラスのインスタンスのクローンを作成する


# ＜仕組み＞
# - インターフェースで福世宇するオブジェクトの骨組みを作成する
# - 複製したいクラスはインターフェースを継承する
# - 複製したい状態でクラスを登録して必要に応じて複製を作成する


# ＜構成要素＞
# - Prototype         ： 複製するオブジェクトの構成要素を定義するインターフェース
# - ConcretePrototype ： Prototypeを具体化したクラス
# - Manager           ： ConcretePrototypeを登録して複製するクラス


# ＜目次＞
# 0 準備
# 1 Prototypeの定義
# 2 ConcretePrototypeの定義（その1）
# 3 ConcretePrototypeの定義（その2）
# 4 Managerの定義
# 5 動作確認


# 0 準備 ----------------------------------------------------

# ライブラリ
from abc import ABC, abstractmethod
from copy import deepcopy


# 1 Prototypeの定義 ------------------------------------------

# ＜ポイント＞
# - プロトタイプは抽象クラスとして定義して必要な実装を抽象メソッドとして定義しておく


class Prototype(ABC):

    @abstractmethod
    def use(self, msg):
        pass

    @abstractmethod
    def _clone(self):
        pass


# 2 ConcretePrototypeの定義（その1） ---------------------------

# ＜ポイント＞
# - プロトタイプの具体的な実装を行う


class MessageBox(Prototype):

    def __init__(self, decoration_char):
        self.__decoration_char = decoration_char
    
    def use(self, msg):
        str_msg = str(msg)
        print(self.__decoration_char * (len(str_msg) + 4))
        print(self.__decoration_char + ' ' + str_msg + ' ' + self.__decoration_char)
        print(self.__decoration_char * (len(str_msg) + 4))
    
    def _clone(self):
        print('MessageBoxのクローンを作成します')
        return deepcopy(self)
    
    @property
    def decoration_char(self):
        return self.__decoration_char
    
    @decoration_char.setter
    def decoration_char(self, decoration_char):
        self.__decoration_char = decoration_char


# 動作確認
m_box = MessageBox('*')
m_box.use('Hello')


# 3 ConcretePrototypeの定義（その2） ---------------------------

class UnderlinePen(Prototype):

    def __init__(self, undeline_char):
        self.__underline_char = undeline_char
    
    def use(self, msg):
        str_msg = str(msg)
        print(str_msg)
        print(self.__underline_char * len(str_msg))
    
    def _clone(self):
        print('UnderlinePenのコピーを作成します')
        return deepcopy(self)
    
    @property
    def underline_char(self):
        return self.__underline_char
    
    @underline_char.setter
    def underline_char(self, underline_char):
        self.__underline_char = underline_char


# 動作確認
u_pen = UnderlinePen('-')
u_pen.use('Hello')


# 4 Managerの定義 -------------------------------------------------

class Manager:

    def __init__(self):
        self.__products = {}
    
    def register(self, name, proto_type: Prototype):
        self.__products[name] = deepcopy(proto_type)

    def create_product(self, name):
        product = self.__products.get(name)
        return product._clone()


# 5 動作確認 ------------------------------------------------------

# インスタンス生成
manager = Manager()

# プロトタイプに登録
manager.register('message_box', m_box)
manager.register('underline_pen', u_pen)

#
new_m_box = manager.create_product('message_box')
new_m_box.use('New Box')
m_box.decoration_char = '-'
m_box.use('Hello')
# m_box_clone = m_box._clone()
m_box_clone = manager.create_product('message_box')
m_box_clone.use('Hello 2')

new_u_pen = manager.create_product('underline_pen')
new_u_pen.use('New Pen')
