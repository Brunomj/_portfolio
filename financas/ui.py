# app/ui.py

import tkinter as tk
from financas.controller import adicionar_transacao_ui, atualizar_saldo_ui, carregar_transacoes_ui


class FinanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Finanças Pessoais")
        self.root.geometry("720x720")

        self.criar_widgets()
        self.atualizar_saldo()

    def criar_widgets(self):
        """Função responsável por criar todos os widgets da interface."""

        # Título
        self.title_label = tk.Label(self.root, text="Controle de Finanças", font=("Arial", 16))
        self.title_label.pack(pady=10)

        # Descrição da transação
        self.descricao_label = tk.Label(self.root, text="Descrição:")
        self.descricao_label.pack()
        self.descricao_entry = tk.Entry(self.root, width=30)
        self.descricao_entry.pack(pady=5)

        # Valor da transação
        self.valor_label = tk.Label(self.root, text="Valor:")
        self.valor_label.pack()
        self.valor_entry = tk.Entry(self.root, width=30)
        self.valor_entry.pack(pady=5)

        # Tipo de transação (Receita ou Despesa)
        self.tipo_label = tk.Label(self.root, text="Tipo (receita/despesa):")
        self.tipo_label.pack()
        self.tipo_entry = tk.Entry(self.root, width=30)
        self.tipo_entry.pack(pady=5)

        # Botão para adicionar transação
        self.add_button = tk.Button(self.root, text="Adicionar Transação", command=self.adicionar_transacao)
        self.add_button.pack(pady=10)

        # Label para exibir o saldo
        self.saldo_label = tk.Label(self.root, text="Saldo Atual: R$0.00", font=("Arial", 14))
        self.saldo_label.pack(pady=20)

        # Lista de transações
        self.transacoes_label = tk.Label(self.root, text="Transações:", font=("Arial", 14))
        self.transacoes_label.pack(pady=10)

        self.transacoes_listbox = tk.Listbox(self.root, width=50, height=10)
        self.transacoes_listbox.pack(pady=10)

        # Botão para carregar transações
        self.load_button = tk.Button(self.root, text="Carregar Transações", command=self.carregar_transacoes)
        self.load_button.pack(pady=10)

    def adicionar_transacao(self):
        """Função chamada para adicionar uma transação no banco de dados."""

        descricao = self.descricao_entry.get()
        valor = self.valor_entry.get()
        tipo = self.tipo_entry.get().lower()

        adicionar_transacao_ui(descricao, valor, tipo)  # Chama a função do controller

        # Limpar os campos
        self.descricao_entry.delete(0, tk.END)
        self.valor_entry.delete(0, tk.END)
        self.tipo_entry.delete(0, tk.END)

        # Atualizar o saldo
        self.atualizar_saldo()

    def atualizar_saldo(self):
        """Função para atualizar o saldo exibido na interface."""
        saldo = atualizar_saldo_ui()  # Chama a função do controller
        self.saldo_label.config(text=f"Saldo Atual: R${saldo:.2f}")  # Exibe o saldo formatado

    def carregar_transacoes(self):
        """Função para carregar as transações no Listbox."""
        transacoes = carregar_transacoes_ui()  # Chama a função do controller

        # Limpar a lista atual
        self.transacoes_listbox.delete(0, tk.END)

        # Adicionar cada transação à lista na interface
        for transacao in transacoes:
            descricao, valor, tipo = transacao
            self.transacoes_listbox.insert(tk.END, f"{descricao} - {tipo.capitalize()} - R${valor:.2f}")


# Função para rodar a interface
def run_ui():
    root = tk.Tk()
    app = FinanceApp(root)
    root.mainloop()
