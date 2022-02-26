# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 6 デザインパターン講座
# Theme       : 生成に関するパターン（Abstract Factory）
# Creat Date  : 2022/2/27
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜Abstract Factoryパターン＞
# - 抽象的な工場と抽象的なパーツを利用して関連するパーツを組み合わせることで新しい製品を作成する
#   --- factory_methodの発展形（複数のProductを扱う）


# ＜仕組み＞
# - 抽象クラスを継承した複数の部品を組み合わせて一つの製品を作成する


# ＜構成要素＞
# Factory         : Productを生成する処理を定義したインタフェース
# ConcreteFactory : ConcreteProductを作成するFactoryを具体化したクラス
# Product         : 作成するオブジェクトの部品を定義するインタフェース
# ConcreteProduct : Productを具体化したクラス（複数作成する）


# ＜目次＞
# 0 準備
# 1 Factoryの定義
# 2 ConcreteFactoryの定義
# 3 Productの定義
# 4 ConcreteProductの定義
# 5 各パーツから製品を作成
# 6 実行例


# 0 準備 --------------------------------------------------

# ライブラリ
from abc import ABC, abstractmethod


# 1 Factoryの定義 ---------------------------------------------------

class Factory(ABC):

    @abstractmethod
    def create_page_item(self, title, author):
        pass

    @abstractmethod
    def create_link_item(self, caption, url):
        pass

    @abstractmethod
    def create_list_item(self, caption):
        pass


# 2 ConcreteFactoryの定義 -------------------------------------

class HtmlFactory(Factory):

    def create_page_item(self, title, author):
        return HtmlPageItem(title, author)

    def create_link_item(self, caption, url):
        return HtmlLinkItem(caption, url)

    def create_list_item(self, caption):
        return HtmlListItem(caption)


# 3 Productの定義 ---------------------------------------------------

class AbcItem(ABC):

    def __init__(self, caption):
        self.caption = caption

    @abstractmethod
    def make_html(self):
        pass


# 4 ConcreteProductの定義 -------------------------------------

class PageItem(AbcItem):

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.content = []

    def add(self, item):
        self.content.append(item)

    def write_html(self, file_name):
        with open(file_name, 'w', encoding='utf-8') as fh:
            fh.write(self.make_html())


class LinkItem(AbcItem):
    # <li><a></a>
    def __init__(self, caption, url):
        super().__init__(caption)
        self.url = url


class ListItem(AbcItem):
    # <li></li>
    def __init__(self, caption):
        super().__init__(caption)
        self.items = []

    def add(self, item):
        self.items.append(item)


# 5 各パーツから製品を作成 --------------------------------------------

class HtmlPageItem(PageItem):

    def __init__(self, title, author):
        super().__init__(title, author)

    def make_html(self):
        output = f'<html>\n<head>\n<title>{self.title}</title>\n</head>\n'
        output += f'<body>\n'
        output += f'<h1>{self.title}</h1>\n'
        output += f'<ul>'
        for list_item in self.content:
            output += list_item.make_html()
        output += f'</ul>\n'
        output += f'<hr>\n<address>{self.author}</address>\n'
        output += '</body>\n</html>\n'
        return output


class HtmlLinkItem(LinkItem):

    def __init__(self, caption, url):
        super().__init__(caption, url)

    def make_html(self):
        return f'<li><a href= "{self.url}">{self.caption}</a></li>'


class HtmlListItem(ListItem):
    # linkitemを入れるようにする
    def __init__(self, caption):
        super().__init__(caption)

    def make_html(self):
        output = '<li>\n'
        output += self.caption + '\n'
        output += '<ul>\n'
        for link_item in self.items:
            output += link_item.make_html()
        output += '</ul>\n'
        output += '</li>\n'
        return output


# 6 実行例 -----------------------------------------------------

# インスタンスの生成
html_factory = HtmlFactory()
asahi = html_factory.create_link_item('朝日新聞', 'http://asahi')
yomiuri = html_factory.create_link_item('読売新聞', 'http://yomiuri')
yahoo = html_factory.create_link_item('Yahoo', 'http://yahoo')
google = html_factory.create_link_item('Google', 'http://google')
wikipedia = html_factory.create_link_item('Wikipedia', 'http://wikipedia')

news_pages = html_factory.create_list_item('新聞')
news_pages.add(asahi)
news_pages.add(yomiuri)

other_pages = html_factory.create_list_item('その他のページ')
other_pages.add(yahoo)
other_pages.add(google)
other_pages.add(wikipedia)

all_page = html_factory.create_page_item('My Page', 'Taro')
all_page.add(news_pages)
all_page.add(other_pages)

all_page.write_html('practice/chap6/生成に関するパターン/output/tmp.html')
