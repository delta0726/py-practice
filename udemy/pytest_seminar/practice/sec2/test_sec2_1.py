# ******************************************************************************
# Course      : 0から始めるPytest超基礎講座
# Chapter     : 2 Pytestの基礎
# Theme       : 単純な関数でテストを実行
# Creat Date  : 2022/2/20
# Final Update:
# URL         : https://www.udemy.com/course/python_pytest/
# ******************************************************************************


# ＜Pytestの実行＞
# - ターミナルから"pytest FILE_PATH"で実行する
# - 実行構成の編集から"Pythonテスト"で実行構成を作成して実行する


# ＜Pytestの振舞い＞
# - スクリプトを指定して実行した場合、スクリプト内の"test_*"ではじまるスクリプトのみが実行される
#   --- pytest I:/Project/Python/py_practice/udemy/pytest_seminar/practice/sec2/test_sec2_1.py

# - スクリプトの中身をコンソールに表示したい場合は"-s"を付ける
#   --- pytest I:/Project/Python/py_practice/udemy/pytest_seminar/practice/sec2/test_sec2_1.py -s

# - スクリプトをディレクトリに対して適用すると全てのファイルに適用される
#   --- pytest I:/Project/Python/py_practice/udemy/pytest_seminar/practice/sec2


# メイン処理 ----------------------------------------------------------------------------------

def test_hello_world():
    print("hello world!")

# def hello_world():
#     print("hello world 2!")