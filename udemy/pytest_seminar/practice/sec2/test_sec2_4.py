# ******************************************************************************
# Course      : 0から始めるPytest超基礎講座
# Chapter     : 2 Pytestの基礎
# Theme       : メソッドに対するテストの実行
# Creat Date  : 2022/2/20
# Final Update:
# URL         : https://www.udemy.com/course/python_pytest/
# ******************************************************************************


# ＜ポイント＞
# - メソッドに対してもassert文を用いたテストを行うことができる
#   --- クラス名は"Test"で始まる必要がある
#   --- メソッド名は"test_"で始まる必要がある


# ＜実行コマンド＞
# - ターミナルより実行
# pytest I:/Project/Python/py_practice/udemy/pytest_seminar/practice/sec2/test_sec2_4.py


# メイン処理 --------------------------------------------------------------

# メソッドのテスト
class TestExample():
    def test_example1(self):
        assert True

    def test_example2(self):
        assert True
