import math
import time
import random
start_time=time.time()
file = open("resultadosp1.txt", "w")

global Q
Q = 50 #cantidad de stock

#-------------------------------------------------------------------------
#funciones
#-------------------------------------------------------------------------

def expo(p):
    if p>0:
    	return 1


#funcion F(Xt):
def cost(precio):
    if precio==50 or precio==60:
        return 0.1
    elif precio==70:
        return 0.2
    else:
        return 0.3

#funcion distribucion demanda:
def dem(precio):#e=cantidad de publicidad: 1=a, 2=b, 3=c
    s = random.random()
    e = expo(s)
    if e==1:
        if precio==50:
            return 0.781
        elif precio==60:
            return 0.664
        elif precio==70:
            return 0.562
        elif precio==80:
            return 0.491
        else:
            return 0.428
    elif e==2:
        if precio==50:
            return 0.644
        elif precio==60:
            return 0.558
        elif precio==70:
            return 0.467
        elif precio==80:
            return 0.421
        else:
            return 0.347
    else:
        if precio==50:
            return 0.503
        elif precio==60:
            return 0.453
        elif precio==70:
            return 0.394
        elif precio==80:
            return 0.334
        else:
            return 0.226
def v2(q,t):
    if t==T:
        return 10*(Q-q)
    else:
        a=(Q+1)*abs(t+1-T)+q
        b=vector[a]
        c=b[1]
        return c

                
#funcion beneficio:
def ven(x,q,d,t):
    a=int(round(q-min(q,d),0))
    b=int(round(min(q,d),0))
    c=int(round(max(0,d-q),0))
    return x*b-cost(x)*x*b-15*c+v2(a,t)


#-------------------------------------------------------------------------
#codigo
#-------------------------------------------------------------------------

#parametros:
X = [50 , 60, 70, 80, 90] #precios
T = 6 #meses
Q = 50 #cantidad de stock
n = 15 #parametro binomial
vector=[]

for t in range(1,T+1):
    tiempo=T+1-t
    print "Mes: ",tiempo
    file.write("Mes: "+ str(tiempo)+"\n")
    for q in range (0,Q+1):
        vo=-1000000000
        xo=0
        for x in X:
            densesperada=n*dem(x)
            v=ven(x,q,densesperada,tiempo)
            if vo<v:
                vo=v
                xo=x
        vector.append([tiempo,vo,xo])
        if tiempo==1:
            if q==Q:
                print q,": v*(q) = ",vo, " x = ", xo
                file.write(str(q) + ": v*(q) = " + str(vo) + " x = " + str(xo) + "\n")   
        else:
            print q,": v*(q) = ",vo, " x = ", xo
            file.write(str(q) + ": v*(q) = " + str(vo) + " x = " + str(xo) + "\n")


print "utilidad esperada = ",vector[(Q+1)*(T-1)+Q][1]
file.write("utilidad esperada = " + str(vector[(Q+1)*(T-1)+Q][1]) + "\n")

xf=vector[(Q+1)*(T-1)+Q][2]
i=1
qi=Q
for t in range (1,T+1):
    print "Mes = ",t
    file.write("Mes = " + str(t) + "\n")
    print "Precio a fijar (asignacion optima): X = ",xf
    file.write("Precio a fijar (asignacion optima): X = " + str(xf) + "\n")
    #el print de abajo no es necesario, usar para revisar si los valores estan bien
    #print "Cantidad esperada a principio de mes=",qi
    espdem=n*dem(xf)
    qi=int(round(qi-min(qi,espdem),0))
    i=i+1
    xf=vector[(Q+1)*(T-i)+qi][2]

print("Tiempo de resolucion en %s segundos ---" % (time.time() - start_time))
file.write("Tiempo de resolucion en %s segundos ---" + str(time.time() - start_time) + "\n")
file.close()

