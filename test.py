from Ferramentas.Calculo import multi_Matriz
from Ferramentas.Transformador import conversor
from variavel import msg

msg = conversor(msg)
msg = multi_Matriz(msg,[[2,5,3,8]])
print(conversor(msg,True))
#msg = multi_Matriz(msg,[[8,-5,-3,2]])
#print(conversor(msg,True))