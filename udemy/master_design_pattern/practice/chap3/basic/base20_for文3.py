# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 20 if文3
# Creat Date  : 2022/2/11
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜概要＞
# - for文をカスタマイズする記法(continue/braek/else)を確認


# ＜目次＞
# 1 continue
# 2 break
# 3 else
# 4 while文の場合


# 1 continue --------------------------------------------

# ＜ポイント＞
# - continue文を実行すると処理を中断してカウンタを1つ更新する


# ループ処理
for i in range(10):
    if i == 3:
        continue
    print(i)


# 2 else --------------------------------------------

# ＜ポイント＞
# - for文にelseを指定するとループ終了時に実行される


# ループ処理
for i in range(10):
    if i == 3:
        continue
    print(i)
else:
    print('ループ処理終了')


# 3 break -----------------------------------------------

# ＜ポイント＞
# - break文を実行すると処理を中断してループから出る
#   --- for文のelseは実行されない


# ループ処理
for i in range(10):
    if i == 5:
        break
    print(i)
else:
    print('ループ処理終了')


# 4 while文の場合 -----------------------------------------------

# ＜ポイント＞
# - for文の場合と同じルールで適用される


# 変数定義
num = 0

# ループ処理
while num < 10:
    if num == 5:
        num += 1
        continue
    # if num == 7:
    #     break
    print(num)
    num += 1
else:
    print('whileループ終了')
