import pandas as pd
import matplotlib.pyplot as plt

dados = {
    'Filial': ['Sul', 'Norte', 'Sul', 'Centro', 'Norte'],
    'Produto': ['Saca de Milho', 'Saca de Soja', 'Saca de Trigo', 'Saca de Milho', 'Saca de Soja'],
    'Quantidade': [100, 50, 200, 30, 80],
    'Valor_Total': [8500.00, 6000.00, 14000.00, 2550.00, 9600.00]
}

tabela_vendas = pd.DataFrame(dados)

faturamento_por_produto = tabela_vendas.groupby('Produto')['Valor_Total'].sum()

plt.figure(figsize=(6, 6))
plt.pie(
    faturamento_por_produto, 
    labels=faturamento_por_produto.index,
    autopct='%1.1f%%',                      
    startangle=140,                        
    colors=['#2ca02c', '#ff7f0e', '#1f77b4']
)

plt.title('Participação de Cada Produto no Faturamento Total')

plt.show()
