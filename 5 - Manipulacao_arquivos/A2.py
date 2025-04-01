arquivo = open("5 - Manipulacao_arquivos\teste.txt", "r")

print(arquivo.read())
arquivo.close()

for linha in arquivo.readline():
    print(linha)

arquivo.close()

while (linha := arquivo.readline()):
    print(linha)

arquivo.close()

