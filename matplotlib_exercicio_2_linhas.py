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

vendas_id = [f"Venda {i+1}" for i in range(len(tabela_vendas))]

plt.plot(vendas_id, tabela_vendas['Valor_Total'], marker='o', color='blue', linewidth=2, linestyle='--')

plt.title('Evolução do Faturamento por Operação de Venda')
plt.xlabel('Histórico de Operações')
plt.ylabel('Valor da Operação (R$)')

plt.grid(True, linestyle=':', alpha=0.6)

plt.show()

