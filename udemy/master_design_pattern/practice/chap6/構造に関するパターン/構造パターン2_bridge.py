# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 6 デザインパターン講座
# Theme       : 構造に関するパターン（Bridge）
# Creat Date  : 2022/2/28
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜Bridgeパターン＞
# - 各機能を構成している要素を抽象クラスでつないで柔軟に機能追加を行う
#   --- クラス継承を階層が多くならないように実装する工夫


# ＜目的＞
# - 機能拡張が容易にできるようにして、拡張時に他のクラスに影響がないようにする


# ＜仕組み＞
# - ある機能を持ったImplementerとConcreteImplementerを作成する
# - Bridgeを用いて別のクラスとつなぎ新規の機能を追加する


# ＜構成要素＞
# Implementer         : 基本的な機能を記述したインタフェース
# ConcreteImplementer : Implementer を 継承して処理 を具体的に記述するクラス
# Abstraction         : 追加として実装される機能をImplementerと切り離して作成する処理を記述した抽象クラス
# RefinedAbstraction  : Abstractionの処理を具体的に記述したクラス


# ＜目次＞
# 0 準備
# 1 Implementerの定義
# 2 ConcreteImplementerの定義（その1）
# 3 ConcreteImplementerの定義（その2）
# 4 Abstractionの定義
# 5 RefinedAbstractionの定義


# 0 準備 ---------------------------------------------------------------

# ライブラリ
from abc import ABC, abstractmethod


# 1 Implementerの定義 ---------------------------------------------------

class Shape(ABC):

    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @abstractmethod
    def create_shape_str(self):
        pass


# 2 ConcreteImplementerの定義（その1） -------------------------------------------

class RectangleShape(Shape):

    def __init__(self, width, height):
        super().__init__(width, height)
    
    def create_shape_str(self):
        rectangle = '*' * self._width + '\n'
        for _ in range(self._height - 2):
            rectangle += '*' + ' ' * (self._width - 2) + '*' + '\n'
        rectangle += '*' * self._width + '\n'
        return rectangle


# 動作確認
rectangle = RectangleShape(10, 5)
print(rectangle.create_shape_str())


# 3 ConcreteImplementerの定義（その2） --------------------------------------------

class SquareShape(Shape):

    def __init__(self, width):
        super().__init__(width, width)
    
    def create_shape_str(self):
        square = '*' * self._width + '\n'
        for _ in range(self._width - 2):
            square += '*' + ' ' * (self._width - 2) + '*' + '\n'
        square += '*' * self._width + '\n'
        return square


# 動作確認
square = SquareShape(10)
print(square.create_shape_str())


# 4 Abstractionの定義 -----------------------------------------------------

class WriteAbstraction(ABC):

    def __init__(self, shape: Shape):
        self._shape = shape
    
    def read_shape(self):
        return self._shape.create_shape_str()
    
    @abstractmethod
    def write_to_text(self, file_name):
        pass


# 5 RefinedAbstractionの定義 -----------------------------------------------

class WriteShape(WriteAbstraction):

    def write_to_text(self, file_name):
        with open(file_name, mode='w', encoding='utf-8') as fh:
            fh.write(self.read_shape())


# 6 動作確認 ---------------------------------------------------------------

# インスタンス生成
write_shape = WriteShape(square)
write_shape.write_to_text('practice/chap6/構造に関するパターン/output/tmp.txt')
