# ******************************************************************************
# Course      : アルゴリズム・データ構造・コーディングテスト入門
# Chapter     : 3 ソート
# Theme       : Combソート
# Creat Date  : 2022/3/6
# Final Update:
# URL         : https://www.udemy.com/course/python-algo/
# ******************************************************************************


# ＜概要＞
# - Combソートのアルゴリズムを学ぶ（Combとは｢くし｣のことを指す）


# ＜Combソート＞
# - Gapという概念を使って並び替え対象を選択する
#   --- Gap1 = len(List) / 1.3 ⇒ Gap2 = Gap1 / 1.3
#   --- 隣同士で並び替えるのではなく、Gap分だけ離れた箇所と並び替える
# - Gapが1になったらswappedがTrueにならなくなるまで並び替える


# ＜目次＞
# 0 準備
# 1 ソート関数の定義
# 2 実行


# 0 準備 ----------------------------------------------------------------------

# ライブラリ
from typing import List
import random


# 1 ソート関数の定義 --------------------------------------------------------------

def comb_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    gap = len_numbers
    swapped = True

    while gap != 1 or swapped:
        gap = int(gap / 1.3)
        if gap < 1:
            gap = 1

        swapped = False

        for i in range(0, len_numbers - gap):
            if numbers[i] > numbers[i + gap]:
                numbers[i], numbers[i + gap] = numbers[i + gap], numbers[i]
                swapped = True

    return numbers


# 2 実行 ------------------------------------------------------------------------

if __name__ == '__main__':
    # 例題の数字
    nums = [2, 9, 1, 8, 7, 3, 5]
    comb_sort(numbers=nums)

    # ランダムな数字
    nums = [random.randint(0, 1000) for _ in range(10)]
    comb_sort(numbers=nums)
