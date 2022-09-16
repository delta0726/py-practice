# ******************************************************************************
# Book     : Pythonプロフェッショナル大全
# Chapter  : 11 Webとネットワーク
# Section  : 1 Webでよく使うファイル形式
# Theme    : 3 JSONの読み込み
# Date     : 2022/09/17
# URL      : https://www.kadokawa.co.jp/product/322201000299/
# ******************************************************************************


# ＜ポイント＞
# - JSONファイルを読み込む際はloadメソッドを使用する


# ＜目次＞
# 0 準備
# 1 JSONファイルの読み込み


# 0 準備 ------------------------------------------------------------------

# ライブラリ
import json
import os

# ディレクトリ変更
os.chdir('./practice/lesson11')


# 1 JSONファイルの読み込み -------------------------------------------------

# 辞書型の作成
j = {
    "employee":
        [
            {"id": 111, "name": "Mike"},
            {"id": 222, "name": "Nancy"}
        ]
}

# JSONファイルの書き込み
with open('test.json', 'w') as f:
    json.dump(j, f)

# JSONファイルの読み込み
with open('test.json', 'r') as f:
    print(json.load(f))
