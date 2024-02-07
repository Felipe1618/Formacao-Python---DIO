menu = '''
Escolha uma das opções abaixo:
[d] Deposito
[s] Sacar 
[e] Extrato
[x] Sair
=> '''
LIMITE_NUMERO_SAQUES = 3
saldo = 0.0
LIMITE_POR_SAQUE = 500
extrato = ""
numero_saques = 0

while True:
    opcao = input(menu)
    if opcao == 'd':
        valor_deposito = float(input("Digite o valor de depósito: "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += (f"Depositado: R${valor_deposito:.2f}\n")
        else:
            print("Operação falhou! O valor informado é invalido\n")

    elif opcao == 's':
        valor_saque = float(input("Digite o valor a ser sacado: "))
        excedeu_saldo = valor_saque > saldo
        excedeu_limite_saque = valor_saque > LIMITE_POR_SAQUE
        excedeu_numero_saques = numero_saques > LIMITE_NUMERO_SAQUES

        if excedeu_saldo:
            print("\nOperação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite_saque:
            print(f"\nOperação falhou! Limite máximo por saque é de R$ {LIMITE_POR_SAQUE}")
        elif excedeu_numero_saques:
            print(f"\nVocê já realizou {numero_saques} saques hoje, ultrapassando o limite")

        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += (f"Saque: R$ {valor_saque:.2f}\n")
            numero_saques += 1
        else:
            print("\nOperação falhou! O valor informado é inválido.")

    elif opcao == 'e':
        print("Extrato".center(20,"="))
        print("\nNão foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo atual: R${saldo:.2f} | Numero de Saques Realizados hoje: {numero_saques}")

    elif opcao == "x": 
        print("Saindo ... Obrigado por usar nossos serviços!")
        break
    else:
        print("\nOpção inválida, por favor selecione novamente a opção desejada:")