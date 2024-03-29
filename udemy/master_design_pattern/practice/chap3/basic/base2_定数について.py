# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 9 定数について
# Creat Date  : 2022/8/19
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜目次＞
# - 1 変数定義の決まり事
# - 2 定数の定義
# - 3 print関数のformat文


# - 1 変数定義の決まり事 -------------------------------------------

# ＜ポイント＞
# - 予約語(33個ある)を変数に用いない
# - 変数は英語で定義する


# 変数の応用
# --- 基本的に英語に格納
# --- 一応、日本語文字にも格納することができる
animal = 'dog'
動物 = 'cat'
print(animal)
print(動物)


# - 2 定数の定義 ------------------------------------------------

# ＜ポイント＞
# - Pythonには定数は存在しない
#   --- すべて大文字の変数を定数として扱う（暗黙のルール）


# 定数の定義
# --- 定数は大文字で宣言する
# --- 大文字を定数とみなすという暗黙のルールに基づく
LEGAL_AGE = 20
age = 18

# ageが20より小さいときに処理を実行
# --- 条件式の大文字だと定数とすぐに判別できる
if age < LEGAL_AGE:
    print('未成年')
else:
    print('成人')


# 3 print関数のformat文 -------------------------------------------

# ＜ポイント＞
# - print文に変数を出力する場合はf記法が使える
#   --- f'{変数}'
#   --- print文の書き方がスッキリする


# 変数定義
age = 18

# format文
# --- ブレースで囲った部分に変更を用いることができる
# --- 上はPython3.6以降の記法、下はPython3.8以降の記法
print(f'age = {age}')
print(f'{age=}')
