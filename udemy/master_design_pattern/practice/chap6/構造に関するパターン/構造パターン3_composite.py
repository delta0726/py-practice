# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 6 デザインパターン講座
# Theme       : 構造に関するパターン（Composite）
# Creat Date  : 2022/2/28
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜*パターン＞
# - 木と葉を持った階層構造をプログラム上で表現したい場合に用いられる
# - どの節にどの葉を要素として追加していくのか把握することが難しい場合にツリー構造を表現する


# ＜目的＞
# - ツリー構造をわかりやすく表現する


# ＜仕組み＞
# - 葉と節のもつ共通機能を持つComponentを作成して、Componentを継承したCompositeとReafを作成する
# - Compositeをインスタンス化してその Compositeの子要素とするCompositeとReafを追加していく


# ＜構成要素＞
# - Component : CompositeとReafの共通機能を持った抽象クラス
# - Composite : 容器を表す役割を持ったクラス（この中にComposite,Reafを入れて階層構造を作成）
# - Reaf      : 中身を表す役割を持ったクラス（この中には要素を入れることができない）


# ＜目次＞
# 0 準備
# 1 Componentの定義
# 2 Compositeの定義
# 3 Reafの定義
# 4 動作確認

# 0 準備 -----------------------------------------------------------------

# ライブラリ
from abc import ABC, abstractmethod


# 1 Componentの定義 -------------------------------------------------------

class Component(ABC):

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def size(self):
        pass

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent
    
    @abstractmethod
    def print_list(self, path):
        pass
    
    def __str__(self):
        return f"{self.name} ({self.size})"


# 2 Compositeの定義 ------------------------------------------------------

class File(Component):

    def __init__(self, name, size):
        self.__name = name
        self.__size = size
        self._parent = None
    
    @property
    def name(self):
        return self.__name
    
    @property
    def size(self):
        return self.__size
    
    # 自分のパスと名前を表示します
    def print_list(self, path=''):
        print(path + '/' + str(self))


# 3 Reafの定義 -----------------------------------------------------------

class Directory(Component):

    def __init__(self, name):
        self.__name = name
        self.__children = {} # ファイルやディレクトリを入れていく
        self._parent = None
    
    @property
    def name(self):
        return self.__name
    
    @property
    def size(self):
        file_size = 0
        for child in self.__children:
            file_size += self.__children[child].size
        return file_size
    
    def add_child(self, child):
        self.__children[child.name] = child
        child.parent = self
    
    def remove_child(self, child):
        if child.name in self.__children:
            del self.__children[child.name]
            child.parent = None
    
    def print_list(self, path=''):
        print(path + '/' + str(self))
        for child in self.__children:
            self.__children[child].print_list(path + '/' + self.name)


# 4 動作確認 ----------------------------------------------------

file1 = File('tmp1.txt', 1000)
file2 = File('tmp2.txt', 2000)
file3 = File('tmp3.txt', 3000)
file4 = File('tmp4.txt', 4000)

root_dir = Directory('root')
home_dir = Directory('home')
sys_dir = Directory('sys')
taro_dir = Directory('taro')

root_dir.add_child(home_dir)
root_dir.add_child(sys_dir)
root_dir.print_list()

home_dir.add_child(taro_dir)
taro_dir.add_child(file1)
taro_dir.add_child(file2)

home_dir.add_child(file3)
sys_dir.add_child(file4)

sys_dir.remove_child(file4)

root_dir.print_list()
file2.print_list()
