from financas.database import init_db
from financas.models import adicionar_transacao, calcular_saldo
from financas.ui import run_ui

init_db()
def main():
    run_ui()
    
if __name__ == "__main__":
    main()