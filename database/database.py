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

def show_customers():
    con = sqlite3.connect("database.db")
    cursor_show = con.cursor()
    cursor_show.execute("SELECT * FROM customer")
    result = cursor_show. fetchall()
    con.close()
    return result

def search_customer(cpf):
    con = sqlite3.connect("database.db")
    cursor_search = con.cursor()
    cursor_search.execute("SELECT name, cpf, age, email FROM customer WHERE cpf = ?", (cpf,))
    result = cursor_search.fetchone()
    con.close()
    return result

def update_customer(old_cpf, name_update, cpf_update, age_update, email_update, date_update):
    con = sqlite3.connect("database.db")
    cursor_update = con.cursor()
    cursor_update.execute("UPDATE customer SET name = ?, cpf = ?, age = ?, email = ?, date = ? WHERE cpf = ?", (name_update, cpf_update, age_update, email_update, date_update, old_cpf))
    con.commit()
    con.close()