from Hill import CriptoMatriz

cripto = CriptoMatriz()


def aviso():
    print('''

                                    
                                                   Aviso!
    
* A chave é uma matriz de ordem 2 que por representação é a11 a12 a21 a22.
* Para funcionar corretamente a criptografia é necessario que o determinante da chave seja igual a 1.
* Para descriptografar é necessario colocar a matriz inversa da chave no lugar da chave.
* Se colocou mais de uma chave, para descriptografar usa a mesma regra só que invertendo a ordem das chaves.
* Para sair do loop basta digitar "break" logo depois da criptografia ou aperte enter se quer continuar.
    

    ''')


while True:
    aviso()
    mensagem = str(input('Digite a mensagem: '))
    cripto.setMsg(mensagem)
    while True:
        try:
            nchave = int(input('Quantidade de chaves: '))
            break
        except:
            print('apenas numero inteiro\n')
    while True:
        for indice in range(0, nchave):
            chave = str(input(f'Digite a chave {indice + 1}: '))
            cripto.setChave(chave)
            if cripto.cond == False:
                break
        if cripto.cond:
            break
    print(f'\nCriptografia "{cripto.msg}"\n')
    if input().strip() == 'break':
        break
