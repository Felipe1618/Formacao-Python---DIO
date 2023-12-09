texto = input('Escreva uma palavra qualquer: ')
VOGAIS   = 'AEIOU'

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
    else:  #pouco usado
        print()
        print('Execute no final do laço: ')