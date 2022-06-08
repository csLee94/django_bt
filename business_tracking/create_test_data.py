import sqlite3
import datetime as dt
def handler():
    conn = sqlite3.connect("./db.sqlite3")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mbt_contract")
    rows = cursor.fetchall()
    if len(rows) <1:
        print("None")
    elif len(rows) >=1:
        for row in rows:
            print(row)
        conn.close()

if __name__=="__main__":
    handler()