lista1 = [45, 22, None, 67]
lista2 = [45, None, 98, None]
lista3 = [0,0,0,0]

def trocar(listA, listB):
    for c in range(0, listA.count(None)):
        listA[listA.index(None)] = listB[listA.index(None)]
    return listA

lista2 = trocar(lista2,lista1)
print(lista2)

print(lista3.count(1))