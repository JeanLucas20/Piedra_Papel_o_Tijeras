# importo la libreria tkinter, con el alias tk
from msilib.schema import Font
from pydoc import plain
import tkinter as tk
from tkinter import Button, messagebox
import random
from tkinter import Tk, Label, StringVar
from turtle import left




#---------------------------
# Funciones Finales
# --------------------------
def Salir():
    messagebox.showinfo("Salir","Gracias Por Jugar, Adios")
    ventana_principal.destroy()
def Reiniciar():
    messagebox.showinfo("Reiniciar", "Vamos de Nuevo")
    at_resultados.delete("1.0","end")
def op():
    messagebox.showinfo("¿ ?", "¡¡¡Que Curioso Eres!!!")


# -----------------------------
# VENTANA PRINCIPAL
# -----------------------------
# creacion objeto Tk (ventana principal)
ventana_principal = tk.Tk()
# Titulo ventana principal
ventana_principal.title("El Pequeño Robert")
# dimensiones de la ventana
ventana_principal.geometry("500x500")
# deshabilitar boton maximizar
ventana_principal.resizable(0,0)
# color de fondo ventana principal
ventana_principal.config(bg="Red")
# icono de la ventana
ventana_principal.iconbitmap('Siu.ico')

#:0
secreto = tk.Button(ventana_principal, text="¿ ?", command=op)
secreto.config(bg="wHITE", width=7, height=4, fg="red", bitmap="warning")
secreto.pack()

# Variable para random
computadora= {
    "0":"Piedra",
    "1":"Papel",
    "2":"Tijera"
}
#-----------------------------
# Definir y dar Instrucciones a variables
#-----------------------------
def Piedra():
    com= computadora[str(random.randint(0 ,2))]
    if com == "Piedra": 
        resultado = "Empate"
    elif com=="Tijera": 
        resultado = "Ganaste :D"
    else: 
        resultado = "Perdiste :/"
    at_resultados.insert(tk.INSERT, str(com) + " + " + "Piedra" + " = " + str(resultado))

def Papel():
    com= computadora[str(random.randint(0 ,2))]
    if com == "Papel":
        resultado = "Empate"
    elif com=="Tijera": 
        resultado = "Ganaste :D"
    else: 
        resultado = "Perdiste :/"
    at_resultados.insert(tk.INSERT, str(com) + " + " + "Papel" + " = " + str(resultado))

def Tijera():
    com= computadora[str(random.randint(0 ,2))]
    if com == "Piedra":
        resultado = "Empate"
    elif com=="Tijera": 
        resultado = "Ganaste :D"
    else: 
        resultado = "Perdiste :/"
    at_resultados.insert(tk.INSERT, str(com) + " + " + "Tijera" + " = " + str(resultado))

# -----------------------------
# FRAME ENTRADA DATOS
# -----------------------------
frame_entrada = tk.Frame(ventana_principal)
frame_entrada.config(bg="black", width=480, height=85)
frame_entrada.place(x=10,y=10)

# Variable Titulo movimiento
incremento = 1
periodo = 60
tamanio_max = 50
tamanio = tamanio_min = 47
def modifica_tamanio():
    global tamanio, incremento
    if tamanio > tamanio_max or tamanio < tamanio_min:
        incremento = -incremento
    tamanio += incremento
    titulo.configure(bg="black", fg="White", font=("Chiller",str(tamanio)))
    titulo.after(periodo, modifica_tamanio)
titulo = tk.Label(frame_entrada,text="Piedra Papel o Tijera")
titulo.pack(expand=True)

# Titulo Lugar
titulo.place(x=40, y=1)

# -----------------------------
# FRAME OPERACIONES
# -----------------------------
frame_operaciones = tk.Frame(ventana_principal)
frame_operaciones.config(bg="Black", width=480, height=390)
frame_operaciones.place(x=10,y=100)


# boton Piedra
boton_Piedra = tk.Button(frame_operaciones, text="Piedra", command=Piedra)
boton_Piedra.config(bg="wHITE", width=6, height=1, fg="Black", font=("Chiller", 20, ))
boton_Piedra.place(x=10, y=30)
# Imagen Piedra
logo_piedra = tk.PhotoImage(file="piedra.png")
Label_logo = tk.Button(frame_operaciones, image = logo_piedra, command= Piedra)
Label_logo.place(x=10, y=100)


# boton Papel
boton_Papel = tk.Button(frame_operaciones, text="Papel", command=Papel)
boton_Papel.config(bg="wHITE", width=6, height=1, fg="Black", font=("Chiller", 20, ))
boton_Papel.place(x=200, y=30)
# Imagen Papel
logo_papel = tk.PhotoImage(file="papel.png")
Label_logo = tk.Button(frame_operaciones, image = logo_papel, command= Papel)
Label_logo.place(x=190, y=100)


# boton Tijera
boton_Tijera = tk.Button(frame_operaciones, text="Tijera", command=Tijera)
boton_Tijera.config(bg="wHITE", width=6, height=1, fg="Black", font=("Chiller", 20, ))
boton_Tijera.place(x=390, y=30)
# Imagen Tijera
logo_tijera = tk.PhotoImage(file="Tijera.png")
Label_logo = tk.Button(frame_operaciones, image = logo_tijera, command=Tijera)
Label_logo.place(x=380, y=100)


#Boton Reiniciar
boton_Reiniciar = tk.Button(frame_operaciones, text="Reiniciar", command=Reiniciar)
boton_Reiniciar.config(bg="wHITE", width=6, height=1, fg="Black", font=("Chiller", 20, ))
boton_Reiniciar.place(x=10, y=330)
#Boton Salir
boton_Salir = tk.Button(frame_operaciones, text="Salir", command=Salir)
boton_Salir.config(bg="wHITE", width=6, height=1, fg="Black", font=("Chiller", 20, ))
boton_Salir.place(x=400, y=330)

# -----------------------------
# FRAME RESULTADOS
# -----------------------------
frame_resultados = tk.Frame(ventana_principal)
frame_resultados.config(bg="Red", width=480, height=110)
frame_resultados.pack(fill=tk.BOTH)
frame_resultados.place(x=10,y=300)

# area de texto de resultados
at_resultados = tk.Text(frame_resultados)
at_resultados.place(x=0,y=10)

# Borde Inferior Rojo
frame_relleno = tk.Frame(ventana_principal)
frame_relleno.config(bg="red", width=490, height=10)
frame_relleno.place(x=0,y=410)

modifica_tamanio()

# desplegar ventana principal y queda a la espera de eventos del usuario
ventana_principal.mainloop()
