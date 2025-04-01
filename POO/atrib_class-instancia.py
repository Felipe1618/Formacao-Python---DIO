class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    #Formatação para retorno da classe 'Estudante'
    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)
    

aluno_1 = Estudante("Felipe", 1) #atributos de instâncias
aluno_2 = Estudante("Maria", 2)

print(aluno_1)
print(aluno_2)

mostrar_valores(aluno_1, aluno_2)

Estudante.escola = "Python"
aluno_3 = Estudante("Giovana", 3)
mostrar_valores(aluno_1, aluno_2, aluno_3)
