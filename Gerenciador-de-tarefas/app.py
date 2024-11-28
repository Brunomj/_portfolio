import PySimpleGUI as sg

# Criar Layout
def home():
    sg.theme("DarkBlue4")
    linha = [
        [sg.Checkbox("", key="checkbox_0"), sg.Input("", key="input_0")]
    ]
    layout = [
        [sg.Frame("Tarefas", layout=linha, key="container")],
        [sg.Button("Nova Tarefa"), sg.Button("Resetar")],
    ]

    return sg.Window("Gerenciador de Tarefas", layout=layout, finalize=True)

# Criar a janela
janela = home()

# Contador de tarefas para criar chaves únicas
task_counter = 1

# Criar regras da janela
while True:
    event, values = janela.read()
    
    # Verificar fechamento da janela
    if event == sg.WIN_CLOSED:
        break

    elif event == "Nova Tarefa":
        janela.extend_layout(janela["container"], [[sg.Checkbox(""),sg.Input("")]])
    
    if event == "Resetar":
        janela.close()
        janela = home()
# Fechar a janela
janela.close()
