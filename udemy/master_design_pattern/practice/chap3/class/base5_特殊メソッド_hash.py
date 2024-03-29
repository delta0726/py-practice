# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 60 特殊メソッド2  __hash__
# Creat Date  : 2022/2/6
# Final Update: 2022/3/2
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜概要＞
# - 特殊メソッドはクラスに定型的な機能を持たせるために実装するメソッド
# - __hash__は文字列のハッシュ変換(数値変換)を行う


# ＜目次＞
# 1 ハッシュ変換とは
# 2 クラス定義
# 3 __hash__を実行する


# 1 ハッシュ変換とは ----------------------------------------------

# ＜ポイント＞
# - ハッシュ変換とは文字列を数値に変換する仕組み
#   --- 辞書型のキーやセット型のような重複を許さないオブジェクトの生成などに用いる


# ハッシュ関数
hash('Taro')
hash('Taro')
hash('Jiro')


# 2 クラス定義 ----------------------------------------------

# クラス定義
class Human:

    # コンストラクタ
    def __init__(self, name, age, phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number

    def __eq__(self, ohter):
        return (self.name == ohter.name) and \
               (self.phone_number == ohter.phone_number)

    # 文字列変換
    def __str__(self):
        return 'name = {}, age = {}, phone_number: {}'.format(self.name, self.age, self.phone_number)

    # ハッシュを返す
    def __hash__(self):
        print('hash関数が呼ばれました')
        return hash(self.name + self.phone_number)


# 3 __hash__を実行する ----------------------------------------------

# ＜ポイント＞
# - __hash__はsetなどオブジェクトに一意性が求められる際に適用される


# インスタンス生成
# --- man1とman2は__eq__で同一と判断される
man1 = Human(name='Taro', age=20, phone_number='08011111111')
man2 = Human(name='Taro', age=18, phone_number='08011111111')
man3 = Human(name='Jiro', age=18, phone_number='09011111111')

# 出力確認
print(man1)
print(man2)
print(man3)

# 一致確認
# --- nameとphone_numberで一致確認
print(man1 == man2)
print(man1 == man3)
print(man2 == man3)

# インスタンスをセットに格納
# --- 同じものは格納できないのでhash変換が行われる
set_men = {man1, man2, man3}
print(set_men)

# 確認
# --- 要素が2つしか格納されていない（man1とman2はイコールなため）
for x in set_men:
    print(x)
