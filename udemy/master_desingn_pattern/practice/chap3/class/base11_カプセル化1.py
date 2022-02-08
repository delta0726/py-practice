# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 68 カプセル化1（setter / getter）
# Creat Date  : 2022/2/9
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜概要＞
# - プライベート変数は外部からアクセス/変更できないようにしたい
#   --- 変数名にアンダースコアを(__)つけるだけでは変更可能な状態
# - --- getterとsetterを定義して変数にアクセスできないようにする（カプセル化）


# ＜目次＞
# 1 クラス定義
# 2 クラス実行


# 1 クラス定義 ----------------------------------------------------------

# ＜ポイント＞
# - コンストラクタでインスタンス変数をプライベート変数として定義している（前提）
#   --- 通常だとプライベート変数は外から見えないようにする（変更不可）
# - プライベート変数の取得/変更をproperty()を介して行っている
#   --- "def get_変数名"で変数名を取得する
#   --- "def set_変数名"で変数名を設定する


class Human:

    # コンストラクタ
    # --- インスタンス変数をプライベート変数として定義する
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def get_name(self):
        print('getter name を呼び出しました')
        return self.__name
    
    def get_age(self):
        print('getter ageを呼び出しました')
        return self.__age
    
    def set_name(self, name):
        print('setter nameを呼び出しました')
        self.__name = name
    
    def set_age(self, age):
        print('setter ageを呼び出しました')
        self.__age = age

    # プロパティの設定
    # --- nameを指定するとget_name, set_nameが呼び出される, human.set_name()
    name = property(get_name, set_name)
    age = property(get_age, set_age)

    # 出力用のメソッド
    def print_msg(self):
        print(self.name, self.age)


# 2 クラス実行 -------------------------------------------------

# ＜ポイント＞
# - インスタンス変数を変更する際に内部的にはproperty()を介して行っている


# インスタンス生成
human = Human(name='Taro', age=15)

# インスタンス変数の変更
# --- "def set_*"を介して変更している（直接書き換えているわけでない）
human.name = 'Jiro'
human.age = 18

# 変数の確認
# --- "def get_*"を介して出力している
name = human.name
age = human.age
print(name, age)

# インスタンス変数の確認
human.print_msg()
