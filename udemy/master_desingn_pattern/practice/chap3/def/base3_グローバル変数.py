# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 41 グローバル変数
# Creat Date  : 2022/2/4
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜目次＞
# 1 名前空間
# 2 グローバル変数


# 1 名前空間 -----------------------------------------------------

# ＜ポイント＞
# - 名前空間が異なれば、同じ変数も別のものとして管理される
#   --- 変数は名前空間ごとに管理される


# 関数定義
def printAnimal():
    animal = 'Cat'
    print('関数内animal = {}, id = {}'.format(animal, id(animal)))


# 関数外でanimalを指定
animal = 'Dog'

# 関数内のanimal
printAnimal()

# 関数外のanimal
print('関数外animal = {}, id = {}'.format(animal, id(animal)))


# 2 グローバル変数 -----------------------------------------------

# ＜ポイント＞
# - globalで引数を指定すると名前空間の外側の変数を変更することが可能になる
#   --- 同じアドレスのanimalを指定するようになる


# 関数定義
# --- グローバル変数を書換え
def printAnimal():
    global animal
    animal = 'Cat'
    print('関数内animal = {}, id = {}'.format(animal, id(animal)))

# 関数外でanimalを指定
animal = 'Dog'
print('関数外animal = {}, id = {}'.format(animal, id(animal)))

# 関数内のanimal
printAnimal()

# 関数外のanimal
print('関数外animal = {}, id = {}'.format(animal, id(animal)))
