# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 5 SOLIDの原則
# Theme       : 3 リスコフの置換原則
# Creat Date  : 2022/2/25
# Final Update: 2022/3/4
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜リスコフの置換原則＞
# - サブクラスは、そのスーパークラスの代用ができなければならない
#   --- 関数XをクラスTのインスタンスが実行出来たら、サブクラスSのインスタンスも実行出来なければならない


# ＜メリット＞
# - スーパークラスの仕様を理解すれば、サブクラスの中身を全て確認せずに利用することができる
#   --- 拡張性と保守性の向上


# ＜目次＞
# 1 基本となるクラスの定義
# 2 クラスに適用する関数
# 3 動作確認


# 1 基本となるクラスの定義 ------------------------------------------

# クラス定義
# --- 長方形（スーパークラス）
class Rectangle:

    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width):
        self._width = width
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, height):
        self._height = height
    
    def calcurate_area(self):
        return self._width * self._height


# クラス定義
# --- 正方形（サブクラス）
class Square(Rectangle):

    def __init__(self, size):
        self._width = size
        self._height = size

    @Rectangle.width.setter
    def width(self, size):
        self._width = size
        self._height = size
    
    @Rectangle.height.setter
    def height(self, size):
        self._width = size
        self._height = size


# 2 クラスに適用する関数 --------------------------------------------

# ＜ポイント＞
# - リスコフの置換原則ではスーパークラスとサブクラスに同じ関数が適用できる必要がある
#   --- 当然結果も一致している必要がある
#   --- 関数定義1は結果が一致しない（関数定義2で解消）


# 関数定義1
# --- 問題あり
def print_area(obj):
    change_to_width = 10
    change_to_height = 20
    obj.width = change_to_width
    obj.height = change_to_height
    # if isinstance(obj, Square):
    #     change_to_width = change_to_height

    print('予想面積 = {}, 実際面積 = {}'.format(
        change_to_height * change_to_width,
        obj.calcurate_area()
    ))


# 関数定義2
# --- 問題解消
def print_area_2(obj):
    change_to_width = 10
    change_to_height = 20
    obj.width = change_to_width
    obj.height = change_to_height
    if isinstance(obj, Square):
        change_to_width = change_to_height

    print('予想面積 = {}, 実際面積 = {}'.format(
        change_to_height * change_to_width,
        obj.calcurate_area()
    ))


# 3 動作確認 -------------------------------------------------------

# ＜ポイント＞
# - print_area()ではスーパークラスとサブクラスで振舞いが異なる
#   --- 関数内でchange_to_*の入力が長方形を想定したものになっている


# ＜ソリューション＞
# - 今回はprint_area()で正方形の場合の条件文を追加することで解消
#   --- 関数内にサブクラスのための条件分岐を持ってくるのは本来は不適切
#   --- SquareはRectangleをスーパークラスにすべきではなかった


# 長方形（スーパークラス）
# --- インスタンス生成
# --- 関数実行
rc = Rectangle(2, 3)
print_area(rc)
print_area_2(rc)


# 正方形（サブクラス）
# --- インスタンス生成
# --- 関数実行
sq = Square(5)
print_area(sq)
print_area_2(sq)
