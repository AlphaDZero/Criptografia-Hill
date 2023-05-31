from Ferramentas.Tradutor import tratar, resetar

def conversor(mensagem,reset = False):
    if reset:
        return resetar(mensagem)
    return tratar(mensagem)
