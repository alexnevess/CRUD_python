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

def register_customer(name, cpf, age, email, date_register):
    con = sqlite3.connect("database.db")
    cursor_register = con.cursor()
    cursor_register.execute("""INSERT INTO customer(name, cpf, age, email, date) VALUES(?,?,?,?,?)""", (name, cpf, age, email, date_register))
    con.commit()
    con.close()
