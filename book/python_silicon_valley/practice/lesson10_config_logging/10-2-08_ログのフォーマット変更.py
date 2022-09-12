# ******************************************************************************
# Book     : Pythonプロフェッショナル大全
# Chapter  : 10 コンフィグとロギング
# Section  : 2 適切なロギングの書き方
# Theme    : 8 ログのフォーマット変更
# Date     : 2022/09/13
# URL      : https://www.kadokawa.co.jp/product/322201000299/
# ******************************************************************************


# ＜ポイント＞
# - ロギングするには標準ライブラリの{logging}をインポートする


# ＜目次＞
# 0 準備
# 1 ログのフォーマット変更


# 0 準備 -----------------------------------------------------------------------

# ライブラリ
import logging


# 1 ログのフォーマット変更 -------------------------------------------------------

# フォーマット設定
formatter = '%(levelname)s:%(message)s'

# ログの設定
# --- ログレベル
# --- ログフォーマット
logging.basicConfig(level=logging.INFO, format=formatter)

# ログ出力
logging.info('info %s %s', 'test', 'test2')
