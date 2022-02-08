# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 72 ファイル出力
# Creat Date  : 2022/2/9
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜概要＞
# - ファイル出力の注意点を学ぶ
#   --- with文を使って入力する


# ＜目次＞
# 1 ファイル出力
# 2 with文を用いたファイル出力


# 1 ファイル出力 --------------------------------------------------------------

# ファイル出力設定
file_path = 'resources/output.csv'
f = open(file_path, mode='w', encoding='utf-8', newline='\n')

# ファイル書き込み
f.write('あああ\nいいい')

# ファイルを閉じる
f.close()


# 2 with文を用いたファイル出力 -------------------------------------------------

# ファイル出力設定
file_path = 'resources/output.csv'

# ファイル書き込み
with open(file_path, mode='a', encoding='utf-8', newline='\n') as f:

    # リスト定義
    list_a = [['A', 'B', 'C'], ['あ', 'い', 'う']]
    for x in list_a:
        f.write('\n')
        f.write(','.join(x))
    # f.writelines(list_a[0])
