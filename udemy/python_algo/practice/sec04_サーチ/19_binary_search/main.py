# ******************************************************************************
# Course      : アルゴリズム・データ構造・コーディングテスト入門
# Chapter     : 4 サーチ
# Theme       : Binaryサーチ
# Creat Date  : 2022/3/6
# Final Update:
# URL         : https://www.udemy.com/course/python-algo/
# ******************************************************************************


# ＜概要＞
# - 最も基本的なサーチは配列の最初から順に検索値を探す（リニアサーチ）
#   --- Binaryサーチは検索速度を高速化/安定化させるための工夫


# ＜Binaryサーチ＞
# - まず配列を小さい順に並べる
# - 配列で3点(LMR)を調べて検索値の位置を確認（繰り返して位置を絞り込む）


# ＜目次＞
# 0 準備
# 1 リニアサーチ
# 2 バイナリサーチ
# 3 実行


# 0 準備 -------------------------------------------------------------------------

# ライブラリ
from typing import List, NewType

# 出力値のデータ型の定義
IndexNum = NewType('IndexNum', int)


# 1 リニアサーチ -------------------------------------------------------------------

def linear_search(numbers: List[int], value: int) -> IndexNum:
    for i in range(0, len(numbers)):
        if numbers[i] == value:
            return i
    return -1


# 2 バイナリサーチ ----------------------------------------------------------------

def binary_search(numbers: List[int], value: int) -> IndexNum:
    # 検索パラメータ
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            left = mid + 1
        else:
            right = mid -1
    return -1


# 3 実行 ------------------------------------------------------------------------

if __name__ == '__main__':
    # 配列定義
    nums = [0, 1, 5, 7, 9, 11, 15, 20, 24]

    # リニアサーチ
    linear_search(numbers=nums, value=15)
    linear_search(numbers=nums, value=2)

    # バイナリサーチ
    binary_search(numbers=nums, value=15)
    binary_search(numbers=nums, value=2)
