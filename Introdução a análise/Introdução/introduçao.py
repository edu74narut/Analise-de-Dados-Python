import pandas
import streamlit as st
st.title('Entendo o Streamlit')
tabela = pandas.read_excel("Vendas.xlsx", engine="openpyxl")
print(tabela)


faturamentoTotal = tabela['Valor Final'].sum()
print('Faturamento total da empresa: {0}'.format(faturamentoTotal))
st.write('Faturamento total da empresa: {0}'.format(faturamentoTotal))

faturamento_por_loja = tabela[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(faturamento_por_loja)

faturamento_por_produtoLoja = tabela[['ID Loja' ,'Produto', 'Valor Final']].groupby(['ID Loja', 'Produto']).sum()
print(faturamento_por_produtoLoja)
faturamento_por_produtoLoja

