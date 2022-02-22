# ******************************************************************************
# Course      : 0から始めるPytest超基礎講座
# Chapter     : 7 複数のパラメータでテストを実行
# Theme       : parametrizeの使い方
# Creat Date  : 2022/2/23
# Final Update:
# URL         : https://www.udemy.com/course/python_pytest/
# ******************************************************************************


# ＜ポイント＞
# - 1つの関数に対して複数パターンの引数でテストを行う


# ＜実行コマンド＞
# - ターミナルより実行
# pytest I:/Project/Python/py_practice/udemy/pytest_seminar/practice/sec7/test_sec7_1.py -s -v


# ＜出力結果＞
# create Translator
# input_a:私の名前は佐藤です。
# input_b:日本語
# input_c:英語
# input_d:My name is Sato.
# PASSED
# input_a:こんにちは
# input_b:日本語
# input_c:英語
# input_d:Hello
# PASSED
# input_a:おはよう
# input_b:日本語
# input_c:英語
# input_d:good morning
# PASSED


# メイン処理 --------------------------------------------------------------

# ライブラリ
import sys
sys.path.append('I:/Project/Python/py_practice/udemy/pytest_seminar')

from practice.sec7.translator import GoogleTranslator
import pytest


# パラメータリストの作成
input_data = [
    ("私の名前は佐藤です。","日本語","英語", "My name is Sato."),
    ("こんにちは","日本語","英語", "Hello"),
    ("おはよう","日本語","英語", "good morning")
]

# 前処理の設定
@pytest.fixture(scope="module")
def trans():
    t = GoogleTranslator()
    print("create Translator")
    return t

# パラメータ設定
# --- リストをパラメータに入力
# --- 各パラメータは複数パターンの要素を保持する
@pytest.mark.parametrize("input_a, input_b, input_c, input_d", input_data)

# 関数定義
# --- 英語を日本語に変換
def test_convert(input_a, input_b, input_c, input_d, trans):
    # パラメータの出力
    print(f"input_a:{input_a}")
    print(f"input_b:{input_b}")
    print(f"input_c:{input_c}")
    print(f"input_d:{input_d}")

    # モジュールの実行
    # --- 引数をパラメータに変更
    # --- 戻り値をパラメータに変更
    text_translated = trans.convert(input_a, input_b, input_c)
    assert text_translated == input_d
