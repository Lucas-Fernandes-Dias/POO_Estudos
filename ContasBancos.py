from datetime import datetime
import pytz
from random import randint


class ContaCorrente:
    '''
    Cria um objeto ContaCorrente para gerenciar as contas dos clientes.

    Atributos:
        nome(str) = nome do cliente ( nome completo, igual constar no documento oficial apresentado na abertura da conta)
        cpf(str) = cpf do cliente ( deve ser colocado com pontos e traço, conforme é na receita federal)
        saldo (int) = é a quantia que o cliente dispoe em conta corrente
        limite (int) = limite disponivel para o cliente
        agencia (int) = agencia responsável pela conta do cliente ( deve ser 4 numeros antes do traço e 1 numero após o traço)
        num conta (int) = é o numero da conta do cliente dentro do banco ( o numero deve conter o traço e o digíto)
        transções (str) = é onde fica armazenada as transações do cliente ( dados das ultimas transações)




    '''

    @staticmethod
    def data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%y %H: %M:%S')

    def __init__(self, nome, cpf, agencia, num_conta):
        self._nome = nome
        self._cpf = cpf
        self._saldo = 0
        self._limite_especial = None
        self._agencia = agencia
        self._num_conta = num_conta
        self._transacoes = []
        self.cartoes = []

    def consultar_saldo(self):
        if self._saldo < 0:
            print("Você entro no limite especial em R$ {:,.2f}".format(self._limite_especial() - self._saldo))
            print('O seu saldo atual é de R$ {:,.2f}'.format(self._saldo))
        elif self._saldo > 0:
            print('O seu saldo atual é de R$ {:,.2f}'.format(self._saldo))

    def consultar_limite_especial(self):
        if self._saldo < 0:
            print('O seu limite especial atual é de R$ {:,.2f}'.format(self._limite_especial()))
            print('O seu saldo atual é R$ {:,.2f}'.format(self._saldo))
            print('O seu limite especial disponivel é de R$ {:,.2f}'.format(self._limite_especial() - self._saldo))
        else:
            print('O seu limite especial atual é de R$ {:,.2f}'.format(self._limite_especial()))

    def depositar(self, valor):
        self._saldo += valor
        self._transacoes.append((valor, self._saldo, ContaCorrente.data_hora()))


    def _limite_especial(self):
        self._limite_especial = 1000
        return self._limite_especial

    def sacar_dinheiro(self, valor):
        if self._saldo - valor < self._limite_especial():
            print('Seu saldo atual não é suficiente para essa transação.')
            print('Seu saldo atual é de R$ {:,.2f}'.format(self._saldo))
        else:
            self._saldo -= valor
            print('Seu saldo atual é de R$ {:,.2f}'.format(self._saldo))
            self._transacoes.append((-valor, self._saldo, ContaCorrente.data_hora()))

    def consultar_historio_transaçoes(self):
        print('Histórico de transações')
        print('Valor', 'Saldo', 'Data/Hora')
        for transaçao in self._transacoes:
            print(transaçao)

    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append((-valor, self._saldo, ContaCorrente.data_hora()))
        conta_destino._saldo += valor
        conta_destino._transacoes.append((valor, conta_destino._saldo, ContaCorrente.data_hora()))

class CartaoCredito:

    @staticmethod
    def data():
        data = datetime.now()
        return data

    def __init__(self, titular, conta_corrente):
        self._num = randint(1000000000000000, 9999999999999999)
        self._titular = titular
        self._validade = '{}/{}'.format(CartaoCredito.data().month, CartaoCredito.data().year + 4)
        self._cod_seguranca = '{}{}{}'.format(randint(0, 9), randint(0, 9), randint(0, 9))
        self._limite_cartao = 1000
        self.senha = '1234'
        self._conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print('NOVA SENHA INVÁLIDA')






