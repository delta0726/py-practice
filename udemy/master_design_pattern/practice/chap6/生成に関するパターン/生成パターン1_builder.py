# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 6 デザインパターン講座
# Theme       : 生成に関するパターン（Builder）
# Creat Date  : 2022/2/26
# Final Update: 2022/3/6
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜Builderパターン＞
# - ｢作成されるオブジェクト｣と｢作成するオブジェクト｣を分けたい場合に使用する
#   --- 作成されるオブジェクト： インターフェースを継承したサブクラス
#   --- 作成するオブジェクト  ： インスタンス
# - Builder(インターフェース)を介して様々なパターンのオブジェクトが生成される


# ＜目的＞
# - 同じ作成過程で異なる表現形式の結果を得ること
# - サブクラスに応じて作成されるクラスのインスタンスの中身を変える
#   --- サブクラスの段階で様々な車のパターンを作る


# ＜構成要素＞
# Product         : 作成されるオブジェクト（サブクラス）
# Builder         : Productを生成する処理を記述（インタフェース： 抽象クラス）
# ConcreteBuilder : Builderの処理を具体化したクラス（複数作成してパターン化）
# Director        : Builderを利用するクラス（外部から呼び出すクラス）


# ＜目次＞
# 0 準備
# 1 Productの設定
# 2 Builderの設定 (インタフェースの設定)
# 3 ConcreteBuilderの設定
# 4 Directorの設定
# 5 動作確認


# 0 準備 --------------------------------------------------

# ライブラリ
from abc import ABC, abstractmethod


# 1 Productの設定 -----------------------------------------

class SetMeal:

    @property
    def main_dish(self):
        return self.__main_dish

    @main_dish.setter
    def main_dish(self, main_dish):
        self.__main_dish = main_dish

    @property
    def side_dish(self):
        return self.__side_dish

    @side_dish.setter
    def side_dish(self, side_dish):
        self.__side_dish = side_dish

    def __str__(self):
        return f'メインディッシュ: {self.main_dish}, ' \
               f'サイドディッシュ: {self.side_dish}'


# 2 Builderの設定 (インタフェースの設定) ----------------------

class SetMealBuilder(ABC):

    def __init__(self):
        self._set_meal = SetMeal()

    @abstractmethod
    def product(self):
        pass

    @abstractmethod
    def build_main_dish(self):
        pass

    @abstractmethod
    def build_side_dish(self):
        pass


# 3 ConcreteBuilderの設定 ------------------------------------------

# ＜ポイント＞
# - BuilderであるSetMealBuilderクラスを継承する
#   --- 抽象メソッドを実装する


class SanmaSetBuilder(SetMealBuilder):

    def __init__(self):
        super().__init__()

    @property
    def product(self):
        return self._set_meal

    def build_main_dish(self):
        self._set_meal.main_dish = 'さんま'
        return self

    def build_side_dish(self):
        self._set_meal.side_dish = 'お味噌汁'
        return self


class PastaSetBuilder(SetMealBuilder):

    def __init__(self):
        super().__init__()

    @property
    def product(self):
        return self._set_meal

    def build_main_dish(self):
        self._set_meal.main_dish = 'パスタ'
        return self

    def build_side_dish(self):
        self._set_meal.side_dish = 'スープ'
        return self


# 4 Directorの設定 -----------------------------------------

class Director:

    def __init__(self, set_meal_builder: SetMealBuilder):
        self.__builder = set_meal_builder

    @property
    def builder(self):
        return self.__builder

    @builder.setter
    def builder(self, builder: SetMealBuilder):
        self.__builder = builder

    def build(self):
        # self.builder.build_main_dish()
        # self.builder.build_side_dish()
        self.builder.build_main_dish().build_side_dish()
        return self.builder


# 5 動作確認 -----------------------------------------------------

# インスタンス生成
sanma_builder = SanmaSetBuilder()
pasta_builder = PastaSetBuilder()

#
director = Director(sanma_builder)
print(director.build().product)


director.builder = pasta_builder
print(director.build().product)
