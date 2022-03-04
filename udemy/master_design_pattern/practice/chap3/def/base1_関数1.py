# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 39 関数1
# Creat Date  : 2022/2/4
# Final Update: 2022/3/2
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜概要＞
# - 関数とは一連の処理をまとめたもの


# ＜目次＞
# 1 関数定義と関数実行
# 2 関数の引数


# 1 関数定義と関数実行 -----------------------------------------------

# 関数定義
def print_hello():
    print('Hello World')


# 関数実行
print_hello()


# 2 関数の引数 --------------------------------------------------------

# ＜ポイント＞
# - 引数にはデータ型を指定することができる
#   --- 型ヒントが表示されるだけで、入力を制限しているわけではない


# 関数定義
# --- 大きいほうの値を表示
def num_max(a: int, b: int):
    print('a = {}, b = {}'.format(a, b))
    if a > b:
        return a
    else:
        return b


# 関数実行
# --- 引数名を指定して順序を入れ替えて実行
# --- 引数のデータ型を指定しても実行可能（ただし、期待した出力が得られない）
# --- 引数がないとエラー
print(num_max(b=100, a=20))
print(num_max(a='20', b='100'))
print(num_max())
