# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 5 SOLIDの原則
# Theme       : 5 依存性逆転の原則
# Creat Date  : 2022/2/23
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜依存性逆転の原則＞
# - ソフトウェアモジュール間の依存関係を切り離すための方法
# - 高水準モジュールは低水準モジュールに依存してはいけない（両者は抽象化に依存すべき）
# - 詳細は抽象化に依存すべきである（「抽象化は詳細に依存すべきでない）


# ＜メリット＞
# - 低水準モジュールを継承したクラスを利用した機能拡張が容易になる


# ＜目次＞
# 0 準備
# 1 原則に準じない実装
# 2 原則に準じた実装


# 0 準備 -------------------------------------------------------------

# ライブラリ
from abc import ABCMeta, abstractmethod


# 1 原則に準じない実装 -------------------------------------------------

# ＜ポイント＞
# - メソッドが直接クラスを参照している（クラス継承が適切に行われていない）
# - クラスの上位/下位を無視して参照が行われている（依存関係が複雑化）


# 上位クラス
# --- 抽象クラスになっていないのが問題（インターフェースの要件を満たさない）
class Book:
    def __init__(self, content):
        self.content = content


# クラス定義
# --- formatメソッドの引数が具体的なクラス(Book)を参照している(依存性逆転)
class Formatter:
    def format(self, book: Book):
        return book.content


# クラス定義
# --- Formatterの機能拡張
# class Formatter2:
#     def format(self, book: Book):
#         return book.content


# クラス定義
# --- 引数がBookクラスを参照している（クラス継承していない）
# --- メソッド内で具体的なクラス(Formatter)のインスタンスを生成している
# --- 具体的なクラス(Formatter)を参照しているので機能拡張に脆弱（Formatter2を参照できない）
class Printer:
    def print(self, book: Book):
        formatter = Formatter()
        formatted_book = formatter.format(book)
        print(formatted_book)


# インスタンス生成
book = Book('My Book')
printer = Printer()

# メソッド実行
# --- とりあえず動作する
printer.print(book)


# 2 原則に準じた実装 -------------------------------------------------

# インターフェース定義
# --- 慣例としてクラス名に"I"を付ける
# --- インターフェースではABCMetaを継承して抽象クラスであることを明示（実装は行わない）
# --- contentを継承先で実装を義務づける（抽象メソッド）
class IBook(metaclass=ABCMeta):

    @abstractmethod
    def content(self):
        pass


# クラス定義
# --- インターフェースを継承
# --- contentをプロパティとして実装
class Book(IBook):

    def __init__(self, content):
        self._content = content

    @property
    def content(self):
        return self._content


# クラス定義
# --- 機能拡張が容易に行える（Bookクラスの拡張）
class EBook(IBook):

    def __init__(self, content):
        self._content = content

    @property
    def content(self):
        return 'E' + self._content


# 抽象クラスの定義
# --- メソッドは抽象クラス(IBook)を参照している（通常クラスの参照を回避）
class IFormatter(metaclass=ABCMeta):

    @abstractmethod
    def format(self, i_book: IBook):
        pass


# クラス定義
class HtmlFormatter(IFormatter):

    def format(self, i_book: IBook):
        return '<h1>' + i_book.content + '</h1>'


# クラス定義
class XmlFormatter(IFormatter):

    def format(self, i_book: IBook):
        return '<xml>' + i_book.content + '</xml>'


class Printer:

    def __init__(self, i_formatter: IFormatter):
        self._i_formatter = i_formatter

    def print(self, i_book: IBook):
        formatted_book = self._i_formatter.format(i_book)
        print(formatted_book)


# インスタンス生成
book = Book('My Book')
html_formatter = HtmlFormatter()
html_printer = Printer(html_formatter)
html_printer.print(book)

#
xml_formatter = XmlFormatter()
xml_printer = Printer(xml_formatter)
xml_printer.print(book)

# 機能拡張の動作確認
# --- インスタンス生成
# --- メソッド実行
ebook = EBook('My EBook')
xml_printer.print(ebook)
