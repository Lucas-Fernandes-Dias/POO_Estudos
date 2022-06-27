class ContaCorrente:

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None

    def consultar_saldo(self):
        if self.saldo < 0:
            print("Você entro no limite especial em R$ {:,.2f}".format(self._limite_especial() - self.saldo))
            print('O seu saldo atual é de R$ {:,.2f}'.format(self.saldo))
        elif self.saldo > 0:
            print('O seu saldo atual é de R$ {:,.2f}'.format(self.saldo))

    def consultar_limite_especial(self):
        if self.saldo < 0:
            print('O seu limite especial atual é de R$ {:,.2f}'.format(self._limite_especial()))
            print('O seu saldo atual é R$ {:,.2f}'.format(self.saldo))
            print('O seu limite especial disponivel é de R$ {:,.2f}'.format(self._limite_especial() - self.saldo))
        else:
            print('O seu limite especial atual é de R$ {:,.2f}'.format(self._limite_especial()))

    def depositar(self, valor):
        self.saldo += valor

    def _limite_especial(self):
        self.limite = -1000
        return self.limite

    def sacar_dinheiro(self, valor):
        if self.saldo - valor < self._limite_especial():
            print('Seu saldo atual não é suficiente para essa transação.')
            print('Seu saldo atual é de R$ {:,.2f}'.format(self.saldo))
        else:
            self.saldo -= valor
            print('Seu saldo atual é de R$ {:,.2f}'.format(self.saldo))





# meu programa
conta_Lucas = ContaCorrente('Lucas', '327.253.848-85')
conta_Lucas.consultar_saldo()

# depositando um valor qualquer

conta_Lucas.depositar(12000)

# sancando um valor qualquer

conta_Lucas.sacar_dinheiro(7000)
conta_Lucas.consultar_limite_especial()

conta_Lucas.sacar_dinheiro(5500)
conta_Lucas.consultar_saldo()





