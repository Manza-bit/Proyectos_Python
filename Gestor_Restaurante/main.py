from tkinter import *
import random
import datetime
from tkinter import filedialog ,messagebox


precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


operador = ""

def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0 , END)
    visor_calculadora.insert(END, operador)

def borrar():
    global  operador
    operador = ""
    visor_calculadora.delete(0, END)

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0 , END)
    visor_calculadora.insert(0, resultado)
    operador = ""

def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == "0":
                cuadros_comida[x].delete(0, END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set("0")
        x += 1
    x = 0
    for c in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == "0":
                cuadros_bebida[x].delete(0,END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set("0")
        x += 1
    x = 0
    for c in cuadros_postres:
        if variables_postres[x].get() == 1:
            cuadros_postres[x].config(state=NORMAL)
            if cuadros_postres[x].get() == "0":
                cuadros_postres[x].delete(0,END)
            cuadros_postres[x].focus()
        else:
            cuadros_postres[x].config(state=DISABLED)
            texto_postres[x].set("0")
        x += 1

def total():
    sub_total_comida = 0
    sub_total_bebida = 0
    sub_total_postre = 0

    p=0
    for cantidad in texto_comida:
        sub_total_comida= sub_total_comida + float(cantidad.get()) * precios_comida[p]
        p +=1

    p=0
    for cantidad in texto_bebida:
        sub_total_bebida= sub_total_bebida + float(cantidad.get()) * precios_bebida[p]
        p +=1

    p = 0
    for cantidad in texto_postres:
        sub_total_postre= sub_total_postre + float(cantidad.get()) * precios_postres[p]
        p +=1


    sub_total = sub_total_comida + sub_total_bebida + sub_total_postre
    impuestos = sub_total * 0.07
    total = sub_total + impuestos

    var_costos_comida.set(f"$ {round(sub_total_comida , 2 )}")
    var_costos_bebida.set(f"$ {round(sub_total_bebida, 2)}")
    var_costos_postre.set(f"$ {round(sub_total_postre, 2)}")
    var_subtotal.set(f"$ {round(sub_total, 2)}")
    var_impuesto.set(f"$ {round(impuestos, 2)}")
    var_total.set(f"$ {round(total, 2)}")

def recibo():
    texto_recibo.delete(1.0 , END)
    num_recibo= f"N# - {random.randint(1000 , 9999)}"
    fecha = datetime.datetime.now()
    fecha_recibo= f"{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}"
    texto_recibo.insert(END , f"Datos: \t{num_recibo}\t\t{fecha_recibo}\n")
    texto_recibo.insert(END, f"*"* 47 +"\n")
    texto_recibo.insert(END,"Items\t\tCant.\tCosto Items\n")
    texto_recibo.insert(END , f"-" * 64 + "\n")
    x = 0
    for comida in texto_comida:
        if comida.get() != "0":
            texto_recibo.insert(END, f"{lista_de_comidas[x]}\t\t {comida.get()}\t"
                                     f" ${int(comida.get()) * precios_comida[x]}\n")
        x +=1
    x = 0
    for bebida in texto_bebida:
        if bebida.get() != "0":
            texto_recibo.insert(END, f"{lista_de_bebidas[x]}\t\t {bebida.get()}\t"
                                     f" ${int(bebida.get()) * precios_bebida[x]}\n")
        x +=1
    x = 0
    for postre in texto_postres:
        if postre.get() != "0":
            texto_recibo.insert(END, f"{lista_de_postres[x]}\t\t {postre.get()}\t"
                                     f" ${int(postre.get()) * precios_postres[x]}\n")
        x +=1
    texto_recibo.insert(END , f"-" * 64 + "\n")
    texto_recibo.insert(END , f"Coste de la Comida: \t\t\t {var_costos_comida.get()}\n")
    texto_recibo.insert(END , f"Coste de la Bebida: \t\t\t {var_costos_bebida.get()}\n")
    texto_recibo.insert(END , f"Coste del Postre: \t\t\t {var_costos_postre.get()}\n")
    texto_recibo.insert(END , f"-" * 64 + "\n")
    texto_recibo.insert(END , f"Sub total : \t\t\t {var_subtotal.get()}\n\n")
    texto_recibo.insert(END , f"Impuestos: \t\t\t {var_impuesto.get()}\n")
    texto_recibo.insert(END , f"Total: \t\t\t {var_total.get()}\n")
    texto_recibo.insert(END , f"-" * 64 + "\n")
    texto_recibo.insert(END , "Lo esperamos pronto")

def guardar():
    info_recibo = texto_recibo.get(1.0 , END)
    archivo = filedialog.asksaveasfile(mode="w" ,defaultextension=".txt" )
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo("Informacion", "Su recibo a sido guardado")

def resetear():
    texto_recibo.delete(0.1 , END)
    for texto in texto_comida:
        texto.set("0")
    for texto in texto_bebida:
        texto.set("0")
    for texto in texto_postres:
        texto.set("0")

    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postres:
        cuadro.config(state=DISABLED)

    for v in variables_comida:
        v.set(0)
    for v in variables_bebida:
        v.set(0)
    for v in variables_postres:
        v.set(0)
    var_costos_comida.set("")
    var_costos_bebida.set("")
    var_costos_postre.set("")
    var_subtotal.set("")
    var_impuesto.set("")
    var_total.set("")
#Iniciar tinket
aplicacion = Tk()

#tamaño de la ventana
aplicacion.geometry("1020x630+0+0")

#Evitar maximizar
aplicacion.resizable(False,False)

#Establecer un titulo
aplicacion.title("MI RESTAURANTE - SISTEMA DE FACTURACION")

#Color de fondo
aplicacion.config(bg="burlywood")

#panel superior
panel_superior = Frame(aplicacion , bd=1 , relief=FLAT)
panel_superior.pack(side=TOP)

#etiqueta titulo
etiqueta_titulo = Label(panel_superior , text="Sistema de Facturacion", fg="azure4",
                        font=("Dosis" , 58), bg="burlywood" , width=27)
#Para centrarlo se puede usar columconfigure y añadir sticky="ew"
panel_superior.columnconfigure(0, weight=1)
etiqueta_titulo.grid(row=0,column=0 , sticky="ew")

#Panel izquierdo
panel_izquierdo = Frame(aplicacion , bd=1 , relief=FLAT)
panel_izquierdo.pack(side=LEFT)

#Panel costos
panel_costos =Frame(panel_izquierdo , bd=1 , relief=FLAT , bg="azure4", padx=52)
panel_costos.pack(side=BOTTOM)

#panel comidas
panel_comidas = LabelFrame(panel_izquierdo , text="comida",font=("Dosis" , 19 , "bold"),
bd=1, relief=FLAT  ,fg="azure4" )
panel_comidas.pack(side=LEFT)
#panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo , text="bebidas",font=("Dosis" , 19 , "bold"),
bd=1, relief=FLAT  ,fg="azure4" )
panel_bebidas.pack(side=LEFT)

#panel postres
panel_postres = LabelFrame(panel_izquierdo , text="postres",font=("Dosis" , 19 , "bold"),
bd=1, relief=FLAT  ,fg="azure4" )
panel_postres.pack(side=LEFT)


#Panel derecha
panel_derecha = Frame(aplicacion , bd=1 , relief=FLAT)
panel_derecha.pack(side=RIGHT)

#Panel calculadora
panel_calculadora = Frame(panel_derecha , bd=1 , relief=FLAT , bg="burlywood")
panel_calculadora.pack()

#Panel recibo
panel_recibo = Frame(panel_derecha , bd=1 , relief=FLAT , bg="burlywood")
panel_recibo.pack()

#Panel botones
panel_botones = Frame(panel_derecha , bd=1 , relief=FLAT , bg="burlywood")
panel_botones.pack()
#listas
lista_de_comidas = ["pollo" ,"pasta", "cordero" , "salmon", "merluza" ,"kebap","pizza1" , "pizza2"]
lista_de_bebidas = ["agua" , "soda" , "jugo", "cola" ,"vino1","vino2" , "cerveza1" ,"cerveza2" ]
lista_de_postres = ["helado" ,"natillas", "fruta" , "brownies", "flan" ,"muss","pastel1" , "pastel2" ]



#generar items comida
variables_comida=[]
cuadros_comida =[]
texto_comida=[]
contador = 0
for comida in lista_de_comidas:


    #Crear checkbuttons
    variables_comida.append("")
    variables_comida[contador] = IntVar()
    comida =Checkbutton(panel_comidas,
                        text=comida.title() ,
                        font=("Dosis",17,"bold"),
                        onvalue=1 ,
                        offvalue=0,
                        variable=variables_comida[contador],
                        command=revisar_check)
    comida.grid(row=contador,
                column=0 ,
                sticky=W)

    #Crear cuadros de entrada

    cuadros_comida.append(f"")
    texto_comida.append("")
    texto_comida[contador] = StringVar()
    texto_comida[contador].set("0")
    cuadros_comida[contador] = Entry(panel_comidas,
                                     font=("Dosis",17 ,"bold"),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_comida[contador]
                                     )
    cuadros_comida[contador].grid(row=contador,
                                  column=1)
    contador +=1

#generar items bebida
variables_bebida=[]
cuadros_bebida =[]
texto_bebida=[]
contador = 0
for bebida in lista_de_bebidas:

    # Crear checkbuttons
    variables_bebida.append("")
    variables_bebida[contador] = IntVar()
    bebida =Checkbutton(panel_bebidas,
                        text=bebida.title() ,
                        font=("Dosis",17,"bold"),
                        onvalue=1 ,
                        offvalue=0,
                        variable=variables_bebida[contador],
                        command=revisar_check)
    bebida.grid(row=contador,
                column=0 ,
                sticky=W)
    # Crear cuadros de entrada

    cuadros_bebida.append(f"")
    texto_bebida.append(f"")
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set("0")
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                     font=("Dosis", 17, "bold"),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_bebida[contador]
                                     )
    cuadros_bebida[contador].grid(row=contador,
                                  column=1)
    contador +=1

