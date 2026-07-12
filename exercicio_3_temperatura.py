leituras_temperatura = [2.5, 3.0, 7.5, 1.8, 6.2]

for temp in leituras_temperatura:
    if temp > 5.0:
        print(f"🚨 ALERTA: Temperatura perigosa ({temp}°C)! Verificar refrigeração.")
    else:
        print(f"❄️ Estável: Temperatura segura ({temp}°C).")