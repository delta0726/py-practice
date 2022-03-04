# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 51-52 リスト内包表記
# Creat Date  : 2022/2/5
# Final Update: 2022/3/4
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜内包表記とは＞
# - ループと条件文を用いて1行でリスト等を定義したい場合に用いる
#   --- 処理素行殿向上や可読性向上が見込める


# ＜目次＞
# 1 リストの書換
# 2 規則性のあるデータの生成
# 3 辞書からアイテムを取り出してリスト作成
# 4 さまざまな内包表記
# 5 内包表記の条件に関数を適用する


# 1 リストの書換 -----------------------------------------------------

# タプル定義
list_a = (1, 2, 3, 'a', 4, 'b')

# リスト内包表記で書換え
# --- 数値のみ抽出して2倍する
list_b = [x * 2 for x in list_a if type(x) == int]

# 確認
print(list_b)


# 2 規則性のあるデータの生成 ---------------------------------------------

# ＜ポイント＞
# - リスト内包表記は規則性のあるデータを生成するのに適している
#   --- 1行で記述できるのでコードがスッキリする

# リスト作成
# --- 0-99で7の倍数のみの値をリスト化
list_c = [x for x in range(100) if x % 7 == 0]

# 確認
print(list_c)


# 3 辞書からアイテムを取り出してリスト作成 --------------------------------

# データ定義
list_a = (1, 2, 3, 'a', 4, 'b')

# 辞書の定義
dict_a = {
    'a': 'Apple',
    'b': 'Banana'
}

# リスト作成
# --- データに応じてキーを探してアイテムを抽出
list_c = [dict_a.get(x) for x in list_a if type(x) == str]

# 確認
print(list_c)


# 4 さまざまな内包表記 -------------------------------------------------

# ジェネレータ内包表記
# --- パレンティス
list_a = (x for x in range(10))
print(list_a)
print(type(list_a))

# タプル内包表記
# --- tuple & パレンティス
list_a = tuple(x for x in range(10))
print(list_a)
print(type(list_a))

# セット内包表記
# --- ブレース
list_a = {x for x in range(10)}
print(list_a)
print(type(list_a))


# 5 内包表記の条件に関数を適用する ----------------------------------------

# ＜ポイント＞
# - 内包表記に関数を適用することで表現に幅を持たせることができる


# 関数定義
def func(n):
    for x in range(2, n):
        if n % x == 0:
            return True
    return False


def calc_power(x):
    return x ** 2


# リスト作成
# --- 関数は条件文にも出力にも適用することが可能
list_a = [x for x in range(100) if func(x) == False]
list_b = [calc_power(x) for x in range(100) if func(x) == False]

# 確認
print(list_a)
print(list_b)
