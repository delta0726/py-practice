# ******************************************************************************
# Book     : Pythonプロフェッショナル大全
# Chapter  : 10 コンフィグとロギング
# Section  : 1 設定ファイルの様々な形式
# Theme    : 5 yamlのフロースタイル
# Date     : 2022/09/11
# URL      : https://www.kadokawa.co.jp/product/322201000299/
# ******************************************************************************


# ＜ポイント＞
# - yamlはライブラリのバージョンによって「ブロックスタイル｣と｢フロースタイル｣がある


# ＜目次＞
# 0 準備
# 1 yamlのフロースタイル
# 2 yamlのブロックスタイル


# 0 準備 -------------------------------------------------------------------

# ライブラリ
import yaml

# 準備：前回ファイルの削除
if os.path.isfile('config2.yml'):
    os.remove('config2.yml')


# 1 yamlのフロースタイル ----------------------------------------------------

with open('config_flow.yml', 'w') as yaml_file:
    yaml.dump({
        'web_server': {
            'host': '127.0.0.1',
            'port': 80
        },
        'db_server': {
            'host': '127.0.0.1',
            'port': 3306
        }
    }, yaml_file, default_flow_style=True)


# ＜確認＞
# - ターミナルから以下のコマンド
# cat .\config_flow.yml

# {db_server: {host: 127.0.0.1, port: 3306}, web_server: {host: 127.0.0.1, port: 80}}


# 2 yamlのブロックスタイル ----------------------------------------------------

with open('config_block.yml', 'w') as yaml_file:
    yaml.dump({
        'web_server': {
            'host': '127.0.0.1',
            'port': 80
        },
        'db_server': {
            'host': '127.0.0.1',
            'port': 3306
        }
    }, yaml_file, default_flow_style=False)


# ＜確認＞
# - ターミナルから以下のコマンド
# cat .\config_block.yml

# db_server:
#   host: 127.0.0.1
#   port: 3306
# web_server:
#   host: 127.0.0.1
#   port: 80