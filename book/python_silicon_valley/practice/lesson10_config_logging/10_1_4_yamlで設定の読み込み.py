# ******************************************************************************
# Book     : Pythonプロフェッショナル大全
# Chapter  : 10 コンフィグとロギング
# Section  : 1 設定ファイルの様々な形式
# Theme    : 4 yamlで設定の読み込み
# Date     : 2022/09/10
# URL      : https://www.kadokawa.co.jp/product/322201000299/
# ******************************************************************************


# ＜ポイント＞
# - yamlファイルに設定を書き込むことができる


# ＜目次＞
# 0 準備
# 1 yamlファイルを読込む


# 0 準備 ---------------------------------------------------------------

# ライブラリ
import yaml


# 1 yamlファイルを読込む -------------------------------------------------

with open('config.yml', 'r') as yaml_file:
    data = yaml.load(yaml_file, Loader=yaml.FullLoader)
    print(data)
    print(type(data))
    print(data['web_server']['host'])
    print(data['web_server']['port'])
    print(data['db_server']['host'])
    print(data['db_server']['port'])
