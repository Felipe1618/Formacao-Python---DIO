arquivo = open("C:\Users\felip\OneDrive\Área de Trabalho\DIO\Formação Python Developer\5 - Manipulacao_arquivos\teste.txt", "w")

arquivo.write("Escrevendo dados em um novo arquivo")
arquivo.writelines(["\n", "escrevendo", "\n", "um", "\n", "novo", "\n", "tesxto"])
arquivo.close()