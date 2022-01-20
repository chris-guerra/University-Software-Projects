import random
from tkinter import *

#-------------------------------------------------------------
# funcion Palabra Aleatoria: palabraf()
#-------------------------------------------------------------
def palabraf():
    nl=0
    txt=open("palabras.txt", "r")
    while True:
        linea=txt.readline()
        if linea=="": break
        nl=nl+1
    lineaRandom=random.randint(1, nl)
    txt.close()
    txt=open("palabras.txt", "r")
    nl2=0
    while True:
        palabra=txt.readline()
        nl2=nl2+1
        if nl2==lineaRandom: break
    if nl2!=nl:
        palabra=palabra[:-1]
    txt.close()
    return palabra

#-------------------------------------------------------------
# Entry: letraUsada(x)
#-------------------------------------------------------------
eliminar=""
vidas=5
palabra=palabraf()
letrasJugadas=""
resp=""
ignorar=4
def letraUsada(x):
    global eliminar
    global vidas
    global letrasJugadas
    global guiones
    resp=str(respuesta.get()).lower()
    if vidas>0 and guiones!=palabra:
        if resp.isalpha():
            if len(resp)>1:
                letras_jugadas.config(text="Please Inserta a Letter Only")
                letras_label.config(text="")
        #-------------------------------------------------------------
        # caso correcto:
        #-------------------------------------------------------------
            else:
                letrasJugadas=letrasJugadas+resp+" "
                letras_jugadas.config(text=letrasJugadas)
                letras_label.config(text="Used Letters:")
                #-------------------------------------------------------------
                # modificar letras restantes (palabra secreta)
                #-------------------------------------------------------------
                if resp in palabra and resp not in eliminar:
                    guiones= guionesf(resp)
                    palabra_codificada.config(text=guiones)
                #-------------------------------------------------------------
                # vidas
                #-------------------------------------------------------------
                if resp not in palabra:
                    vidas=vidas-1
                if resp in eliminar:
                    vidas=vidas-1
                if resp in palabra:
                    eliminar=eliminar+resp
                #-------------------------------------------------------------
                # graficar
                #-------------------------------------------------------------
                global ignorar
                if vidas==4 and ignorar==4:
                    palo()
                    ignorar=ignorar-1
                if vidas==3 and ignorar==3:
                    piernas()
                    ignorar=ignorar-1
                if vidas==2 and ignorar==2:
                    cuerpo()
                    ignorar=ignorar-1
                if vidas==1 and ignorar==1:
                    brazos()
                    ignorar=ignorar-1
                if vidas==0 and ignorar==0:
                    cabeza()
                    ignorar=ignorar-1
                #-------------------------------------------------------------
                # final del juego
                #-------------------------------------------------------------
                if vidas<=0:
                    letras_jugadas.config(text="You Lost. The Word Was "+palabra)
                    letras_label.config(text="")
                if guiones == palabra:
                    letras_jugadas.config(text="Congratulations!")
                    letras_label.config(text="")
                    canvas.create_rectangle(0,0,400,500,fill="Cornsilk",outline="Cornsilk")
                    sonrisa()
        elif resp=="":
            letras_label.config(text="")
            letras_jugadas.config(text="No input was added")
        else:
            letras_label.config(text="")
            letras_jugadas.config(text="Insert Letters Only")
    respuesta.delete(0, END)
    
#-------------------------------------------------------------
# funcion letras restantes: letrasRestantes(x)
#-------------------------------------------------------------
restantes="abcdefghijklmnopqrstuvwxyz:"
def letrasRestantes(x):
    global restantes
    find_restantes=restantes.find(x)
    restantes1= restantes[:find_restantes]
    restantes2= restantes[find_restantes+1:]
    restantes=restantes1+restantes2
    return restantes

