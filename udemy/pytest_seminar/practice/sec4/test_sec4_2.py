# ******************************************************************************
# Course      : 0から始めるPytest超基礎講座
# Chapter     : 4 fixtureによる前処理＆後処理の代替
# Theme       : fixtureによるメソッドの前処理/後処理の代替
# Creat Date  : 2022/2/20
# Final Update:
# URL         : https://www.udemy.com/course/python_pytest/
# ******************************************************************************


# ＜ポイント＞
# - クラス内の特定のメソッドのみに前処理/後処理を行う場合はfixtureを使う
# - 前処理/後処理を行う関数を定義してのデコレータ(@pytest.fixture)を付与する
# - クラスのメソッドの引数に前処理/後処理を行う関数を与える
#   --- クラス外の関数を参照することになる


# ＜実行コマンド＞
# - ターミナルより実行
# pytest I:/Project/Python/py_practice/udemy/pytest_seminar/practice/sec4/test_sec4_2.py -s


# ＜出力結果＞
# - 前処理/後処理を設定していないメソッド(*)では前処理/後処理が実行されていない
# setup_processing
# hello
# teardown_processing
# goodmorning (*)
# setup_processing
# goodafternoon
# teardown_processing


# メイン処理 --------------------------------------------------------------

# ライブラリ
import pytest

# 関数定義
# --- 前処理/後処理
@pytest.fixture()
def setup_processing(request):
    print("setup_processing")
    def teardown_processing():
        print("teardown_processing")
    request.addfinalizer(teardown_processing)

# クラス定義
class TestExample():
    def test_hello(self, setup_processing):
        print("hello")

    def test_goodmorning(self):
        print("goodmorning")

    def test_goodafternoon(self, setup_processing):
        print("goodafternoon")
