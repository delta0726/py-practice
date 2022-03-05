# ******************************************************************************
# Course      : アルゴリズム・データ構造・コーディングテスト入門
# Chapter     : 3 ソート
# Theme       : Bubbleソート
# Creat Date  : 2022/3/5
# Final Update:
# URL         : https://www.udemy.com/course/python-algo/
# ******************************************************************************


# ＜概要＞
# - Bubbleソートのアルゴリズムを学ぶ


# ＜Bubbleソート＞
# - となり同士を比較して左の方が大きければ並び替える
# - リストの最大値は1回目のイテレーションで一番右端まで入れ替わっていく
# - 2回目のイテレーションはn-1回にすることで右端に最大値を集めていく（前回までの最大値が右端にあることが保証されるため）
# - 処理速度がリストに格納されている数字の大きさに異存ない


# ＜目次＞
# 0 準備
# 1 ソート関数の定義
# 2 実行


# 0 準備 ----------------------------------------------------------------------

# ライブラリ
from typing import List
import random


# 1 ソート関数の定義 -------------------------------------------------------------

# ＜ポイント＞
# - limitがイテレーションごとにiだけ減っていくことを表現する
#   --- range(len_numbers - 1 - i)


# 関数定義
def bubble_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        for j in range(len_numbers - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


# 2 実行 -----------------------------------------------------------------------

if __name__ == '__main__':
    # 小さい数字
    nums = [2, 5, 1, 8, 7, 3]
    bubble_sort(numbers=nums)

    # 大きい数字
    nums = [random.randint(0, 1000) for _ in range(10)]
    bubble_sort(numbers=nums)
