from tkinter import ttk
import tkinter as tk
from unittest import result

root = tk.Tk()
root.geometry("150x200")
root.title("Calculadora")
root.config(bg="gray")
root.resizable(False, False)

#Entrada
texto= tk.Entry(root)
texto.grid(row=0, column=0, padx=5, pady=2, columnspan=4)

#Funciones
i= 0

def aggNUmero(num):
    global i
    texto.insert(i, num)
    i +=1

def borrar():
    global i
    texto.delete(0, i)
    i= 0

def operacion():
    global i
    nuevoTexto= texto.get()
    resultado= eval(nuevoTexto)
    texto.delete(0,i)
    texto.insert(0,resultado)
    i= 100


#Botones AC y operacion
borrar1= tk.Button(root, text="Borar", command=borrar)
borrar1.grid(row=1, column=0, padx=2, pady=2)
paren1= tk.Button(root, text="(", command= lambda: aggNUmero("("))
paren1.grid(row=1, column=1, padx=2, pady=2)
paren2= tk.Button(root, text=")", command= lambda: aggNUmero(")"))
paren2.grid(row=1, column=2, padx=2, pady=2)
sumar= tk.Button(root, text="+", command= lambda: aggNUmero("+"))
sumar.grid(row=1, column=3, padx=2, pady=2)
resta= tk.Button(root, text="-", command= lambda: aggNUmero("-"))
resta.grid(row=2, column=3, padx=2, pady=2)
multi= tk.Button(root, text="x", command= lambda: aggNUmero("*"))
multi.grid(row=3, column=3, padx=2, pady=2)
divi= tk.Button(root, text="/", command= lambda: aggNUmero("/"))
divi.grid(row=4, column=3, padx=2, pady=2)

#Botones Numericos
siete= tk.Button(root, text="7", command= lambda: aggNUmero("7"))
siete.grid(row=2, column=0, padx=2, pady=2)
ocho= tk.Button(root, text="8", command= lambda: aggNUmero("8"))
ocho.grid(row=2, column=1, padx=2, pady=2)
nueve= tk.Button(root, text="9", command= lambda: aggNUmero("9"))
nueve.grid(row=2, column=2, padx=2, pady=2)

cuatro= tk.Button(root, text="4", command= lambda: aggNUmero("4"))
cuatro.grid(row=3, column=0, padx=2, pady=2)
cinco= tk.Button(root, text="5", command= lambda: aggNUmero("5"))
cinco.grid(row=3, column=1, padx=2, pady=2)
seis= tk.Button(root, text="6", command= lambda: aggNUmero("6"))
seis.grid(row=3, column=2, padx=2, pady=2)

uno= tk.Button(root, text="1", command= lambda: aggNUmero("1"))
uno.grid(row=4, column=0, padx=2, pady=2)
dos= tk.Button(root, text="2", command= lambda: aggNUmero("2"))
dos.grid(row=4, column=1, padx=2, pady=2)
tres= tk.Button(root, text="3", command= lambda: aggNUmero("3"))
tres.grid(row=4, column=2, padx=2, pady=2)

cero= tk.Button(root, text="0", command= lambda: aggNUmero("0"), width=8)
cero.grid(row=5, column=0,columnspan=2, padx=2, pady=2)

#Botones punto e igual
punto= tk.Button(root, text=".", command= lambda: aggNUmero("."))
punto.grid(row=5, column=2, padx=2, pady=2)
igual= tk.Button(root, text="=", command= operacion)
igual.grid(row=5, column=3, padx=2, pady=2)

#Boton Apagar
Apagar= tk.Button(root, text="Apagar", command= root.destroy)
Apagar.grid(row=6, column=0, padx=2, pady=2)

root.mainloop()