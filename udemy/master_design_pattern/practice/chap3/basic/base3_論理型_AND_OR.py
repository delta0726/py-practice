# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 10 論理型、AND、OR
# Creat Date  : 2022/1/28
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜目次＞
# 1 単一条件の論理判定
# 2 複数条件の論理判定


# 1 単一条件の論理判定 ----------------------------------

# 論理型
is_animal = False
if is_animal:
    print('動物です')


# 2 複数条件の論理判定 ----------------------------------

# パラメータ設定
is_man = False
is_adult = True

# or文
if is_man or is_adult:
    print('男か大人です')     # Trueなので実行される

# and文
if is_man and is_adult:
    print('成人男性です')     # Falseなので実行されない