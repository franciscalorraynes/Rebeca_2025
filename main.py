import pandas as pd
import plotly.express as px
import streamlit as st

# Título do dashboard - DASHCOVID - Um Painel de Informações sobre a COVID-19 - Ano 2020]
st.title('DASHCOVID - Um Painel de Informações sobre a COVID-19 - Ano 2020')
# Configuração do layout
st.set_page_config(page_title='DASHCOVID', layout='wide')


# Carregamento dos dados - /content/WHO_time_series.csv
df = pd.read_csv('WHO_time_series.csv')

# Conversão da data Date_reported

df['Date_reported'] = pd.to_datetime(df['Date_reported'])
# --- GRÁFICO 1: LINHA GLOBAL --- Date_reported, Cumulative_cases, Cumulative_cases, Casos Acumulados de Covid-19 por País (2020)
fig1 = px.line(df, x = 'Date_reported', y='Cumulative_cases', color='Country', title='Casos Acumulados de Covid-19 por País (2020)')

fig1.update_layout(xaxis_title = 'Data', yaxis_title = 'Casos Acumulados')
#streamlit

st.plotly_chart(fig1, use_container_width=True)
# --- GRÁFICO 2: PIZZA BRASIL x EUA x ÍNDIA --- Country. 'Brazil', 'United States of America', 'India
#Filtrar apenas os 3 países
df_three = df[df['Country'].isin(['Brazil', 'United States of America', 'India'])]

# Pegar os valores do último dia disponível 
df_last = df_three.sort_values('Date_reported').groupby('Country').tail(1)

#plotar o grafico - Comparativo Total de Casos – Brasil x EUA x Índia
fig2 = px.pie(df_last, names='Country', values='Cumulative_cases', title='Comparativo Total de Casos – Brasil x EUA x Índia')
#stemlit
st.plotly_chart(fig2, use_container_width=True)

