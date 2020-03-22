#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 14:58:03 2018

@author: fcolombini
"""

#graphics top line {0 0 0} {5 0 0} width 5 style solid
#graphics top line {0 0 0} {0 5 0} width 5 style solid
#graphics top line {0 5 0} {5 5 0} width 5 style solid
#graphics top line {5 0 0} {5 5 0} width 5 style solid
import random 

salida=open("coord.xyz","w")
num_part = 5
xmax = 5
xmin = 0
ymax = 5
ymin = 0
pasos = 10000
deltat = 0.01
Vx_inicial = []
Vy_inicial = [] 
x_inicial = []
y_inicial = []


for d in range(num_part):
    Vx_inicial.append(random.randint(1,2))
    Vy_inicial.append(random.randint(1,2)) 
    x_inicial.append(random.randint(1,4))
    y_inicial.append(random.randint(1,4))
    
Vx = Vx_inicial# + F * deltat
Vy = Vy_inicial# + F * deltat

x = x_inicial 
y = y_inicial
k = 5






for i in range (pasos):
    e = 0
    for j in range(num_part):
        fx = 0
        fy = 0
        for r in range(num_part):
            if j != r:
                d2 = (x[j]- x[r])**2 + (y[j] - y[r]) ** 2 
                fx += 4 * k * (x[j] - x[r]) / d2**3
                fy += 4 * k * (y[j] - y[r]) / d2**3
                if r > j:
                    e += k / (d2 ** 2)
        Vx[j]=Vx[j]+fx*deltat
        x[j]=x[j]+Vx[j]*deltat
        Vy[j] = Vy[j] + fy*deltat
        y[j] = y[j] + Vy[j] *deltat
        if x[j] > xmax:
            Vx[j] = -Vx[j]
            x[j] = x[j] -2 * (x[j] - xmax)
    
        elif x[j] < xmin:
            Vx[j] = -Vx[j]
            x[j] = x[j] + 2 * (xmin - x[j])
    
        if y[j] > ymax:
            Vy[j] = -Vy[j]
            y[j] = y[j] - 2 * (y[j] - ymax)

        elif y[j] < ymin:
            Vy[j] = -Vy[j]
            y[j] = y[j] + 2 * (ymin - y[j])
    if (i % 20) == 0: 
        print(num_part,file=salida)
        print(" ", file=salida)
        for s in range(num_part):
            print("6",x[s],y[s],"0",file=salida)
        


        
salida.close()