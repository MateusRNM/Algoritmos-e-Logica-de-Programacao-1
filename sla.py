class ObjetoQualquer:
    cor = "Vermelho"
    lista = [10]

    def mudarCor(self, c):
        self.cor = c
    
    def pegarLista(self):
        return self.lista

objeto = ObjetoQualquer()
print(objeto.cor)
print(objeto.lista)
print(objeto.pegarLista().pop(0))
print(objeto.lista)