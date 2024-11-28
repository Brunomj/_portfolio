import tkinter as tk
from tkinter import ttk
from openpyxl import load_workbook, workbook
from openpyxl.utils import get_column_letter
from datetime import date, datetime, timedelta
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import calendar

#janela de Exibição
janela = tk.Tk()
janela.title("Finanças Pessoais")
janela.geometry("700x500")
janela.configure(bg="#252525")

style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#252525", foreground="#FFFFFF", font=("Arial", 14))
style.configure("TEntry", fieldbackground="#FFFFFF", font=("Arial", 14))
style.configure("TButton", background="#4CAF50", foreground="#FFFFFF", font=("Arial", 14))

label_instrução = ttk.Label(janela, text="Insira um valor diário")
label_status = ttk.Label(janela, text="10000", foreground="red")
label_total = ttk.Label(janela, text="000", font=("Arial", 14, "bold"))
entry_valor = ttk.Entry(janela)
button_salvar = ttk.Button(janela, text="Salvar")

#posicionar elementos
label_instrução.pack(pady=5)
entry_valor.pack(pady=5)
button_salvar.pack(pady=10)
label_status.pack()
label_total.pack(pady=10)

janela.mainloop()

