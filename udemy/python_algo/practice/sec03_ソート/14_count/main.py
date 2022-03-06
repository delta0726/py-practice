# ******************************************************************************
# Course      : アルゴリズム・データ構造・コーディングテスト入門
# Chapter     : 3 ソート
# Theme       : Countソート
# Creat Date  : 2022/3/6
# Final Update:
# URL         : https://www.udemy.com/course/python-algo/
# ******************************************************************************


# ＜概要＞
# - Countソートのアルゴリズムを学ぶ


# ＜Countソート＞
# - 動画確認（少しわかりにくい）
# - 配列の最大値だけのリストを用意するためメモリを消費する傾向にある


# ＜目次＞
# 0 準備
# 1 ソート関数の定義
# 2 実行


# 0 準備 ----------------------------------------------------------------------

# ライブラリ
from typing import List
import random


# 1 ソート関数の定義 ------------------------------------------------------------

def counting_sort(numbers: List[int]) -> List[int]:
    max_num = max(numbers)
    counts = [0] * (max_num + 1)
    result = [0] * len(numbers)

    for num in numbers:
        counts[num] += 1
    
    for i in range(1, len(counts)):
        counts[i] += counts[i-1]

    i = len(numbers) - 1
    while i >= 0:
        index = numbers[i]
        result[counts[index]-1] = numbers[i]
        counts[index] -= 1
        i -= 1

    return result


# 2 実行 ------------------------------------------------------------------------

if __name__ == '__main__':
    # 例題の数字
    nums = [4, 3, 6, 2, 3, 4, 7]
    counting_sort(numbers=nums)

    # ランダムな数字
    nums = [random.randint(0, 1000) for _ in range(10)]
    counting_sort(numbers=nums)
