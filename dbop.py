import sqlite3

class WordList:

    def __init__(self):
        self.conn = sqlite3.connect("words.db")
        self.cur = self.conn.cursor()

    
    #idがa~b（a,bを含む）のレコードのリストを返す
    def __sorted_select(self, a, b):
        print("hoge")   #作るとき消す

    #受け取ったレコードのリストの順番をランダムに並び替えて返す
    def __shuffle(self, rows):
        print("hoge")   #作るとき消す

    #idがa~bのレコードのリストを返す
    #レコードの数はnumとする
    #ともみは…ともみは…ともみは…
    #flg=trueならばシャッフルする
    #返すレコードからはidフィールドを削除する．すなわち，{eng, jap}のリスト．
    def select(self, a, b, num, flg):
        print("hoge")   #作るとき消す

#実施した英単語テストの履歴もDB管理する．
#「受験者名，テスト範囲，問題数，正答数，オプション情報，実施日」を記録する予定
class TestLog:

    def __init__(self):
        print("hoge")

    