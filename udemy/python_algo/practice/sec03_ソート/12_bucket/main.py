# ******************************************************************************
# Course      : アルゴリズム・データ構造・コーディングテスト入門
# Chapter     : 3 ソート
# Theme       : Bucketソート
# Creat Date  : 2022/3/6
# Final Update:
# URL         : https://www.udemy.com/course/python-algo/
# ******************************************************************************


# ＜概要＞
# - Bucketソートのアルゴリズムを学ぶ（insertionソートを使用）


# ＜Bucketソート＞
# - 配列を複数のバケットに分割してバケットごとにinsertionソートを適用する
# - バケットは数値の水準が似たものを集める仕組みになっている
# - ソートされたバケットを結合してソート完了となる
# - デバッガーで動きを見ると分かりやすい


# ＜目次＞
# 0 準備
# 1 insertionソートの定義
# 2 ソート関数の定義
# 3 実行


# 0 準備 --------------------------------------------------------------------

# ライブラリ
from typing import List
import random


# 1 insertionソートの定義 ----------------------------------------------------

# ＜ポイント＞
# - 前回のinsertion_sort()をそのまま流用


def insertion_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(1, len_numbers):
        temp = numbers[i]
        j = i - 1

        while j >= 0 and numbers[j] > temp:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = temp

    return numbers


# 2 ソート関数の定義 ----------------------------------------------------------

def bucket_sort(numbers: List[int]) -> List[int]:
    # バケットサイズの決定
    max_num = max(numbers)
    len_numbers = len(numbers)
    size = max_num // len_numbers

    # リスト内リストの作成
    # --- サイズの長さ分の要素数
    buckets = [[] for _ in range(size)]

    for num in numbers:
        i = num // size
        #if i != size:
        if i < size:
            buckets[i].append(num)
        else:
            buckets[size-1].append(num)

    for i in range(size):
        insertion_sort(buckets[i])

    result = []
    for i in range(size):
        result += buckets[i]

    return result


# 3 実行 --------------------------------------------------------------------

if __name__ == '__main__':
    # 例題の数字
    nums = [1, 5, 28, 25, 100, 52, 27, 91, 22, 99]
    bucket_sort(numbers=nums)

    # ランダムな数字
    nums = [random.randint(0, 1000) for _ in range(10)]
    bucket_sort(numbers=nums)

