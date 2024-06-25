import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px
from PIL import Image


# Set page configuration
st.set_page_config(page_title="store", page_icon=":bar_chart", layout="wide")

# Your other imports and code
# import other_libraries

# Streamlit code
st.title("Customers")
# Additional Streamlit commands

categories_df = pd.read_csv("Arquivos/nortwind-préprocessada/categories.csv",sep=';')
st.session_state["data"] = categories_df


caminho_arquivo = 'Arquivos/nortwind-préprocessada/customers.csv'

# Ler o arquivo CSV
customers_df = pd.read_csv(caminho_arquivo)

# Verificar e remover espaços em branco nos nomes das colunas
customers_df.columns = customers_df.columns.str.strip()

# Tentar acessar a coluna 'contact_name'

cliente_counts = customers_df['contact_name'].value_counts()


# sidebar
with st.sidebar:
    logo_teste = Image.open("img/icon-project.jpeg")
    st.image(logo_teste, use_column_width=True)
    st.subheader('Seleção de filtros:')
    
    # Adicione a opção "Todos" como a primeira opção para cada filtro
    fCategoria = st.selectbox(
        "Categoria do Cliente:",
        options=['Todos'] + list(customers_df['customer_id'].unique())
    )

if fCategoria != 'Todos':
    customers_df = customers_df[customers_df['customer_id'] == fCategoria]

# KPI

# Definindo os valores que você quer exibir
if not customers_df.empty:
    # Acessando os dados filtrados ou não filtrados, dependendo do filtro aplicado
    address = customers_df.iloc[0]['address']
    region = customers_df.iloc[0]['region']
    postal_code = customers_df.iloc[0]['postal_code']
    phone = customers_df.iloc[0]['phone']
    fax = customers_df.iloc[0]['fax']

# Layout com cartões no Streamlit
left_column,  middle_left_column, middle_column, middle_right_column, right_column = st.columns(5)

with left_column:
    st.info("📊 Address:")
    st.subheader(address)

with middle_left_column:
    st.info("📊 Region:")
    st.subheader(region)

with middle_column:
    st.info("📊 Postal Code:")
    st.subheader(postal_code)

with middle_right_column:
    st.info("📊 Phone:")
    st.subheader(phone)

with right_column:
    st.info("📊 Fax:")
    st.subheader(fax)

st.markdown("---")



# Divisão da tela (Gráficos)

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
col5, col6 = st.columns(2)

# Criando o gráfico de barras 1

#cliente_counts = customers_df['contact_name'].value_counts()
city_counts = customers_df['city'].value_counts().reset_index()
city_counts.columns = ['city', 'count']
 

fig1 = px.bar(city_counts, x='city', y='count', title='Distribuição de Clientes por País', labels={'country': 'País', 'count': 'Número de Clientes'}, color='count', color_continuous_scale='Blues')
col1.plotly_chart(fig1, use_container_width=True)

# Graph2
country_counts = customers_df['country'].value_counts().reset_index()
country_counts.columns = ['country', 'count']



fig2 = px.choropleth(country_counts,
                    locations='country',
                    locationmode='country names',
                    color='count',
                    hover_name='country',
                    title = 'PIB País',
                    color_continuous_scale='Viridis'
                    )
col2.plotly_chart(fig2, use_container_width=True)

# Graph 3

counts2 = customers_df.groupby(['company_name','contact_title'])["customer_id"].count().reset_index()

fig3 = px.bar(counts2,x="company_name", y="customer_id", title="Total de Clientes por Método de Pagamento")
fig3.update_layout(
    xaxis_title="Método de Pagamento",
    yaxis_title="Clientes"
)
col3.plotly_chart(fig3, use_container_width=True)

counts = customers_df.groupby(['contact_name','contact_title'])["customer_id"].count().reset_index()


# Criando o gráfico de treemap
fig = px.treemap(counts, 
                 path=['contact_title', 'contact_name'], 
                 values='customer_id', 
                 title='Distribuição de Clientes por País, Região e Cidade')
st.plotly_chart(fig, use_container_width=True)
