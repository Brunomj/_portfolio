import tkinter as tk
from tkinter import messagebox
from financas.models import adicionar_transacao, calcular_saldo


class FinanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Finanças Pessoais")

        # Tamanho da janela
        self.root.geometry("400x300")

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

        # Atualizar o saldo
        self.atualizar_saldo()

    def adicionar_transacao(self):
        descricao = self.descricao_entry.get()
        valor = self.valor_entry.get()
        tipo = self.tipo_entry.get().lower()

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

        # Limpar os campos
        self.descricao_entry.delete(0, tk.END)
        self.valor_entry.delete(0, tk.END)
        self.tipo_entry.delete(0, tk.END)

        # Atualizar o saldo
        self.atualizar_saldo()

    def atualizar_saldo(self):
        saldo = calcular_saldo()
        self.saldo_label.config(text=f"Saldo Atual: R${saldo:.2f}")


# Função para rodar a interface
def run_ui():
    root = tk.Tk()
    app = FinanceApp(root)
    root.mainloop()
