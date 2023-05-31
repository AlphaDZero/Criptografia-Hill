from Tradutor import tratar, resetar
from variavel import msg

def conversor(mensagem,reset = False):
    if reset:
        return resetar(mensagem)
    return tratar(mensagem)

print(conversor(conversor(msg), True))