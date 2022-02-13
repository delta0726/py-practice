# ******************************************************************************
# Course      : Python3.8マスター講座
# Chapter     : 10 ファイル圧縮ライブラリ（gzip）
# Theme       : gzip
# Creat Date  : 2022/2/13
# Final Update:
# URL         : https://www.udemy.com/course/python-python/
# ******************************************************************************


# ＜概要＞
# - gzip形式は圧縮効率が高くzipと並んでスタンダードな圧縮形式
#   --- ".txt.gz"など中身のファイルの拡張子を明示する


# ＜参考＞
# 公式ドキュメント
# https://docs.python.org/ja/3/library/gzip.html


# ＜目次＞
# 0 準備
# 1 gzipの書き込み
# 2 gzipの読み込み
# 3 追記モードでデータ追加


# 0 準備 ----------------------------------------------------------

# ライブラリ
import gzip


# 1 gzipの書き込み -------------------------------------------------

# データ作成
data = 'こんにちは\nさようなら'

# テキストファイル
# --- 文字列の書き込みの場合はエンコーディングを指定する
with gzip.open('gzip/text.txt.gz', mode='wb') as f:
    f.write(data.encode('utf-8'))


# 2 gzipの読み込み ----------------------------------------------------

# バイナリ形式で読み込み
with gzip.open('gzip/text.txt.gz', mode='rb') as f:
    print(f.read().decode('utf-8'))

# テキスト形式で読み込み
with gzip.open('gzip/text.txt.gz', mode='rt', encoding='utf-8') as f:
    print(f.read())

# テキスト形式で読み込み
# --- readlinesで読み込み
with gzip.open('gzip/text.txt.gz', mode='rt', encoding='utf-8') as f:
    line = f.readlines()
    print(line)

# テキスト形式で読み込み
# --- 1行ずつ読み込み（readline）
with gzip.open('gzip/text.txt.gz', mode='rt', encoding='utf-8') as f:
    while (line := f.readline()):
        print(line)


# 3 追記モードでデータ追加 ---------------------------------------------

# ＜ポイント＞
# - 追記モードではmodeをバイナリモードの場合は"ab"とする


# 準備：ファイル作成
data = 'こんにちは\nさようなら'
with gzip.open('gzip/text2.txt.gz', mode='wb') as f:
    f.write(data.encode('utf-8'))

# ファイルに追記
with gzip.open('gzip/text2.txt.gz', mode='ab') as f:
    f.write('さようなら\nお疲れ様です。'.encode('utf-8'))

# 確認
with gzip.open('gzip/text2.txt.gz', mode='rt', encoding='utf-8') as f:
    while (line := f.readline()):
        print(line)
