import pandas as pd

tabela = pd.read_csv("bcdata.sgs.22711.csv", sep=';', decimal=',')
print(tabela)
tabela["data"] = pd.to_datetime(tabela['data'])
print(tabela['data'])
tabela = tabela.sort_values(by=('data'))
print(tabela.max())
