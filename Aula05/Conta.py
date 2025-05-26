class Conta:
    logado = True
    tarifa = 1.99

    def __init__(self):
        self.__saldo = 0.0

    def getSaldo(self):
        if self.logado:
            return self.__saldo
        else:
            return None

    def setSaldo(self, valor):
        if valor > self.__saldo:
            self.__saldo = valor

    def __discountTaxes(self):
        self.__saldo -= self.tarifa

    def sacar(self, valor):
        if self.__saldo >= valor + self.tarifa:
            self.__saldo -= valor
            self.__discountTaxes()
            print("Saque realizado!")
        else:
            return("Saldo insuficiente!")

    @property
    def saldo(self):
        if self.logado:
            return self.__saldo
        else:
            return None

    @saldo.setter
    def saldo(self, valor):
        if valor > self.__saldo:
            self.__saldo = valor

x = Conta()
x.setSaldo(100)
print(x.getSaldo())

y = Conta()
y.saldo = 100
print(y.saldo)