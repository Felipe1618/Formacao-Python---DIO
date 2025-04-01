class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_data_nasc(self, ano, mes, dia, nome):
        idade = 2024 - ano
        return Pessoa(nome, idade)
    
    @staticmethod
    def maior_idade(idade):
        return idade >= 18


p = Pessoa.criar_data_nasc(1997, 11, 5, 'Felipe')
print(p.nome, p.idade)

print(Pessoa.maior_idade(18))
print(Pessoa.maior_idade(17))
