# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 5 SOLIDの原則
# Theme       : 4 インターフェース分離の原則
# Creat Date  : 2022/2/26
# Final Update: 2022/3/2
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜インターフェース分離の原則＞
# - インターフェースとはメソッドの中身を定義せず継承して利用するためのクラス（抽象クラス）
# - スーパークラス(抽象クラス)に無駄なメソッドを定義しないようにする
#   --- 新しいインターフェース(抽象クラス)を作成して、必要に応じてクラスを選択する(分離)


# ＜メリット＞
# - サブクラスのメソッドが減って実装が簡素化される
# - インターフェースの仕様変更によるサブクラスの保守を最小限にする


# ＜目次＞
# 0 準備
# 1 原則に準じない実装
# 2 原則に準じた実装
# 3 動作確認


# 0 準備 --------------------------------------------------

# ライブラリ
from abc import ABCMeta, abstractmethod


# 1 原則に準じない実装 --------------------------------------

# ＜ポイント＞
# - サブクラスで必ずしも実装しないメソッドがインターフェースに定義されている
#   --- 抽象メソッドのためサブクラスで実装しないと動作しない
#   --- インターフェースで抽象メソッドの定義が適切でなかった


# スーパークラスの定義
# --- インターフェースとして抽象メソッドを定義
class Athlete(metaclass=ABCMeta):

    @abstractmethod
    def swim(self):
        pass

    @abstractmethod
    def high_jump(self):
        pass

    @abstractmethod
    def long_jump(self):
        pass


# サブクラスの定義
# --- 必要ない抽象メソッドを実装しなければならない
class Athlete1(Athlete):

    def swim(self):
        print('I swim')
    
    def high_jump(self):
        pass

    def long_jump(self):
        pass


# インスタンスの生成
john = Athlete1()

# メソッドの実行
john.swim()


# 2 原則に準じた実装 --------------------------------------------------

# ＜ポイント＞
# - サブクラスで抽象メソッドによる無駄な実装が入らないようにする
#   --- インターフェースを分離する(SwimAthlete/JumpAthlete)
#   --- サブクラスは必要なインターフェースのみを継承する


# ＜クラス構成＞
# - Athlete(metaclass=ABCMeta)
#   --- SwimAthlete(Athlete)
#   --- JumpAthlete(Athlete)
#       --- Athlete1(SwimAthlete)
#       --- Athlete2(SwimAthlete, JumpAthlete)


# スーパークラスの定義
# --- 抽象クラス
class Athlete(metaclass=ABCMeta):
    pass


# インターフェースの定義
# --- 抽象メソッドを指定
class SwimAthlete(Athlete):
    @abstractmethod
    def swim(self):
        pass


# インターフェースの定義
# --- 抽象メソッドを指定
class JumpAthlete(Athlete):
    @abstractmethod
    def high_jump(self):
        pass

    @abstractmethod
    def long_jump(self):
        pass


# サブクラスの定義
# --- 必要なメソッドのみを実装
class Athlete1(SwimAthlete):
    def swim(self):
        print('I swim')


# サブクラスの定義
# --- 必要なメソッドのみを実装
class Athlete2(SwimAthlete, JumpAthlete):

    def swim(self):
        print('I swim')

    def high_jump(self):
        print('I high jump')

    def long_jump(self):
        print('I long jump')


# 3 動作確認 ------------------------------------------------------------

# インスタンス生成
# --- スイマー
# --- スイマー＆陸上
john = Athlete1()
yuji = Athlete2()

# メソッド実行
john.swim()
yuji.swim()
yuji.high_jump()
yuji.long_jump()
