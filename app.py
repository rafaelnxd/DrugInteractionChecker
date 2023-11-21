import streamlit as st
import json

def carregar_substancias():
    with open("substancias.json", "r", encoding="utf-8") as file:
        substancias = json.load(file)

    # Carrega as descrições dos arquivos de texto e as interações
    for substancia, info in substancias.items():
        descricao_file = info.get("descricao_file")
        interacoes_file = info.get("interacoes_file")

        if descricao_file:
            with open(descricao_file, "r", encoding="utf-8") as descricao_file:
                info["descricao"] = descricao_file.read()

        if interacoes_file:
            with open(interacoes_file, "r", encoding="utf-8") as interacoes_file:
                info["interacoes"] = interacoes_file.read()

    return substancias

def main():
    st.title("Drug Interaction Checker")

    # Carrega substâncias do arquivo JSON
    substancias = carregar_substancias()

    # Barra de navegação
    tabs = ["Substâncias", "Interações", "Condições", "Sobre"]
    choice = st.radio("Escolha uma opção:", tabs)

    # Renderiza a aba escolhida
    if choice == "Substâncias":
        show_substancias(substancias)
    elif choice == "Interações":
        show_interacoes(substancias)
    

def show_substancias(substancias):
    st.subheader("Lista de Substâncias")

    # Mostra o nome das substâncias como uma lista
    selected_substancia = st.selectbox("Selecione uma substância:", list(substancias.keys()))

    # Mostra a descrição quando uma substância é selecionada
    st.write(f"Descrição: {substancias[selected_substancia]['descricao']}")

def show_interacoes(substancias):
    st.subheader("Interações")

    # Lista de substâncias para escolher
    substancias_disponiveis = list(substancias.keys())

    # Select Box para escolher substâncias
    substancia_1 = st.selectbox("Selecione a primeira substância:", substancias_disponiveis)

    # Select Box para escolher substâncias
    substancia_2 = st.selectbox("Selecione a segunda substância:", substancias_disponiveis)

    
    #st.write(f"Interações: {substancias[substancia_2]['interacoes']}")

  



def show_condicoes(substancias):
    st.subheader("Condições")

    # Lista de condições para escolher
    #condicoes_disponiveis = list(condicoes.keys())
   
   

if __name__ == "__main__":
    main()
