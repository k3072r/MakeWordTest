import sqlite3
import csv

dbname = "log.db"
conn = sqlite3.connect(dbname)

#sqliteを操作するカーソルオブジェクト
#カーソルを用いると，クエリをカプセル化することで，クエリ全体を一度に実行せず，
#クエリの結果を一度に数行ずつ読み取れる．それによりメモリの枯渇を防ぐ．らしい．
#https://www.postgresql.jp/document/9.2/html/plpgsql-cursors.html
cur = conn.cursor()

sql = "CREATE TABLE testlog(name TEXT, min INTEGER, max INTEGER, num INTEGER, "

#executeメソッドの引数のSQL文を実行
cur.execute(sql)

""" open_csv = open("target.csv", encoding = "utf-8-sig")
read_csv = csv.reader(open_csv)



rows = []
for row in read_csv:
    rows.append(row)

cur.executemany(
    "INSERT INTO wordlist (id, eng, jap) VALUES (?, ?, ?)", rows) """

conn.commit()
#open_csv.close()
conn.close()    #データベースへのコネクションを閉じる（必須！）