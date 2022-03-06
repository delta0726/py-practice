# ******************************************************************************
# Course      : アルゴリズム・データ構造・コーディングテスト入門
# Chapter     : 3 ソート
# Theme       : Insertionソート
# Creat Date  : 2022/3/6
# Final Update:
# URL         : https://www.udemy.com/course/python-algo/
# ******************************************************************************


# ＜概要＞
# - Insertionソートのアルゴリズムを学ぶ（挿入ソート）


# ＜Insertionソート＞
# - イテレーションを回しながら左の値と比較する
# - 隣の値が大きければテンポラリに格納して、backwardで適切な位置に戻す


# ＜目次＞
# 0 準備
# 1 ソート関数の定義
# 2 実行


# 0 準備 ----------------------------------------------------------------------

from typing import List
import random


# 1 ソート関数の定義 ------------------------------------------------------------

def insertion_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(1, len_numbers):
        temp = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > temp:
            numbers[j+1] = numbers[j]
            j -= 1

        numbers[j+1] = temp

    return numbers


# 2 実行 ------------------------------------------------------------------------

if __name__ == '__main__':
    # 例題の数字
    nums = [1, 7, 3, 2, 8, 5]
    insertion_sort(numbers=nums)

    # ランダムな数字
    nums = [random.randint(0, 1000) for _ in range(10)]
    insertion_sort(numbers=nums)


