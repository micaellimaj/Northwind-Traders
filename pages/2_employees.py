import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px
from PIL import Image
import plotly.graph_objects as go


# Set page configuration
st.set_page_config(page_title="Employees", page_icon=":bar_chart", layout="wide")

st.title("Employees")

caminho_arquivo = 'Arquivos/nortwind-préprocessada/employees.csv'

employees_df = pd.read_csv(caminho_arquivo)

employees_df.columns = employees_df.columns.str.strip()


# sidebar
with st.sidebar:
    logo_teste = Image.open("img/icon-project.jpeg")
    st.image(logo_teste, use_column_width=True)
    st.subheader('Seleção de filtros:')
    
    # Adicione a opção "Todos" como a primeira opção para cada filtro
    fCategoria = st.selectbox(
        "Categoria do Cliente:",
        options=['Todos'] + list(employees_df['employee_id'].unique())
    )

if fCategoria != 'Todos':
    employees_df = employees_df[employees_df['employee_id'] == fCategoria]

# kpis

if not employees_df.empty:
    # Acessando os dados filtrados ou não filtrados, dependendo do filtro aplicado
    address = employees_df.iloc[0]['address']
    region = employees_df.iloc[0]['region']
    postal_code = employees_df.iloc[0]['postal_code']
    phone = employees_df.iloc[0]['home_phone']
    fax = employees_df.iloc[0]['reports_to']

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

city_counts = employees_df['city'].value_counts().reset_index()
city_counts.columns = ['city', 'count']

fig1 = px.bar(city_counts, x='city', y='count', title='Distribuição de Clientes por País', labels={'country': 'País', 'count': 'Número de Clientes'}, color='count', color_continuous_scale='Blues')
col1.plotly_chart(fig1, use_container_width=True)

# Graph2
country_counts = employees_df['country'].value_counts().reset_index()
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


# fig 4

# Função para criar um link clicável com um ícone de imagem
def create_image_link(url: str) -> str:
    return f'<a href="{url}" target="_blank"><img src="{url}" width="100"></a>'

# Adicionando coluna com links clicáveis para as imagens


# Criando a tabela com Plotly
fig3 = go.Figure(
    data=[
        go.Table(
            columnwidth=[1, 1, 0.5],
            header=dict(values=["first_name", "photo_path","	birth_date","hire_date"]),
            cells=dict(values=[employees_df.first_name, employees_df.birth_date,employees_df.hire_date,employees_df['photo_path']])
        )
    ]
)
st.plotly_chart(fig3, use_container_width=True)



counts = employees_df.groupby(['title','last_name'])["employee_id"].count().reset_index()




# Criando o gráfico de treemap
fig = px.treemap(counts, 
                 path=['title', 'last_name'], 
                 values='employee_id', 
                 title='Distribuição de Clientes por País, Região e Cidade')
st.plotly_chart(fig, use_container_width=True)
