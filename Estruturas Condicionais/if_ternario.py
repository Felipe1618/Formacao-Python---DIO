saldo = 100
saque = 500

status = 'sucesso' if saldo >= saque else 'falha'

print(f'{status} ao realizar o saque!')