#Exercicio 1
# num1 = int(input())
# num2 = int(input())

# class Calculadora:
#   @staticmethod
#   def soma(num1, num2):
#     return num1 + num2

  
# # Criando uma instância da calculadora
# calc = Calculadora()

# resultado = calc.soma(num1, num2)
# print(resultado)


#Exercicio 2
# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

# #TODO: Crie um método para retornar as informações formatas com Nome e Idade:    
#     def __str__(self) -> str:
#       return (f"Nome: {self.nome}, Idade: {self.idade}")

# # Entrada do usuário
# nome = input()
# idade = int(input())

# #TODO: Crie uma instância da pessoa:
# pessoa1 = Pessoa(nome, idade)
# #TODO: Chame o método para retornar as informações formatadas e imprima o resultado:
# print(pessoa1)

# Exercicio 3
class ConversorTemperatura:
   def celsius_para_fahrenheit(self, celsius):
      return 32 + (1.8 * celsius)

celsius = float(input())

# Criação do método de conversão (instanciação)
conversor = ConversorTemperatura()

#Chamada do método de conversão
fahrenheit = conversor.celsius_para_fahrenheit(celsius)

#Exibe o resultado da conversão
print(fahrenheit)