# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 19-21 リスト
# Creat Date  : 2022/2/10
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜概要＞
# - リストはブラケット([])で定義する
# - リストは箱の中に複数のオブジェクトを格納することができる（異なるデータ型も可能）
# - リスとの中にリストを格納したり、他のオブジェクトを格納することもできる


# ＜目次＞
# 1 リストの定義
# 2 多重リストの作成
# 3 リスト要素の更新
# 4 リストのスライス


# 1 リストの定義  -----------------------------------------------

# リストの作成
list_a = [1, 2, 3, 4]
list_b = []

# 確認
print(list_a)
print(list_a[-2])


# 2 多重リストの作成 ------------------------------------------

# リストの作成
list_a = [1, [1, 2, 'apple'], 3, 'banana']

# 確認
print(list_a)
print(list_a[1][2])


# 3 リスト要素の更新 ------------------------------------------

# リスト定義
list_a = [1, [1, 2, 'apple'], 3, 'banana']

# 要素の更新
list_a[1][2] = 'lemon'

# 確認
print(list_a)


# 4 リストのスライス --------------------------------------------

# ＜ポイント＞
# - スライスはリストに限らずルールは一緒になっている


# リスト定義
list_a = [1, 2, 3, 4, 5]

# リストのスライス
list_b = list_a[:3]

# 確認
print(list_b)
print(list_a[0:5:2])


# 5 リストのメソッド ---------------------------------------------

# ＜ポイント＞
# - リストの持つメソッドは限られているので全て覚えておくとよい


# 要素の追加(append)
# --- 末尾に要素を追加する
list_a = [1, 2, 3, 4, 5]
list_a.append('apple')
print(list_a)

# リストの拡張(extend)
# --- 指定したリストを末尾に結合する（1つのリストとして定義される）
list_a = [1, 2, 3, 4, 5]
list_a.extend(['banana', 'lemon'])
print(list_a)

# 特定の位置に要素を挿入(insert)
list_a = [1, 2, 3, 4, 5]
list_a.insert(1, 'grape')
print(list_a)

# リストのクリア（clear）
# --- 空のリストオブジェクトのみが残る
list_a = [1, 2, 3, 4, 5]
list_a.clear()
print(list_a)

# 特定要素の削除（remove）
# --- 指定した要素で最も左にあるものが削除される
# --- リストに指定した要素が無ければエラーとなる
list_a = [0, 1, 2, 2, 3, 3, 3, 4, 5]
list_a.remove(3)
print(list_a)

# 要素の取り出し（pop）
list_a = [0, 1, 2, 2, 3, 3, 3, 4, 5]
value = list_a.pop(1)
print(list_a)

# 要素数のカウント（count）
list_a = [0, 1, 2, 2, 3, 3, 3, 4, 5]
print(list_a.count(3))

# 要素の検索（index）
# --- 指定した要素の最初のインデックスを取得
list_a = [0, 1, 2, 2, 3, 3, 3, 4, 5]
print(list_a.count(1))

# 要素の並び替え（sorted関数）
# --- abcや123の順番で並び替える（降順も可能）
list_a = ['banana', 'lemon', 'apple', 'grape']
list_a = sorted(list_a)
print(list_a)

# 要素の逆順並び替え
list_a = ['banana', 'lemon', 'apple', 'grape']
list_a.reverse()
print(list_a)


# 6 コピーと参照の違い -----------------------------------

# ＜ポイント＞
# - コピー(copy)もメソッドの1つだが参照と混同しやすいので注意が必要


# リストのコピー（copy）
# --- コピーすると別のidを持つのでリストの変更の影響を受けない
list_a = [0, 1, 2, 2, 3, 3, 3, 4, 5]
list_b = list_a.copy()
print(list_b)
list_b[0] = 'AAAAA'
print(list_a)
print(id(list_a), id(list_b))

# リストの参照
# --- 参照したリストに操作を加えるとそれぞれ影響を受ける
list_a = [0, 1, 2, 2, 3, 3, 3, 4, 5]
list_b = list_a
print(list_b)
list_b[0] = 'AAAAA'
print(list_a)
print(id(list_a), id(list_b))
