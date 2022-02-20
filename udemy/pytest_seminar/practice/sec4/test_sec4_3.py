# ******************************************************************************
# Course      : 0から始めるPytest超基礎講座
# Chapter     : 4 fixtureによる前処理＆後処理の代替
# Theme       : fixtureによるクラスの前処理/後処理の代替
# Creat Date  : 2022/2/20
# Final Update:
# URL         : https://www.udemy.com/course/python_pytest/
# ******************************************************************************


# ＜ポイント＞
# - 今回(sec4-3)はクラス全体に対して前処理/後処理を行う
#   --- 前回(sec4-2)ではクラスの各メソッドに対して前処理/後処理を行った
#   --- デコレータ(@pytest.fixture)でスコープ引数で"scope=class"を設定する


# ＜実行コマンド＞
# - ターミナルより実行
# pytest I:/Project/Python/py_practice/udemy/pytest_seminar/practice/sec4/test_sec4_3.py -s


# ＜出力結果＞
# - クラスに対してテストを行っているので、クラスの前後のみで前処理/後処理が行われている
# setup_processing
# hello world!
# goodmorning
# pytest!
# teardown_processing


# メイン処理 --------------------------------------------------------------

# ライブラリ
import pytest

# 関数定義
# --- 前処理/後処理
# --- scopeはフィクスチャ関数が実行される粒度を指定
# --- scopeのデフォルト値は"function"になっている
@pytest.fixture(scope="class")
def setup_processing(request):
    print("setup_processing")
    def teardown_processing():
        print("teardown_processing")
    request.addfinalizer(teardown_processing)

# クラス定義
class TestExample():
    def test_example1(self, setup_processing):
        print("hello world!")

    def test_goodmorning(self):
        print("goodmorning")

    def test_example2(self, setup_processing):
        print("pytest!")
