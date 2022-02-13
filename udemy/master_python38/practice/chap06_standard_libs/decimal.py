# ******************************************************************************
# Course      : Python3.8マスター講座
# Chapter     : 6 基本的な標準ライブラリ
# Theme       : decimal
# Creat Date  : 2022/2/13
# Final Update:
# URL         : https://docs.python.org/ja/3/library/decimal.html
# ******************************************************************************

# ＜概要＞
# - decimalモジュールは小数点以下の数値を厳密に扱うための仕組みを提供する
#   --- パソコンは2進数計算なので非常に小さい桁で誤差が生じる
#   --- 厳密性が必要なシステムで使用する


# ＜参考＞
# 公式ドキュメント
# https://docs.python.org/ja/3/library/datetime.html


# ＜目次＞
# 0 準備
# 1 小数点以下の計算における誤差
# 2 decimalモジュールによる誤差の回避
# 3 decimalのデータ型を変換
# 4 decimalを用いた演算
# 5 decimalの四捨五入


# 0 準備 ---------------------------------------------------

# ライブラリ
from decimal import Decimal, ROUND_DOWN, ROUND_UP, ROUND_HALF_UP


# 1 小数点以下の計算における誤差 ------------------------------

# ＜ポイント＞
# - コンピュータの演算では非常に小さな誤差が生じるケースがある
#   --- 単独では影響が少ないが、掛け算などで誤差が拡張するケースには要注意


# 初期値の指定
float_sum = 0.0

# 1.01を100回加算する
float_num = 1.01
for _ in range(100):
    float_sum += float_num

# 確認
print(f'float_sum = {float_sum}')


# 2 decimalモジュールによる誤差の回避 ----------------------------------

# 初期値の指定
decimal_sum = Decimal('0.0')

# 1.01を100回加算する
decimal_num = Decimal('1.01')
for _ in range(100):
    decimal_sum += decimal_num

# 確認
print(f'decimal_sum = {decimal_sum}')


# 3 decimalのデータ型を変換 ---------------------------------------------

# decimalの定義
decimal_num = Decimal('1.01')
decimal_val = Decimal('2.02')

# データ型の変換
float_val = float(decimal_val)
str_val = str(decimal_val)

# 確認
print(type(float_val), float_val)
print(type(str_val), str_val)


# 4 decimalを用いた演算 ---------------------------------------------

# decimalの定義
decimal_num = Decimal('1.01')
decimal_val = Decimal('2.02')

# Decimalを用いた演算
print(decimal_num / decimal_val)
print(decimal_num * decimal_val)
print(decimal_num + decimal_val)
print(decimal_num - decimal_val)


# 5 decimalの四捨五入 -------------------------------------------

# decimalの定義
decimal_val = Decimal('87.325')

# 切り下げ
print(decimal_val.quantize(Decimal('0.0'), rounding=ROUND_DOWN))

# 四捨五入
print(decimal_val.quantize(Decimal('0.0'), rounding=ROUND_HALF_UP))

# 切り上げ
print(decimal_val.quantize(Decimal('0.0'), rounding=ROUND_UP))
