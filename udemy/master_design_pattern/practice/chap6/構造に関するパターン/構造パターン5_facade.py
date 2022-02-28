# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 6 デザインパターン講座
# Theme       : 構造に関するパターン（Facade）
# Creat Date  : 2022/2/28
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜Facadeパターン＞
# - Facadeとは建物の正面のこと
# - 各クラスが関連しあって実行される複雑な処理を、Facadeが各クラスを利用して分かりやすく実行できるようにする


# ＜目的＞
# - 複雑なシステムを扱うためのシンプルなインタフェースを提供すること


# ＜仕組み＞
# - システムを構成するクラスを作成するシステムを構成するクラスを利用するための
# - Facadeを作成してユーザに対するインタフェースを提供する


# ＜構成要素＞
# Facade       : システムを構成する様々なクラスを利用するためのクラス
# その他のクラス : いろんな処理を記載されたFacadeに利用されるクラス


# ＜目次＞
# 1 パーツとなるのクラスの定義
# 2 Facadeの定義


# 1 パーツとなるのクラスの定義 ----------------------------------------------

class Knife:

    def __init__(self, name):
        self.__name = name
    
    def cut_vegetables(self):
        print(f'野菜を{self.__name}でカットします')


class Boiler:

    def __init__(self, name):
        self.__name = name
    
    def boil_vegetables(self):
        print(f'野菜を{self.__name}でボイルします')


class Frier:

    def __init__(self, name):
        self.__name = name
    
    def fry_vegetables(self):
        print(f'野菜を{self.__name}でフライします')


# 2 Facadeの定義 ---------------------------------------------------

class Cook:

    def __init__(self, knife: Knife, frier: Frier, boiler: Boiler):
        self.__knife = knife
        self.__frier = frier
        self.__boiler = boiler
    
    def cook_dish(self):
        self.__knife.cut_vegetables()
        self.__frier.fry_vegetables()
        self.__boiler.boil_vegetables()


# 3 動作確認 --------------------------------------------------------

# インスタンス生成
knife = Knife('My knife')
frier = Frier('My Frier')
boiler = Boiler('My Boiler')

# 個別にメソッドを実行
knife.cut_vegetables()
boiler.boil_vegetables()
frier.fry_vegetables()

# インターフェースを統一して実行
cook = Cook(knife, frier, boiler)
cook.cook_dish()
