# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 演習問題4
# Creat Date  : 2022/3/2
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜概要＞
# - キャラクターを作成して戦わせる


# ＜Characterクラス＞
# - インスタンス変数として以下のプロパティ(変数)を持たせる
#   --- name    : 名前
#   --- hp      : ヒットポイント
#   --- offence : 攻撃力
#   --- Defense : 防御力


# ＜その他の動作＞
# - attachメソッドを実行すると｢自分のoffence-敵のdefense｣だけhpが減る
# - critical_hitメソッドを実行するとattachメソッドの2倍のダメージを与える
# - HPが0になると死んでしまい攻撃できなくなる


# ＜目次＞
# 0 準備
# 1 AllCharactersクラスの定義
# 2 Charactersクラスの定義
# 3 動作確認


# 0 準備 --------------------------------------------------------------------

# クラス定義
# --- 例外処理用
class CharacterAlreadyExistException(Exception):
    pass


# 1 AllCharactersクラスの定義 -----------------------------------------------

# ＜ポイント＞
# - キャラクターの出入りを管理するクラス


class AllCharacters:
    # キャラクターを格納
    all_characters = []
    alive_characters = []
    dead_characters = []

    @classmethod
    def character_append(cls, name):
        if name in cls.all_characters:
            raise CharacterAlreadyExistException('キャラクターはすでに存在します')
        cls.all_characters.append(name)
        cls.alive_characters.append(name)

    @classmethod
    def character_delete(cls, name):
        cls.dead_characters.append(name)
        cls.alive_characters.remove(name)


# 2 Charactersクラスの定義 -----------------------------------------------------

# ＜ポイント＞
# - 個別のキャラクターのインスタンスの作成と攻撃メソッドを定義する


class Character:

    # コンストラクタ
    # --- キャラクターのプロパティを設定
    def __init__(self, name, hp, offense, defense):
        AllCharacters.character_append(name)
        self.name = name
        self.hp = hp
        self.offense = offense
        self.defense = defense

    def attack(self, enemy, critical_point=1):
        if self.hp <= 0:
            print('キャラクターはすでに死んでいます')
            return
        attack_point = self.offense - enemy.defense
        attack_point = 1 if attack_point <= 0 else attack_point
        enemy.hp -= attack_point * critical_point
        if enemy.hp <= 0:
            AllCharacters.character_delete(enemy.name)

    def critical_hit(self, enemy):
        self.attack(enemy, 2)


# 3 動作確認 -----------------------------------------------------------------

# インスタンス生成
# --- キャラクターの定義
character_a = Character(name='A', hp=10, offense=5, defense=3)
character_b = Character(name='B', hp=8, offense=6, defense=2)

# クリティカルヒット
print(character_b.hp)
character_a.critical_hit(character_b)  # (5-2)*2 ->  8 -> 2
print(character_b.hp)

# 現存キャラクター
print(AllCharacters.alive_characters)
print(AllCharacters.dead_characters)

# 通常ヒット
print(character_b.hp)
character_a.attack(character_b)  # 2 -> -1
print(character_b.hp)

# 現存キャラクター
print(AllCharacters.alive_characters)
print(AllCharacters.dead_characters)

# 死んだキャラクターへの操作
character_b.attack(character_a)
