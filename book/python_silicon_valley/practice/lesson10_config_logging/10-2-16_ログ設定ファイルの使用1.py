# ******************************************************************************
# Book     : Pythonプロフェッショナル大全
# Chapter  : 10 コンフィグとロギング
# Section  : 2 適切なロギングの書き方
# Theme    : 16 ログ設定ファイルの作成１
# Date     : 2022/09/14
# URL      : https://www.kadokawa.co.jp/product/322201000299/
# ******************************************************************************


# ＜ポイント＞
# - 当ファイルのロガーに__name__を入れることでログがどこから出力されているか分かりやすくなる


# ＜目次＞
# 0 準備
# 1 ログの設定
# 2 ログの出力
# 参考 loging.ini


# 0 準備 -------------------------------------------------------------------

# ライブラリ
import logging.config


# 1 ログの設定 --------------------------------------------------------------

# ログ設定の取得
logging.config.fileConfig('setting/logging.ini')

# ロガーの作成
logger = logging.getLogger(__name__)


# 2 ログの出力 ---------------------------------------------------------------

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')


# 参考 loging.ini -------------------------------------------------------

"""
[loggers]
keys=root,simpleExample

[handlers]
keys=streamHandler

[formatters]
keys=formatter

[logger_root]
level=WARNING
handlers=streamHandler

[logger_simpleExample]
level=DEBUG
handlers=streamHandler
qualname=simpleExample
propagate=0

[handler_streamHandler]
class=StreamHandler
level=DEBUG
formatter=formatter
args=(sys.stderr,)

[formatter_formatter]
format=%(asctime)s %(name)-12s %(levelname)-8s %(message)s
"""
