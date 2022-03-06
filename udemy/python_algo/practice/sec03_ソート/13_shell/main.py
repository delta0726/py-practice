# ******************************************************************************
# Course      : アルゴリズム・データ構造・コーディングテスト入門
# Chapter     : 3 ソート
# Theme       : Shellソート
# Creat Date  : 2022/3/6
# Final Update:
# URL         : https://www.udemy.com/course/python-algo/
# ******************************************************************************


# ＜概要＞
# - Shellソートのアルゴリズムを学ぶ


# ＜Shellソート＞
# -


# ＜目次＞
# 0 準備
# 1 ソート関数の定義
# 2 実行


# 0 準備 --------------------------------------------------------------------

# ライブラリ
from typing import  List
import random


# 1 ソート関数の定義 ----------------------------------------------------------

def shell_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    gap = len_numbers // 2

    while gap > 0:
        for i in range(gap, len_numbers):
            temp = numbers[i]
            j = i
            while j >= gap and numbers[j-gap] > temp:
                numbers[j] = numbers[j-gap]
                j -= gap
            numbers[j] = temp
        gap //= 2

    return numbers


# 2 実行 -------------------------------------------------------------------

if __name__ == '__main__':
    # 例題の数字
    nums = [5, 6, 9, 2, 3]
    shell_sort(numbers=nums)

    # ランダムな数字
    nums = [random.randint(0, 1000) for _ in range(10)]
    shell_sort(numbers=nums)
