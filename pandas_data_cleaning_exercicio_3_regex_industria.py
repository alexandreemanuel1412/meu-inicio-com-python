import pandas as pd

print("--- EXERCÍCIO 3: EXTRAÇÃO DE TEXTO E CONVERSÃO DE TIPOS NA INDÚSTRIA ---")

dados_industria = {
    'Robo_ID': ['R-01', 'R-02', 'R-03', 'R-04'],
    'Tempo_Solda': ['12.5 seg', '14.2 segundos', '11.8s', '13.0 seg'] # Texto puro para a máquina!
}

df_fabrica = pd.DataFrame(dados_industria)
print("\n🔴 TABELA DA FÁBRICA (O Pandas lê a coluna de tempo como TEXTO/object):")
print(df_fabrica)
print(f"Tipo original da coluna: {df_fabrica['Tempo_Solda'].dtype}")

print("\n--------------------------------------------------")

df_fabrica['Tempo_Solda'] = df_fabrica['Tempo_Solda'].str.extract(r'(\d+\.\d+|\d+)')

df_fabrica['Tempo_Solda'] = df_fabrica['Tempo_Solda'].astype(float)

print("🟢 TABELA INDUSTRIAL LIMPA (Pronta para calcular médias de eficiência):")
print(df_fabrica)
print(f"Novo tipo da coluna (Mágica da Engenharia): {df_fabrica['Tempo_Solda'].dtype}")