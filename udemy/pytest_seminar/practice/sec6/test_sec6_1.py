# ******************************************************************************
# Course      : 0から始めるPytest超基礎講座
# Chapter     : 6 mockの使い方
# Theme       : サンプルスクリプトの基本的なテスト
# Creat Date  : 2022/2/22
# Final Update:
# URL         : https://www.udemy.com/course/python_pytest/
# ******************************************************************************


# ＜ポイント＞
# - スクリプトに対してfixtureを用いた基本的なテストを行う


# ＜実行コマンド＞
# - ターミナルより実行
# pytest I:/Project/Python/py_practice/udemy/pytest_seminar/practice/sec6/test_sec6_1.py -v


# ＜出力結果＞
# practice\sec6\test_sec6_1.py::test_japanese_to_english PASSED
# practice\sec6\test_sec6_1.py::test_english_to_japanese PASSED
# ================ 2 passed in 0.55s =======================


# メイン処理 --------------------------------------------------------------

# ライブラリ
import sys
sys.path.append('I:/Project/Python/py_practice/udemy/pytest_seminar')

from practice.sec6.translator import GoogleTranslator
import pytest


# 前処理の設定
# --- クラスを宣言して渡している
@pytest.fixture(scope="module")
def trans():
    t = GoogleTranslator()
    print("create Translator")
    return t

# 関数定義
# --- 日本語を英語に変換
def test_japanese_to_english(trans):
    text_translated = trans.convert("私の名前は佐藤です。", "日本語", "英語")
    assert text_translated == "My name is Sato."

# 関数定義
# --- 英語を日本語に変換
def test_english_to_japanese(trans):
    text_translated = trans.convert("My name is Sato.", "英語", "日本語")
    assert text_translated == "私の名前は佐藤です。"