#generar items postre
variables_postres=[]
cuadros_postres =[]
texto_postres=[]
contador = 0
for postres in lista_de_postres:
    variables_postres.append("")
    variables_postres[contador] = IntVar()
    postres =Checkbutton(panel_postres,
                         text=postres.title() ,
                         font=("Dosis",17,"bold"),
                         onvalue=1 ,
                         offvalue=0,
                         variable=variables_postres[contador],
                         command=revisar_check)
    postres.grid(row=contador,
                 column=0 ,
                 sticky=W)
    # Crear cuadros de entrada

    cuadros_postres.append(f"")
    texto_postres.append(f"")
    texto_postres[contador] = StringVar()
    texto_postres[contador].set("0")
    cuadros_postres[contador] = Entry(panel_postres, font=("Dosis", 18, "bold"),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_postres[contador]
                                     )
    cuadros_postres[contador].grid(row=contador,
                                  column=1)
    contador +=1
#variables
var_costos_comida = StringVar()
var_costos_bebida = StringVar()
var_costos_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()
#etiquetas de costo y campos de entrada
etiqueta_costo_comida = Label(panel_costos ,
                              text="Costo Comida",
                              font=("Dosis" , 12 , "bold"),
                              bg="azure4",
                              fg="white")
etiqueta_costo_comida.grid(row=0 , column=0)

