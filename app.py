import pandas as pd
import plotly.express as px
import streamlit as st

# Caminho para o arquivo
arq_caminho = 'vehicles_us.csv'

car_data = pd.read_csv(arq_caminho)  # lendo os dados

st.header('Vendas de carros')  # criando o titulo

# criando botão para o histograma
hist_button = st.button('Criar histograma')
if hist_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    # criar um histograma
    fig_hist = px.histogram(car_data, x="odometer")
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig_hist, use_container_width=True)

# criando botão para o grafico de disperão
scatter_button = st.button('Criar gráfico de dispersão')
if scatter_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    # criar um grafico de dispersão
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig_scatter, use_container_width=True)
