# ******************************************************************************
# Course      : 0から始めるPytest超基礎講座
# Chapter     : 4 fixtureによる前処理＆後処理の代替
# Theme       : fixtureによるモジュールの前処理/後処理の代替（モジュールのみ）
# Creat Date  : 2022/2/20
# Final Update:
# URL         : https://www.udemy.com/course/python_pytest/
# ******************************************************************************


# ＜ポイント＞
# - 今回(sec4-4-1)はモジュール(関数とクラス)に対して前処理/後処理を行う
#   --- 前回(sec4-2)ではクラスの各メソッドに対して前処理/後処理を行った
#   --- デコレータ(@pytest.fixture)でスコープ引数で"scope=class"を設定する


# ＜実行コマンド＞
# - ターミナルより実行
# pytest I:/Project/Python/py_practice/udemy/pytest_seminar/practice/sec4/test_sec4_4_1.py -s


# ＜出力結果＞
# - モジュール(関数とクラス)をはさんで前処理/後処理を実行している
# setup_module
# function: hello world!
# function: pytest
# method: hello world!
# method: pytest
# teardown_module




# メイン処理 --------------------------------------------------------------

# ライブラリ
import pytest

# 関数定義
# --- 前処理/後処理
# --- scopeはフィクスチャ関数が実行される粒度を指定（"module"を指定）
@pytest.fixture(scope="module")
def setup_module(request):
    print("setup_module")
    def teardown_module():
        print("teardown_module")
    request.addfinalizer(teardown_module)

# 関数定義1：
def test_hello_world(setup_module):
    print("function: hello world!")

# 関数定義2：
def test_pytest(setup_module):
    print("function: pytest")

# クラス定義
class TestExample():
    def test_hello_world(self, setup_module):
        print("method: hello world!")

    def test_pytest(self, setup_module):
        print("method: pytest")
