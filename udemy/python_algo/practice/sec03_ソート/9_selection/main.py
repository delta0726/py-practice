# ******************************************************************************
# Course      : アルゴリズム・データ構造・コーディングテスト入門
# Chapter     : 3 ソート
# Theme       : Selectionソート
# Creat Date  : 2022/3/5
# Final Update:
# URL         : https://www.udemy.com/course/python-algo/
# ******************************************************************************


# ＜概要＞
# - Selectionソートのアルゴリズムを学ぶ


# ＜Selectionソート＞
# - イテレーションの開始位置の値をテンポラリで保持して以降の値と比較する
# - テンポラリの値より小さい値を見つけたら入れ替える


# ＜目次＞
# 0 準備
# 1 ソート関数の定義
# 2 実行


# 0 準備 ----------------------------------------------------------------------

# ライブラリ
from typing import List
import random


# 1 ソート関数の定義 ------------------------------------------------------------

def selection_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        min_idx = i
        for j in range(i + 1,  len_numbers):
            if numbers[min_idx] > numbers[j]:
                min_idx = j

        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

    return numbers


# 2 実行 -----------------------------------------------------------------------

if __name__ == '__main__':
    # 例題の数字
    nums = [1, 5, 2, 8, 7, 3]
    selection_sort(numbers=nums)

    # ランダムな数字
    nums = [random.randint(0, 1000) for _ in range(10)]
    selection_sort(numbers=nums)
