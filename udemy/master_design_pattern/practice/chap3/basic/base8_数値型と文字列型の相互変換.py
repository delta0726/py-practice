# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 18 数値型と文字列型の相互変換
# Creat Date  : 2022/1/28
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# int str 変換
int_num = 12
str_num = str(int_num)
print(str_num)
print(type(str_num))
float_num = -20.5
str_float = str(float_num)
print(str_float)
print(type(str_float))

# str => int, float
msg = '12'
int_msg = int(msg)
float_msg = float(msg)

print('value = {}, type = {}'.format(int_msg, type(int_msg)))
print('value = {}, type = {}'.format(float_msg, type(float_msg)))

