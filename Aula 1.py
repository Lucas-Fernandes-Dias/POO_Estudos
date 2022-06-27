# criado nossa primeira classe em Python
# sempre que quiser criar uma classe, deve fazer o seguinte:

#classe Nome_Classe(object):

# dentro da classe, você vai criar a "função" (método) __init__
# esse método é quem define o que acontece quando você cria uma instância de classe

class TV():

    def __init__(self):
        self.cor = 'preta'
        self.ligada = False
        self.tamanho = 55
        self.canal = 'NetFlix'
        self.volume = 10

    def mudar_canal(self, novo_canal):
        self.canal =novo_canal



tv_sala = TV()
tv_quarto = TV()

tv_sala.cor = 'branca'

print(tv_sala.cor)
print(tv_quarto.cor)

tv_quarto.tamanho = 32
tv_sala.mudar_canal('SporTV2')

print(tv_sala.canal)
print(tv_quarto.canal)
print(tv_sala.tamanho)
print(tv_quarto.tamanho)




