class Bicicleta: #classe
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano 
        self.valor = valor
        self.marcha = 1
    
    def buzinar(self):
        print("Plim Plim...")

    def correr(self):
        print("Pedalando ...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicileta parada")

    def trocar_marcha(self):
        print("Trocando de marcha...")
        #self = self 

        # def _trocar_marcha(n_marcha):
        #     if n_marcha > self.marcha:
        #         print("Marcha trocada...")
        #     else:
        #         print("Marcha não trocada...")

    #def __str__(self):
        #return f"Bicicleta: cor = {self.cor}, modelo = {self.modelo}, ano = {self.ano}, valor = {self.valor}"
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta("vermelha", "thc", 2024, 800)
b1.buzinar() #equivalente (chamada do método 'buzinar')
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 200)
Bicicleta.buzinar(b2)
#b2.valor() #o objeto 'b2' possui os próprios atributos, mas utiliza dos métodos da classe 'Bicileta'
b2.trocar_marcha()
