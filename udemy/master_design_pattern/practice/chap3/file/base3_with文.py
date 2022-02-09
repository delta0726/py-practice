# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : with
# Creat Date  : 2022/2/10
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜概要＞
# - withの中の処理を実行する前に、withの後に指定したクラスの__init__と__enter__が呼ばれる
# - 処理終了後に__exit__が呼ばれる
#   --- ここではwithの中で行われているフローを実装する


# ＜目次＞
# 1 クラス定義
# 2 クラス実行


# 1 クラス定義 ----------------------------------------------------------

# ＜ポイント＞
# - withを用いる代表例である｢ファイル書込｣のフローを実装する
#   --- __enter__でファイルが開かれる
#   --- メイン処理(write)をメソッドで実装する
#   --- withを抜ける際に__exit__が実行される



class WithTest:

    def __init__(self, file_name):
        print('init called')
        self.__file_name = file_name
    
    def __enter__(self):
        print('enter called')
        self.__file = open(self.__file_name, mode='w', encoding='utf-8')
        return self
    
    def write(self, msg):
        self.__file.write(msg)

    def __exit__(self, exc_type, exc_val, traceback):
        print('exit called')
        self.__file.close()


# 2 クラス実行 ----------------------------------------------------------

# ＜ポイント＞
# - 処理は以下の順序で実行される
#   --- init called
#   --- enter called
#   --- with の中
#   --- exit called


with WithTest('resources/output.txt') as t:
    print('with の中')
    t.write('ああああああ')
