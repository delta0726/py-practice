# ******************************************************************************
# Category  : Grammar of Pandas
# Chapter   : 01 基本操作
# Title     : 03 オブジェクトの作成
# Date      : 2022/07/11
# ******************************************************************************


# ＜目次＞
# 0 準備
# 1 Seriesの作成
# 2 DataFrameの作成


# 0 準備 ---------------------------------------------------------------------

# ライブラリ
import pandas as pd
import numpy as np


# 1 Seriesの作成 --------------------------------------------------------------

# ＜ポイント＞
# - Pandas Seriesがリストやndarrayと異なる点としてインデックスを持つ


# リストからの作成
data1 = [12, 24, 36]
index1 = ["Row1", "Row2", "Row3"]
pd.Series(data = data1, index = index1)

# 辞書からの作成
dict1 = {'Row1': 12, 'Row2': 24, 'Row3': 36}
pd.Series(dict1)

# ndarrayからの作成
arr1 = np.array([12, 24, 36])
index1 = ["Row1", "Row2", "Row3"]
pd.Series(data = arr1, index = index1)


# 2 DataFrameの作成 ---------------------------------------------------------

# 辞書から作成
# --- リストから作成
pd.DataFrame(
    data={'Col1': [10, 20, 30, 40],
          'Col2': [50, 60, 70, 80],
          'Col3': ['a', 'b', 'c', 'd']})

# 辞書から作成
# --- 1次元配列を辞書に格納
pd.DataFrame(
    data={'Col1': np.array([10, 20, 30, 40]),
          'Col2': np.array([50, 60, 70, 80]),
          'Col3': np.array(['a', 'b', 'c', 'd'])})


# Pandas Seriesから作成
pd.DataFrame(
    data={'Col1': pd.Series([10, 20, 30, 40]),
          'Col2': pd.Series([50, 60, 70, 80]),
          'Col3': pd.Series(['a', 'b', 'c', 'd'])}
)

# 二次元配列から作成
pd.DataFrame(
    data=np.array([[10, 20, 30, 40],
                   [11, 21, 31, 41],
                   [12, 22, 32, 42]]),
    index=['Row1', 'Row2', 'Row3'],
    columns=['Col1', 'Col2', 'Col3', 'Col4']
)
