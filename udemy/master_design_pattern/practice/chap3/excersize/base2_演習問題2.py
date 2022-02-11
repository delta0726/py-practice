# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 演習問題2
# Creat Date  : 2022/2/12
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜概要＞
# - for文と条件文を使った演習


# ＜問題＞
# - 数値を1-100までループさせる
# - 3と5の倍数の場合はFizz Buzzを表示
# - 3の倍数の場合はFizz、5の倍数の場合はBuzzを表示
# - それ以外は数値を表示


for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('{}: Fizz Buzz'.format(i))
    elif i % 3 == 0:
        print('{}: Fizz'.format(i))
    elif i % 5 == 0:
        print('{}: Buzz'.format(i))
    else:
        print(i)
