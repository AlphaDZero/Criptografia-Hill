from Ferramentas.Char import char

def converter(mensagem, numero = 1):
    if numero == 1:
        for valor in range(0,10):
            mensagem = mensagem.replace(char()['numero']['n'][valor], char()['numero']['l'][valor])

        for valor in mensagem:
            if valor not in char()['digito']['l']:
                mensagem = mensagem.replace(valor, '?')

        matriz = []
        for valor in mensagem:
            matriz.append(valor)
        
        mensagem = matriz.copy()
        matriz.clear()

        for cont, elemento in enumerate(mensagem):
            for enum, valor in enumerate(char()['digito']['l']):
                if elemento == valor:
                    mensagem[cont] = elemento.replace(elemento, char()['digito']['n'][enum])
                    break
        
        #separar em 2 linhas a mensagem e transformar em int
    
    else:
        pass
    
    return mensagem

print(converter('Delta11Δ'))
