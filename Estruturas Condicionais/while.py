opcao = -1

while opcao != 0:
    opcao = int(input("[1]Sacar \n[2]Extrato \n[0]Sair \n:"))

    if opcao == 1:
        print('Sacando ...')
    elif opcao == 2:
        print('Exibindo extrato...')
    else:
        print('Saindo.')

while True:
    numero = int(input('Informe um número: '))
    if numero ==10:
        break       #para(interrompe) uma instrução

    if numero % 2 == 0:
        continue        #pula uma instrução

    print(numero)
