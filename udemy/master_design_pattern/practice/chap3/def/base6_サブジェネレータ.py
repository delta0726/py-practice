# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       :
# Creat Date  : 2022//
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# サブジェネレータ

def sub_sub_generator():
    yield "Sub Subのyield"
    return "sub sub のreturn"

def sub_generator():
    yield "subのyield"
    res = yield from sub_sub_generator()
    print("sub res = {}".format(res))
    return "subのreturn"

def generator():
    yield "generatorのyield"
    res = yield from sub_generator()
    print('gen res = {}'.format(res))
    return 'generatorのreturn'


# インスタンス生成
gen = generator()

# 実行
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
