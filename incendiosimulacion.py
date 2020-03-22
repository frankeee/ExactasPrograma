#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 15:04:48 2018

@author: fcolombini
"""

import random 
#import matplotlib.pyplot as plt


def bosquevacio(n):
    lista = []
    for i in range(n):
        lista.append(0)
    return lista
        
def bosquelimpio(n):
    lista = []
    
    for i in range(n):
        d = random.random()
        if d < 0.6:
            lista.append(1)
        else:
            lista.append(0)
    return lista
            
def bosquequemado(n):
    lista = []
    for i in range(n):
        d = random.random()
        if d < 0.8:
            lista.append(-1)
        else:
            lista.append(0)
        
        

def brotes(bosque, p):
    for i in range(len(bosque)):
        t = random.random()
        if t < p:
            bosque[i] = 1
    return bosque
        
#print(brotes(bosquevacio(100),0.6))

def cuantos(bosque, tipo_celda):
    r = 0
    for i in range(len(bosque)):
        if bosque[i] == tipo_celda:
            r += 1
    return r

def rayos(bosque, f):
    for i in range(len(bosque)):
        y = random.random()
        if y<f and bosque[i] == 1:
            bosque[i] = -1
    return bosque

#print(propagacion(rayos(bosquelimpio(100),0.02)))


def propagacion(bosque):
    for i in range(len(bosque)-1):
        if bosque[i] == -1 and bosque[i+1] == 1:
            bosque[i+1] = -1
    n = len(bosque)-1
    while n > 0:
        if bosque[n] == -1 and bosque[n-1] == 1:
            bosque[n-1] = -1
        n -= 1
    return bosque

def limpieza(bosque):
    for i in range(len(bosque)):
        if bosque[i] == -1:
            bosque[i] = 0
    return bosque


def ciclos(repeticiones,p,f,n):
    listapromedios = []
    
    bosque = bosquevacio(n)
    
    while repeticiones >1:
        brotes(bosque,p)
        rayos(bosque,f)
        propagacion(bosque)
        limpieza(bosque)
        d = 0
        for i in range(len(bosque)):
            if bosque[i] == 1:
                d += 1
        listapromedios.append(d)
        repeticiones -= 1
    w = len(listapromedios)
    z = 0
    for h in range(len(listapromedios)):
        z += listapromedios[h]
        
    return z/w

def ayudagraficar(repeticiones,n):
    d = 0
    listax = []
    listay = []
    while d <= 1:
        listax.append(d)
        listay.append(ciclos(repeticiones,d,0.02,n))
        d += 0.01
    x = [listax,listay]
    return x


ciclos(50,0.5,0.02,100)

x = ayudagraficar(50,100)

#plt.plot(x[0],x[1])

#plt.show(plt.plot(x[0],x[1]))
#entre 0.5 y 0.6 conviene tener los valores de brotes

def brotedinamico(listap,bosque):
    for i in range(len(bosque)):
        t = random.random()
        if t < listap[i]:
            bosque[i] = 1
    return bosque

def cambioprobabrote(listabrote,bosque):
    for i in range(len(bosque)):
        if bosque[i] == -1 :
            listabrote[i] -= 0.05
        elif bosque[i] == 1:
            listabrote[i] += 0.05
    
def ciclosdinamicos(repeticiones,p,f,n):
    listapromedios = []
    listaprobabrote = []
    for i in range(n):
        listaprobabrote.append(p)
    bosque = bosquevacio(n)
        
    while repeticiones >1:
        brotedinamico(listaprobabrote,bosque)
        rayos(bosque,f)
        propagacion(bosque)
        cambioprobabrote(listaprobabrote,bosque)
        limpieza(bosque)
        d = 0
        for i in range(len(bosque)):
            if bosque[i] == 1:
                d += 1
        listapromedios.append(d)
        repeticiones -= 1
    w = len(listapromedios)
    z = 0
    for h in range(len(listapromedios)):
        z += listapromedios[h]
        
    return z/w

def ayudagraficardinamica(repeticiones):
    d = 0
    listax = []
    listay = []
    while d <= 1:
        listax.append(d)
        listay.append(ciclosdinamicos(repeticiones,d,0.1,100))
        d += 0.01
    x = [listax,listay]
    return x

    
y = ayudagraficardinamica(50)

#plt.show(plt.plot(y[0],y[1]))
    


            
    
    

