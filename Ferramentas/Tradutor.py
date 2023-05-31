from Ferramentas.Char import char


def trocarSTR(mensagem, d1 = 'l', d2 = 'n'):
    #converter as letras e simbolos para numeros em string de forma otimizada
    soma = 0
    for pos, valor in enumerate(char()['digito'][d1]):
        repetir = mensagem.count(valor)
        for d in range(0, repetir):
            mensagem[mensagem.index(valor)] = char()['digito'][d2][pos]
        soma += repetir
        if soma == len(mensagem):
            return mensagem


def trocarN(mensagem, d1 = 'n', d2 ='l'):
    #se na mensagem tiver um numero, o mesmo sera convertido na forma escrita
    #se d1 e d2 for trocado fará o contrario
    for valor in range(0,10):
        mensagem = mensagem.replace(char()['numero'][d1][valor], char()['numero'][d2][valor])
    return mensagem


def tratar(mensagem):
    #se na mensagem tiver um numero, o mesmo sera convertido na forma escrita
    mensagem = trocarN(mensagem)

    #caso tiver um digito que saia do limite de Char() será substituido por '?'
    for valor in mensagem:
        if valor not in char()['digito']['l']:
            mensagem = mensagem.replace(valor, '?')

    #converter uma string em lista de digitos
    mensagem = [v for v in mensagem]

    #verificar se a lista é impar para adicionar um espaço para virar par
    if len(mensagem)%2!=0:
        mensagem.append(' ')

    #converter as letras e simbolos para numeros em string
    mensagem = trocarSTR(mensagem).copy()

    #Transformar em uma matriz com 2 linhas e seus elementos em inteiros
    mensagem = [[int(v) for v in mensagem[0:int(len(mensagem)/2)]], [int(v) for v in mensagem[(int(len(mensagem)/2))::]]]

    return mensagem


def resetar(mensagem):
    #transformar uma matriz em uma lista de elementos string(int)
    matriz = []
    for valor in mensagem:
        for elemento in valor:
            matriz.append(str(elemento))
    mensagem = matriz.copy()

    #converter os numeros para letras e simbolos
    mensagem = trocarSTR(mensagem,'n','l').copy()

    #transformar a lista em string
    msg =''
    for valor in mensagem:
        msg += valor
    mensagem = msg.strip()

    #os numeros escritos será convertidos em inteiros
    mensagem = trocarN(mensagem,'l','n')

    return mensagem