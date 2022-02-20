# ******************************************************************************
# Course      : 0から始めるPytest超基礎講座
# Chapter     : 5 テストのスキップ
# Theme       : グループ化によるテストのスキップ
# Creat Date  : 2022/2/20
# Final Update:
# URL         : https://www.udemy.com/course/python_pytest/
# ******************************************************************************


# ＜ポイント＞
# - スキップしたい関数にデコレータでグループを指定してスキップする
#   --- iniファイルでグループ指定を行う
#   --- 指定したグループ名を用いてスキップしたい関数にデコレータを付ける


# ＜iniファイル＞
# [pytest]
# markers =
#     morning
#     afternoon


# ＜実行コマンド＞
# - ターミナルより実行
# pytest I:/Project/Python/py_practice/udemy/pytest_seminar/practice/sec5/test_sec5_2.py -v -m "morning" -s
# pytest I:/Project/Python/py_practice/udemy/pytest_seminar/practice/sec5/test_sec5_2.py -v -m "not morning" -s


# ＜出力結果＞
# practice\sec5\test_sec5_2.py::test_goodmorning PASSED
# =========== 1 passed, 2 deselected in 0.03s ===============

# practice\sec5\test_sec5_2.py::test_hello hello PASSED
# practice\sec5\test_sec5_2.py::test_goodafternoon good afternoon PASSED
# =========== 2 passed, 1 deselected in 0.01s ====================


# メイン処理 --------------------------------------------------------------

# テストのスキップ
import pytest

def test_hello():
    print("hello")

@pytest.mark.morning
def test_goodmorning():
    print("good morning")

@pytest.mark.afternoon
def test_goodafternoon():
    print("good afternoon")
