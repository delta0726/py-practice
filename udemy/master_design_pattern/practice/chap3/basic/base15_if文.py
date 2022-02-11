# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 15 if文
# Creat Date  : 2022/2/11
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜概要＞
# - if文はあらゆる言語で用いられるが、ここではPythonにおけるif文の原理を確認する
# - 評価式で真偽を評価する
#   --- "None", "False", "0", "空のオブジェクト"が偽として扱われる
#   --- 真偽の評価は__bool__が行っている


# ＜目次＞
# 1 if文の動作確認
# 2 クラスにおけるboolを用いた判定


# 1 if文の動作確認 ----------------------------------------

# 変数定義
# --- True / False / None / 0 / 空のオブジェクト などで実験
var_bool = None

# 確認
print('boolの計算結果: {}'.format(bool(var_bool)))

# 条件文
if var_bool:
    print('if文の中の処理')
else:
    print('Falseの処理')


# 2 クラスにおけるboolを用いた判定 ------------------------------------

# ＜ポイント＞
# - クラスのメソッドに__bool__を実装することでインスタンスにbool()が使えるようになる
#   --- 特殊メソッドは別途解説


# クラス定義
# --- クラスに判定機能(__bool__)を実装する
class ClassA:

    def __init__(self, a):
        self.a = a

    def __bool__(self):
        if self.a == 'a':
            return True
        return False


# インスタンス生成
# --- 引数が"b"なのでFalse
var = ClassA('b')
print('boolの計算結果: {}'.format(bool(var)))

# インスタンス定義
# --- 引数が"a"なのでTrue
var = ClassA('a')
print('boolの計算結果: {}'.format(bool(var)))
