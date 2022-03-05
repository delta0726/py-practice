# ******************************************************************************
# Course      : アルゴリズム・データ構造・コーディングテスト入門
# Chapter     : 3 ソート
# Theme       : Cooktailソート
# Creat Date  : 2022/3/5
# Final Update:
# URL         : https://www.udemy.com/course/python-algo/
# ******************************************************************************


# ＜概要＞
# - Cooktailソートのアルゴリズムを学ぶ
# - Backwardなループ処理を記述する
# - While文でループ処理を記述する


# ＜Cooktailソート＞
# - Bubbleソートは大きい値を右に移動させたが、Cooktailソートは小さい値を左に移動させる処理も行う
# - ソートを行ったかどうかをswapフラグで判定する（最初はFalse ⇒ ソートするとTrue）
# - SwapフラグでTrueが発生する間は処理を続ける
#   --- 全てのパターンだけイテレーションを回す必要がないだけBubbleソートより速くなる


# ＜目次＞
# 0 準備
# 1 range関数の振舞い
# 2 ソート関数の定義
# 3 実行


# 0 準備 ----------------------------------------------------------------------

# ライブラリ
from typing import List


# 1 range関数の振舞い ---------------------------------------------------------------

# ＜ポイント＞
# - ソート関数でイテレーションを逆に回す際に逆方向のインデックスを生成する必要がある


def range_practice():
    # 数値でサイズを指定
    [i for i in range(10)]

    # 開始と終点を指定
    [i for i in range(1, 6)]

    # ステップを指定
    [i for i in range(1, 6, 2)]

    # 逆方向
    # --- ステップで-1を指定
    [i for i in range(6, 1, -1)]


# 2 ソート関数の定義 --------------------------------------------------------------

def cooktail_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    swapped = True
    start = 0
    end = len_numbers - 1
    while swapped:
        # 順方向
        swapped = False
        for i in range(start, end):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True

        if not swapped:
            break

        # カウンタ更新
        # --- 右のリミットをずらす
        end = end - 1

        # 逆方向
        swapped = False
        for i in range(end-1, start-1, -1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True

        # カウンタ更新
        # --- 左のリミットをずらす
        start = start + 1

    return numbers


# 3 実行 ------------------------------------------------------------------------

if __name__ == '__main__':
    # 例題の数字
    nums = [2, 5, 1, 8, 7, 3]
    cooktail_sort(numbers=nums)

    # ランダムな数字
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(cooktail_sort(numbers=nums))
