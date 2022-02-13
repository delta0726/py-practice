# ******************************************************************************
# Course      : Python3.8マスター講座
# Chapter     : 6 基本的な標準ライブラリ
# Theme       : sysモジュール
# Creat Date  : 2022/2/13
# Final Update:
# URL         : https://www.udemy.com/course/python-python/
# ******************************************************************************


# ＜概要＞
# - osモジュールがos関連を扱うのに対して、sysモジュールはpythonインタープリターを扱う


# ＜参考＞
# 公式ドキュメント
# https://docs.python.org/ja/3/library/sys.html


# ＜目次＞
# 0 準備
# 1 Pythonの情報取得
# 2 実行時の引数取得
# 3 システム終了


# 0 準備 ----------------------------------------------------------

# ライブラリ
import sys
import pathlib
from pprint import pprint


# 1 Pythonの情報取得 -----------------------------------------------

# ＜ポイント＞
# - Pythonパスはsys.path.append()で追加することが可能


# Pythonのバージョン
print(sys.version)

# Pythonパス
pprint(sys.path)

# Pythonパスの追加
sys.path.append('C:/')
pprint(sys.path)

# オブジェクトのサイズ取得
list_a = [x for x in range(100)]
print(sys.getsizeof(list_a))


# 2 実行時の引数取得 ------------------------------------------------

# ＜ポイント＞
# - 実行構成の編集(Edit Configration)から実行
#   --- runfile('*/sys.py', args=['1', '2', '3'])

# 引数取得
# --- ターミナルからの実行時
# --- 引数に"1 2 3"を指定する
print(sys.argv)
print('引数取得1: ', sys.argv[1])
print('引数取得2: ', sys.argv[2])
print('引数取得3: ', sys.argv[3])


# 3 システム終了 -----------------------------------------------------

# ＜ポイント＞
# - システム終了は引数に応じてステータスの取得が可能

# システムを終了させる
sys.exit(0)

# 追加処理
# --- 実行されないことを確認
print('終了チェック')
