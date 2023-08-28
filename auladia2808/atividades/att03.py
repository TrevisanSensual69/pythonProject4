class ContaBancaria:
    def __init__(self, titular, numero):
        self.titular = titular
        self.saldo = 0
        self.numero = numero

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def exibir_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")


conta1 = ContaBancaria("João", "12345")
conta1.depositar(1000)
conta1.sacar(300)
conta1.exibir_saldo()

conta2 = ContaBancaria("Maria", "54321")
conta2.depositar(1500)
conta2.sacar(200)
conta2.exibir_saldo()
