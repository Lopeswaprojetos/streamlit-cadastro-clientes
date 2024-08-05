import streamlit as st

st.title("Cadastro de Clientes")

# Coleta de dados do cliente
nome = st.text_input("Digite o nome do cliente")
endereco = st.text_input("Digite o endereço do cliente")
dt_nasc = st.date_input("Escolha a data de nascimento")  # Certifique-se de que isso está correto
tipo_cliente = st.selectbox("Escolha a categoria do cliente", ("Pessoa Física", "Pessoa Jurídica"))

# Botão de cadastro
cadastrar = st.button("Cadastrar cliente")

# Ação do botão de cadastro
if cadastrar:
    with open("clientes.csv", "a") as arquivo:
        arquivo.write(f"{nome}, {endereco}, {dt_nasc}, {tipo_cliente}\n")
        st.success("Cliente cadastrado com sucesso!")

