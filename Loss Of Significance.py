# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

import numpy as np
from numpy import *
from matplotlib import pyplot
from matplotlib import pyplot as plt

lista32 = np.zeros((2**22), dtype=np.float32)
lista64 = np.zeros((2**22), dtype=np.float64)
errores64 = []
errores32R = []
errores32M = []
i = 0
while i < len(lista32):
    lista32[i] = random.randint(10)
    lista64[i] = lista32[i]
    i += 1

def cosenoManual(x,n):
    contador = 0
    coseno = 0
    x = np.mean(x)
    def factorial (*n):
        for x in n:
            fac=1
            for y in range(1,x+1):
                fac=fac*y
        return fac
    while contador < n: #PAR
        if contador%2 == 0:
            coseno += (x**(2*contador))/(factorial(2*contador))
        else: #IMPAR
            coseno -= (x**(2*contador))/(factorial(2*contador))
        contador += 1
    return coseno

a = 15
while 22 >= a:
    listaa32 = lista32[:a]
    listaa64 = lista64[:a]
    cosenoReal32 = cos(np.mean(listaa32))
    cosenoReal64 = cos(np.mean(listaa64))
    errores64.append(abs((cosenoManual(listaa64,12)-cosenoReal64)/cosenoReal64))#ERROR ENTRE 64 REAL Y 64 MANUAL
    errores32R.append(abs((cosenoReal32-cosenoReal64)/cosenoReal64))#ERROR ENTRE 64 REAL Y 32 REAL    
    errores32M.append(abs((cosenoManual(listaa32,12)-cosenoReal64)/cosenoReal64))#ERROR ENTRE 64 REAL Y 32 MANUAL
    a +=1
    print "N =",2**a
    print cosenoManual(listaa32,12),"       ", abs((cosenoManual(listaa32,12)-cosenoReal64)/cosenoReal64)
    print cosenoReal32,"       ", abs((cosenoReal32-cosenoReal64)/cosenoReal64)
    print cosenoManual(listaa64,12),"       ", abs((cosenoManual(listaa64,12)-cosenoReal64)/cosenoReal64)
    print cosenoReal64,"       ", abs((cosenoReal64-cosenoReal64)/cosenoReal64)
    print " "

pyplot.plot([15,16,17,18,19,20,21,22],errores64,"b")
pyplot.plot([15,16,17,18,19,20,21,22],errores32R,"r")
pyplot.plot([15,16,17,18,19,20,21,22],errores32M,"m")
pyplot.ylabel("Error relativo")
pyplot.xlabel("N, donde a.size = 2^N")
plt.legend(["cosenoManual(lista64,N)","cos(np.mean(lista32))","cosenoManual(lista32,N)"])
plt.title("Perdida de Significancia")
pyplot.show()