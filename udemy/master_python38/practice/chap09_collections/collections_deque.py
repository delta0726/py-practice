# ******************************************************************************
# Course      : Python3.8マスター講座
# Chapter     : 9 標準ライブラリ（collections）
# Theme       : collections（dequeモジュール）
# Creat Date  : 2022/2/14
# Final Update:
# URL         : https://www.udemy.com/course/python-python/
# ******************************************************************************


# ＜概要＞
# - リストと似たオブジェクトだが処理時間が速いのが特徴


# ＜参考＞
# 公式ドキュメント
# https://docs.python.org/ja/3/library/collections.html


# ＜目次＞
# 0 準備
# 1 オブジェクトの作成
# 2 リストとの処理時間の違い


# 0 準備 ---------------------------------------------------

# ライブあり
from collections import deque
from time import time


# 1 オブジェクトの作成 ----------------------------------------

# ＜ポイント＞
# - dequeはリストと似たオブジェクトでメソッドも似たものが多い


# オブジェクト定義
q = deque([1, 2, 3, 4])
print(q)

# 最後の要素を取得
# --- 元のオブジェクトから削除される
q = deque([1, 2, 3, 4])
print(q.pop())
print(q)

# 最初の要素を取得
# --- 元のオブジェクトから削除される
q = deque([1, 2, 3, 4])
print(q.popleft())
print(q)

# 要素の追加
q = deque([1, 2, 3, 4])
q.append(5)
q.appendleft(10)
print(q)

# リストに変換
print(list(q), type(list(q)))


# 2 リストとの処理時間の違い ----------------------------------------

# ＜ポイント＞
# - 処理時間に違いがあるとされるが実測値は変わらないようだ


# パラメータ設定
LOOP_COUNT = 5000000

# オブジェクト定義
# --- いずれかを選択
q = deque([1, 2, 3, 4])
q = [1, 2, 3, 4]

# 要素の追加
start_time = time()
for x in range(LOOP_COUNT):
    q.append(x)
mid_time = time()
print('append time: {}'.format(mid_time - start_time))

# 要素の削除
for _ in range(LOOP_COUNT):
    tmp = q.pop()
pop_time = time()
print('pop time: {}'.format(pop_time - mid_time))

# 要素の挿入
for x in range(LOOP_COUNT):
    q.insert(x, x)

end_time = time()
print('insert time: {}'.format(end_time - pop_time))
