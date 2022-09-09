# ******************************************************************************
# Book     : Pythonプロフェッショナル大全
# Chapter  : 10 コンフィグとロギング
# Section  : 1 設定ファイルの様々な形式
# Theme    : 1 configparserの作成
# Date     : 2022/09/10
# URL      : https://www.kadokawa.co.jp/product/322201000299/
# ******************************************************************************


# ＜ポイント＞
# - configparserオブジェクトに設定を辞書型で書き込んでファイル書き込みする
# - プロジェクトディレクトリにconfig.iniファイルが作成される


# ＜目次＞
# 0 準備
# 1 configparserで書き込む
# 2 iniファイルの確認


# 0 準備 ---------------------------------------------------------------------

# ライブラリ
import configparser
import os


# 準備：前回ファイルの削除
if os.path.isfile('config.ini'):
    os.remove('config.ini')


# 1 configparserで書き込む -----------------------------------------------------

# インスタンス生成
config = configparser.ConfigParser()

# コンフィグの設定
config['DEFAULT'] = {
    'debug': True
}
config['web_server'] = {
    'host': '127.0.0.1',
    'port': 80
}
config['db_server'] = {
    'host': '127.0.0.1',
    'port': 3306
}

# コンフィグの書き込み
with open('config.ini', 'w') as config_file:
    config.write(config_file)


# 2 iniファイルの確認 ----------------------------------------------------------

# ＜configファイルの確認＞
# - ターミナルから以下のコマンド
# cat .\config.ini
