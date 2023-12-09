MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input('Informe sua idade: '))
if idade >= MAIOR_IDADE:
    print('Maior de idade, pode tirar a CNH.')

if idade < MAIOR_IDADE:
    print("Menor de Idade, não pode tirar a CNH.")

if idade >= MAIOR_IDADE:
    print('Você já tem mais de 18 anos, portanto, precisa fazer o curso de habilitação')
else:
    print('Ainda não pode tirar a CNH.')

if idade >= MAIOR_IDADE:
    print('Maior de idade, pode tirar a CNH.')
elif idade == IDADE_ESPECIAL:
    print('Pode fazer aulas teóricas, mas não pode fazer aulas práticas.')
else:
    print('Ainda não pode tirar a CNH.')