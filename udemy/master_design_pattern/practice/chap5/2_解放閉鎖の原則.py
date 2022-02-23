# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 5 SOLIDの原則
# Theme       : 2_解放閉鎖の原則
# Creat Date  : 2022/2/24
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜解放閉鎖の原則＞
# - クラス/モジュール/関数は拡張に対して開いていて、修正に対して閉じている状態にする
#   --- コードの追加によって拡張が容易
#   --- コードの修正箇所をなるべく少なくする


# ＜メリット＞
# - 機能拡張が容易になるため拡張性が向上する
# - 拡張時にテスト対象が拡張機能に限定されるため保守性が向上する


# ＜目次＞
# 0 準備
# 1 基本クラスの定義
# 2 原則を満たさない実装例
# 3 原則に即した実装例
# 4 動作確認：単一項目のフィルタ
# 5 動作確認：複数項目のフィルタ


# 0 準備 ---------------------------------------------------------

# ライブラリ
from abc import ABCMeta, abstractmethod


# 1 基本クラスの定義 ------------------------------------------------

# ＜ポイント＞
# - ユーザー情報を保持するクラス


class UserInfo:

    def __init__(self, user_name, job_name, nationality):
        self.user_name = user_name
        self.job_name = job_name
        self.nationality = nationality
    
    def __str__(self):
        return '{} {} {}'.format(
            self.user_name, self.job_name, self.nationality
        )


# 2 原則を満たさない実装例 ---------------------------------------

# ＜ポイント＞
# - ユーザー情報(UserInfoクラス)から指定した属性のユーザーを抽出する
# - フィルタ項目ごとにメソッドが定義されている
#   --- フィルタ項目を変更するたびにメソッドを追加する必要がある
#   --- 複数項目のAND条件やOR条件を含めるとメソッドが膨大になる可能性がある


# クラス定義
class UserInfoFilter:

    @staticmethod
    def filter_users_job(users, job_name):
        for user in users:
            if user.job_name == job_name:
                yield user

    @staticmethod
    def filter_users_nationality(users, nationality):
        for user in users:
            if user.nationality == nationality:
                yield user


# インスタンス生成
# --- ユーザー情報
taro = UserInfo('taro', 'salary man', 'Japan')
jiro = UserInfo('jiro', 'police man', 'Japan')
john = UserInfo('john', 'salary man', 'USA')

# リスト格納
user_list = [taro, jiro, john]

# フィルタの適用
for man in UserInfoFilter.filter_users_job(user_list, 'police man'):
    print(man)

# フィルタの適用
for man in UserInfoFilter.filter_users_nationality(user_list, 'Japan'):
    print(man)


# 3 原則に即した実装例-----------------------------------------------

# ＜ポイント＞
# - 複数のフィルタ項目を自由に選択できるようにする
#   --- フィルタ項目ごとの条件判定を実装する
#   --- クラス単位でANDとORで条件判定ができるようにする


# ＜クラス定義＞
# - Comparation(metaclass=ABCMeta)
#   --- AndComparation(Comparation)
#   --- OrComparation(Comparation)
#   --- JobNameComparation(Comparation)
#   --- NationalityComparation(Comparation)
# - Filter(metaclass=ABCMeta)
#   --- UserInfoFilter(Filter)


# 比較操作
# --- 抽象メソッドにしておいて別途実装
class Comparation(metaclass=ABCMeta):

    @abstractmethod
    def is_equal(self, other):
        pass

    def __and__(self, other):
        return AndComparation(self, other)
    
    def __or__(self, other):
        return OrComparation(self, other)


# 比較操作の実装
# --- AND比較の実装（Compareクラスの__and__の実装）
class AndComparation(Comparation):

    def __init__(self, *args):
        self.comparations = args
    
    def is_equal(self, other):
        return all(
            map(lambda comparation: comparation.is_equal(other),
                self.comparations)
        )


# 比較操作の実装
# --- OR比較の実装（Compareクラスの__or__の実装）
class OrComparation(Comparation):

    def __init__(self, *args):
        self.comparations = args
    
    def is_equal(self, other):
        return any(
            map(lambda comparation: comparation.is_equal(other),
                self.comparations)
        )


class JobNameComparation(Comparation):

    def __init__(self, job_name):
        self.job_name = job_name
    
    def is_equal(self, other):
        return self.job_name == other.job_name


class NationalityComparation(Comparation):

    def __init__(self, nationality):
        self.nationality = nationality
    
    def is_equal(self, other):
        return self.nationality == other.nationality


# フィルタ操作
# --- 抽象メソッドにしておいて別途実装
class Filter(metaclass=ABCMeta):

    @abstractmethod
    def filter(self, comparation, items):
        pass


# フィルタ操作の実装
# --- Comparationクラスに対してフィルタ操作
class UserInfoFilter(Filter):
    def filter(self, comparation, items):
        for item in items:
            if comparation.is_equal(item):
                yield item


# 4 動作確認：単一項目のフィルタ----------------------------------------

# ＜ポイント＞
# - フィルタ操作は以下の要領で行われる
#   --- user_info_filter.filter(salary_man_comparation, user_list)


# インスタンス生成
# --- ユーザー情報
taro = UserInfo(user_name='taro', job_name='salary man', nationality='Japan')
jiro = UserInfo(user_name='jiro', job_name='police man', nationality='Japan')
john = UserInfo(user_name='john', job_name='salary man', nationality='USA')

# リスト格納
user_list = [taro, jiro, john]

# インスタンス生成（共通）
# --- フィルタ動作
user_info_filter = UserInfoFilter()


# インスタンス生成（Job）
# --- 比較用のオブジェクト生成
salary_man_comparation = JobNameComparation('salary man')

# フィルタ操作
for user in user_info_filter.filter(salary_man_comparation, user_list):
    print(user)


# インスタンス生成（Nationality）
# --- 比較用のオブジェクト生成
japan_comparation = NationalityComparation('Japan')

# フィルタ操作
for user in user_info_filter.filter(japan_comparation, user_list):
    print(user)


# 5 動作確認：複数項目のフィルタ----------------------------------------

# ＜ポイント＞
# - 比較用オブジェクトをANDやORでつないで複数条件のオブジェクトを生成


# インスタンス生成
# --- ユーザー情報
taro = UserInfo(user_name='taro', job_name='salary man', nationality='Japan')
jiro = UserInfo(user_name='jiro', job_name='police man', nationality='Japan')
john = UserInfo(user_name='john', job_name='salary man', nationality='USA')

# リスト格納
user_list = [taro, jiro, john]

# インスタンス生成（共通）
# --- フィルタ動作
user_info_filter = UserInfoFilter()

# インスタンス生成（Job & Nationality）
# --- 比較用オブジェクト
# --- AND比較
salary_man_and_japan = \
    JobNameComparation('salary man')\
    & NationalityComparation('Japan')

# フィルタ操作
for user in user_info_filter.filter(salary_man_and_japan, user_list):
    print(user)


# インスタンス生成（Job & Nationality）
# --- 比較用オブジェクト
# --- OR比較
salary_man_or_japan = \
    salary_man_comparation\
    | japan_comparation

# フィルタ操作
for user in user_info_filter.filter(salary_man_or_japan, user_list):
    print(user)
