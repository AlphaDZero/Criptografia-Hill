from Ferramentas.Transformador import conversor
from Ferramentas.Calculo import multi_Matriz
class Hill:

    def __init__(self, mensagem = ' ', lista_chave = [[1,0,0,1]]) -> None:
        self.mensagem    =  mensagem
        self.lista_chave =  lista_chave

    def criptografar(self):
        self.mensagem = conversor(self.mensagem)
        self.mensagem = multi_Matriz(self.mensagem,self.lista_chave)
        self.mensagem = conversor(self.mensagem, True)
