# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 11-12 数値について
# Creat Date  : 2022/8/19
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜目次＞
# 1 数値の変数格納と演算
# 2 複合代入演算子
# 3 べき乗
# 4 浮動小数点数
# 5 シフト演算とビット演算


# 1 数値の変数格納と演算 -----------------------------------------------

# ＜ポイント＞
# - printで返される値を考えてみよう
#   --- // は割り算で整数部分のみ出力
#   --- % は割り算で小数部分のみ出力


value = 1
print(value)
value = -2
print(value)
value = value + 4  # 2
print(value)
print(value * 4)  # 8
print(value / 3)  # 0.6666
value = 10
print(value // 3)  # 3
print(value % 3)  # 1


# 2 複合代入演算子 ----------------------------------------------------

# 加算
# --- value = value + 3
value = 1
value += 3

# 減算
# --- value = value - 2
value = 1
value -= 2

# 掛け算
# --- value = value * 2
value = 1
value *= 2

# 割り算
# --- value = value / 2
value = 1
value /= 2


# 3 べき乗 -------------------------------------------------------------

# 累乗
value = 2
print(value)
print(value ** 3)

# 4 浮動小数点数 ---------------------------------------------------------

# 浮動小数点数
# --- 小数点を付けて数値を定義
height = 175.5

# 確認
print(height)
print(type(height))

# 整数型
# --- 小数点を付けて数値を定義
height = 175
print(type(height))

# 浮動小数点数型(float)と整数型(int)の演算
height = 175.5
height2 = height + 10
print(height2)
print(type(height2))

# 5 シフト演算とビット演算 --------------------------------------------------

# シフト演算
value = 8  # 1000 => 0010
print(value >> 2)
print(value << 3)  # 1000 => 1000000

# ビット演算
print(12 & 21)  # 01100 and 10101 = 00100 => 4
print(12 | 21)  # 01100 or 10101 = 11101 => 29

value = 12
value &= 21  # value = value & 21
print(value)
