class CriptoMatriz:


    def __init__(self,chave = '1 0 0 1',msg = ''):
        self.msg            =  str(msg)
        self.chave          =  chave
        self.matriz         =  [[],[]]
        self.matrizcripto   =  []
        self.cond           =  False
    

    def setChave(self,chave):
        self.chave = chave
        self.iniciar()
    

    def setMsg(self,msg):
        self.msg = str(msg)
    

    def nstr(self,c):
        from Digitos import lista
        if c == 0:
            for elemento in range(0,len(lista()[2])):
                self.msg = self.msg.replace(lista()[3][elemento],lista()[2][elemento])
        if c == 1:
            for indice in range(0,len(lista()[2])):
                self.msg = self.msg.replace(lista()[2][indice],lista()[3][indice]) 


    def analiseFormat(self):
        try:
            for elemento in self.chave.split():
                self.matriz[0].append(int(elemento))
        except:
            return True
        if len(self.matriz[0]) != 4:
            return True
        return False
    

    def strFormat(self):
        from Digitos import lista
        for elemento in self.msg:
            if elemento not in lista()[0] and elemento not in lista()[1]:
                self.msg = self.msg.replace(elemento,' ')
        if len(self.msg) % 2 != 0:
            self.msg += ' '
        self.matriz[1] = [cada for cada in self.msg]
        for d in range(0,len(self.matriz[1])):
            for indice in range(0,len(lista()[1])):
                self.matriz[1][d] = self.matriz[1][d].replace(lista()[0][indice],lista()[1][indice])
        self.matriz[1] = [int(el) for el in self.matriz[1]]
    

    def multiMatriz(self):
        from Digitos import lista
        matrizchave      =    [[],[]]
        matrizmsg        =    [[],[]]
        matrizcripto     =    [[],[]]
        matrizchave[0]   =    [self.matriz[0][a] for a in range(0,2)]
        matrizchave[1]   =    [self.matriz[0][b] for b in range(2,4)]
        matrizmsg[0]     =    [self.matriz[1][x] for x in range(0,int(len(self.matriz[1])/2))]
        matrizmsg[1]     =    [self.matriz[1][y] for y in range(int(len(self.matriz[1])/2),len(self.matriz[1]))]
        matrizcripto[0]  =    [(matrizchave[0][0]*matrizmsg[0][s] + matrizchave[0][1]*matrizmsg[1][s]) for s in range(0,len(matrizmsg[0]))]
        matrizcripto[1]  =    [(matrizchave[1][0]*matrizmsg[0][s] + matrizchave[1][1]*matrizmsg[1][s]) for s in range(0,len(matrizmsg[0]))]
        for indice in range(0,2):
            for elemento in range(0,len(matrizcripto[0])):
                var = matrizcripto[indice][elemento]
                while(var < 1):
                    var += len(lista()[0])
                while(var > len(lista()[0])):
                    var -= len(lista()[0])
                self.matrizcripto.append(var)
    

    def conversor(self):
        from Digitos import lista
        self.matrizcripto = [str(self.matrizcripto[s]) for s in range(0,len(self.matrizcripto))]
        for indice in range(0,len(self.matrizcripto)):
            for elemento in range(0,len(lista()[1])):
                self.matrizcripto[indice] = self.matrizcripto[indice].replace(lista()[1][len(lista()[0]) -1 -elemento],lista()[0][len(lista()[0]) -1 -elemento])
        s =''
        for cada in self.matrizcripto:
            s += cada
        self.msg = s

   
    def inicio(self):
        self.matriz         =  [[],[]]
        self.matrizcripto   =  []
        self.cond           =  False
        if self.analiseFormat():
            print('a chave deve ter exatamente 4 numeros inteiros quais quer com espaço entre eles;\nexemplo: 9 11 234 87')
            self.cond = False
            return False
        self.cond = True
        return True
    

    def iniciar(self):
        if self.inicio():
            self.nstr(0)
            self.strFormat()
            self.multiMatriz()
            self.conversor()
            self.nstr(1)
        else:
            return           

