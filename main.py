from ContasBancos import ContaCorrente, CartaoCredito



# meu programa
conta_Lucas = ContaCorrente('Lucas', '111.222.333-45', 1234, 2323-0)
conta_Leticia = ContaCorrente('Leticia', '222.254.236-87',  1234, 2424-0)

cartao_Lucas = CartaoCredito('Lucas', conta_Lucas)

print(conta_Lucas.cartoes[0]._titular)
print(cartao_Lucas._num)
print(cartao_Lucas._validade)
print(cartao_Lucas._cod_seguranca)


cartao_Lucas.senha = '258'
print(cartao_Lucas._senha)