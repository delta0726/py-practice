# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 69 カプセル化2（setter / getter）
# Creat Date  : 2022/2/9
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜概要＞
# - プライベート変数は外部からアクセス/変更できないようにしたい
#   --- 変数名にアンダースコアを(__)つけるだけでは変更可能な状態
# - --- getterとsetterを定義して変数にアクセスできないようにする（カプセル化）


# ＜カプセル化の方法＞
# - ここではデコレータを用いてgetter/setterを作成する（一般的な方法）
#   --- @property   : getter
#   --- @var.setter : setter


# ＜目次＞
# 1 クラス定義
# 2 クラス実行


# 1 クラス定義 ----------------------------------------------------------

# ＜ポイント＞
# - デコレータだけでgetter/setterを設定することが可能
#   --- property関数は不要
#   --- デコレータを付けることでsetter/getterの両方でname()やage()の同名が使える


class Human:

    # コンストラクタ
    # --- インスタンス変数をプライベート変数として定義する
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # getter
    # --- 変数を取得
    @property
    def name(self):
        print('getter nameが呼ばれました')
        return self.__name

    # getter
    # --- 変数を取得
    @property
    def age(self):
        print('getter ageを呼ばれました')
        return self.__age

    # setter
    # --- プライベート変数を変更
    @name.setter
    def name(self, name):
        print('setter nameが呼ばれました')
        self.__name = name

    # setter
    # --- プライベート変数を変更
    # --- 条件文を介在させることも可能
    @age.setter
    def age(self, age):
        print('setter ageが呼ばれました')
        if age < 0:
            print('0以上の値を設定してください')
            return
        self.__age = age


# 2 クラス実行 -------------------------------------------------

# ＜ポイント＞
# - 操作面ではカプセル化1と同様
#   --- property()を用いないため動作が直感的（デバッガーを使って確認）、


# インスタンス生成
human = Human(name='Koichi', age=22)

# インスタンス変数の変更
human.name = 'Makoto'
print(human.name)

# インスタンス変数の変更
human.age = -1
print(human.age)
