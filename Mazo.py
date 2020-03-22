import random


def generar_mazo(n):
    i = 1
    mazo = []
    while  i <= 13:
        mazo.append(i)
        mazo.append(i)
        mazo.append(i)
        mazo.append(i)
        i += 1
    t = 1
    mazogrande = []
    while n >= t:
        mazogrande = mazogrande + mazo
        t += 1
    
    random.shuffle(mazogrande)
    
    return mazogrande

#print(generar_mazo(1)) 


def jugar(m):
    j = 0
    while j < 21:
        if len(m) == 0:
            return j
        else :
            j += m.pop(0)   
    return j
    
#print(jugar(generar_mazo(1)))

def jugar_varios(m,j):
    valorjugador = []
    while j > 0:
        valorjugador.append(jugar(m))
        j = j -1
    
    return valorjugador
        
#jugada = jugar_varios(generar_mazo(1),3)

#print(jugada)

def ver_quien_gano(resultados):
    i = 0
    while i < len(resultados):
        if resultados[i] == 21:
            resultados[i] = 1
        else:
            resultados[i] = 0
        i += 1
    return resultados

#print(ver_quien_gano(jugar_varios(generar_mazo(1),3)))


def experimentar(rep,n):
    listadef =[]
    ingramo = [0] * n
    j = 0
    while j < rep:
        listadef = ver_quien_gano(jugar_varios(generar_mazo(1),n))
        for i in range(n):           
            ingramo[i] = ingramo[i] + listadef[i]        
        j += 1
    return ingramo
        
#print(experimentar(6,5))        
    

print(random.random())
    
    
    
