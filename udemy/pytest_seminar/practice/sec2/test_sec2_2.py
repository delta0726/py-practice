# ******************************************************************************
# Course      : 0から始めるPytest超基礎講座
# Chapter     : 2 Pytestの基礎
# Theme       : assert文の使い方
# Creat Date  : 2022/2/20
# Final Update:
# URL         : https://www.udemy.com/course/python_pytest/
# ******************************************************************************


# ＜アサート文とは＞
# - assert以降の条件がTrueになるかをテストするための構文
# - assert文の後にはTrue/Falseが戻り値となる変数を与える
#   --- assert Condition Result Variable (True/False)


# ＜実行コマンド＞
# - ターミナルより実行
# pytest I:/Project/Python/py_practice/udemy/pytest_seminar/practice/sec2/test_sec2_2.py


# メイン処理 ----------------------------------------------------------------------------------

# テストが成功するケース
def test_example1():
    assert True

# テストが失敗するケース
def test_example2():
    assert False