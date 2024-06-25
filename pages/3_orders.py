import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px
from PIL import Image
import plotly.graph_objects as go


# Set page configuration
st.set_page_config(page_title="orders", page_icon=":bar_chart", layout="wide")

st.title("Orders")

orders = 'Arquivos/nortwind-préprocessada/orders.csv'

orders_df = pd.read_csv(orders)

orders_df.columns = orders_df.columns.str.strip()

# sidebar
with st.sidebar:
    logo_teste = Image.open("img/icon-project.jpeg")
    st.image(logo_teste, use_column_width=True)
    st.subheader('Seleção de filtros:')
    
    # Adicione a opção "Todos" como a primeira opção para cada filtro
    fCategoria = st.selectbox(
        "Categoria do Cliente:",
        options=['Todos'] + list(orders_df['order_id'].unique())
    )

if fCategoria != 'Todos':
    orders_df = orders_df[orders_df['order_id'] == fCategoria]


# kpis

if not orders_df.empty:
    # Acessando os dados filtrados ou não filtrados, dependendo do filtro aplicado
    ship_address = orders_df.iloc[0]['ship_address']
    ship_region = orders_df.iloc[0]['ship_region']
    ship_postal_code = orders_df.iloc[0]['ship_postal_code']
    ship_via = orders_df.iloc[0]['ship_via']
    employee_id	 = orders_df.iloc[0]['employee_id']

# Layout com cartões no Streamlit
left_column,  middle_left_column, middle_column, middle_right_column, right_column = st.columns(5)

with left_column:
    st.info("📊 Address:")
    st.subheader(ship_address)

with middle_left_column:
    st.info("📊 ship_region:")
    st.subheader(ship_region)

with middle_column:
    st.info("📊 Postal Code:")
    st.subheader(ship_postal_code)

with middle_right_column:
    st.info("📊 ship_via:")
    st.subheader(ship_via)

with right_column:
    st.info("📊 employee_id	:")
    st.subheader(employee_id	)

st.markdown("---")

# Divisão da tela (Gráficos)

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
col5, col6 = st.columns(2)

# fig1

fig1 = px.bar(orders_df, x='ship_name', y='freight', title='Distribuição de Clientes por País', labels={'country': 'País', 'count': 'Número de Clientes'}, color='freight', color_continuous_scale='Blues')
col1.plotly_chart(fig1, use_container_width=True)

# fig 2 

fig2 = px.choropleth(orders_df,
                    locations='ship_country',
                    locationmode='country names',
                    color='freight',
                    hover_name='ship_country',
                    title = 'PIB País',
                    color_continuous_scale='Viridis'
                    )
col2.plotly_chart(fig2, use_container_width=True)


fig3 = px.bar(orders_df,x="ship_city", y="freight", title="Total de Clientes por Método de Pagamento")
fig3.update_layout(
    xaxis_title="Método de Pagamento",
    yaxis_title="Clientes"
)
col3.plotly_chart(fig3, use_container_width=True)

