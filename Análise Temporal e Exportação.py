import pandas as pd
import numpy as np

print("--- ANÁLISE TEMPORAL E IMPORTAÇÃO DE DADOS ---")

# Simulando um arquivo bruto exportado do sistema ERP da empresa
dados_vendas = {
    'ID_Pedido': ['PED-501', 'PED-502', 'PED-503', 'PED-504', 'PED-505', 'PED-506', 'PED-507'],
    'Data_Venda': ['2026-07-01', '2026-07-02', '2026-07-05', '2026-07-05', '2026-07-10', '2026-07-12', '2026-07-15'],
    'Data_Entrega': ['2026-07-04', '2026-07-08', '2026-07-07', '2026-07-12', '2026-07-13', '2026-07-20', '2026-07-18'],
    'Categoria': ['Eletrônicos', 'Acessórios', 'Eletrônicos', 'Eletrodomésticos', 'Acessórios', 'Eletrodomésticos', 'Eletrônicos'],
    'Valor_Venda': [2500.00, 150.00, 3200.00, 1800.00, 80.00, 2100.00, 4100.00]
}

df_vendas = pd.DataFrame(dados_vendas)

print("\n📦 BASE BRUTA DE VENDAS RECEBIDA:")
print(df_vendas)

# Verificando os tipos de dados atuais
print("\n🔍 TIPOS DE DADOS ATUAIS (Repare em Data_Venda e Data_Entrega):")
print(df_vendas.dtypes)