# ******************************************************************************
# Book     : Pythonプロフェッショナル大全
# Chapter  : 10 コンフィグとロギング
# Section  : 1 設定ファイルの様々な形式
# Theme    : configpaserで設定の読み込み
# Date     : 2022/09/10
# URL      : https://www.kadokawa.co.jp/product/322201000299/
# ******************************************************************************


# ＜ポイント＞
# - 設定読込の際はConfigParserのインスタンスを生成してreadメソッドで読込む
# - 設定情報は辞書形式で取り出す


# ＜目次＞
# 0 準備
# 1 configparserで読み込む
# 2 iniファイルの確認


# 0 準備 --------------------------------------------------------------

# ライブラリ
import configparser


# 1 configparserで読み込む --------------------------------------------

# インスタンス生成
config = configparser.ConfigParser()

# 読み込み
config.read('config.ini')

# 確認
print(config['web_server'])
print(config['web_server']['host'])
print(config['web_server']['port'])

print(config['DEFAULT']['debug'])
