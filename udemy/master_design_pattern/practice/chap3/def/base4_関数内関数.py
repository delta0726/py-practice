# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 42 関数内関数
# Creat Date  : 2022/2/5
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜関数内関数の使いどころ＞
# 1 外からアクセスされない関数を定義したい場合
# 2 関数内で処理が重複する場合
# 3 デコレータ関数を作成する場合


# ＜目次＞
# 1 関数内関数(Inner関数)
# 2 nonlocal変数の宣言
# 3 nonlocal変数宣言後の再定義


# 1 関数内関数(Inner関数) ---------------------------------------------

# ＜ポイント＞
# - 関数内関数とは特定の関数内で定義された関数というだけ
#   --- 外側の関数の名前空間に定義されている点に注意


# 関数定義
def outer():
    def inner():
        print('A')
    inner()

# 関数実行
outer()

# 関数実行
# --- inner関数はouter関数の外から実行することができない
# --- outer関数の名前空間で定義されているため
# inner()


# 2 nonlocal変数の宣言 -------------------------------------------------

# ＜ポイント＞
# - nonlocalで変数を宣言すると、｢内側の変数｣は｢外側の変数｣を参照するようになる
#   --- 関数内で変数を定義しなくても使えるようになる


# 関数定義
def outer():
    outer_value = '外側の変数'
    print('outer: outer_value = {}, id = {}'.format(outer_value, id(outer_value)))
    def inner():
        nonlocal outer_value
        print('inner: outer_value = {}, id = {}'.format(outer_value, id(outer_value)))
    inner()
    print('outer: outer_value = {}, id = {}'.format(outer_value, id(outer_value)))

# 関数実行
outer()


# 3 nonlocal変数宣言後の再定義 --------------------------------------------

# ＜ポイント＞
# - nonlocalで変数を宣言後に変数を再定義すると、外側の変数も再定義されたものを参照する


# 関数定義
def outer():
    outer_value = '外側の変数'
    print('outer: outer_value = {}, id = {}'.format(outer_value, id(outer_value)))
    def inner():
        nonlocal outer_value
        outer_value = '内側の変数'
        print('inner: outer_value = {}, id = {}'.format(outer_value, id(outer_value)))
    inner()
    print('outer: outer_value = {}, id = {}'.format(outer_value, id(outer_value)))

# 関数実行
outer()