texto_costos_comida = Entry(panel_costos,
                         font=("Dosis" ,12 ,"bold"),
                         bd=1,
                         width=10,
                         state="readonly",
                         textvariable=var_costos_comida)

texto_costos_comida.grid(row=0 , column=1, padx=41 )
#etiquetas de costo y campos de entrada
etiqueta_costo_bebida = Label(panel_costos ,
                              text="Costo Bebida ",
                              font=("Dosis" , 12 , "bold"),
                              bg="azure4",
                              fg="white")
etiqueta_costo_bebida.grid(row=1 , column=0)

texto_costos_bebida = Entry(panel_costos,
                         font=("Dosis" ,12 ,"bold"),
                         bd=1,
                         width=10,
                         state="readonly",
                         textvariable=var_costos_bebida)
texto_costos_bebida.grid(row=1 , column=1, padx=41)

#etiquetas de costo y campos de entrada
etiqueta_costo_postre = Label(panel_costos ,
                              text="Costo Postre  ",
                              font=("Dosis" , 12 , "bold"),
                              bg="azure4",
                              fg="white")
etiqueta_costo_postre.grid(row=2 , column=0)

texto_costos_postre = Entry(panel_costos,
                         font=("Dosis" ,12 ,"bold"),
                         bd=1,
                         width=10,
                         state="readonly",
                         textvariable=var_costos_postre)
