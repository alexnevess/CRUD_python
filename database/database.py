import sqlite3

con = sqlite3.connect("database.db")

cursor = con.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS customer(
                    id integer PRIMARY KEY,
                    name TEXT NOT NULL,
                    CPF TEXT UNIQUE NOT NULL,
                    age integer NOT NULL,
                    email TEXT NOT NULL,
                    date TEXT NOT NULL)""")

con.commit()
con.close()