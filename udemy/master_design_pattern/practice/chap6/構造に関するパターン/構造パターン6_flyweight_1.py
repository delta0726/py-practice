# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 6 デザインパターン講座
# Theme       : 構造に関するパターン（Flyweight-1）
# Creat Date  : 2022/2/28
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜Flyweightパターン＞
# - ボクシングのフライ級のこと
# - オブジェクトを共有することでメモリの使用料を少なくするために用いる


# ＜目的＞
# - オブジェクトを共有してメモリの使用量を下げること


# ＜仕組み＞
# - Flyweightを作成する
# - Flyweightをインスタンスとして所有する FlyweightFactory を作成する


# ＜構成要素＞
# Flyweight        : 普通に用いるとメモリ使用量が大きいため、共有したほうがよいものを表す
# FlyweightFactory : Flyweightを作成する工場の役（FlyweightFactoryを利用してFlyweightを作成するとオブジェクトが共有される）


# ＜目次＞
# 1 Flyweightの定義
# 2 FlyWeightFactoryの定義
# 3 動作確認


# 1 Flyweightの定義 --------------------------------------------------

class User:

    def __init__(self, name='', age=''):
        self.__name = name
        self.__age = age
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        self.__age = age
    
    def __str__(self):
        return f'name: {self.name}, age: {self.age}'


# 2 FlyWeightFactoryの定義 ---------------------------------------

class UserFactory:

    __instances = {}

    @classmethod
    def get_instance(cls, id):
        if id not in cls.__instances:
            user = User()
            cls.__instances[id] = user
            return user
        return cls.__instances.get(id)


# 3 動作確認 -----------------------------------------------------------

user1 = UserFactory.get_instance(1)
user1.name = 'Taro'
user1.age = 20

user2 = UserFactory.get_instance(2)

user3 = UserFactory.get_instance(1)

print(id(user1))
print(id(user2))
print(id(user3))
print(user3)
user3.name = 'Hanako'
print(user1)
