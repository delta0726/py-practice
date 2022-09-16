# ******************************************************************************
# Book     : Pythonプロフェッショナル大全
# Chapter  : 11 Webとネットワーク
# Section  : 2 Pythonで通信してみよう
# Theme    : 5 POSTでWebにデータ登録
# Date     : 2022/09/17
# URL      : https://www.kadokawa.co.jp/product/322201000299/
# ******************************************************************************


# ＜ポイント＞
# - RESTはHTTPメソッドを用いてWebサーバーにアクセスする手法


# ＜目次＞
# 0 準備
# 1 POSTでデータを登録


# 0 準備 ------------------------------------------------------------------

# ライブラリ
import urllib.request
import json


# 1 POSTでデータを登録 -----------------------------------------------------

# 辞書の作成
payload = {"key1": "value1", "key2": "value2"}

# JSONに変換
# --- UTF-8にエンコード
payload = json.dumps(payload).encode('utf-8')

# URLにリクエストデータを作成
req = urllib.request.Request(
    'http://httpbin.org/post', data=payload, method='POST')

# 登録したデータの読み込み
with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))
