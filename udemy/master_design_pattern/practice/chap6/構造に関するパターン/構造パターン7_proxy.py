# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 6 デザインパターン講座
# Theme       : 構造に関するパターン（Proxy）
# Creat Date  : 2022/3/1
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜Proxyパターン＞
# - Proxyとは代理を表しており、あるオブジェクトの代わりの処理を行う
# - オリジナルのオブジェクトのアクセスをコントロールしたい場合に使用する
#   --- インスタンス化に時間がかかる / 処理が複雑 / 危険な処理


# ＜目的＞
# - 特定のオブジェクトに代わって処理を行う


# ＜仕組み＞
# - Subjectを継承したRealSubjectに処理を記述する
# - Subjectを継承したProxyを作成してRealSubjectの代わりに処理を行う


# ＜構成要素＞
# - Subject     : RealSubject と Proxy を同一視して利用するためのインタフェース
# - RealSubject : Subject を継承して処理を記述する
# - Proxy       : RealSubjectの代わりにクライアントからの処理を返す
#               : 自分で処理ができなかった場合にRealSubjectを呼び出す


# ＜目次＞
# 0 準備
# 1 Subjectの定義
# 2 RealSubjectの定義
# 3 Proxyの定義
# 4 動作確認


# 0 準備 ---------------------------------------------------------------

# ライブラリ
from abc import ABC, abstractmethod
import time


# 1 Subjectの定義 -------------------------------------------------------

class APICaller(ABC):

    @abstractmethod
    def request(self):
        pass


# 2 RealSubjectの定義 ----------------------------------------------------

class RealAPICaller(APICaller):

    # 処理の重いコンストラクタとする
    def __init__(self, url):
        self.__url = url
        time.sleep(5)
    
    def request(self):
        print('APIを呼び出す')
        return


# 動作確認
caller = RealAPICaller('http://api.com')
caller.request()


# 3 Proxyの定義 ------------------------------------------------------------

class RealAPICallerProxy(APICaller):

    def __init__(self, url):
        self.__url = url
    
    def __check_access(self):
        print('アクセスに成功しました')
        return True
    
    def __write_log(self):
        print('ログを出力します')
    
    def request(self):
        if self.__check_access():
            real_api_caller = RealAPICaller(self.__url)
            real_api_caller.request()
            self.__write_log()


# 4 動作確認 ----------------------------------------------------------------

# インスタンス生成
proxy = RealAPICallerProxy('https://api.com')

# リクエスト
proxy.request()
