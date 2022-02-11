# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 23 例外処理
# Creat Date  : 2022/2/11
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜概要＞
# - raiseを使うと関数の結果にエラーオブジェクトを返すことができる
# - 例外を自作することもできる


# ＜目次＞
# 1 関数の戻り値でエラーを返す
# 2 自作のエラー処理


# 1 関数の戻り値でエラーを返す --------------------------------------

# ＜ポイント＞
# - tyr文で関数を実行してエラーかどうかを判定する
#   --- 関数はエラーの場合にraise文でエラーコードを返す
#   --- exceptでエラーを受け取って処理を実行


# 関数定義
# --- エラーの場合にraiseで例外を戻り値として返す
def devide(a, b):
    if b == 0:
        raise ZeroDivisionError('0では割り切れません')
    else:
        return a / b


# エラー処理
# --- ゼロで割るのでエラー発生
try:
    c = devide(10, 0)
except ZeroDivisionError as e:
    print(e, type(e))


# 2 自作のエラー処理 -----------------------------------------------

# ＜ポイント＞
# - raise文で使用するエラーを独自クラスで定義することができる
#   --- 関数はエラーの場合にraise文でエラーコードを返す


# クラス定義
# --- 例外を自作
class MyException(Exception):
    pass


# 関数定義
# --- エラーの場合にraiseで例外を戻り値として返す
def devide(a, b):
    if b == 0:
        raise MyException('0では割り切れません')
    else:
        return a / b


# エラー処理
# --- ゼロで割るのでエラー発生
try:
    c = devide(10, 0)
except Exception as e:
    print(e, type(e))
