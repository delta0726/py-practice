# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 6 デザインパターン講座
# Theme       : 構造に関するパターン（）
# Creat Date  : 2022//
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜構成要素＞
# Flyweight        : 普通に用いるとメモリ使用量が大きいため、共有したほうがよいものを表す
# FlyweightFactory : Flyweightを作成する工場の役（FlyweightFactoryを利用してFlyweightを作成するとオブジェクトが共有される）


# ＜目次＞
# 1 Flyweightの定義
# 2 FlyWeightFactoryの定義
# 3 動作確認


# 1 Flyweightの定義 ----------------------------------------------------

class FlyweightMixin:

    _instances = {}
    
    @classmethod
    def get_instance(cls, *args, **kwargs):
        if (cls, *args) not in cls._instances:
            new_instance = cls(**kwargs)
            cls._instances[(cls, *args)] = new_instance
            return new_instance
        else:
            return cls._instances.get((cls, *args))


# 2 FlyWeightFactoryの定義 ----------------------------------------------

class User(FlyweightMixin):

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Car(FlyweightMixin):

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


# 3 動作確認 -------------------------------------------------------------

user = User.get_instance(1, name='Taro', age=21)
user2 = User.get_instance(1)
print(id(user), id(user2))
car = Car.get_instance(1, brand='Toyota', model='Prius')
print(car.brand)
