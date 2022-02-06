# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 64 クラスの多重継承
# Creat Date  : 2022/2/7
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜概要＞
# - 複数のスーパークラスから継承することを多重継承という
#   --- ClassA.__init__(self)で親クラスを呼び出す


# ＜目次＞
# 1 スーパークラス1の定義
# 2 スーパークラス2の定義
# 3 サブクラスの定義
# 4 クラスの実行


# 1 スーパークラス1の定義 ---------------------------------------------------

class ClassA:

    def __init__(self, name):
        self.a_name = name
    
    def print_a(self):
        print('ClassAのメソッド実行')
        print('a = {}'.format(self.a_name))
    
    def print_hi(self):
        print('A hi')


# 2 スーパークラス2の定義 ---------------------------------------------------

class ClassB:

    def __init__(self, name):
        self.b_name = name
    
    def print_b(self):
        print('ClassBのメソッド実行')
        print('b = {}'.format(self.b_name))
    
    def print_hi(self):
        print('B hi')


# 3 サブクラスの定義 --------------------------------------------------------

# ＜ポイント＞
# - 複数のスーパークラスを多重継承している
#   --- ClassA.__init__(self)で親クラスを呼び出す


class NewClass(ClassA, ClassB):

    # コンストラクタ
    # --- それぞれのスーパークラスのコンストラクタを実行
    def __init__(self, a_name, b_name, name):
        ClassA.__init__(self, a_name)
        ClassB.__init__(self, b_name)
        self.name = name

    # サブクラス独自の実装
    def print_new_name(self):
        print('name = {}'.format(self.name))

    # オーバーライド
    def print_hi(self):
        ClassA.print_hi(self)
        ClassB.print_hi(self)
        print('NewClass hi')


# 4 クラスの実行 ------------------------------------------------------------

# インスタンス生成（サブクラス）
sample = NewClass(a_name='AName', b_name='BName', name='New Class Name')

# メソッドの実行
# --- 親クラス1： ClassA
sample.print_a()

# メソッドの実行
# --- 親クラス2： ClassB
sample.print_b()

# メソッドの実行
# --- サブクラス
sample.print_new_name()

# メソッドの実行
# --- サブクラス（親クラスのメソッドを継承）
sample.print_hi()
