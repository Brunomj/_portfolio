from financas.models import criar_tabela
from financas.ui import run_ui

if __name__ == "__main__":
    criar_tabela()  # Cria a tabela no banco de dados, se necessário
    run_ui()  # Inicia a interface gráfica