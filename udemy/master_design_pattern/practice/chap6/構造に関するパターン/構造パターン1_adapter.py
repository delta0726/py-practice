# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 6 デザインパターン講座
# Theme       : 構造に関するパターン（Adapter）
# Creat Date  : 2022/2/28
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜Adapterパターン＞
# - コンセントのアダプターの意味（iphoneに接続する端子をandroidでも使えるように変換）
# - クラスとクラスをつないで様々なフォーマットに変換して対応できるようにする


# ＜目的＞
# - クラスとクラスの間をつないで型の違いを解消すること


# ＜仕組み＞
# - Adapterにつなぎたいクラスを作成する（Adaptee）
# - Adapterに処理を記述するためのインタフェースを作成する
# - Adapterを作成して Adapteeと接続できるようにする


# ＜構成要素＞
# - Adaptee         : Adapterに接続されるクラスを抽象化したインタフェース
# - ConcreteAdaptee : Adapteeの処理を具体的に記述したクラス
# - Adapter(Target) : Adapteeを利用する処理を記載したインタフェース
# - ConcreteAdapter : Adapterの処理を具体化したクラス


# ＜目次＞
# 0  準備
# 1 Adapteeの定義
# 2 ConcreteAdapteeの定義
# 3 Adapterの定義
# 4 ConcreteAdapterの定義
# 5 動作確認


# 0  準備 ------------------------------------------------------------

# ライブラリ
from abc import ABC, abstractmethod


# 1 Adapteeの定義 -----------------------------------------------------

class ModelAdaptee(ABC):

    @abstractmethod
    def load_headers(self):
        pass

    @abstractmethod
    def yield_row(self):
        pass


# 2 ConcreteAdapteeの定義 -------------------------------------------------

class UserModel(ModelAdaptee):

    def __init__(self):
        self.__users = []
        self.__headers = ['Name', 'Age']

    def load_headers(self):
        return self.__headers
    
    def yield_row(self):
        for user in self.users:
            yield user
    
    @property
    def users(self):
        return self.__users
    
    def add_user(self, user: list):
        self.users.append(user)


# 動作確認
users = UserModel()
users.add_user(['Taro', 19])

print(users.load_headers())
for user in users.yield_row():
    print(user)


# 3 Adapterの定義 ----------------------------------------------------

class ModelAdapter(ABC):

    @abstractmethod
    def write_to_csv(self):
        pass


# 4 ConcreteAdapterの定義 ---------------------------------------------

class UserModelAdapter(ModelAdapter):
    
    def __init__(self, user_model: UserModel):
        self.__user_model = user_model
    
    def write_to_csv(self, file_name):
        with open(file_name, mode='w', encoding='utf-8', newline='\n') as fh:
            csv_header = ','.join(self.__user_model.load_headers())
            fh.write(csv_header + '\n')
            for row in self.__user_model.yield_row():
                csv_row = ','.join([str(r) for r in row])
                fh.write(csv_row + '\n')


# 5 動作確認 -------------------------------------------------------------

# インスタンス生成
users = UserModel()

# ユーザー追加
users.add_user(['Taro', 19])
users.add_user(['Jiro', 19])
users.add_user(['Saburo', 19])

#
user_model_adapter = UserModelAdapter(users)
user_model_adapter.write_to_csv('practice/chap6/構造に関するパターン/output/tmp.csv')
