#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 15:08:50 2018

@author: fcolombini
"""

import random
import numpy as np


#figurita = random.randint(1,6)



#album = [1,2,3,4,5,6]

#i=0

#while len(album)!= 0:
    
#    z= 0
#    figurita = random.randint(1,6)
#    while z < len(album):
#        if album[z] == figurita:
#            album.pop(z)
#            
 #       z +=1    
 #   i +=1   
        
        
#print(i)


        
def cuantas_figus(figus_total):
    i=figus_total
    album = []
    while i > 0 :
        album.append(i)
        i -= 1
    while len(album)!= 0:
        z= 0
        figurita = random.randint(1,figus_total)
        while z < len(album):
            if album[z] == figurita:
                album.pop(z)
            
            z +=1    
        i +=1      
    return i
    

#print(cuantas_figus(12))
album =[]
for y in range(1000):
    
    album.append(cuantas_figus(6))
    
    promedio = np.mean(album)

#print(promedio)

for y in range(100):
    
    album.append(cuantas_figus(669))
    
    promedia = np.mean(album)
    
#print(promedia)


def generar_paquete(figus_total, figus_paquete):
    otroalbum = []
    for i in range(figus_paquete):
        figu = random.randint(1,figus_total)
        otroalbum.append(figu)
    
    return otroalbum

#print(generar_paquete(100,5))


    

def cuantos_paquetes(figus_total, figus_paquete):
    h=0
    n=figus_total
    album = []
    while n> 0 :
        album.append(n)
        n -= 1
    
    while len(album)!= 0:
        paquete = generar_paquete(figus_total,figus_paquete)
        z=0
        while z <len(album):           
            for r in range(len(paquete)):
                               
                if len(album)>0 and album[z] == paquete[r]:
                    
                    album.pop(z)
                    
                    r = 0
                    z= 0
            z +=1       
                    
              
        h +=1      
    return h

#print(cuantos_paquetes(6,2))

def promediopaquetes(figus_total, figus_paquete,cuantasveces):
    
    promediolista = []
    for i in range(cuantasveces):
        promediolista.append(cuantos_paquetes(figus_total, figus_paquete))
        
      
    return np.mean(promediolista)
print(promediopaquetes(669,5,100))
        
    
    
    