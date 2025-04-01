from abc import ABC, abstractmethod
#importação módulo abstrato 'abc'

class controleRemoto(ABC):
    @abstractmethod # interface 'ligar' com a classe abstrata '@abstractmethod'
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass
    
    @property #propriedade / decorador
    @abstractproperty #propriedade/decorador para criar classe abstrata 'marca'
    def marca(self):
        pass

class ControleTV(controleRemoto):
    def ligar(self):
        print("Ligando TV ...")
        print('Ligar')

    def desligar(self):
        print("Desligando TV ...")
        print('Desligar')

    def marca(self):
        return 'Sony'


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)