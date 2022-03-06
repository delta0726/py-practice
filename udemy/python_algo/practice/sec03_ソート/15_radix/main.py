# ******************************************************************************
# Course      : アルゴリズム・データ構造・コーディングテスト入門
# Chapter     : 3 ソート
# Theme       : Radixソート
# Creat Date  : 2022/3/6
# Final Update:
# URL         : https://www.udemy.com/course/python-algo/
# ******************************************************************************


# ＜概要＞
# - Radixソートのアルゴリズムを学ぶ


# ＜Radixソート＞
# - 動画確認


# ＜目次＞
# 0 準備
# 1 Countingソート
# 2 ソート関数の定義
# 3 実行


# 0 準備 ----------------------------------------------------------------------

# ライブラリ
from typing import List
import random


# 1 Countingソート ------------------------------------------------------------

# ＜ポイント＞
# - 前回のものをカスタマイズ


def counting_sort(numbers: List[int], place: int) -> List[int]:
    counts = [0] * 10
    result = [0] * len(numbers)

    for num in numbers:
        index = int(num / place) % 10
        counts[index] += 1

    for i in range(1, 10):
        counts[i] += counts[i - 1]

    i = len(numbers) - 1
    while i >= 0:
        index = int(numbers[i] / place) % 10
        result[counts[index] - 1] = numbers[i]
        counts[index] -= 1
        i -= 1

    return result


# 2 ソート関数の定義 -------------------------------------------------------------

def radix_sort(numbers: List[int]) -> List[int]:
    max_num = max(numbers)
    place = 1
    while max_num > place:
        numbers = counting_sort(numbers=numbers, place=place)
        place *= 10
    return numbers


# 3 実行 ------------------------------------------------------------------------

if __name__ == '__main__':
    # 例題の数字
    nums = [4, 3, 6, 2, 3, 4, 7]
    radix_sort(numbers=nums)

    # ランダムな数字
    nums = [random.randint(0, 1000) for _ in range(10)]
    radix_sort(numbers=nums)
