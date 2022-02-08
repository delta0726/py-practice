# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 71 ファイル入力
# Creat Date  : 2022/2/9
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜概要＞
# - ファイル入力の注意点を学ぶ
#   --- with文を使って入力する


# ＜目次＞
# 1 ファイル入力
# 2 セイウチ演算子を用いた読込
# 3 with文を使った読込


# 1 ファイル入力 ------------------------------------------------------------


# ファイル入力設定
file_path = 'resources/input.csv'
f = open(file_path, mode='r', encoding='utf-8')

# ファイル読み込み
line = f.read()
print(line)

# ファイル読み込み
# --- 改行区切りを表示
lines = f.readlines()
print(lines)

# 改行コードを削除して表示
for x in lines:
    print(x.rstrip('\n'))

# ファイルを閉じる
f.close()


# 2 セイウチ演算子を用いた読込 ---------------------------------------------------------

# ファイル入力設定
file_path = 'resources/input.csv'
f = open(file_path, mode='r', encoding='utf-8')

# ファイル読み込み
# --- ジェネレータを利用
while line:
    print(line.rstrip('\n'))
    line = f.readline()

# ファイル読み込み
# --- セイウチ演算子を利用
while (line := f.readline()):
    print(line.rstrip('\n'))

# ファイルを閉じる
f.close()


# 3 with文を使った読込 ------------------------------------------------------------

# ＜ポイント＞
# - 開いたファイルをclose()することを忘れないようにwith文でファイルを開く
#   --- with文を出るとファイルが自動的に閉じられる
#   --- メモリ消費や書き込みエラーの予防


# ファイルを開く
with open(file_path, mode='r', encoding='utf-8') as f:
    lines = f.readlines()
    print(lines)

# 再度ファイルを読込む
# --- エラー（with文を出て既に閉じられている）
print(f.read())
