# ******************************************************************************
# Book     : Pythonプロフェッショナル大全
# Chapter  : 10 コンフィグとロギング
# Section  : 2 適切なロギングの書き方
# Theme    : 15 ログ出力のフィルタ
# Date     : 2022/09/14
# URL      : https://www.kadokawa.co.jp/product/322201000299/
# ******************************************************************************


# ＜ポイント＞
# - ログの出力に当たってフィルタを適用することで、重要情報のログ出力を回避する予防策となる


# ＜目次＞
# 0 準備
# 1 ログフィルターの設定
# 2 ログの出力


# 0 準備 -------------------------------------------------------------------

# ライブラリ
import logging


# ログレベルの設定
logging.basicConfig(level=logging.INFO)


# 1 ログフィルターの設定 -------------------------------------------------------

# クラス定義
# --- logging.Filterをオーバーライド
class NoPassFilter(logging.Filter):
    def filter(self, record):
        log_message = record.getMessage()
        return 'password' not in log_message


# ロガーの作成
logger = logging.getLogger(__name__)

# ロガーにフィルタの適用
# --- オーバーライドしたfilterメソッドが使用される
logger.addFilter(NoPassFilter())


# 2 ログの出力 ---------------------------------------------------------------

# ログ出力
# --- 当ファイル
logger.info('from main')

# ログ出力
# --- 参照ファイル
logger.info('from main password = "test"')
