# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 6 デザインパターン講座
# Theme       : 生成に関するパターン（factory_method）
# Creat Date  : 2022/2/27
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜Factory_methodパターン＞
# - メイン工場側でテンプレートを作成する
# - テンプレートに応じた工場を作成して、各工場で製品を作成する


# ＜仕組み＞
# - ｢生成(Creator)｣と｢具体的な処理(Product)｣を分離することで柔軟性と再利用性を高める
# - インターフェースで処理の枠組みを作り、サブクラスを用いてオブジェクトを作成する
# - サブクラスに応じて作成されるオブジェクトのタイプを変える


# ＜構成要素＞
# Creator         : Productを生成する処理を定義したインタフェース
# ConcreteCreator : Creatorを具体化したConcreteProductを作成するクラス
# Product         : 作成するオブジェクトの構成要素を定義するインタフェース
# ConcreteProduct : Productを具体化したクラス（複数作成する）


# ＜目次＞
# 0 準備
# 1 Creatorの定義
# 2 ConcreteProductの定義
# 3 Productの定義
# 4 ConcreteProductの定義
# 5 動作確認


# 0 準備 --------------------------------------------------

# ライブラリ
from abc import ABC, abstractmethod


# 1 Creatorの定義 ------------------------------------------

# ＜ポイント＞
# - CreatorはProductを生成する共通処理を定義したインターフェース
#   --- 全クラスで共通の処理


class IFactory(ABC):

    def __init__(self):
        self._owner = None
        self.registered_owners = []

    def create(self, owner):
        self._owner = owner
        product = self._create_product()
        self._register_product(product)
        return product

    @abstractmethod
    def _create_product(self):
        pass

    @abstractmethod
    def _register_product(self, product):
        pass


# 2 ConcreteCreatorの定義 --------------------------------

# ＜ポイント＞
# - Creatorを具体化したConcreteProductを作成するクラス
#   --- インターフェースであるIFactoryの抽象メソッドを定義

class CarFactory(IFactory):

    def _create_product(self):
        return Car(self._owner)

    def _register_product(self, product):
        self.registered_owners.append(product.owner)


class ShipFactory(IFactory):

    def _create_product(self):
        return Ship(self._owner)

    def _register_product(self, product):
        self.registered_owners.append(product.owner)


# 3 Productの定義 ------------------------------------------

# ＜ポイント＞
# - Productは作成するオブジェクトの構成要素を定義するインターフェース


class IProduct(ABC):

    def __init__(self, owner):
        self._owner = owner

    @abstractmethod
    def use(self):
        pass

    @abstractmethod
    def owner(self):
        pass


# 4 ConcreteProductの定義 -----------------------------------

# ＜ポイント＞
# - Productは作成するオブジェクトの構成要素を定義するインターフェース


class Car(IProduct):

    def use(self):
        print(f'{self.owner}: 車を運転します')

    @property
    def owner(self):
        return self._owner


class Ship(IProduct):

    def use(self):
        print(f'{self.owner}: 船を運転します')

    @property
    def owner(self):
        return self._owner


# 5 動作確認 -------------------------------------------------

# 車を作る
car_factory = CarFactory()
yamada_car = car_factory.create('山田')
sato_car = car_factory.create('佐藤')
yamada_car.use()
sato_car.use()
print(car_factory.registered_owners)

# 船を作る
ship_factory = ShipFactory()
john_ship = ship_factory.create('John')
mike_ship = ship_factory.create('Mike')
john_ship.use()
mike_ship.use()
print(ship_factory.registered_owners)
