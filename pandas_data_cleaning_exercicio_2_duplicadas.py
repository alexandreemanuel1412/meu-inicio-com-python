import pandas as pd

print("--- EXERCÍCIO 2: TRATANDO DUPLICADAS E TEXTO NO SETOR DE SERVIÇOS ---")

dados_streaming = {
    'ID_Cliente': [101, 102, 103, 101, 104, 102], # ID 101 e 102 estão duplicados!
    'Plano': ['Premium', 'basic', 'Standard', 'Premium', 'STANDARD', 'basic'], # Mistura de maiúsculas/minúsculas
    'Mensalidade_R$': [55.90, 34.90, 45.90, 55.90, 45.90, 34.90]
}

df_streaming = pd.DataFrame(dados_streaming)
print("\n🔴 DADOS DE ASSINATURA SUJOS:")
print(df_streaming)

print("\n--------------------------------------------------")

df_streaming['Plano'] = df_streaming['Plano'].str.upper()

df_streaming_limpo = df_streaming.drop_duplicates()

print("🟢 DADOS DE ASSINATURA LIMPOS (Faturamento Real Garantido):")
print(df_streaming_limpo)