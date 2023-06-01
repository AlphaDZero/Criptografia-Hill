from Ferramentas.Char import char

#Essa função faz os numeros estar no limite de char
tamanho_char = len(char()['digito']['n'])
normalizar = lambda x : x -(x // tamanho_char)*tamanho_char if x -(x // tamanho_char)*tamanho_char != 0 else tamanho_char

# a chave é uma matriz de ordem 2 e determinate igual a 1
# a representação de uma chave é [[a11, a12], [a21, a22]]
def multi_Matriz(mensagem, lista_chave):
    for valor in lista_chave:
        mensagem = [[normalizar(valor[0]*mensagem[0][s] + valor[1]*mensagem[1][s]) for s in range(0, len(mensagem[0]))],[normalizar(valor[2]*mensagem[0][s] + valor[3]*mensagem[1][s]) for s in range(0, len(mensagem[0]))]]
    return mensagem
