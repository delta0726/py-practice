# ******************************************************************************
# Book     : Pythonプロフェッショナル大全
# Chapter  : 10 コンフィグとロギング
# Section  : 2 適切なロギングの書き方
# Theme    : 2 ログレベルの変更
# Date     : 2022/09/12
# URL      : https://www.kadokawa.co.jp/product/322201000299/
# ******************************************************************************


# ＜ポイント＞
# - ログレベルは高い順から｢CRITICAL｣｢ERROR｣｢WARNING｣｢INFO｣｢DEBUG｣となっている
# - 指定したログレベルよりも上位のログのみ出力される


# ＜目次＞
# 0 準備
# 1 ログレベルの変更


# 0 準備 -----------------------------------------------------------------

# ライブラリ
import logging


# 1 ログレベルの変更 -------------------------------------------------------

# ＜ポイント＞
# - INFOのログレベルはアプリケーションで情報を得たい場合に使用する
# - DEGUGは開発中にのみ使用する（開発後はINFOに変更）


# ログレベルの変更
logging.basicConfig(level=logging.DEBUG)

# ログの出力
logging.critical('critical')
logging.error('error')
logging.warning('warning')
logging.info('info')
logging.debug('debug')