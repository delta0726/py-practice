# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 56 クラス変数・インスタンス変数
# Creat Date  : 2022/2/6
# Final Update: 2022/3/2
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜概要＞
# - ｢クラス変数｣とはクラス内で予め定義された変数（全インスタンスが共通で持つ）
# - ｢インスタンス変数｣とはインスタンスごとに定義される変数


# ＜クラス変数の使いどころ＞
# - クラス変数はインスタンス変数と比べると利用頻度が少ない
# - クラス変数は定数を定義する使うケースが多い
#   --- Pythonには標準で定数を扱う仕組みが用意されていない
#   --- 変数名を大文字で定義する


# ＜目次＞
# 1 クラスの定義
# 2 クラス実行
# 3 クラス変数のアクセス方法
# 4 クラス変数の上書き


# 1 クラスの定義 ----------------------------------------------

# ＜ポイント＞
# - クラス変数はクラス直下に定義する
# - インスタンス変数は"self.変数名 = "の形で定義される
#   --- 通常はインスタンス生成時に引数として受け取り、コンストラクタでインスタンス変数として定義する

# クラス定義
class SampleA:
    # クラス変数の定義
    class_val = 'class val'

    # メソッド定義
    # --- インスタンス変数の定義
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

# クラス変数へのアクセス
instance_a.class_val

# メソッド実行
# --- メソッド内でインスタンス変数の定義
# --- インスタンス変数へのアクセス
instance_a.set_val()
instance_a.instance_val

# 確認
instance_a.print_val()


# 3 クラス変数のアクセス方法 --------------------------------------

# ＜ポイント＞
# - クラス変数はインスタンス化しなくてもアクセスすることが可能
# - クラス変数は__class__でアクセスできるようになる


# クラス定義からアクセス
# --- インスタンス化しないでアクセス
SampleA.class_val

# インスタンスからアクセス
instance_a.class_val
instance_a.__class__.class_val


# 4 クラス変数の上書き -------------------------------------------

# ＜前提＞
# - クラス変数の用途は｢定数｣なので、クラス変数の上書きは行うべきではない
#   --- クラス変数の変更は全てのインスタンスで共有される（予想外な動作につながる）

# ＜ポイント＞
# - クラス変数に値を代入するとは外部から変更することができる
# - クラス変数はインスタンス間で共通して使用される
#   --- メモリIDも同じものを指している（IDが同じ）


# 別名のインスタンス生成
instance_b1 = SampleA()
instance_b2 = SampleA()

# インスタンス変数の定義
instance_b1.set_val()
instance_b2.set_val()

# インスタンス変数の確認
instance_b1.print_val()
instance_b2.print_val()

# クラス変数の変更
# --- ｢instance_a｣を変更している点に注意
instance_b2.__class__.class_val = 'class val 2'

# 変更の確認
# --- ｢instance_b｣にも変更が反映している
instance_b1.print_val()
instance_b2.print_val()

# 確認
# --- IDが同じ
print(id(instance_b1.__class__.class_val))
print(id(instance_b2.__class__.class_val))

# 全く新しいクラスを定義
# --- クラス自体の定義が変わってしまっているので変更の影響を受ける（予想外の動作）
instance_b3 = SampleA()
instance_b3.set_val()
instance_b3.print_val()

