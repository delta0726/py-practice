# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 5 SOLIDの原則
# Theme       : 1 単一責任の原則
# Creat Date  : 2022/2/23
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜単一責任の原則＞
# - 全てのモジュールとクラスは1つの役割を提供して責任を持つべきとする原則
#   --- 具体的には、クラス名に沿った内容のメソッドのみを定義するようにする


# ＜メリット＞
# - クラスとモジュールで役割を整理することで可読性が向上する
# - 役割を細分化/明確化することで再利用性が向上する


# ＜目次＞
# 1 原則を満たしている状態
# 2 原則を超えてしまった状態
# 3 ソリューション


# 1 原則を満たしている状態 -----------------------------------------------

# ＜ポイント＞
# - UserInfoクラスはユーザー情報を保持するという役割を持つ
#   --- 以下のクラス定義は原則を満たしている


# クラス定義
class UserInfo:

    def __init__(self, name, age, phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number
    
    def __str__(self):
        return "{}, {}, {}".format(
            self.name, self.age, self.phone_number
        )


# インスタンス生成
user_info = UserInfo(name='Taro', age=21, phone_number='000-0000-0000')

# 出力確認
print(user_info)


# 2 原則を超えてしまった状態 ---------------------------------------------

# ＜ポイント＞
# - ファイルへの書き込みは、UserInfoクラスはユーザー情報を保持するという役割を超えてしまう
#   --- 別のクラスからUserInfoクラスに対して書き込み操作を行うようにするべき


# クラス定義
class UserInfo2:

    def __init__(self, name, age, phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number

    def __str__(self):
        return "{}, {}, {}".format(
            self.name, self.age, self.phone_number
        )

    def write_str_to_file(self, filepath, filename):
        with open(filepath + '/' + filename, mode='w') as fh:
            fh.write(str(self))


# インスタンス生成
user_info2 = UserInfo2(name='Taro', age=21, phone_number='000-0000-0000')

# ファイル出力
user_info2.write_str_to_file(filepath='practice/chap5/output',
                             filename='tmp.txt')


# 3 ソリューション --------------------------------------------------

# ＜ポイント＞
# - ファイルへの書き込みを別クラスとして定義する
# - インスタンスのstrを出力するという汎用性の高い処理なので静的メソッド
#   --- UserInfoクラスに限らず、情報を保持するクラスに対して汎用的に使用することを想定
#   --- 出力処理を統一することで仕様変更もしやすくなる


# クラス定義
class FileManager:

    @staticmethod
    def write_str_to_file(obj, filepath, filename):
        with open(filepath + '/' + filename, mode='w') as fh:
            fh.write(str(obj))


# インスタンス生成
user_info = UserInfo(name='Taro', age=21, phone_number='000-0000-0000')

# ファイル出力
FileManager.write_str_to_file(obj=user_info,
                              filepath='practice/chap5/output',
                              filename='tmp2.txt')
