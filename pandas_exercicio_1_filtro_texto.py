import pandas as pd

dados = {
    'Filial': ['Sul', 'Norte', 'Sul', 'Centro', 'Norte'],
    'Produto': ['Saca de Milho', 'Saca de Soja', 'Saca de Trigo', 'Saca de Milho', 'Saca de Soja'],
    'Quantidade': [100, 50, 200, 30, 80],
    'Valor_Total': [8500.00, 6000.00, 14000.00, 2550.00, 9600.00]
}


tabela_vendas = pd.DataFrame(dados)

print("--- TABELA COMPLETA DE VENDAS ---")
display(tabela_vendas)


vendas_sul = tabela_vendas[tabela_vendas['Filial'] == 'Sul']

print("--- RELATÓRIO: APENAS VENDAS DA FILIAL SUL ---")
display(vendas_sul)