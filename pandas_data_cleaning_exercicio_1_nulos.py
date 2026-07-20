import pandas as pd
import numpy as np

print("--- EXERCÍCIO 1: IDENTIFICANDO E TRATANDO DADOS NULOS ---")

dados_sujos = {
    'Filial': ['Norte', 'Sul', 'Leste', 'Oeste', 'Centro'],
    'Produto': ['Soja', 'Milho', None, 'Soja', 'Trigo'],  
    'Sacas_Estoque': [1500, None, 1200, 1500, 1800],      
    'Responsavel': ['Carlos', 'Ana', 'Bruno', 'Carlos', 'Diego']
}

tabela_cooperativa = pd.DataFrame(dados_sujos)
print("\n🔴 TABELA ORIGINAL COM ERROS (COMO VEIO DO SISTEMA):")
print(tabela_cooperativa)

print("\n--------------------------------------------------")

print("🔍 PROCURANDO CÉLULAS EM BRANCO (NULAS):")
print(tabela_cooperativa.isna().sum())

print("\n--------------------------------------------------")

media_sacas = tabela_cooperativa['Sacas_Estoque'].mean()
tabela_cooperativa['Sacas_Estoque'] = tabela_cooperativa['Sacas_Estoque'].fillna(media_sacas)

tabela_cooperativa['Produto'] = tabela_cooperativa['Produto'].fillna("Não Informado")

print("🟢 TABELA CORRIGIDA E TRATADA (PRONTA PARA O DIRETOR):")
print(tabela_cooperativa)