# ******************************************************************************
# Course      : 0から始めるPytest超基礎講座
# Chapter     : 6 mockの使い方
# Theme       : クラスの動作確認
# Creat Date  : 2022/2/22
# Final Update:
# URL         : https://www.udemy.com/course/python_pytest/
# ******************************************************************************


# ＜ポイント＞
# - GoogleTranslatorクラスの動作確認


# 動作確認 ----------------------------------------------------------------------

# ライブラリ
from practice.sec6.translator import GoogleTranslator

# インスタンス作成
trans = GoogleTranslator()

# 翻訳
text_translated = trans.convert("私の名前は佐藤です。", "日本語", "英語")
print(text_translated)
