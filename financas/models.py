
import sqlite3



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