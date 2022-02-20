# ******************************************************************************
# Course      : 0から始めるPytest超基礎講座
# Chapter     : 3 前処理＆後処理
# Theme       : 関数に対する前処理＆後処理の実行
# Creat Date  : 2022/2/20
# Final Update:
# URL         : https://www.udemy.com/course/python_pytest/
# ******************************************************************************


# ＜ポイント＞
# - 前処理/後処理の関数のテストに対する前処理と後処理を行う関数を定義する
#   --- 前処理のメソッド名：setup_function
#   --- 後処理のメソッド名：teardown_function


# ＜実行コマンド＞
# - ターミナルより実行（実行確認のため出力表示）
# pytest I:/Project/Python/py_practice/udemy/pytest_seminar/practice/sec3/test_sec3_1.py -s


# ＜出力結果＞
# - 実行関数の処理が前処理/後処理の関数でラップされている
# setup_function
# hello world!
# teardown_function
# setup_function
# pytest
# teardown_function


# メイン処理 --------------------------------------------------------------

# 前処理＆後処理の関数の作成
# 前処理
def setup_function(function):
    print("setup_function")

# 後処理
def teardown_function(function):
    print("teardown_function")

# 実行関数1
def test_hello_world():
    print("hello world!")

# 実行関数2
def test_pytest():
    print("pytest")
