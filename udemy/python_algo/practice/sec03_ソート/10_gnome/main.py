# ******************************************************************************
# Course      : アルゴリズム・データ構造・コーディングテスト入門
# Chapter     : 3 ソート
# Theme       : gnomeソート
# Creat Date  : 2022/3/6
# Final Update:
# URL         : https://www.udemy.com/course/python-algo/
# ******************************************************************************


# ＜概要＞
# - Gnomeソートのアルゴリズムを学ぶ（ノームソート）


# ＜Gnomeソート＞
# - Bubbleソートと似た考え方
# - イテレーション内で小さい値を見つけると適切な位置までbackwardで移動させる
#   --- 全体でループは1つのみ


# ＜目次＞
# 0 準備
# 1 ソート関数の定義
# 2 実行


# 0 準備 ----------------------------------------------------------------------

# ライブラリ
from typing import List
import random


# 1 ソート関数の定義 ------------------------------------------------------------

# ＜ポイント＞
# - ｢イテレーション番号の値｣と｢その前の値｣を比較する
# - 小さい値を見つけると適切な位置までbackwardで移動させる


def gnome_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    index = 0
    while index < len_numbers:
        if index == 0:
            index += 1

        if numbers[index] >= numbers[index-1]:
            index += 1
        else:
            numbers[index], numbers[index-1] = numbers[index-1], numbers[index]
            index -= 1

    return numbers


# 2 実行 -----------------------------------------------------------------------

if __name__ == '__main__':
    # 例題の数字
    nums = [2, 5, 1, 8, 7, 3]
    gnome_sort(numbers=nums)

    # ランダムな数字
    nums = [random.randint(0, 1000) for _ in range(10)]
    gnome_sort(numbers=nums)
