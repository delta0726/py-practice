# ******************************************************************************
# Course      : 0から始めるPytest超基礎講座
# Chapter     : 4 fixtureによる前処理＆後処理の代替
# Theme       : fixtureによるモジュールの前処理/後処理の代替（モジュール + 関数）
# Creat Date  : 2022/2/20
# Final Update:
# URL         : https://www.udemy.com/course/python_pytest/
# ******************************************************************************


# ＜ポイント＞
# - モジュール全体に対して前処理/後処理をしつつ、特定の関数でも前処理/後処理を行うことができる
#   --- 関数の引数にそれぞれの前処理/後処理の指定する


# ＜実行コマンド＞
# - ターミナルより実行
# pytest I:/Project/Python/py_practice/udemy/pytest_seminar/practice/sec4/test_sec4_4_2.py -s


# ＜出力結果＞
# - モジュール全体に前処理/後処理を実行しつつ、特定の関数でも独自の前処理/後処理を実行する
# setup_module
# setup_function
# function: hello world! (*)
# teardown_function
# function: pytest
# class: hello world!
# class: pytest
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

# 関数定義
# --- 前処理/後処理
# --- scopeはフィクスチャ関数が実行される粒度を指定（"function"を指定）
@pytest.fixture(scope="function")
def setup_function(request):
    print("setup_function")
    def teardown_function():
        print("teardown_function")
    request.addfinalizer(teardown_function)

# 関数定義1：
# --- モジュールのテストと関数のテストの両方で前処理/後処理を行う
def test_hello_world(setup_module, setup_function):
    print("function: hello world!")

# 関数定義2：
def test_pytest(setup_module):
    print("function: pytest")

# クラス定義
class TestExample():
    def test_hello_world(self, setup_module):
        print("class: hello world!")

    def test_pytest(self, setup_module):
        print("class: pytest")