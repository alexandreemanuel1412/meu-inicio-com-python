import pandas as pd
import matplotlib.pyplot as plt

dados = {
    'Filial': ['Sul', 'Norte', 'Sul', 'Centro', 'Norte'],
    'Produto': ['Saca de Milho', 'Saca de Soja', 'Saca de Trigo', 'Saca de Milho', 'Saca de Soja'],
    'Quantidade': [100, 50, 200, 30, 80],
    'Valor_Total': [8500.00, 6000.00, 14000.00, 2550.00, 9600.00]
}

tabela_vendas = pd.DataFrame(dados)

print("--- TABELA COMPLETA DE VENDAS ---")
display(tabela_vendas)

plt.bar(tabela_vendas['Produto'], tabela_vendas['Quantidade'], color='green')

plt.title('Volume de Sacas Vendidas por Produto')
plt.xlabel('Produtos')
plt.ylabel('Quantidade de Sacas')

plt.show()