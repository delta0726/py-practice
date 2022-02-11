# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 10 辞書
# Creat Date  : 2022/2/11
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜概要＞
# - 辞書はブレース({})で定義する
# - リストはキーと値をセットで持つ
# - キーと値はデータ型が統一されている必要はない


# ＜目次＞
# 1 辞書の値を抽出
# 2 各種一覧の取得
# 3 for文で辞書をループ
# 4 if文でキーの存在を確認


# 1 辞書の値を抽出 ----------------------------------------------

# 辞書の定義
car = {'brand': 'Toyota', 'model': 'Prius', 'year': 2015, 1: 100}

# キーを指定して値を抽出
# --- ブラケットで抽出
# --- キーが存在しない場合はエラーとなる
print(car['brand'])
print(car['bran'])


# キーを指定して値を抽出
# --- getメソッドで抽出
# --- 値が存在しなかった場合の戻り値を指定（指定が無ければNoneが返される）
print(car.get('brand', 12))
print(car.get('bran', 'Does not exist'))
print(car.get('bran', 12))
print(car.get('bran'))

# キーは数値でも可能
car.get(1)


# 2 各種一覧の取得 -------------------------------------------------

# ＜ポイント＞
# - 各種を取得するメソッドがある
# - 独自のクラスで値を返す


# 辞書の定義
car = {'brand': 'Toyota', 'model': 'Prius', 'year': 2015, 1: 100}

# キー一覧
print(car.keys())
print(type(car.keys()))

# 値一覧
print(car.values())
print(type(car.values()))

# キー + 値
print(car.items())
print(type(car.items()))


# 3 for文で辞書をループ ---------------------------------------

# キーとアイテムの表示
for k, v in car.items():
    print('key = {}, value = {}'.format(k, v))


# 4 if文でキーの存在を確認 -------------------------------------

# キーの存在を確認して処理
if 'brand' in car:
    print('carのブランドは{}'.format(car['brand']))
else:
    print('キーが存在しません')
