nome = "Felipe"
idade = 26
profissao = "Programador"

print("old style '%'".center(50, "-"))
print("Olá, me chamo %s. Eu tenho %d anos, trabalho como %s\n" %(nome, idade, profissao))

print("format".center(50, "-"))
print("Olá, me chamo {}. Eu tenho {} anos, trabalho como {}.\n".format(nome, profissao, idade))

print("'f' string".center(50, "-"))
print(f"Olá, me chamo {nome}. Tenho {idade}, trabalho como {profissao}.\n".format(nome, idade, profissao))

print("'f' string 2".center(50, "-"))
print(f"Olá, me chamo {nome}. Tenho {idade}, trabalho como {profissao}.".format(profissao, nome, idade)) #mudando a ordem das variaveis, saída continua sendo a mesma do primeiro caso.

saldo = 45.55
print(f"Nome: {nome} | Idade: {idade} | Saldo: {saldo:.2f}")
print(f"Nome: {nome} | Idade: {idade} | Saldo: {saldo:.1f}")