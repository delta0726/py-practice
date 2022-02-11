# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 演習問題1
# Creat Date  : 2022/2/12
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# 1 numという変数に数値の10を入れてください
num = 10

# 2 numの型を標準出力してください
# --- 標準出力はprintのこと
print(type(num))

# 3 2のnumを文字列に変換してnum_strという変数に入れてください
num_str = str(num)

# 4 リスト num_list に num_strと'20'と'30'を入れてください
num_list = [num_str, '20', '30']
print('num_list = {}'.format(num_list))

# 5 num_list から新たな要素'40'を入れてください
num_list.append('40')

# 6 num_listをタプルに変換してnum_tupleに格納してください
num_tuple = tuple(num_list)

# 7 標準入力を受け付けてnum_tupleに受け付けた標準入力を追加してください
# --- 標準入力はinput()で定義する
val = input()
num_tuple += (val,)

# 8 セットでnum_setを作成してください。中身は ’40’,’50’,'60'としてください
num_set = {'40', '50', '60'}
print('num_tuple = {}'.format(num_tuple))
print('num_set = {}'.format(num_set))

# 9 num_tupleとnum_setのユニオン(和集合)を表示してください
print(set(num_tuple) | num_set)

# 10 辞書型num_dictをキー(num_tuple) と値(num_str)として作成してください
num_dict = {
    num_tuple: num_str
}

# 11 リスト(num_list)の長さを表示してください
print(len(num_list))

# 12 num_dictからキー(MyKey)を取り出してください
# 見つからない場合は‘ Does not exist’ を返すようにして標準出力してください
print(num_dict.get('MyKey', 'Does not exist'))

# 13 リスト(num_list)に新たに ‘50’,’60'を一行で追加してください
num_list.extend(['50', '60'])
print('num_list = {}'.format(num_list))

# 14 標準入力を受け付け、 is_under_50 という論理型変数に標準入力が 50 より 小さいかどうかを 入れてください
val = input()
is_under_50 = int(val) < 50
print('is_under_50 = {}'.format(is_under_50))

# 15 num_str = num_str の値 として標準出力してください
print(f'num_str = {num_str}')

# 16 num_dict が持っているメソッドを標準出力してください
print(dir(num_dict))
