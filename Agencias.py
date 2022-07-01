from random import randint

class agencia:

    def __init__(self, telefone, cnpj, numero_agencia):
        self.telefone = telefone
        self.cnoj = cnpj
        self.numero_agencia = numero_agencia
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []


    def verificar_caixa(self):
        if self.caixa < 1000000:
            print('Caixa abaixo do nível recomendado. Caixa Atual: R$ {:,.2f}'.format(self.caixa))
        else:
            print('Valor do Caixa está em nível aceitável. Caixa Atual: R$ {:,.2f}'.format(self.caixa))

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
            self.caixa -= valor
        else:
            print('Empréstimo não é possível, Dinheiro não disponível em caixa.')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


class agenciaVirtual(agencia):

    def __init__(self, site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, 1000)
        self.caixa = 1000000
        self.caixa_paypal = 0

    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.caixa_paypal += valor

    def saque_paypal(self, valor):
        self.caixa += valor
        self.caixa_paypal -= valor


class agenciaComum(agencia):

    def __init__(self, telefone, cnpj, numero=randint(1001, 9999)):
        super().__init__(telefone, cnpj, numero)
        self.caixa = 1000000


class agenciaPremium(agencia):

    def __init__(self, telefone, cnpj, numero=randint(1000, 9999)):
        super().__init__(telefone, cnpj,  numero)
        self.caixa = 10000000

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            super().adicionar_cliente(nome, cpf, patrimonio)
        else:
            print('Cliente não tem patrimonimo minímo necessário para fazer parte da Agência Premium.')



agencia_Assis = agencia('3322-2233', '01.555.487.0001-87', '143')
agencia_virtual = agenciaVirtual('www.agenciavirtual.com.br', '32215-5959', '12352350001')
agencia_premium = agenciaPremium('3232-2587','0154878484')
agencia_premium.verificar_caixa()
agencia_premium.adicionar_cliente('Lucas', '324236456513225', 15000000)
print(agencia_premium.clientes)
