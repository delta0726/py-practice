# ******************************************************************************
# Book     : Pythonプロフェッショナル大全
# Chapter  : 11 Webとネットワーク
# Section  : 1 Webでよく使うファイル形式
# Theme    : 1 JSONの操作
# Date     : 2022/09/17
# URL      : https://www.kadokawa.co.jp/product/322201000299/
# ******************************************************************************


# ＜ポイント＞
# - JSONファイルを作成する際には辞書を作成してからdumpsメソッドを実行する


# ＜目次＞
# 0 準備
# 1 辞書型とJSON形式の比較


# 0 準備 ------------------------------------------------------------------

# ライブラリ
import json


# 1 辞書型とJSON形式の比較 --------------------------------------------------

# 辞書型のオブジェクト作成
j = {
    "employee":
        [
            {"id": 111, "name": "Mike"},
            {"id": 222, "name": "Nancy"}
        ]
}

# 確認
# --- 辞書型
# --- JSON形式
print(j)
print(json.dumps(j))

# 出力結果
# --- 文字列がダブルクオートになっている
# {'employee': [{'id': 111, 'name': 'Mike'}, {'id': 222, 'name': 'Nancy'}]}
# {"employee": [{"id": 111, "name": "Mike"}, {"id": 222, "name": "Nancy"}]}
