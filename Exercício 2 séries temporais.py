print("--- EXERCÍCIO 2: TRADUÇÃO DE DIAS E EXPORTAÇÃO DE ARQUIVOS ---")

# 1. MAPEAMENTO DE TRADUÇÃO DO INGLÊS PARA PORTUGUÊS
dias_pt = {
    'Monday': 'Segunda-feira',
    'Tuesday': 'Terça-feira',
    'Wednesday': 'Quarta-feira',
    'Thursday': 'Quinta-feira',
    'Friday': 'Sexta-feira',
    'Saturday': 'Sábado',
    'Sunday': 'Domingo'
}

# 2. APLICANDO A TRADUÇÃO NA COLUNA
df_vendas['Dia_Semana_Venda'] = df_vendas['Dia_Semana_Venda'].map(dias_pt)

# 3. CALCULANDO O RELATÓRIO DE DESEMPENHO POR CATEGORIA
relatorio_categoria = df_vendas.groupby('Categoria').agg(
    Faturamento_Total=('Valor_Venda', 'sum'),
    Tempo_Medio_Entrega_Dias=('Tempo_Entrega_Dias', 'mean')
).reset_index()

print("📊 RELATÓRIO DE EFICIÊNCIA POR CATEGORIA:")
print(relatorio_categoria)

# 4. EXPORTANDO OS RESULTADOS PARA ARQUIVOS REAIS NO SEU COMPUTADOR/COLAB
df_vendas.to_csv('vendas_tratadas.csv', index=False, encoding='utf-8-sig')
relatorio_categoria.to_excel('relatorio_executivo_categoria.xlsx', index=False)

print("\n💾 Arquivos 'vendas_tratadas.csv' e 'relatorio_executivo_categoria.xlsx' gerados com sucesso!")