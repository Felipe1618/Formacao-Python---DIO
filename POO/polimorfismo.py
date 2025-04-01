class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        return super().voar()
    
class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa")

#FIXME: Exemplo RUIM do uso de herança para 'ganhar' o método voar
class Aviao(Passaro): #Polimorfismo -> Classe 'Aviao' está utilizando o método 'voar' da classe 'Passaro'
    def voar(self):
        print("Avião está decolando...")

def plano_voo(obj):
    obj.voar() #polimorfismo -> método 'voar' sendo usado no objeto 'obj'

p1 = Pardal()
p2 = Avestruz()

plano_voo(p1)
plano_voo(p2)

plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())
