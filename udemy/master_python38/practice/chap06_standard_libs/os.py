# ******************************************************************************
# Course      : Python3.8マスター講座
# Chapter     : 6 基本的な標準ライブラリ
# Theme       : osモジュール
# Creat Date  : 2022/2/13
# Final Update:
# URL         : https://www.udemy.com/course/python-python/
# ******************************************************************************


# ＜概要＞
# - os関連なので非常に多くの関数がある
# - 実際に使うのは｢パス/ファイル操作｣や｢環境変数関連｣が多い


# ＜参考＞
# 公式ドキュメント
# https://docs.python.org/ja/3/library/os.html


# ＜目次＞
# 0 準備
# 1 OS情報の取得
# 2 環境変数の取得
# 3 ディレクトリの取得
# 4 プロセスIDの取得
# 5 ディレクトリ操作


# 0 準備 --------------------------------------------------------

# ライブラリ
import os
from pprint import pprint

# カレントディレクトリの取得
cwd = os.getcwd()


# 1 OS情報の取得 -------------------------------------------------

# OS名の取得
# --- Windows: nt  Linux: linux, Mac: posix
print(os.name)

# 活用方法
if os.name == 'nt':
    pass  # Windows用の処理
elif os.name == 'posix':
    pass  # Mac用の処理


# 2 環境変数の取得 -----------------------------------------------

# 環境変数の取得
# --- 変数名を指定すると値を取得することができる
pprint(os.environ.get('PYTHONPATH'))
pprint(os.getenv('PYTHONPATH'))

# 環境変数の設定
os.environ['my_var'] = 'development'
pprint(os.getenv('my_var'))

# 活用方法
enveron = os.getenv('enveron')
if enveron == 'development':
    pass  # 開発環境用の設定
elif enveron == 'production':
    pass  # 本番環境用の設定


# 3 ディレクトリの取得 -----------------------------------------------

# カレントディレクトリ
print(os.getcwd())

# ディレクトリ変更
os.chdir('practice')
print(os.getcwd())

# カレントディレクトリのファイル一覧
pprint(os.listdir())

# 1つ上のディレクトリに移動
os.chdir('..')
print(os.getcwd())

os.chdir(os.environ['HOME'])
print(os.getcwd())


# 4 プロセスIDの取得 ------------------------------------------------

# 自分のプロセスID
print(os.getpid())

# 親プロセスID
print(os.getppid())


# 5 ディレクトリ操作 ------------------------------------------------

# ＜ポイント＞
# - 簡単なディレクトリ操作を行うことができる
#   --- ターミナルの操作をPythonスクリプトで行っているイメージ


# 準備：カレントディレクトリに移動
os.chdir(cwd)
os.getcwd()

# フォルダ作成
os.mkdir('sample')

# フォルダ名の変更
os.rename('sample', 'sample2')

# フォルダの削除
os.rmdir('sample2')
