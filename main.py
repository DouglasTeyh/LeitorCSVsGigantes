import streamlit as st
import pandas as pd
import io

def run_app():
    """
    Função para fazer upload de múltiplos arquivos e exibir cada um com paginação.
    """
    st.set_page_config(layout="wide")

    st.title("Visualizador de Múltiplos CSVs com Paginação")
    st.write("Faça o upload de um ou mais arquivos CSV para explorá-los de forma interativa e segura.")

    # Componente para upload de MÚLTIPLOS arquivos
    uploaded_files = st.file_uploader(
        "Escolha um ou mais arquivos CSV", 
        type="csv",
        accept_multiple_files=True
    )

    if uploaded_files:
        # Loop para processar cada arquivo que foi enviado
        for file in uploaded_files:
            st.divider()
            st.header(f"Análise do arquivo: `{file.name}`")

            with st.spinner(f"Processando `{file.name}`..."):
                try:
                    # Usamos uma função com cache para cada arquivo
                    @st.cache_data
                    def load_data(uploaded_file):
                        # É preciso resetar o ponteiro do arquivo dentro da função cacheada
                        uploaded_file.seek(0)
                        list_of_dataframes = []
                        chunk_size = 500000
                        for chunk in pd.read_csv(
                            uploaded_file, 
                            chunksize=chunk_size, 
                            low_memory=False, 
                            encoding='latin-1', 
                            sep=';'
                        ):
                            list_of_dataframes.append(chunk)
                        
                        df = pd.concat(list_of_dataframes, ignore_index=True)
                        return df

                    df = load_data(file)
                    total_rows = len(df)

                    st.success(f'Arquivo `{file.name}` processado! Total de linhas: {total_rows:,}'.replace(',', '.'))
                    
                    st.subheader("Explore a Tabela com Paginação")

                    # --- CONTROLES DE PAGINAÇÃO INDIVIDUAIS ---
                    # Usamos colunas para organizar os controles
                    col1, col2, col3 = st.columns([0.3, 0.3, 0.4])

                    with col1:
                        # O parâmetro 'key' é ESSENCIAL para que cada controle seja único
                        rows_per_page = st.number_input(
                            "Linhas por página", 
                            min_value=50, max_value=1000, value=100, step=50,
                            key=f"rows_per_page_{file.name}"
                        )
                    
                    total_pages = (total_rows // rows_per_page) + (1 if total_rows % rows_per_page > 0 else 0)
                    
                    with col2:
                        page_number = st.number_input(
                            "Página", 
                            min_value=1, max_value=total_pages, value=1, step=1,
                            key=f"page_number_{file.name}"
                        )
                    
                    with col3:
                        st.text(f"Mostrando página {page_number} de {total_pages}")

                    start_index = (page_number - 1) * rows_per_page
                    end_index = start_index + rows_per_page
                    
                    st.dataframe(df.iloc[start_index:end_index])
                    
                    with st.expander("Visualizar informações do DataFrame"):
                        buffer = io.StringIO()
                        df.info(buf=buffer, verbose=True)
                        s = buffer.getvalue()
                        st.text(s)

                except Exception as e:
                    st.error(f"Ocorreu um erro ao processar o arquivo `{file.name}`: {e}")
    else:
        st.info("Por favor, faça o upload de um ou mais arquivos CSV para começar.")

if __name__ == "__main__":
    run_app()