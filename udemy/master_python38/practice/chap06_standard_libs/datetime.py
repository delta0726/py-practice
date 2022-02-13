# ******************************************************************************
# Course      : Python3.8マスター講座
# Chapter     : 6 基本的な標準ライブラリ
# Theme       : datetime(datetime)
# Creat Date  : 2022/2/13
# Final Update:
# URL         : https://www.udemy.com/course/python-python/
# ******************************************************************************


# ＜概要＞
# - datetimeモジュールは日付を秒単位で扱うもので{datetime}に含まれる
#   --- タイムゾーンの概念が含まれる


# ＜参考＞
# 公式ドキュメント
# https://docs.python.org/ja/3/library/datetime.html


# ＜目次＞
# 0 準備
# 1 日付の作成
# 2 現在時刻の取得
# 3 文字列からdatetimeに変換
# 4 datetimeから文字列に変換
# 5 日付演算
# 6 タイムゾーンの変換
# 7 dateとdatetimeの変換


# 0 準備 ---------------------------------------------------

# ライブラリ
from datetime import datetime, timedelta, timezone, date


# 1 日付の作成 ----------------------------------------------

# 日付を秒単位で作成
my_date = datetime(2018, 11, 11, 18, 15, 25)
print(my_date, type(my_date))


# 2 現在時刻の取得 ------------------------------------------

# ＜ポイント＞
# - 時刻を含むのでタイムゾーンの概念が含まれる


# 日本時間
now_datetime = datetime.now()

# UTC時間
utc_now = datetime.utcnow()

# 確認
print(now_datetime)
print(utc_now)

# 日付要素の取得
# --- プロパティにより取得
print(now_datetime.year)
print(now_datetime.month)
print(now_datetime.day)
print(now_datetime.hour)
print(now_datetime.minute)
print(now_datetime.microsecond)


# 3 文字列からdatetimeに変換 ---------------------------------------

# ＜ポイント＞
# - strptimeメソッドを用いると文字列をdatetimeに変換することができる
# - ログなどの文字列からdatetimeに変換するケースは多い


# 準備：文字列日時の作成
timestr = '2019/12/12 16:40'

# 日付/日時のフォーマットを指定
dt = datetime.strptime(timestr, '%Y/%m/%d %H:%M')

# 確認
print(dt, type(dt))


# 4 datetimeから文字列に変換 ---------------------------------------

# ＜ポイント＞
# - strftimeメソッドを用いるとdatetimeを文字列に変換することができる


# 準備：datetimeの作成
dt = datetime(2019, 12, 12, 16, 40)

# 文字列に変換
# --- フォーマットは自由に指定可能
date_str = dt.strftime('%Y %m %d')

# 確認
print(date_str, type(date_str))


# 5 日付演算 ----------------------------------------------------

# ＜ポイント＞
# - timedeltaを用いると日付の加算と減算ができるようになる
#   --- プラス値は過去にシフト
#   --- マイナス値は過去にシフト


# 日付の加算と減算
my_delta_1 = datetime.today() - timedelta(days=12)
my_delta_2 = datetime.today() - timedelta(days=-12)

# 確認
print(my_delta_1)
print(my_delta_2)


# 6 タイムゾーンの変換 --------------------------------------------

# UTC時間
my_date = datetime(2019, 11, 11, 18, 15, 25)

# タイムゾーンの変換
# --- UTC => JST
local_date = my_date.replace(tzinfo=timezone.utc).astimezone()

# 確認
print(my_date, local_date)


# 7 dateとdatetimeの変換 ---------------------------------------

# ＜ポイント＞
# - datetimeクラスの方が情報量が多いので変換方法は対照的ではない点に注意
#   --- dateクラスから日付要素を取得してdatetimeクラスのオブジェクトを定義する
#   --- datetimeクラスにはdateクラスへの変換モジュールがある


# 準備：dateクラスののオブジェクト作成
date_obj = date.today()

# datetimeクラス
datetime_obj = datetime(date_obj.year, date_obj.month, date_obj.day)

# 確認
print(date_obj, type(date_obj))
print(datetime_obj, type(datetime_obj))


# 準備： datetimeクラスのオブジェクト作成
datetime_obj = datetime.now()

# dateクラスに変換
# --- datetimeクラスにはdateクラスへの変換モジュールがある
date_obj = datetime_obj.date()

# 確認
print(date_obj, type(date_obj))
print(datetime_obj, type(datetime_obj))
