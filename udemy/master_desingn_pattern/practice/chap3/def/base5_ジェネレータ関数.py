# ******************************************************************************
# Course      : デザインパターン・マスター講座
# Chapter     : 3 Python基本文法講座
# Theme       : 43 ジェネレータ関数
# Creat Date  : 2022/2/5
# Final Update:
# URL         : https://www.udemy.com/course/python-mx/
# ******************************************************************************


# ＜目次＞
# 1 基本動作
# 2 for文で実行
# 3 send文で値を送る
# 4 throw文で例外を発生させる
# 5 close文で終了させる


# 1 基本動作 -------------------------------------------------------

# ＜ポイント＞
# - ジェネレータ関数はインスタンス生成してから逐次実行する（直接実行するのではない）
# - 関数はyield文で指定した値(n)を出力する
# - 指定したイテレーション回数を超えてnext()を実行するとエラーとなる


# ジェネレータ関数
# --- yield文が含まれるとジェネレータ関数とみなされる
def generator(max):
    print('ジェネレータ作成')
    for n in range(max):
        yield n
        print('yield実行')

# インスタンス生成
# --- この時点で関数は実行されていない（関数にyield文が無ければ実行される）
gen = generator(10)

# 実行（1回目）
# --- yieldまで実行されて止まる（'yield実行'は出力されない、nは0が入っている）
n = next(gen)
print('n = {}'.format(n))

# 実行（2回目）
# --- 次のyieldまで実行されて止まる（'yield実行'が出力され、nも更新される）
n = next(gen)
print('n = {}'.format(n))

# 実行（3回目）
# --- 次のyieldまで実行されて止まる（'yield実行'が出力され、nも更新される）
n = next(gen)
print('n = {}'.format(n))



# 2 for文で実行 -------------------------------------------------

# ＜ポイント＞
# - ジェネレータはイテラブルなので、for文の回数指定に使うことができる
#   --- ジェネレータをループで一気に回すことが可能


# ジェネレータ関数
def generator(max):
    print('ジェネレータ作成')
    for n in range(max):
        yield n
        print('yield実行')

# インスタンス生成
gen = generator(10)

# ループで実行
for x in gen:
    print('x = {}'.format(x))


# 3 send文で値を送る -----------------------------------------------

# ＜ポイント＞
# - sendメソッドを用いるとyield文の戻り値に指定した値を送り込むことができる


# 関数定義
# --- ジェネレータ関数
def generator(max):
    print('ジェネレータ作成')
    for n in range(max):
        x = yield n
        print('x = {}'.format(x))
        print('yield実行')

# インスタンス生成
gen = generator(10)

# イテレーションを2回まわす
# --- 1回目はyieldの前で止まる（'ジェネレータ作成'のみ表示）
# --- x = None が表示される（yield n の戻り値がないため）
next(gen)
next(gen)

# 値を送り込む
# --- xに指定した値を送り込む
gen.send(100)


# 4 throw文で例外を発生させる ----------------------------------------


# 関数定義
# --- ジェネレータ関数
def generator(max):
    print('ジェネレータ作成')
    for n in range(max):
        try:
            x = yield n
            print('x = {}'.format(x))
            print('yield実行')
        except ValueError as e:
            print('throwを実行しました')

# インスタンス生成
gen = generator(10)

# イテレーションを1回まわす
next(gen)

# 例外処理を発生させる
gen.throw(ValueError('Invalid Value'))


# 5 close文で終了させる ----------------------------------------

# ＜ポイント＞
# - close文を用いるとジェネレータを途中で終了させることができる


# 関数定義
# --- ジェネレータ関数
def generator(max):
    print('ジェネレータ作成')
    for n in range(max):
        try:
            x = yield n
            print('x = {}'.format(x))
            print('yield実行')
        except ValueError as e:
            print('throwを実行しました')

# インスタンス生成
gen = generator(10)

# イテレーションを1回まわす
next(gen)

# クローズする
gen.close()

# イテレーションを1回まわす
# --- ジェネレータがクローズしたのでエラー（StopIteration）
# next(gen)
