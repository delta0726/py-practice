# ******************************************************************************
# Course      : アルゴリズム・データ構造・コーディングテスト入門
# Chapter     : 3 ソート
# Theme       : Bogoソート
# Creat Date  : 2022/3/5
# Final Update:
# URL         : https://www.udemy.com/course/python-algo/
# ******************************************************************************


# ＜概要＞
# - Bogoソートのアルゴリズムを学ぶ
# - for文の処理を内包表記とall関数で簡素化する
# - 型ヒントの書き方を学ぶ


# ＜Bogoソート＞
# - 乱数で配列を並び替えて並び替え条件の並び方と一致するまでループ処理する
#   --- 処理速度は乱数の出方に依存する（安定しない）
#   --- 処理速度がリストに格納されている数字の大きさに異存する（探索範囲が広くなる）


# ＜参考＞
# typing --- 型ヒントのサポート
# https://docs.python.org/ja/3/library/typing.html


# ＜目次＞
# 0 準備
# 1 ソート関数の定義
# 2 実行


# 0 準備 ----------------------------------------------------------------------

# ライブラリ
import random
from typing import List


# 1 ソート関数の定義 -----------------------------------------------------------

# 並び替えチェック
# --- 要素比較でi+1まで見ているのでループはi-1まででよい
def in_order(numbers: List[int]) -> bool:
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i+1]:
            return False
    return True


# 並び替えチェック
# --- 要素比較でi+1まで見ているのでループはi-1まででよい
def in_order_2(numbers: List[int]) -> bool:
    return all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-1))


# 動作チェック
# all([numbers[i] <= numbers[i+1] for i in range(len(numbers)-1)])


# 配列のシャッフル
# --- 条件文にin_order()を使用してFalseの場合には回し続ける
def bogo_sort(numbers: list) -> List[int]:
    while not in_order_2(numbers):
        random.shuffle(numbers)
    return numbers


# 2 実行 ---------------------------------------------------------------------

if __name__ == '__main__':
    # 小規模なリスト
    print(bogo_sort(numbers=[1, 5, 3, 2, 4]))

    # 大規模なリスト
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(nums)
    print(bogo_sort(numbers=nums))
