nome = "feLIpe"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "    ola mundo       "
print(texto)
print(texto.strip())
print(texto.rstrip())
print(texto.lstrip())

menu = 'Python'
print(menu.center(14))
print(menu.center(20, "_"))
print("P-y-t-h-o-n")

#laço de repetição equivalente ao exemplo de baixo
for letra in menu:
    print(letra, end="-")
print()

print("-".join(menu))


