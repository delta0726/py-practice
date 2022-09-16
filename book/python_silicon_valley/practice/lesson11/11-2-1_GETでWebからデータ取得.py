# ******************************************************************************
# Book     : Pythonプロフェッショナル大全
# Chapter  : 11 Webとネットワーク
# Section  : 2 Pythonで通信してみよう
# Theme    : 1 GETでWebからデータ取得
# Date     : 2022/09/17
# URL      : https://www.kadokawa.co.jp/product/322201000299/
# ******************************************************************************


# ＜ポイント＞
# - RESTはHTTPメソッドを用いてWebサーバーにアクセスする手法
# - GETによるデータ取得に対応する操作を確認する


# ＜目次＞
# 0 準備
# 1 URLからデータを取得
# 2 パラメーターを付加してURLにアクセス


# 0 準備 ------------------------------------------------------------------

# ライブラリ
import urllib.request
import json


# 1 URLからデータを取得 ----------------------------------------------------

# URLの指定
url = 'http://httpbin.org/get'

# URLからデータ取得
# --- bがついたバイト形式の形で結果が返ってくる
with urllib.request.urlopen(url) as f:
    print(f.read())

# URLからデータ取得
# --- UTF-8でデコードする
with urllib.request.urlopen(url) as f:
    print(f.read().decode('utf-8'))

# URLからデータ取得
# --- UTF-8でデコードしたものを辞書型に変換
with urllib.request.urlopen(url) as f:
    r = json.loads(f.read().decode('utf-8'))
    print(r)
    print(type(r))


# 2 パラメーターを付加してURLにアクセス ----------------------------------------

# パラメータ作成
payload = {"key1": "value1", "key2": "value2"}

# URLにパラメータを追加
url = 'http://httpbin.org/get' + '?' + urllib.parse.urlencode(payload)
print(url)

# URLからデータ取得
# --- argsにパラメータが入っている
with urllib.request.urlopen(url) as f:
    print(f.read().decode('utf-8'))
