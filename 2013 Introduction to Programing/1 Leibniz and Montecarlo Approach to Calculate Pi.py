import math
import random

#serie de leibniz

def termino (i):
    return ((-1.0)**(i+1))/((i*2)-1)

def suma (n):
    nsec=n
    numero= termino (nsec)
    while nsec >= 2.0:
        nsec= nsec-1.0
        numero= numero + termino (nsec)
    return numero

def leibniz (n):
    return suma (n) *4.0

#algoritmo de montecarlo

def estaDentro (x, y):
    if math.sqrt ((x-1.0)**2.0+(y-1.0)**2.0) <= 1.0:
        return True
    else:
        return False

def montecarlo (n):
    c1= 2.0*random.random ()
    c2= 2.0*random.random ()
    a=0.0
    d= n*1.0
    while True:
        if d>0.0:
            if estaDentro (c1, c2) == True:
                a=a+1.0
                d=d-1.0
                c1= 2.0*random.random ()
                c2= 2.0*random.random ()
            else:
                d=d-1.0
                c1= 2.0*random.random ()
                c2= 2.0*random.random ()
        else:
            break
    return 1.0*a/n*4.0

#analisis comparativo de los metodos de aproximacion:

def errorPorcentual (valor):
    y=100*valor/math.pi
    return abs(100-y)

#programa principal
    
iteraciones= int(input ("Ingrese el numero de iteraciones: "))

while iteraciones < 1:
    print ("Por favor, ingrese un numero positivo!!")
    iteraciones= int(input ("Ingrese el numero de iteraciones: "))

if iteraciones >= 1:
    print ("N" "\t" "Leibniz" "\t" "\t" "Error" "\t" "\t" "Montecarlo" "\t" "Error")
    j=0
    x=iteraciones
    while x>=1:
        j=j+1
        print (j, "\t", leibniz (j), "\t", errorPorcentual (leibniz(j)), "\t", montecarlo (j), "\t", errorPorcentual (montecarlo (j)))
        x=x-1
