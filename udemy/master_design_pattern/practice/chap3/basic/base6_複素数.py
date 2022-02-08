# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 14 複素数
# Creat Date  : 2022/1/28
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜目次＞
# 1 複素数の定義
# 2 Complex関数で複素数の定義


# 1 複素数の定義 ------------------------------------------------

# 複素数

a = 1 + 3j
b = 3 + 5j
# print(a,b)
# print(a+b)
# print(a-b)
# print(a*b)

# 2 Complex関数で複素数の定義 ------------------------------------------------

a = complex(1, 3)
b = complex(3, 5)
print(a, b)
print(a + b)
print(a - b)
print(a * b)

print(a.real)
print(a.imag)
