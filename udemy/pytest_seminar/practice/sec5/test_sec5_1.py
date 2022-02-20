# ******************************************************************************
# Course      : 0から始めるPytest超基礎講座
# Chapter     : 5 テストのスキップ
# Theme       : pytest.mark.skipによるテストのスキップ
# Creat Date  : 2022/2/21
# Final Update:
# URL         : https://www.udemy.com/course/python_pytest/
# ******************************************************************************


# ＜ポイント＞
# - 特定の関数(未実装など)をスキップしてテストを行う
#   --- 対象の関数にデコレータ(@pytest.mark.skip)をつける


# ＜実行コマンド＞
# - ターミナルより実行（"-v"で実行時に理由を表示）
# pytest I:/Project/Python/py_practice/udemy/pytest_seminar/practice/sec5/test_sec5_1.py -v


# ＜出力結果＞
# - 指定した関数のテストがスキップされている
# practice\sec5\test_sec5_1.py::test_hello PASSED                                                                                                                                                                                                                    [ 33%]
# practice\sec5\test_sec5_1.py::test_goodmorning SKIPPED                                                                                                                                                                                                             [ 66%]
# practice\sec5\test_sec5_1.py::test_goodafternonn PASSED
# ======== 2 passed, 1 skipped in 0.04s ==========


# メイン処理 --------------------------------------------------------------

# テストのスキップ
import pytest

def test_hello():
    print("hello")

@pytest.mark.skip(reason="write reason")
def test_goodmorning():
    print("good morning")

def test_goodafternonn():
    print("good afternoon")
