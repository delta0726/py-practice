# ******************************************************************************
# Course      : 0から始めるPytest超基礎講座
# Chapter     : 3 前処理＆後処理
# Theme       : モジュールに対する前処理/後処理の実行
# Creat Date  : 2022/2/20
# Final Update:
# URL         : https://www.udemy.com/course/python_pytest/
# ******************************************************************************


# ＜ポイント＞
# - 前回(sec3-3)のクラスの単一の名前空間で前処理/後処理を行っていた
#   --- 今回は複数の関数やクラスをもつモジュール(今回はグローバル空間)に対してテストを行う


# ＜実行コマンド＞
# - ターミナルより実行（実行確認のため出力表示）
# pytest I:/Project/Python/py_practice/udemy/pytest_seminar/practice/sec3/test_sec3_4.py -s


# ＜出力結果＞
# - 一連のモジュール(関数やクラスの実行)の前後で前処理/後処理が実行されている
# setup_module
# hello world! function
# pytest function
# hello world! method
# pytest method
# teardown_module


# メイン処理 --------------------------------------------------------------

# 前処理
def setup_module(module):
    print("setup_module")

# 後処理
def teardown_module(module):
    print("teardown_module")

def test_hello_world():
    print("hello world! function")

def test_pytest():
    print("pytest function")

class TestExample():
    def test_hello_world(self):
        print("hello world! method")

    def test_pytest(self):
        print("pytest method")
