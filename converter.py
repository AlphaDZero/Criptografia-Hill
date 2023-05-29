from Ferramentas.Char import char

def converter(mensagem, numero = 1):
    if numero == 1:
        for valor in range(0,10):
            mensagem = mensagem.replace(char()['numero']['n'][valor], char()['numero']['l'][valor])

        for valor in mensagem:
            if valor not in char()['digito']['l']:
                mensagem = mensagem.replace(valor, '?')
    
    else:
        pass
    
    return mensagem

print(converter('Delta11Δ'))
