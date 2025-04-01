from datetime import datetime, timedelta, date, time

tipo_carro = "P" #P, M, G
tempo_P = 30
tempo_M = 45
tempo_G = 60
data_atual = datetime.now()

if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_P)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes=tempo_M)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
else: 
    data_estimada = data_atual + timedelta(minutes=tempo_G)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")

print(date.today() - timedelta(days=1)) #parametro 'days'