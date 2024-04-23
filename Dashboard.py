import pandas
import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide")
df = pandas.read_csv('supermarket_sales.csv', sep=';', decimal=',')
df["Date"] = pandas.to_datetime(df["Date"])
df = df.sort_values(by=("Date"))

df["Month"] = df["Date"].apply(lambda x: str(x.year) + '-'+ str(x.month))
month = st.sidebar.selectbox("Mês", df["Month"].unique())

df_filtrado = df[df["Month"] == month]

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

fig_date = px.bar(df_filtrado, x="Date", y="Total"
                  , color='City',title="Faturamento por mês")
col1.plotly_chart(fig_date, use_container_width=True)

fig_prod = px.bar(df_filtrado, x="Date", y="Product line"
                  , color='City',title="Faturamento por tipo de produto",
                  orientation="h")
col2.plotly_chart(fig_prod, use_container_width=True)

city_total = df_filtrado.groupby("City")[["Total"]].sum().reset_index()
fig_city = px.bar(df_filtrado, x="City", y="Total"
                  , title="Faturamento por filial")
col3.plotly_chart(fig_city, use_container_width=True)

fig_kind = px.pie(df_filtrado, values="Total", names="Payment"
                  , title="Faturamento por tipo de pagamento")
col4.plotly_chart(fig_kind, use_container_width=True)

city_total = df_filtrado.groupby("City")[["Rating"]].mean().reset_index()
fig_rating = px.bar(df_filtrado, x="City", y="Rating"
                  , title="Avaliação")
col5.plotly_chart(fig_rating, use_container_width=True)




