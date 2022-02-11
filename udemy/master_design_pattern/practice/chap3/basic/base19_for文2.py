# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 19 for2
# Creat Date  : 2022/2/11
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜概要＞
# - for文とセットで用いられる関数としてenumerate/zipがある


# ＜目次＞
# 1 enumerate関数
# 2 zip関数


# 1 enumerate関数 --------------------------------------------------

# ＜ポイント＞
# - enumerate()は要素の抽出と併せてカウンタを返す
#   --- (index, value)


# リスト定義
fruits = ['grape', 'Pine', 'Apple']

# ループ
for index, value in enumerate(fruits):
    print('index = {}'.format(index))
    print('value = {}'.format(value))


# 2 zip関数 --------------------------------------------------------

# ＜ポイント＞
# - zip()は複数のオブジェクトから要素を抽出する


# リスト定義
classA = ['Taro', 'Hanako', 'Jiro']
classB = ['Katsuo', 'Wakame', 'Taro']

# ループ
for A, B in zip(classA, classB):
    print('classA student: {}'.format(A))
    print('classB student: {}'.format(B))


# 3 while文 -------------------------------------------------------

# カウンタ定義
count = 0

# countが10より小さい場合は中の処理を実行
while count < 10:
    print(count)
    count += 1
