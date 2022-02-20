# ******************************************************************************
# Course      : 0から始めるPytest超基礎講座
# Chapter     : 4 fixtureによる前処理＆後処理の代替
# Theme       : fixtureによる関数の前処理/後処理の代替
# Creat Date  : 2022/2/20
# Final Update:
# URL         : https://www.udemy.com/course/python_pytest/
# ******************************************************************************


# ＜ポイント＞
# - 特定のメソッドのみに前処理/後処理を行う場合はfixtureを使う
# - 前処理/後処理を行う関数を定義してのデコレータ(@pytest.fixture)を付与する


# ＜実行コマンド＞
# - ターミナルより実行
# pytest I:/Project/Python/py_practice/udemy/pytest_seminar/practice/sec4/test_sec4_1.py -s


# ＜出力結果＞
# - 前処理/後処理を設定していない関数(*)では前処理/後処理が実行されていない
# setup_processing
# hello
# teardown_processing
# goodmorning (*)
# setup_processing
# goodafternoon
# teardown_processing


# メイン処理 --------------------------------------------------------------

# ライブラリ
# --- fixtureを使えるようにする
import pytest

# 前処理/後処理
# --- 前処理のみ行う場合はteardown_processing()を削除する
# --- 後処理だけの部分はsetup_processing()直下の処理を削除する
@pytest.fixture()
def setup_processing(request):
    print("setup_processing")
    def teardown_processing():
        print("teardown_processing")
    request.addfinalizer(teardown_processing)

# 関数1：前処理/後処理あり
def test_hello(setup_processing):
    print("hello")

# 関数2：前処理/後処理なし
def test_goodmorning():
    print("goodmorning")

# 関数3：前処理/後処理あり
def test_goodafternoon(setup_processing):
    print("goodafternoon")
