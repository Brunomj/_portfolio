# app/controller.py

from financas.models import adicionar_transacao, calcular_saldo, listar_transacoes
from tkinter import messagebox


def adicionar_transacao_ui(descricao, valor, tipo):
    """Função chamada pela UI para adicionar uma transação"""
    # Verificar se os campos foram preenchidos corretamente
    if not descricao or not valor or tipo not in ['receita', 'despesa']:
        messagebox.showerror("Erro", "Preencha todos os campos corretamente!")
        return

    try:
        valor = float(valor)
    except ValueError:
        messagebox.showerror("Erro", "O valor deve ser um número válido!")
        return

    # Adicionar a transação ao banco de dados
    adicionar_transacao(descricao, valor, tipo)


def atualizar_saldo_ui():
    """Função chamada pela UI para atualizar o saldo"""
    saldo = calcular_saldo()  # Chama a função para calcular o saldo
    return saldo


def carregar_transacoes_ui():
    """Função chamada pela UI para carregar as transações"""
    transacoes = listar_transacoes()
    return transacoes
