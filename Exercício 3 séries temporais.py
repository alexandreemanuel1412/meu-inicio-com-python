import matplotlib.pyplot as plt

print("--- ETAPA 3: GRÁFICO DE TENDÊNCIA TEMPORAL DE VENDAS ---")

# 1. Agrupando as vendas por data
vendas_por_dia = df_vendas.groupby('Data_Venda')['Valor_Venda'].sum().reset_index()

# 2. Criando o gráfico de linha temporal
plt.figure(figsize=(10, 5))
plt.plot(vendas_por_dia['Data_Venda'], vendas_por_dia['Valor_Venda'], 
         marker='o', color='#2b5c8f', linewidth=2.5, markersize=8)

plt.title('Evolução Diária do Faturamento (Julho/2026)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Data da Venda', fontsize=12)
plt.ylabel('Faturamento (R$)', fontsize=12)

# Formatação e grid
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(rotation=45)

# Adicionando os valores nos pontos do gráfico
for idx, row in vendas_por_dia.iterrows():
    plt.text(row['Data_Venda'], row['Valor_Venda'] + 150, 
             f"R$ {row['Valor_Venda']:.0f}", 
             ha='center', fontsize=9, fontweight='bold')

plt.tight_layout()
plt.show()