import pandas as pd
import numpy as np

print("--- ETAPA 1: DIAGNÓSTICO E LIMPEZA PROFISSIONAL DE DADOS ---")

dados_brutos = {
    'ID_Veiculo': ['VEC-101', 'VEC-102', 'VEC-103', 'VEC-104', 'VEC-105', 'VEC-106'],
    'Filial': ['  São Paulo ', 'sao paulo', 'Ribeirão Preto', 'RIBEIRAO PRETO', 'Curitiba', 'curitiba '],
    'Km_Rodados': [1250.0, 980.5, None, 2100.0, 1450.0, 1100.0],  
    'Custo_Combustivel': ['R$ 4500.50', 'R$ 3200.00', 'R$ 5100.20', 'R$ 8900.00', 'R$ 5200.00', 'R$ 3900.00'], 
    'Status': ['Ativo', 'Ativo', 'Ativo', 'Manutenção', 'Ativo', 'Inativo']
}

df_frota = pd.DataFrame(dados_brutos)
print("\n🔴 1. BASE BRUTA ORIGINAL (COMO VEIO DO SISTEMA):")
print(df_frota)

print("\n----------------------------------------------------------------------")

df_frota['Filial'] = df_frota['Filial'].str.strip().str.upper()

df_frota['Custo_Combustivel'] = df_frota['Custo_Combustivel'].str.extract(r'(\d+\.\d+|\d+)').astype(float)

media_km = df_frota['Km_Rodados'].mean()
df_frota['Km_Rodados'] = df_frota['Km_Rodados'].fillna(media_km)

print("🟢 2. BASE TRATADA E PADRONIZADA (PRONTA PARA ENGENHARIA DE DADOS):")
print(df_frota)
print(f"\nTipos das colunas após tratamento:\n{df_frota.dtypes}")


import pandas as pd
import numpy as np
import unicodedata



print("--- ETAPA 1 CORRIGIDA: REMOVENDO ACENTOS E ESPAÇOS ---")

def remover_acentos(texto):
    if isinstance(texto, str):
        return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')
    return texto
dados_brutos = {
    'ID_Veiculo': ['VEC-101', 'VEC-102', 'VEC-103', 'VEC-104', 'VEC-105', 'VEC-106'],
    'Filial': ['  São Paulo ', 'sao paulo', 'Ribeirão Preto', 'RIBEIRAO PRETO', 'Curitiba', 'curitiba '],
    'Km_Rodados': [1250.0, 980.5, None, 2100.0, 1450.0, 1100.0],
    'Custo_Combustivel': ['R$ 4500.50', 'R$ 3200.00', 'R$ 5100.20', 'R$ 8900.00', 'R$ 5200.00', 'R$ 3900.00'],
    'Status': ['Ativo', 'Ativo', 'Ativo', 'Manutenção', 'Ativo', 'Inativo']
}

df_frota = pd.DataFrame(dados_brutos)

df_frota['Filial'] = df_frota['Filial'].apply(remover_acentos).str.strip().str.upper()

df_frota['Custo_Combustivel'] = df_frota['Custo_Combustivel'].str.extract(r'(\d+\.\d+|\d+)').astype(float)

media_km = df_frota['Km_Rodados'].mean()
df_frota['Km_Rodados'] = df_frota['Km_Rodados'].fillna(media_km)

print("🟢 BASE TRATADA SEM ACENTOS:")
print(df_frota[['ID_Veiculo', 'Filial', 'Km_Rodados', 'Custo_Combustivel']])



print("--- ETAPA 2: ENGENHARIA DE MÉTRICAS E AGRUPAMENTOS POR FILIAL ---")

df_frota['Custo_por_KM'] = df_frota['Custo_Combustivel'] / df_frota['Km_Rodados']

relatorio_filiais = df_frota.groupby('Filial').agg(
    Custo_Total_RS=('Custo_Combustivel', 'sum'),
    Km_Total_Rodados=('Km_Rodados', 'sum'),
    Media_Custo_por_KM=('Custo_por_KM', 'mean')
).reset_index()

relatorio_filiais = relatorio_filiais.sort_values(by='Media_Custo_por_KM', ascending=False)

print("\n📊 RELATÓRIO EXECUTIVO POR FILIAL (ORDENADO PELO CUSTO/KM):")
print(relatorio_filiais)



import matplotlib.pyplot as plt

print("--- ETAPA 3: GERANDO O GRÁFICO EXECUTIVO PARA A DIRETORIA ---")

plt.figure(figsize=(10, 5))

barras = plt.bar(relatorio_filiais['Filial'], relatorio_filiais['Media_Custo_por_KM'], color=['#d9534f', '#f0ad4e', '#5cb85c'])

plt.title('Eficiência Operacional: Custo Médio por KM Rodado por Filial', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Filiais da Empresa', fontsize=12)
plt.ylabel('Custo Médio (R$/KM)', fontsize=12)
plt.ylim(0, 5) 

for barra in barras:
    altura = barra.get_height()
    plt.text(barra.get_x() + barra.get_width()/2., altura + 0.1,
             f'R$ {altura:.2f}',
             ha='center', va='bottom', fontsize=11, fontweight='bold')

plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()
