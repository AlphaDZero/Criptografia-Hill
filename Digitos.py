def lista():
    digitos = [[],[],[],[]]
    digitos[0] = ['a','b','A','ã','á','â','à','Ã','Â','À','Á','B','C','D','E','é','è','ê','É','È','Ê','F','G','H','I','í','î','ì','Í','Ì','Î','J','K','L','M','N','O','ó','õ','ò','ô','Ó','Õ','Ò','Ô','P','Q','R','S','T','U','Ú','Ù','Û','ú','ù','û','V','W','X','Y','Z','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','(',')','*','&','¨','%','$','#','@','!',"'",'"','-','_','+','=','§','/','?','°','`','{','[','ª','^','~','}',']','º','|','<',',','>','.',':',';','£','¢','¬',' ']
    digitos[1] = [str(v) for v in range(1,len(digitos[0])+1)]
    digitos[2] = ['zeroN!','umN!','doisN!','tresN!','quatroN!','cincoN!','seisN!','seteN!','oitoN!','noveN!']
    digitos[3] = [str(s) for s in range(0,10)]
    return digitos


