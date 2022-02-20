# ******************************************************************************
# Course      : 0から始めるPytest超基礎講座
# Chapter     : 2 Pytestの基礎
# Theme       : 様々な関数のテストを例示
# Creat Date  : 2022//
# Final Update:
# URL         : https://www.udemy.com/course/python_pytest/
# ******************************************************************************


# ＜ポイント＞
# - assert以降の条件がTrueになるかをテストするための構文
# - assert文の後にはTrue/Falseが戻り値となる変数を与える
#   --- assert Condition Result Variable (True/False)


# ＜実行コマンド＞
# - ターミナルより実行
# pytest I:/Project/Python/py_practice/udemy/pytest_seminar/practice/sec2/test_sec2_3.py


# メイン処理 --------------------------------------------------------------


def test_calculate():
    result = 5 * 2
    assert result == 10

def test_len():
    text = "hello world!"
    assert len(text) == 12

def test_contain():
    text = "hello world!"
    assert "rld" in text