## 🖥️ Como Executar o Projeto

Existem duas maneiras de obter os arquivos do projeto: clonando o repositório (recomendado) ou baixando o arquivo ZIP.

### Opção 1: Clonar o Repositório (Recomendado)

Esta é a forma padrão de se trabalhar com projetos de código. Requer que você tenha o [Git](https://git-scm.com/) instalado.

1.  **Abra o Terminal** (PowerShell no Windows, ou Terminal no Linux).

2.  **Clone o projeto** para a sua máquina usando o comando abaixo. Ele criará uma nova pasta com todos os arquivos do projeto.
    
    ```bash
    # Troque a URL pela URL do seu repositório no GitHub
    git clone [https://github.com/DouglasTeyh/LeitorCSVsGigantes.git](https://github.com/DouglasTeyh/LeitorCSVsGigantes.git)
    ```

3.  **Navegue para a nova pasta** que foi criada.
    ```bash
    # Exemplo
    cd LeitorCSVsGigantes
    ```
4.  Agora, pule para as **Instruções para seu Sistema Operacional** abaixo para continuar a instalação.


### Opção 2: Baixar o Arquivo ZIP

Se você não quer usar o Git, pode baixar o projeto diretamente.

1.  Na página do repositório no GitHub, clique no botão verde **"< > Code"**.
2.  Clique em **"Download ZIP"**.
3.  **Extraia o arquivo .zip** em um local de sua preferência.
4.  Abra o terminal e navegue para a pasta que você acabou de extrair.

---

###  **Instruções para Windows**

*Após clonar ou baixar o projeto e entrar na pasta pelo terminal:*

1.  **(Opcional, mas recomendado) Crie e Ative um Ambiente Virtual**:
    ```powershell
    python -m venv venv
    .\venv\Scripts\activate
    ```
2.  **Execute o Lançador**:
    ```powershell
    python run.py
    ```
    Clique no botão na janela que aparecer para iniciar a aplicação.

---

### 🐧 **Instruções para Linux**

*Após clonar ou baixar o projeto e entrar na pasta pelo terminal:*

1.  **(Opcional, mas recomendado) Crie e Ative um Ambiente Virtual**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
2.  **Execute o Lançador**:
    ```bash
    python3 run.py
    ```
    Clique no botão na janela que aparecer para iniciar a aplicação.
