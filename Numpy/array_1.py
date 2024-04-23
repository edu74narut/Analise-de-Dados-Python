import numpy as np

produtos = ['VideoGames','Filmes','Esporte','Roupas']
custo = [100, 200, 300, 400]
venda = [150, 230, 330, 490]

lucro = np.array(venda) - np.array(custo)
for indice in range(0,4):
    print('{0} R${1}'.format(produtos[indice],lucro[indice]))

# Números aleatórios  --> print(np.random.rand())
print(np.zeros((5, 4)))
