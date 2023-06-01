from Criptografia_Hill import Hill
#primeiro importar a classe Hill

#criar um objeto e passar os parametros
#lembre-se que a chave é uma matriz deve ter o determinante igual a 1
#representação da chave é [a11, a12, a21, a22]

msg = Hill('Hello World!',[[2,5,3,8]])
msg.criptografar() #inicia a criptografia
print(msg.mensagem) #mostra a criptografia

#para decriptografar é necessário ter uma chave que é a matriz inversa da chave dada
#matriz inversa é [a22, -a12, -a21, a11]

msg.lista_chave = [[8,-5,-3,2]] #nova lista de chaves
msg.criptografar() #iniciar novamente
print(msg.mensagem) #mostra a mensagem original

print('-'*30)

#Obs. caso por mais de uma chave, para decriptografar é necessário;
# 1. ter a matriz inversa de cada uma
# 2. por todas na ordem contraria

#exemplo
mensagem = Hill('Exemplo 2',[[2,5,3,8],[3,11,1,4]])
mensagem.criptografar()
print(mensagem.mensagem) #mostra a criptografia
mensagem.lista_chave = [[4,-11,-1,3],[8,-5,-3,2]]
mensagem.criptografar()
print(mensagem.mensagem) #mostra a mensagem original