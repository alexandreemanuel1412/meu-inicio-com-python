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



faturamento_total = tabela_vendas['Valor_Total'].sum()

media_quantidades = tabela_vendas['Quantidade'].mean()



print("--- INDICADORES DE NEGÓCIO ---")
print(f"💰 O faturamento total da empresa foi de: R$ {faturamento_total:.2f}")
print(f"📦 A média de sacas por venda foi de: {media_quantidades} sacas")