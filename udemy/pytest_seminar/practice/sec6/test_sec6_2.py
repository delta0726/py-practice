# ******************************************************************************
# Course      : 0から始めるPytest超基礎講座
# Chapter     : 6 mockの使い方
# Theme       : 関数とメソッドの返り値をmock
# Creat Date  : 2022/2/22
# Final Update:
# URL         : https://www.udemy.com/course/python_pytest/
# ******************************************************************************


# ＜ポイント＞
# - mockは特定の関数が未完成な関数を参照している場合のテストに使用する
# - mockは疑似的などの意味を持つ


# ＜実行コマンド＞
# - ターミナルより実行
# pytest I:/Project/Python/py_practice/udemy/pytest_seminar/practice/sec6/test_sec6_2.py -v


# ＜出力結果＞



# メイン処理 --------------------------------------------------------------

# ライブラリ
import sys
sys.path.append('I:/Project/Python/py_practice/udemy/pytest_seminar')

from practice.sec6.translator2 import GoogleTranslator
import pytest

# 前処理の設定
@pytest.fixture(scope="module")
def trans():
    t = GoogleTranslator()
    print("create Translator")
    return t

# 関数定義（日本語を英語に変換）
# --- mockerを設定
def test_japanese_to_english(trans, mocker):
    mocker.patch("practice.sec6.translator2.GoogleTranslator.convert", return_value = "hello world!")
    text_translated = trans.convert("私の名前は佐藤です。", "日本語", "英語")
    print(text_translated)
    # assert text_translated == "My name is Sato."

# # 関数定義（英語を日本語に変換）
# # --- mockerを設定
# def test_english_to_japanese(trans, mocker):
#     mocker.patch("translator.GoogleTranslator.get_language_id", return_value = "ja")
#     text_translated = trans.convert("私の名前は佐藤です。", "日本語", "英語")
#     print(text_translated)
#     # assert text_translated == "私の名前は佐藤です。"
