# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 42 関数内関数
# Creat Date  : 2022/2/5
# Final Update: 2022/3/4
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜概要＞
# - 関数の中に定義する関数を関数内関数という


# ＜関数内関数の使いどころ＞
# 1 外からアクセスされない関数を定義したい場合
# 2 関数内で処理が重複する場合
# 3 デコレータ関数を作成する場合


# ＜目次＞
# 1 関数内関数(Inner関数)
# 2 nonlocal文による変数の上書き（導入）


# 1 関数内関数(Inner関数) ---------------------------------------------

# ＜ポイント＞
# - 関数内関数は外からアクセスされたくない関数として利用することができる
#   --- 外側の関数のローカルスコープのみで適用可能


# 関数定義
# --- 関数内関数はローカルスコープに定義される
def outer():
    def inner():
        print('A')

    # 関数内関数の実行
    inner()


# 関数実行
outer()


# 関数実行
# --- inner関数はouter関数の外から実行することができない
# --- outer関数の名前空間で定義されているため
# inner()


# 2 nonlocal文による変数の上書き（導入）--------------------------------------

# ＜ポイント＞
# - 関数は関数外の変数(上位スコープの変数)を参照することができる
#   --- 関数内関数も同様に、上の階層の変数を参照することができる
#   --- 上書きすることはできない（関数内関数のローカル変数として管理される）


# 関数定義
def outer():
    outer_value = '外側の変数'
    print('outer: outer_value = {}, id = {}'.format(outer_value, id(outer_value)))

    def inner():
        outer_value = '内側の変数'
        print('inner: outer_value = {}, id = {}'.format(outer_value, id(outer_value)))

    inner()
    print('outer: outer_value = {}, id = {}'.format(outer_value, id(outer_value)))


# 関数実行
# --- 1番目と3番目は同じスコープの変数なので同一（自明）
# --- 2番目は同じ変数名でも関数内関数のローカルスコープに定義された別の変数なのでIDは異なる
outer()


# 3 nonlocal文による変数の上書き --------------------------------------------

# ＜ポイント＞
# - nonlocalで変数を宣言後に変数を再定義すると外側の変数を再定義できるよういなる


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
# --- 1番目はouter()のローカルスコープではじめに定義した変数
# --- 2番目はinnter()からouter()のスコープに定義された変数を上書き（nonlocal文）
# --- 3番目は2番目で書き換えられた値を参照
outer()
