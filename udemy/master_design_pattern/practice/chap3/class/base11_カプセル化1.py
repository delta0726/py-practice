# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 68 カプセル化1（setter / getter）
# Creat Date  : 2022/2/9
# Final Update: 2022/3/2
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜概要＞
# - プライベート変数は外部からアクセス/変更できないようにしたい
#   --- 変数名にアンダースコアを(__)つけるだけでは変更可能な状態
# - --- getterとsetterを定義して変数にアクセスできないようにする（カプセル化）


# ＜カプセル化の方法＞
# - ここではproperty()と各種メソッドを定義することでgetter/setterを作成する
#   --- def get_変数名()
#   --- def set_変数名()
#   --- 変数名 = property(get_変数名, set_変数名)


# ＜目次＞
# 1 クラスにおけるgetter/setterの設定
# 2 クラス実行


# 1 クラスにおけるgetter/setterの設定 ------------------------------------

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

    # getter
    # --- 変数を取得
    def get_name(self):
        print('getter name を呼び出しました')
        return self.__name

    # getter
    # --- 変数を取得
    def get_age(self):
        print('getter ageを呼び出しました')
        return self.__age

    # setter
    # --- プライベート変数を変更
    def set_name(self, name):
        print('setter nameを呼び出しました')
        self.__name = name

    # setter
    # --- プライベート変数を変更
    def set_age(self, age):
        print('setter ageを呼び出しました')
        self.__age = age

    # プロパティの設定
    # --- nameを指定するとget_name, set_nameが呼び出される
    name = property(get_name, set_name)
    age = property(get_age, set_age)

    # 出力用のメソッド
    def print_msg(self):
        print(self.name, self.age)


# 2 クラス実行 -------------------------------------------------

# ＜ポイント＞
# - プライベート変数を外部から変更する手段を提供している
#   --- property()を経由してset_*()を介して変更している
#   --- setter/getterの使用時にproperty()は経由しない（デバッガーで確認）


# インスタンス生成
human = Human(name='Taro', age=15)

# インスタンス変数の変更
# --- setterが動作する
# --- "def set_*"を介して変更している（直接書き換えているわけでない）
human.name = 'Jiro'
human.age = 18

# 変数の確認
# --- getterが動作する
# --- "def get_*"を介して出力している
name = human.name
age = human.age
print(name, age)

# インスタンス変数の確認
human.print_msg()
