numero_meses = int(input())
meses_ingles = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

if 1<= numero_meses <= 12:
    nome_mes = meses_ingles[numero_meses - 1]
    nome_mes_formato = nome_mes[0].upper() + nome_mes[1:].lower()
    print(nome_mes_formato)
else:
    print("Mes invalido")