# ******************************************************************************
# Course      : 0から始めるPytest超基礎講座
# Chapter     : 3 前処理＆後処理
# Theme       : クラスに対する前処理＆後処理の実行
# Creat Date  : 2022/2/20
# Final Update:
# URL         : https://www.udemy.com/course/python_pytest/
# ******************************************************************************


# ＜ポイント＞
# - 今回は前処理⇒メソッド各処理⇒後処理の順でテストを行う
#   --- 前回(sec3-2)のクラスのテストはメソッドごとに前処理/後処理を行っていた


# ＜実行コマンド＞
# - ターミナルより実行（実行確認のため出力表示）
# pytest I:/Project/Python/py_practice/udemy/pytest_seminar/practice/sec3/test_sec3_3.py -s


# ＜出力結果＞
# - 実行メソッドの処理が前処理/後処理のメソッドでラップされている
# setup_class
# hello world!
# pytest!
# teardown_class


# メイン処理 --------------------------------------------------------------

# クラスに対する前処理＆後処理
class TestExample():
    # 前処理
    @classmethod
    def setup_class(cls):
        print("setup_class")

    # 後処理
    @classmethod
    def teardown_class(cls):
        print("teardown_class")

    def test_example1(self):
        print("hello world!")

    def test_example2(self):
        print("pytest!")
