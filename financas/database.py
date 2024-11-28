import sqlite3

def init_db():

    conn = sqlite3.connect("financas.db")
    cursor = conn.cursor()

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS transacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            valor REAL NOT NULL,
            tipo TEXT CHECK(tipo IN ('receita', 'despesa')) NOT NULL
            )
    ''')

    conn.commit()
    conn.close()