#-------------------------------------------------------------
# funcion guiones: guionesf(x)
#-------------------------------------------------------------
def guionesf(x):
    guion=""
    palabrac=palabra
    fun_restantes=letrasRestantes(x)
    for d in palabrac:
        if d in fun_restantes:
            guion=guion+"_ "
        if d not in fun_restantes:
            guion=guion+d
    return guion

#-------------------------------------------------------------
# Boton: empezarDeNuevo()
#-------------------------------------------------------------
def empezarDeNuevo():
    global palabra
    global vidas
    global eliminar
    global resp
    global letrasJugadas
    global guiones
    global restantes
    global palabra
    global ignorar
    palabra=palabraf()
    vidas=5
    eliminar=""
    resp=""
    letrasJugadas=""
    restantes="abcdefghijklmnopqrstuvwxyz:"
    guiones=guionesf(":")
    letras_jugadas.config(text=letrasJugadas)
    letras_label.config(text="Used Letters: ")
    palabra_codificada.config(text= guiones)
    ignorar=4
    canvas.create_rectangle(0,0,400,500,fill="Cornsilk",outline="Cornsilk")
    
#-------------------------------------------------------------
# Interfaz grafica:
#-------------------------------------------------------------
ventana=Tk()
ventana.wm_title("Hangman")

#-------------------------------------------------------------
# 1. Canvas
#-------------------------------------------------------------
canvas= Canvas (ventana, width=400, height=500, bg="Cornsilk")
canvas.pack()
#-------------------------------------------------------------
# a.dibujo general
#-------------------------------------------------------------
def cabeza():
    canvas.create_oval(150,50,250,150)
    canvas.create_line(180,125,220,130)
    canvas.create_line(180,130,220,125)
    canvas.create_oval(184,90,186,100)
    canvas.create_oval(214,90,216,100)
def cuerpo():
    canvas.create_line(200,150,200,325)
def piernas():
    canvas.create_line(200,325,100,425)
    canvas.create_line(200,325,300,425)
def brazos():
    canvas.create_line(200,175,125,250)
    canvas.create_line(200,175,275,250)
def palo ():
    canvas.create_line(50,450,50,25)
    canvas.create_line(50,25,200,25)
    canvas.create_line(200,25,200,50)
def sonrisa():
    canvas.create_line(185,125,215,125)
    canvas.create_line(185,125,180,120)
    canvas.create_line(215,125,220,120)
    canvas.create_oval(184,90,186,100)
    canvas.create_oval(214,90,216,100)

    canvas.create_oval(150,50,250,150)
    canvas.create_line(200,150,200,325)
    canvas.create_line(200,325,100,425)
    canvas.create_line(200,325,300,425)
    canvas.create_line(200,175,125,250)
    canvas.create_line(200,175,275,250)

#-------------------------------------------------------------
# 2. Campo de Texto y letras jugadas
#-------------------------------------------------------------
marco1=Frame(ventana)
marco1.pack()
ingreseLetra=Label(marco1, text="Enter a Letter:")
ingreseLetra.pack(side=LEFT)

respuesta=Entry(marco1)
respuesta.bind("<Return>", letraUsada)
respuesta.pack()

marco2=Frame(ventana)
marco2.pack()
letras_label=Label(marco2, text="Used Letters:")
letras_label.pack(side=LEFT)

letras_jugadas=Label (marco2)
letras_jugadas.pack(side=LEFT)

#-------------------------------------------------------------
# 3. Palabra secreta
#-------------------------------------------------------------
marco3=Frame(ventana)
marco3.pack()
palabra_label=Label(marco3, text="Word: ")
palabra_label.pack(side=LEFT)
guiones=guionesf(":")
palabra_codificada=Label (marco3, text= guiones)
palabra_codificada.pack()

#-------------------------------------------------------------
# 4. Comenzar de nuevo
#-------------------------------------------------------------
marco4=Frame(ventana)
marco4.pack()
boton_denuevo=Button(marco4, text="Start Again", command=empezarDeNuevo)
boton_denuevo.pack()

ventana.mainloop()

