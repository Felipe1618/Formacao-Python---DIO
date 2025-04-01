def mensagem(nome):
    print("executando 'mensagem'")
    return f'Oi {nome}'

def mensagem_longa(nome):
    print("executando mensagem")


#Conceito de 'factory' -> retorna mais de um tipo de objetos
def Calculadora(operacao): 
    def soma(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def mult(a, b):
        return a * b

    def div(a, b):
        return a / b

    match operacao:
        case "+":
            return soma
        case "-":
            return sub
        case "*":
            return mult
        case "/":
            return div

op = Calculadora("+")
print(op(10, 5)) #operacao 'soma'