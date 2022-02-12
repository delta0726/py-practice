# ******************************************************************************
# Course      : Python3.8マスター講座
# Chapter     : 6 基本的な標準ライブラリ
# Theme       : mathモジュール
# Creat Date  : 2022/2/13
# Final Update:
# URL         : https://www.udemy.com/course/python-python/
# ******************************************************************************


# ＜概要＞
# - 基本的な数学関数を提供する
#   --- 統計関数などは含まれずベースとなる数学関数のみを提供
#   --- よって、関数の数自体は多くない


# ＜参考＞
# 公式ドキュメント
# https://docs.python.org/ja/3/library/math.html


# ＜目次＞
# 0 準備
# 1 標準ライブラリの数学関数
# 2 mathモジュールの数学関数


# 0 準備 --------------------------------------------------------

# ライブラリ
import math


# 1 デフォルトで使用可能な数学関数 ------------------------------------

# ＜ポイント＞
# - デフォルトで使用可能な数学関数があるがごくわずか
#   --- max, min, sumくらい


# リスト作成
list_a = [1, 2, 3, 4]

# 数学演算
# --- 最大値
# --- 最小値
# --- 合計
print(max(list_a))
print(min(list_a))
print(sum(list_a))


# 2 mathモジュールの数学関数 ----------------------------------------

# ＜ポイント＞
# - 基本的な数学関数が提供される
#   --- 関数の数は少ないのでざっくり押さえておけば十分


# 切り上げ
print(math.ceil(12.3))

# 切り下げ
print(math.floor(12.3))

# 絶対値
print(math.fabs(-12))

# 最大公約数
print(math.gcd(12, 15))

# 合計値
# --- イテラブル中の値の浮動小数点数の正確な和を返す
# --- 以下の計算でsumは整数として扱うが、fsumは浮動小数点として扱う
list_b = [1, 2, 3, 4, 5]
print(sum(list_b))
print(math.fsum(list_b))

# 2のn乗
print(math.pow(2, 3))

# 2の平方根
print(math.sqrt(2))

# ネイピア数
print(math.e)

# 円周率
print(math.pi)

# eの3乗
print(math.exp(3))

# 自然対数
print(math.log(5))

# 10の対数
print(math.log10(100))

# 対数
print(math.log(8, 2))

# 三角関数
# --- sin
# --- cos
# --- tan
# --- degrees
# --- randians
print(math.sin(math.pi / 2))  # 1
print(math.cos(math.pi / 2))  # 0
print(math.tan(math.pi / 4))  # 1
print(math.degrees(math.pi))  # 180
print(math.radians(180))  # π
