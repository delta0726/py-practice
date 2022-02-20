# ******************************************************************************
# Course      : 0から始めるPytest超基礎講座
# Chapter     : 3 前処理＆後処理
# Theme       : メソッドに対する前処理/後処理の実行
# Creat Date  : 2022/2/20
# Final Update:
# URL         : https://www.udemy.com/course/python_pytest/
# ******************************************************************************


# ＜ポイント＞
# - クラスに対するテストを行うのでクラス名は"Test"、メソッド名は"test_"で始まる必要がある
# - 前処理/後処理のメソッドのテストに対する前処理と後処理を行うメソッドを定義する
#   --- 前処理のメソッド名：setup_method
#   --- 後処理のメソッド名：teardown_method


# ＜実行コマンド＞
# - ターミナルより実行（実行確認のため出力表示）
# pytest I:/Project/Python/py_practice/udemy/pytest_seminar/practice/sec3/test_sec3_2.py -s


# ＜出力結果＞
# - 実行メソッドの処理が前処理/後処理のメソッドでラップされている
# setup_method
# hello world!
# teardown_method
# setup_method
# pytest!
# teardown_method


# メイン処理 --------------------------------------------------------------

# 前処理＆後処理のメソッドの作成
class TestExample():
    # 前処理の実行
    def setup_method(self, method):
        print("setup_method")

    # 後処理の実行
    def teardown_method(self, method):
        print("teardown_method")

    def test_example1(self):
        print("hello world!")

    def test_example2(self):
        print("pytest!")
