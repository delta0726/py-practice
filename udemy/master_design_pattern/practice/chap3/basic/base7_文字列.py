# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 15-17 文字列
# Creat Date  : 2022/1/28
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜目次＞
# 1 文字列の基本操作
# 2 エンコードとデコード
# 3 文字列クラスのメソッド
# 4 文字列の応用操作


# 1 文字列の基本操作 -------------------------------------------------

# 文字列の定義
fruit = 'apple'
print(fruit)
print(type(fruit))

# 文字列の繰り返し連結
# --- 言語によっては対応していないものも多い
print(fruit * 10)

# 文字列同士の連結
# --- +演算子の前後が文字列である必要がある
new_fruit = fruit + ' banana'
print(new_fruit)

# 文字列を改行して格納
# --- 改行キーが自動的に含まれる
fruits = """apple
banana
grape
"""
print(fruits)

# 文字列をブラケットで抽出
fruit = 'banana'
print(fruit[2])
print(fruit[-2])


# 2 エンコードとデコード -------------------------------------------------

# ＜ポイント＞
# - 文字列を数値として扱いたい場合に使用する

# エンコード
# encode, decode(bytes[]型の関数) => bytes[]
byte_fruit = fruit.encode('utf-8')
print(byte_fruit)
print(type(byte_fruit))

# デコード
str_fruit = byte_fruit.decode('shift-jis')
print(str_fruit)
print(type(str_fruit))


# 3 文字列クラスのメソッド ------------------------------------------------

# count
# --- 文字列から指定した文字パターンの個数を出力
msg = 'ABCDEABC'
print(msg.count('ABC'))
print(msg.count('ABCDEF'))

# startswith / endswith
# --- 文字列のパターンが一致しているかでTrue/Falseを返す
msg = 'ABCDEABC'
print(msg.startswith('ABCD'))
print(msg.startswith('BCD'))
print(msg.endswith('ABC'))
print(msg.endswith('FABA'))

# strip, rstrip, lstrip
# --- 文字列から指定した文字を削除する
# --- 指定文字は1文字ずつ独立して評価する
msg = 'ACB'
print(msg)
print(msg.strip('AC'))
print(msg.strip('CA'))
print(msg.rstrip('AC'))
print(msg.lstrip('AC'))

# upper, lower, swapcase
# --- swapcaseは大文字と小文字を入れ替える
msg = 'abcABC'
msg_u = msg.upper()
msg_l = msg.lower()
msg_s = msg.swapcase()

# replace
# --- 第3引数は置き換える最大オカレンス数（デフォルトは-1で全て変換）
msg = 'ABCDEABC'
msg_1 = msg.replace('ABC', 'abc')
msg_2 = msg.replace('ABC', 'abc', 1)

# capitalize
# --- 先頭文字のみを大文字、その他は小文字に変換
msg = 'hELLO world'
print(msg.capitalize())


# 4 文字列の応用操作 -----------------------------------------------

# 文字列のインデックスによる抽出
msg = 'hello, my name is taro'
print(msg[:5])
print(msg[6:])
print(msg[1:6])
print(msg[1:10:1])

# format関数
# --- ブレースで囲った箇所に指定した文字を入力する
print('hello {}'.format('Taro'))

# f記法
# --- ブレースの中に指定した変数を文字として表示する
name = 'Jiro'
print(f'hello {name}')

# islower, isupper
# --- 大文字/小文字の判定
# --- 大文字と小文字が混じっている文字列はどちらもFalse
msg = 'h'
print(msg.isupper())
print(msg.islower())

msg = 'Apple'
print(msg.isupper())
print(msg.islower())

# find
# --- 左から一番最初に見つけた位置のインデックスを返す
msg = 'ABCDEABC'
print(msg.find('ABC'))
print(msg.find('CDE'))

# rfind
# --- 右から一番最初に見つけた位置のインデックスを返す
msg = 'ABCDEABC'
print(msg.rfind('ABC'))
print(msg.rfind('CDE'))

# index
# --- 右から一番最初に見つけた位置のインデックスを返す
msg = 'ABCDEABC'
print(msg.index('ABC'))
print(msg.index('CDE'))

# 文字列が存在しない場合の挙動
# --- findは-1を返す
# --- indexはエラーを返す
msg = 'ABCDEABC'
print(msg.find('ABCE'))
print(msg.index('ABCE'))
