from Ferramentas.Char import char

def converter(mensagem, numero = 1):
    if numero == 1:

        #se na mensagem tiver um numero, o mesmo sera convertido na forma escrita
        for valor in range(0,10):
            mensagem = mensagem.replace(char()['numero']['n'][valor], char()['numero']['l'][valor])

        #caso tiver um digito que saia do limite de Char() será substituido por '?'
        for valor in mensagem:
            if valor not in char()['digito']['l']:
                mensagem = mensagem.replace(valor, '?')

        #converter uma string em lista de digitos
        matriz = []
        for valor in mensagem:
            matriz.append(valor)     
        mensagem = matriz.copy()
        matriz.clear()

        #converter as letras e simbolos para numeros em string
        for cont, elemento in enumerate(mensagem):
            for enum, valor in enumerate(char()['digito']['l']):
                if elemento == valor:
                    mensagem[cont] = elemento.replace(elemento, char()['digito']['n'][enum])
                    break
        
        #verificar se a lista é par, caso contrario ira adicionar um espaço

        #Transformar em uma matriz com 2 linhas e seus elementos em inteiros
    
    else:
        pass
    
    return mensagem

print(converter('Delta11Δ'))
