# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 49 ラムダ式
# Creat Date  : 2022/2/5
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜ラムダ式とは＞
# - 1行で関数を定義したものをラムダ式という
#   --- 無名関数として定義することが多い（名前を付けることは可能）


# ＜目次＞
# 1 条件文を1行で記述する
# 2 ラムダ式
# 3 条件付きラムダ式


# 1 条件文を1行で記述する --------------------------------------------------

# ＜ポイント＞
# - ifと条件文を先に書くとイメージがわきやすい
#   --- ifの前がTure、elseの後がFalse


# 条件文
y = 10
x = 0 if (y - 20) > 0 else 1

# 確認
print(x)


# 2 ラムダ式 -------------------------------------------------------------

# ＜ポイント＞
# - ラムダ式は1行で記述することを除けば通常の関数と作法は同じ


# ラムダ式の定義
# --- 1つの引数のみの場合
lambda_a = lambda x: x * x

# 実行
print(lambda_a(10))


# ラムダ式の定義
# --- 複数の引数を持つ場合
# --- 初期値を指定することも可能
lambda_b = lambda x, y, z = 5: x * y * z

# 実行
print(lambda_b(2, 3))
print(lambda_b(2, 3, 4))


# 3 条件付きラムダ式 ----------------------------------------------------

# ＜ポイント＞
# - 条件文を含む関数も1行で記述することが可能


# 条件式付きlambda
lambda_c = lambda x, y: y if x < y else x

# 確認
print(lambda_c(6, 4))
