class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo
        self._nro_agencia = nro_agencia
    
    def depositar(self, valor):
        # ...
        self._saldo += valor
    
    def sacar(self, valor):
        # ...
        self._saldo -= valor
        
    def mostrar_saldo(self):
        # ...
        return self._saldo
    


conta = Conta("0001", 100)

print(Conta.mostrar_saldo(conta))


