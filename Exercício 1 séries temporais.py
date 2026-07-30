print("--- EXERCÍCIO 1: TRASFORMAÇÃO PARA DATETIME E ENGENHARIA DE TEMPO ---")

# 1. CONVERTENDO COLUNAS DE TEXTO PARA DATETIME DE FATO
df_vendas['Data_Venda'] = pd.to_datetime(df_vendas['Data_Venda'])
df_vendas['Data_Entrega'] = pd.to_datetime(df_vendas['Data_Entrega'])

# 2. CALCULANDO O TEMPO DE ENTREGA (Lead Time) EM DIAS
df_vendas['Tempo_Entrega_Dias'] = (df_vendas['Data_Entrega'] - df_vendas['Data_Venda']).dt.days

# 3. EXTRAINDO O DIA DA SEMANA EM QUE A VENDA ACONTECEU
# .dt.day_name() traz o nome do dia em inglês (ex: Wednesday, Thursday)
df_vendas['Dia_Semana_Venda'] = df_vendas['Data_Venda'].dt.day_name()

print("🟢 BASE APÓS TRATAMENTO TEMPORAL:")
print(df_vendas[['ID_Pedido', 'Data_Venda', 'Tempo_Entrega_Dias', 'Dia_Semana_Venda']])

print("\n🔍 NOVO TIPO DAS COLUNAS:")
print(df_vendas[['Data_Venda', 'Data_Entrega']].dtypes)