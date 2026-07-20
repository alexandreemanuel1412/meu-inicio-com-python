import pandas as pd

print("--- EXERCÍCIO 4: FILTRAGEM DE OUTLIERS EM ENERGIA RENOVAVEL ---")

dados_energia = {
    'Hora': ['01:00', '02:00', '03:00', '04:00', '05:00'],
    'Megawatts_Gerados': [45.2, -999.0, 48.1, 0.0, 51.3], # -999.0 é um erro claro de sensor/comunicação!
    'Status_Sensor': ['OK', 'ERRO_REDE', 'OK', 'MANUTENCAO', 'OK']
}

df_energia = pd.DataFrame(dados_energia)
print("\n🔴 DADOS DE ENERGIA COM ERROS DE LEITURA (-999 e Geração Zero por Manutenção):")
print(df_energia)

tabela_estilizada = df_streaming_limpo.style.set_properties(**{'text-align': 'center'}).set_table_styles(
    [{'selector': 'th', 'props': [('text-align', 'center')]}]
)

print("\n--------------------------------------------------")

filtro_energia_limpa = (df_energia['Megawatts_Gerados'] > 0) & (df_energia['Status_Sensor'] == 'OK')
df_energia_limpa = df_energia[filtro_energia_limpa]

print("🟢 DADOS DE ENERGIA COERENTES (Prontos para Auditoria de ESG):")
print(df_energia_limpa)