import tkinter as tk
from tkinter import font
import subprocess
import sys
import os
import threading

def run_process():
    """
    Esta função contém a lógica de instalação e execução.
    Ela será executada em uma thread separada para não travar a interface.
    """
    try:
        # Passo 1: Instalar dependências do requirements.txt
        if os.path.exists("requirements.txt"):
            print("--- Encontrado o arquivo 'requirements.txt'. Instalando dependências... ---")
            # Atualiza o status na tela
            status_label.config(text="Status: Instalando dependências...")
            
            command_install = [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"]
            # Executa o comando em segundo plano
            subprocess.run(command_install, check=True, capture_output=True, text=True)
            print("--- Dependências instaladas com sucesso! ---")
        else:
            print("--- Aviso: Arquivo 'requirements.txt' não encontrado. ---")

        # Passo 2: Rodar a aplicação Streamlit
        if os.path.exists("main.py"):
            print("--- Iniciando a aplicação Streamlit... ---")
            status_label.config(text="Status: Iniciando Streamlit! Verifique o navegador.")
            
            command_run = [sys.executable, "-m", "streamlit", "run", "main.py", "--server.maxUploadSize", "5000"]
            # Este comando vai prender o terminal, o que é esperado.
            subprocess.run(command_run)
            
            # Quando o servidor Streamlit for fechado, a execução continua aqui
            status_label.config(text="Status: Servidor Streamlit encerrado.")
            print("--- Servidor Streamlit encerrado. ---")
            
        else:
            status_label.config(text="ERRO: main.py não encontrado!")
            print("--- Erro: O arquivo principal 'main.py' não foi encontrado. ---")
    
    except subprocess.CalledProcessError as e:
        status_label.config(text="ERRO: Falha em um dos comandos.")
        print(f"Ocorreu um erro ao executar um sub-processo: {e}")
        print("Saída do erro:\n", e.stderr)
    except Exception as e:
        status_label.config(text="ERRO: Ocorreu um erro inesperado.")
        print(f"Ocorreu um erro inesperado: {e}")
    finally:
        # Reabilita o botão quando o processo terminar ou falhar
        start_button.config(state=tk.NORMAL)


def start_thread():
    """
    Função que desabilita o botão e inicia a thread de processamento.
    """
    # Desabilita o botão para evitar múltiplos cliques
    start_button.config(state=tk.DISABLED)
    # Cria e inicia a thread
    process_thread = threading.Thread(target=run_process)
    process_thread.daemon = True  # Permite que o programa feche mesmo se a thread estiver rodando
    process_thread.start()


# --- Configuração da Interface Gráfica (Tkinter) ---
root = tk.Tk()
root.title("Lançador de Projeto")
root.geometry("400x200")
root.resizable(False, False)

# Define uma fonte um pouco maior
default_font = font.nametofont("TkDefaultFont")
default_font.configure(size=11)

main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack(expand=True, fill=tk.BOTH)

# Rótulo de instrução
info_label = tk.Label(
    main_frame, 
    text="Clique no botão para instalar as dependências\ne iniciar a aplicação Streamlit.",
    justify=tk.CENTER
)
info_label.pack(pady=(0, 10))

# Botão para iniciar
start_button = tk.Button(
    main_frame, 
    text="Iniciar Aplicação", 
    command=start_thread,
    font=("Helvetica", 12, "bold"),
    bg="#00C46B",  # Cor de fundo verde
    fg="white",    # Cor do texto branca
    relief=tk.FLAT,
    pady=5
)
start_button.pack(fill=tk.X, pady=(5, 10))

# Rótulo para mostrar o status
status_label = tk.Label(main_frame, text="Status: Pronto para iniciar.")
status_label.pack()

# Inicia o loop da interface gráfica
root.mainloop()