import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

#os.mkdir(ROOT_PATH / "novo-diretorio-A5") #Cria um diretório

#arquivo = open(ROOT_PATH / "novo.txt", "w") # abre arquivo 'novo.txt'
#arquivo.close()

#os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt") #renomeia arquivo 'novo' para 'alterado'

#os.remove(ROOT_PATH / "alterado.txt")

#shutil.move(ROOT_PATH / "alterado.txt", ROOT_PATH / "novo-diretorio-A5" / "alterado.txt") #mover arquivo para 'novo-diretorio'

arquivoPython = open(ROOT_PATH / "5 - Manipulacao_arquivos" / ROOT_PATH / "A6-tratamentos_excecoes.py", "w")