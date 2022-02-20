# ******************************************************************************
# Course      : 0から始めるPytest超基礎講座
# Chapter     : 5 テストのスキップ
# Theme       : 関数名/メソッド名によるテストのスキップ
# Creat Date  : 2022/2/20
# Final Update:
# URL         : https://www.udemy.com/course/python_pytest/
# ******************************************************************************


# ＜ポイント＞
# - ターミナルでの実行時に共通する関数名を指定することで、それ以外の関数をスキップすることができる


# ＜実行コマンド＞
# - ターミナルより実行（対象関数の一部を文字列で指定）
# pytest I:/Project/Python/py_practice/udemy/pytest_seminar/practice/sec5/test_sec5_3.py -v -k "hello" -s
# pytest I:/Project/Python/py_practice/udemy/pytest_seminar/practice/sec5/test_sec5_3.py -v -k "not hello" -s


# ＜出力結果＞
# practice\sec5\test_sec5_3.py::test_hello1 PASSED
# practice\sec5\test_sec5_3.py::test_hello2 PASSED
# =========== 2 passed, 1 deselected in 0.07s ==============


# practice\sec5\test_sec5_3.py::test_afternoon1 afternoon1 PASSED
# =========== 1 passed, 2 deselected in 0.06s ==============


# メイン処理 --------------------------------------------------------------

# ライブラリ
import pytest

def test_hello1():
    print("hello1")

def test_hello2():
    print("hello2")

def test_afternoon1():
    print("afternoon1")
