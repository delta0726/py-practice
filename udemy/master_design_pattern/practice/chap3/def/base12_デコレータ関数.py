# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 53 デコレータ関数
# Creat Date  : 2022/2/5
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜デコレータとは＞
# - 関数の前に"@関数名"を付けることでメインの関数をラップする処理を行う
# - デコレータを自作すること自体は多くないが、デコレータを呼び出す機会は多い
#   --- セッター / メタクラスなど


# ＜目次＞
# 1 基本的なデコレータ処理
# 2 デコレータ処理の工夫


# 1 基本的なデコレータ処理 ---------------------------------------------

# 関数定義
# --- デコレータ関数（関数の前後に処理を行う）
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('*' * 20)
        func(*args, **kwargs)
        print('*' * 20)
    return wrapper

# 関数定義1
# --- メイン処理
@my_decorator
def func_a(*args, **kwargs):
    print('func_aを実行')
    print(args)

# 関数定義2
# --- メイン処理
@my_decorator
def func_b(*args, **kwargs):
    print('func_bを実行')
    print(args)


# 関数実行
# --- 関数定義1/2の両方にデコレータ処理を適用（記述の簡素化）
func_a(1, 2, 3)
func_b(2, 2, 3)


# 2 デコレータ処理の工夫 ---------------------------------------------

# ＜ポイント＞
# - デコレータ処理を工夫することでコード全体を簡素化することが可能
#   --- 今回はメイン処理を2回行う


# 関数定義
# --- メイン処理を2回行う
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('*' * 20)
        func(*args, **kwargs)
        func(*args, **kwargs)
        print('*' * 20)
    return wrapper

# 関数定義
# --- メイン処理
@my_decorator
def func_a(*args, **kwargs):
    print('func_aを実行')
    print(args)


# 関数実行
func_a(1, 2, 3)
