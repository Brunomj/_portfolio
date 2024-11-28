# app/models.py

import sqlite3

def criar_tabela():
    conn = sqlite3.connect("financas.db")
    cursor = conn.cursor()

    # Criação da tabela transacoes, caso não exista
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS transacoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL,
        valor REAL NOT NULL,
        tipo TEXT NOT NULL CHECK(tipo IN ('receita', 'despesa'))
    )
    ''')

    conn.commit()
    conn.close()

def adicionar_transacao(descricao, valor, tipo):
    conn = sqlite3.connect("financas.db")
    cursor = conn.cursor()

    cursor.execute('''
            INSERT INTO transacoes (descricao, valor, tipo)
            VALUES (?, ?, ?)
    ''', (descricao, valor, tipo))

    conn.commit()
    conn.close()

def calcular_saldo():
    conn = sqlite3.connect("financas.db")
    cursor = conn.cursor()

    cursor.execute("SELECT tipo, valor FROM transacoes")
    transacoes = cursor.fetchall()

    saldo = 0
    for tipo, valor in transacoes:
        if tipo == "receita":
            saldo += valor
        elif tipo == "despesa":
            saldo -= valor

    conn.close()
    return saldo

def listar_transacoes():
    conn = sqlite3.connect("financas.db")
    cursor = conn.cursor()

    cursor.execute("SELECT descricao, valor, tipo FROM transacoes ORDER BY rowid DESC")
    transacoes = cursor.fetchall()

    conn.close()
    return transacoes
