# ******************************************************************************
# Book     : Pythonプロフェッショナル大全
# Chapter  : 10 コンフィグとロギング
# Section  : 2 適切なロギングの書き方
# Theme    : 18 ログ設定を辞書型で定義
# Date     : 2022/09/14
# URL      : https://www.kadokawa.co.jp/product/322201000299/
# ******************************************************************************


# ＜ポイント＞
# - ログの設定は辞書型で書くことも可能
#   --- 設定ファイルをfileConfigで読込むのではなく、setting.pyにdictConfigを記述することもある


# ＜目次＞
# 0 準備
# 1 ログ設定を辞書型で記述
# 2 ログの出力


# 0 準備 -------------------------------------------------------------------

# ライブラリ
import logging.config


# 1 ログ設定を辞書型で記述 ---------------------------------------------------

logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'sampleFormatter': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'sampleHandlers': {
            'class': 'logging.StreamHandler',
            'formatter': 'sampleFormatter',
            'level': logging.DEBUG
        }
    },
    'root': {
        'handlers': ['sampleHandlers'],
        'level': logging.WARNING
    },
    'loggers': {
        'simpleExample': {
            'handlers': ['sampleHandlers'],
            'level': logging.DEBUG,
            'propagate': 0
        }
    }
})


# 2 ログの出力 --------------------------------------------------------------

# ロガーの作成
logger = logging.getLogger('simpleExample')

# ログの出力
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')