texto_costos_postre.grid(row=2 , column=1, padx=41)

etiqueta_subtotal = Label(panel_costos ,
                              text=" Subtotal  ",
                              font=("Dosis" , 12 , "bold"),
                              bg="azure4",
                              fg="white")
etiqueta_subtotal.grid(row=0 , column=2)

texto_subtotal = Entry(panel_costos,
                         font=("Dosis" ,12 ,"bold"),
                         bd=1,
                         width=10,
                         state="readonly",
                         textvariable=var_subtotal)
texto_subtotal.grid(row=0 , column=3, padx=41)

etiqueta_impuesto = Label(panel_costos ,
                              text="Impuesto ",
                              font=("Dosis" , 12 , "bold"),
                              bg="azure4",
                              fg="white")
etiqueta_impuesto.grid(row=1 , column=2)

texto_impuesto = Entry(panel_costos,
                         font=("Dosis" ,12 ,"bold"),
                         bd=1,
                         width=10,
                         state="readonly",
                         textvariable=var_impuesto)
texto_impuesto.grid(row=1 , column=3, padx=41)

etiqueta_total = Label(panel_costos ,
                              text="  Total   ",
                              font=("Dosis" , 12 , "bold"),
                              bg="azure4",
                              fg="white")
etiqueta_total.grid(row=2 , column=2)

texto_total = Entry(panel_costos,
                         font=("Dosis" ,12 ,"bold"),
                         bd=1,
                         width=10,
                         state="readonly",
                         textvariable=var_total)
texto_total.grid(row=2 , column=3, padx=41)

#Botones
botones = ["total" , "recibo", "guardar" , "resetear"]
botones_creados = []
columnas =0
for boton in botones:
    boton= Button(panel_botones,
                  text=boton.title(),
                  font=("Dosis" , 11 , "bold"),
                  fg="white",
                  bg="azure4",
                  bd=1,
                  width=9)
    botones_creados.append(boton)
    boton.grid(row=0,
               column=columnas)
    columnas += 1
botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)

#Area de recibo
texto_recibo = Text(panel_recibo ,
                    font=("Dosis" , 12 ,"bold"),
                    bd=1,
                    width=41,
                    height=10)
texto_recibo.grid(row=0 , column=0)

#Calculadora

visor_calculadora = Entry(panel_calculadora ,
                          font=("Dosis", 16 , "bold"),
                          width=29,
                          bd=1)
visor_calculadora.grid(row=0 ,
                       column=0,
                       columnspan=4)

botones_calculadora = ["7","8","9","+" ,"4" , "5", "6" ,"-" ,
                       "1","2","3","x" ,"R" ,"Borrar" , "0","/"]
botones_guardados = []
fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=("Dosis" ,15 , "bold"),
                   fg="white",
                   bg="azure4",
                   bd=1,
                   width=7)
    botones_guardados.append(boton)
    boton.grid(row=fila,
               column=columna)
    if columna == 3:
        fila+=1
    columna +=1
    if columna==4:
        columna =0


botones_guardados[0].config(command = lambda: click_boton("7"))
botones_guardados[1].config(command = lambda: click_boton("8"))
botones_guardados[2].config(command = lambda: click_boton("9"))
botones_guardados[3].config(command = lambda: click_boton("+"))
botones_guardados[4].config(command = lambda: click_boton("4"))
botones_guardados[5].config(command = lambda: click_boton("5"))
botones_guardados[6].config(command = lambda: click_boton("6"))
botones_guardados[7].config(command = lambda: click_boton("-"))
botones_guardados[8].config(command = lambda: click_boton("1"))
botones_guardados[9].config(command = lambda: click_boton("2"))
botones_guardados[10].config(command = lambda: click_boton("3"))
botones_guardados[11].config(command = lambda: click_boton("*"))
botones_guardados[12].config(command = obtener_resultado) # =
botones_guardados[13].config(command = borrar) # Borrar
botones_guardados[14].config(command = lambda: click_boton("0"))
botones_guardados[15].config(command = lambda: click_boton("/"))


#evitar que la pantalla se cierre
aplicacion.mainloop()