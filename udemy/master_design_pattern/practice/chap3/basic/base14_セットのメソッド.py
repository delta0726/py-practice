# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 14 セットのメソッド
# Creat Date  : 2022/2/11
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜ポイント＞
# - セットは集合演算のメソッドを持つ


# ＜目次＞
# 1 和集合(union)
# 2 積集合(intersection)
# 3 差集合(difference)
# 4 対象差(symmetric_difference)
# 5 判定メソッド


# 1 和集合(union) -------------------------------------------------------

# ＜ポイント＞
# - 和集合はパイプ(|)かunionメソッドで表現する


# セットの定義
s = {'a', 'b', 'c', 'd'}
t = {'c', 'd', 'e', 'f'}

# 和集合
u = s | t
u = s.union(t)

# 確認
print(u)


# 2 積集合(intersection) -------------------------------------------

# ＜ポイント＞
# - 積集合はアンド(&)かintersectionメソッドで表現する


# セットの定義
s = {'a', 'b', 'c', 'd'}
t = {'c', 'd', 'e', 'f'}

# 積集合
u = s & t
u = s.intersection(t)

# 確認
print(u)


# 3 差集合(difference) ---------------------------------------------

# ＜ポイント＞
# - 積集合はマイナス(-)かdifferenceメソッドで表現する


# セットの定義
s = {'a', 'b', 'c', 'd'}
t = {'c', 'd', 'e', 'f'}

# 差集合
u = s - t
u = s.difference(t)

# 確認
print(u)


# 4 対象差(symmetric_difference) ---------------------------------

# ＜ポイント＞
# - 対象差はハット(^)symmetric_differenceメソッドで表現する
#   --- どちらか一方に含まれる


# セットの定義
s = {'a', 'b', 'c', 'd'}
t = {'c', 'd', 'e', 'f'}

# 対象差
u = s ^ t
u = s.symmetric_difference(t)
print(u)

# 要素の追加
# --- s = s | t => sがsとtの和集合 => sにtの要素が入る
s |= t
print(s)


# 5 判定メソッド ---------------------------------------------------

# セットの定義
s = {'apple', 'banana'}
t = {'apple', 'banana', 'lemon'}
u = {'cherry'}

# 別の集合の要素に含まれているか
# --- subset
print(s.issubset(t))

# 別の集合の要素を全て含んでいるか
# --- superset
print(s.issuperset(t))
print(t.issuperset(s))

# 重複要素はないか
# --- disjoint
print(t.isdisjoint(s))
print(t.isdisjoint(u))
