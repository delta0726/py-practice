# ******************************************************************************
# Course      : 0から始めるPytest超基礎講座
# Chapter     :  4 fixtureによる前処理＆後処理の代替
# Theme       : fixtureのautouse設定
# Creat Date  : 2022/2/21
# Final Update:
# URL         : https://www.udemy.com/course/python_pytest/
# ******************************************************************************


# ＜ポイント＞
# - 全ての関数やメソッドに対して前処理/後処理を適用したい場合はautouse引数をTrueにする
#   --- 個々の関数やメソッドの引数に前処理/後処理の関数名を指定する必要がない


# ＜実行コマンド＞
# - ターミナルより実行
# pytest I:/Project/Python/py_practice/udemy/pytest_seminar/practice/sec4/test_sec4_5.py -s


# ＜出力結果＞
# setup_processing
# hello
# teardown_processing
# setup_processing
# goodmorning
# teardown_processing
# setup_processing
# goodafternoon
# teardown_processing


# メイン処理 --------------------------------------------------------------

# ライブラリ
import pytest

# 前処理＆後処理の定義
# --- 全ての処理に対してテストを行う
# --- デフォルトはFalse
@pytest.fixture(autouse=True)
def setup_processing(request):
    print("setup_processing")
    def teardown_processing():
        print("teardown_processing")
    request.addfinalizer(teardown_processing)

class TestExample():
    def test_hello(self, setup_processing):
        print("hello")

    def test_goodmorning(self):
        print("goodmorning")

    def test_goodafternoon(self):
        print("goodafternoon")
