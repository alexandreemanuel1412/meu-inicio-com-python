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


tabela_vendas['Quantidade'] >= 100

grandes_vendas = tabela_vendas[tabela_vendas['Quantidade'] >=100]


print("--- FILTRAR POR VOLUME DE IGUAL E SUPERIOR A 100 ---")
display(grandes_vendas)





