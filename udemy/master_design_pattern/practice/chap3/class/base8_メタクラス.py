# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 65 メタクラス
# Creat Date  : 2022/2/8
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜概要＞
# - メタクラスとはクラスの再定義をするクラス
#   --- クラス定義を検証する仕組み（ポリモーフィズムの基本原理）
#   --- スーパークラスの上位に来る概念（抽象クラスと似ている）


# ＜メタクラスの定義＞
# class Meta(type):
#     def __new__(metacls, name, bases, class_dict):
#         # クラスのチェックを行う
#         name        ： クラスの名前
#         bases       ： 継承しているクラス
#         class_dict  ： クラスの持っている値、関数等
#         return super().__new__(metacls, name, bases, class_dict)


# ＜メタクラスの使いどころ＞
# - その定義でよいのかクラスを検証する際に用いられる


# ＜目次＞
# 0 準備
# 1 メタクラスの定義
# 2 スーパークラスの定義
# 3 サブクラスの定義


# 0 準備 ---------------------------------------------------------

# 例外処理
class MetaException(Exception):
    pass


# 1 メタクラスの定義 -----------------------------------------------

# ＜ポイント＞
# - typeはデフォルトのメタクラス


class Meta1(type):

    def __new__(metacls, name, bases, class_dict):
        print('metacls = {}'.format(metacls))
        print('name = {}'.format(name))
        print('bases = {}'.format(bases))
        print('class_dict = {}'.format(class_dict))
        # if 'my_var' not in class_dict.keys():
        #     raise MetaException('my_varを定義してください。')
        for base in bases:  # 継承しているクラス
            if isinstance(base, Meta1):
                raise MetaException('継承できません')  # finalクラス
        return super().__new__(metacls, name, bases, class_dict)


# 2 スーパークラスの定義 --------------------------------------------

# ＜ポイント＞
# - クラスを定義するとメタクラスが実行される


class ClassA(metaclass=Meta1):
    a = '123'
    my_var = 'AAA'
    pass


# 3 サブクラスの定義 -----------------------------------------------

class SubClassA(ClassA):
    pass
