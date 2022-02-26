# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 6 デザインパターン講座
# Theme       : 生成に関するパターン（singleton）
# Creat Date  : 2022/2/27
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜Singletonパターン＞
# - インスタンス生成時に同じオブジェクトが指定され、インスタンスが1つしかないことを保証する
#   --- インスタンス生成におけるメモリ削減が期待できる


# ＜仕組み＞
# - 複数のインスタンスを生成しても1つのクラス(Singleton)を参照するように定義


# ＜用途＞
# - 主に1つしかインスタンスを作成する必要のない場合に用いられる
#   --- DBにアクセスする際に用いられるインスタンス
#   --- Factoryクラス


# ＜目次＞
# 1 通常のクラス定義
# 2 Sigletonによるクラス定義


# 1 通常のクラス定義 ---------------------------------------------

# ＜ポイント＞
# - インスタンスは同じクラスから生成しても別オブジェクトとして定義される
#   --- IDがインスタンスごとに異なる


# クラス定義
class DataBase1:
    pass


# インスタンス生成
a = DataBase1()
b = DataBase1()

# 確認
print(a == b)
print(id(a), id(b))


# 2 Sigletonによるクラス定義 -------------------------------------

# ＜ポイント＞
# - 複数のインスタンスを生成うぃても同じオブジェクトとして扱う


class DataBase2:
    _instance = None

    def __init__(self):
        self.__database_url = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @property
    def database_url(self):
        return self.__database_url

    @database_url.setter
    def database_url(self, database_url):
        self.__database_url = database_url

    def connect(self):
        # Databaseに接続する
        pass


# インスタンス生成
a = DataBase2()
b = DataBase2()

# 確認
print(a == b)
print(id(a), id(b))

# URLの指定
a.database_url = '128.1.1.1:5678'
print(a.database_url)
print(b.database_url)
