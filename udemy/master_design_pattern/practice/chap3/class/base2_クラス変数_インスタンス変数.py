# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 56 クラス変数・インスタンス変数
# Creat Date  : 2022/2/6
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜概要＞
# - クラス変数とはクラス内で予め定義された変数（全インスタンスが共通で持つ）
# - インスタンス変数とはインスタンスごとに定められる変数


# ＜目次＞
# 1 クラスの定義
# 2 クラス実行
# 3 クラス変数のアクセス方法
# 4 クラス変数の上書き


# 1 クラスの定義 ----------------------------------------------

# クラス定義
class SampleA():
    # クラス変数
    class_val = 'class val'

    # メソッド定義
    # --- インスタンス変数を定義
    def set_val(self):
        self.instance_val = 'instance val'

    # メソッド定義
    # --- 変数を出力
    def print_val(self):
        print('クラス変数 = {}'.format(self.class_val))
        print('インスタンス変数 = {}'.format(self.instance_val))


# 2 クラス実行 ------------------------------------------------

# インスタンス生成
# --- この時点でクラス変数は定義されているが、インスタンス変数は定義されていない
instance_a = SampleA()

# 確認
instance_a.class_val

# メソッド実行
# --- インスタンス変数の定義
instance_a.set_val()

# 確認
instance_a.instance_val
instance_a.print_val()


# 3 クラス変数のアクセス方法 --------------------------------------

# クラス定義からアクセス
SampleA.class_val

# インスタンスからアクセス
instance_a.class_val
instance_a.__class__.class_val


# 4 クラス変数の上書き -------------------------------------------

# ＜ポイント＞
# - クラス変数はインスタンス間で共通して使用される
#   --- クラス変数の変更は全てのインスタンスで共有される（予想外な動作につながる）
#   --- メモリも同じものを指している（IDが同じ）


# 別名のインスタンス生成
instance_b = SampleA()

# インスタンス変数の定義
instance_b.set_val()

# 確認
instance_b.print_val()

# クラス変数の変更
# --- ｢instance_a｣を変更している点に注意
instance_a.__class__.class_val = 'class val 2'

# 確認
# --- ｢instance_b｣にも変更が反映している
instance_b.print_val()

# 確認
# --- IDが同じ
print(id(instance_a.__class__.class_val))
print(id(instance_b.__class__.class_val))
