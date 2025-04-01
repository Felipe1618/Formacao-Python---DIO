class Conta:
    def __init__(self, n_agencia, saldo=0):
        self._saldo = saldo #'_saldo' -> atributo privado
        self.n_agencia = n_agencia

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo


conta = Conta('1234', 100)
conta.depositar(200)
print(conta.n_agencia)
print(conta.mostrar_saldo())