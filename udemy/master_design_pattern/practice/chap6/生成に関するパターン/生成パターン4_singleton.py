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
# 2 Sigletonによるクラス定義（その1）
# 3 Sigletonによるクラス定義（その2）


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


# 2 Sigletonによるクラス定義（その1） -------------------------------------

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


# 2 Sigletonによるクラス定義（その2） -------------------------------------

# ＜ポイント＞
# - その1よりも簡単な実装方法（__new__ を使わない）
# - コンストラクタをプライベートにする
#   ---- Pythonではプライベート化できないので使えないようにする


class DataBase3:
    __instance = None

    def __init__(self):
        raise RuntimeError('このクラスのコンストラクタは呼び出せません')

    @classmethod
    def get_instance(cls, database_url=None):
        if cls.__instance is None:
            cls.__instance = cls.__new__(cls)
        if database_url:
            cls.__instance.__database_url = database_url
        return cls.__instance

    @property
    def database_url(self):
        return self.__database_url

    @database_url.setter
    def database_url(self, database_url):
        self.__database_url = database_url

    def connect(self):
        # Databaseに接続
        pass


# インスタンス生成
# --- コンストラクタを直接呼び出すとエラー
# a = DataBase3()

# インスタンス生成
# --- クラスメソッドであるget_instance()を使う
a = DataBase3.get_instance('128.1.1.1:1111')
b = DataBase3.get_instance()

# 確認
print(a == b)
print(id(a), id(b))
print(a.database_url, b.database_url)

# URLの指定
a.database_url = '128.1.1.1:5678'
print(a.database_url, b.database_url)
