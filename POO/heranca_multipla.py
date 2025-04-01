class Animal:
    def __init__(self, nome, n_patas):
        self.nome = nome
        self.n_patas = n_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)


class FalarMixin():
    def falar(self):
        return "Falei!"


class Cachorro(Mamifero):
    pass


class Gato(Mamifero, FalarMixin):
    pass


class Leao(Mamifero):
    pass



class Ornitorrinco(Mamifero, Ave):
    def __init__(self, nome, cor_bico, cor_pelo, n_patas):
        # print(Ornitorrinco.__mro__)
        super().__init__(nome=nome, cor_pelo=cor_pelo, cor_bico=cor_bico, n_patas=n_patas)

    def __str__(self):
        return "Ornitorrinco"


ornitorrinco = Ornitorrinco(nome="Perry", n_patas=4, cor_pelo="marrom", cor_bico="preto")
print(ornitorrinco)

tony = Gato(nome="Tony", n_patas=4, cor_pelo="cinza")
print(tony)
print(tony.falar())

class Foo: 
    def hello(self): 
        print(self.__class__.__name__.lower()) 

    class Bar(Foo): 
        def hello(self): return super().hello() bar = Bar() bar.hello()