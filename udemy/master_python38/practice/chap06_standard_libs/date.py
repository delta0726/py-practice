# ******************************************************************************
# Course      : Python3.8マスター講座
# Chapter     : 6 基本的な標準ライブラリ
# Theme       : datetime(date / timedelta)
# Creat Date  : 2022/2/13
# Final Update:
# URL         : https://www.udemy.com/course/python-python/
# ******************************************************************************


# ＜概要＞
# - dateモジュールは日付データをを扱うものでdatetimeクラスに含まれる
#   --- datetimeモジュールは日付を秒単位で扱う
#   --- timedeltaモジュールは日付の演算を扱う


# ＜参考＞
# 公式ドキュメント
# https://docs.python.org/ja/3/library/datetime.html


# ＜目次＞
# 0 準備
# 1 日付の作成
# 2 日付の置換
# 3 日付演算
# 4 日付要素の取得
# 5 日付データの文字列変換


# 0 準備 ---------------------------------------------------

# ライブラリ
from datetime import date, timedelta


# 1 日付の作成 --------------------------------------------

# 存在する日付
my_date = date(1000, 1, 1)
print(my_date)

# 存在しない日付
# --- エラー
my_date = date(1000, 2, 30)
print(my_date)

# 本日日付の取得
print(date.today())

# 日付の比較
# --- my_dateがdate.today()より古ければTrue
print(my_date < date.today())


# 2 日付の置換 -----------------------------------------------

# ＜ポイント＞
# - 日付要素を指定した値に上書きすることができる
#   --- replaceという名前のメソッドだが実質的に上書き


# 存在する日付
my_date = date(1000, 1, 1)
print(my_date)

# 日付の置換
# --- 置換といっても新しい要素を指定するだけ
my_date = my_date.replace(year=2000, month=12)
print(my_date)


# 3 日付演算 ----------------------------------------------------

# ＜ポイント＞
# - timedeltaを用いると日付の加算と減算ができるようになる
#   --- プラス値は過去にシフト
#   --- マイナス値は過去にシフト


# 日付の加算と減算
my_delta_1 = date.today() - timedelta(days=12)
my_delta_2 = date.today() - timedelta(days=-12)

# 確認
print(my_delta_1)
print(my_delta_2)


# 4 日付要素の取得 ----------------------------------------------

# ＜ポイント＞
# - 日付の各要素はプロパティとして取得することが可能


# 日付作成
my_date = date.today()

# 確認
print(my_date.year)
print(my_date.month)
print(my_date.day)


# 5 日付データの文字列変換 ----------------------------------------

# ＜ポイント＞
# - strftimeメソッドを用いると日付の文字列変換を行うことができる


# 日付作成
my_date = date.today()

# 日付の文字列変換
str_date = my_date.strftime('%Y/%m/%d')

# 確認
print(str_date)
print(type(str_date))
print(type(my_date))
