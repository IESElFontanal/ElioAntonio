#Operaciones básicas
from tkinter import *
from tkinter import ttk
raiz=Tk()
raiz.title('Aplicación Elio Antonio')

#Imnportación de la referencia

import Referencias

#Configutación de la raiz
raiz.config(bg='#eee7e1', bd=15, relief='ridge')
raiz.iconbitmap('ElioAntonio.ico')

#Imagen
fotografia=PhotoImage(file='ElioAntonio.png')

#Variables de texto
txtpreg=StringVar()
txtpreg.set(Referencias.Preguntas.get('0'))
txtresp=StringVar()
txtresp.set(Referencias.Respuestas.get('0'))

#Lista para el Combobox
Lista=[]
for i in range(1,4):
    Lista.append(i)

#Función preguntas y respuestas
def Elio1():
    txtpreg.set(50*'¿?')
    txtresp.set(50*'¿?')
def Elio2():
    consulta=Combo.get()
    txtpreg.set(Referencias.Preguntas.get(consulta))
def Elio3():
    consulta=Combo.get()
    txtresp.set(Referencias.Respuestas.get(consulta))
def creditos():
    txtpreg.set(Referencia.Preguntas.get('4'))
    txtresp.set(Referencia.Respuestas.get('4'))

#Elementos del Grid
Titulo=Label(raiz, text='CONSÚLTALE A ELIO ANTONIO', fg='gray24', bg='#eee7e1', font=('gadugi',18,'bold'))
Titulo.grid(row=1, column=1, columnspan=3, pady=10, padx=20)
Foto=Button(raiz, image=fotografia, command=creditos)
Foto.grid(row=2, column=1, rowspan=3, padx=30)
Pregunta=Label(raiz, textvariable=txtpreg, wraplength=500, fg='gray24', bg='#eee7e1', font=('gadugi',18,'bold'))
Respuesta=Label(raiz, textvariable=txtresp, wraplength=500, fg='gray24', bg='#eee7e1', font=('gadugi',18))
Pregunta.grid(row=2, column=2, columnspan=2)
Respuesta.grid(row=3, column=2, columnspan=2, rowspan=2, padx=20)
Combopg=Label(raiz, text='Haz una pregunta a Elio Antonio', fg='gray24', bg='#eee7e1', font=('gadugi',14))
Combopg.grid(row=5, column=1, columnspan=3, pady=10)
Combo=ttk.Combobox(raiz, values=Lista, width=50)
Combo.grid(row=6, column=1, columnspan=3, pady=10)
Boton1=Button(raiz, text='Limpiar', command=Elio1)
Boton1.grid(row=7, column=1, pady=10)
Boton2=Button(raiz, text='Pregunta', command=Elio2)
Boton2.grid(row=7, column=2, pady=10)
Boton3=Button(raiz, text='Respuesta', command=Elio3)
Boton3.grid(row=7, column=3, pady=10)

#Bucle infinito al final del programa
raiz.mainloop()