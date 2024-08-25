
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from datetime import datetime
from VIEW_Plano_cartesiano import *
from MODEL_funciones_calculadora import *
from MODEL_funciones_operaciones import *
from MODEL_database import *
from PIL import Image, ImageTk
import zipfile
import io
from tkinter import font
import urllib.request
import json
from tkinter import messagebox
import threading
import requests
import pyrebase


menu_abierto = False
conf_abierto = False
est_modo = False
activar_gird = True
fra_men = []
funciones = []
fun = ""
po_col = 0
po_fil = 0
botones_num = []
botones_oper = []
botones_res = []
botones_conf = []
lista_check = []
bot = []
tam_act = "Pre."
tam = 0
tip_act = "Pre"
usuario = "Invitado"


firebaseConfig = {
    "apiKey": "AIzaSyCm69Mj0oYeQxBBv2fWlTOQf91uny2eRm4",
    "authDomain": "calculadora-grupo-5.firebaseapp.com",
    "databaseURL": "https://calculadora-grupo-5-default-rtdb.firebaseio.com",
    "projectId": "calculadora-grupo-5",
    "storageBucket": "calculadora-grupo-5.appspot.com",
    "messagingSenderId": "795823744695",
    "appId": "1:795823744695:web:8fd3f11283ffa91e084f32"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

def ventana ():

    global entrada,entrada_result,pestaña,fig,ax,frame_calculadora,frame_grafica,frame_funciones,est_modo,botones_num,botones_oper,botones_res,botones_conf,boton_tema,boton_conf,activar_gird

    color_select = ""
    
    pestaña = Tk()
    pestaña.title("CALCULADORA GRAFICA")
    pestaña.geometry("900x500+220+100")
    frame_grafica = Frame(pestaña)
    frame_grafica.place(relx=0.35, rely=0, relwidth=0.65, relheight=0.90)

    frame_calculadora = Frame(pestaña)
    frame_calculadora.place(relx=0, rely=0, relwidth=0.35, relheight=1)

    frame_funciones = Frame(pestaña)
    frame_funciones.place(relx=0.35, rely=0.90, relwidth=0.65, relheight=0.10)

    pestaña.iconbitmap('VIEW_logo.ico')


    fuente = tkFont.Font(family="Open Sans", size=15)

    entrada = Entry(frame_calculadora, font=fuente,bg="#dff6e7", relief="flat")
    entrada.place(relx=0.035, rely=0.06, relwidth=0.92, relheight=0.055 )
    
    entrada_result= Entry(frame_calculadora, font=fuente,bg="#dff6e7", relief="flat", justify="right")
    entrada_result.place(relx=0.035, rely=0.13, relwidth=0.92, relheight=0.055)

    entrada.focus_set()

    fig = Figure()
    ax = fig.add_subplot(111)
    plot_graph(fig,ax,frame_grafica,0,0,entrada,frame_funciones,color_select)

    entradas = [0,0,0,0]

    boton_1 = Button(frame_calculadora, text="1",font=("Open Sans",13),compound="center", command= lambda : [click_boton(pestaña,entradas,entrada,1),boton_presionado("boton_1"),print(boton_1.winfo_width())])
    boton_1.place(relx=0.035, rely=0.7825, relwidth=0.145, relheight=0.09)

    boton_2 = Button(frame_calculadora, text="2",font=("Open Sans",13),compound="center", command= lambda : [click_boton(pestaña,entradas,entrada,2),boton_presionado("boton_2")])
    boton_2.place(relx=0.191, rely=0.7825, relwidth=0.145, relheight=0.09)

    boton_3 = Button(frame_calculadora, text="3",font=("Open Sans",13),compound="center", command= lambda : [click_boton(pestaña,entradas,entrada,3),boton_presionado("boton_3")])
    boton_3.place(relx=0.347, rely=0.7825, relwidth=0.145, relheight=0.09)

    boton_4 = Button(frame_calculadora, text="4",font=("Open Sans",13),compound="center", command= lambda : [click_boton(pestaña,entradas,entrada,4),boton_presionado("boton_4")])
    boton_4.place(relx=0.035, rely=0.685, relwidth=0.145, relheight=0.09)

    boton_5 = Button(frame_calculadora, text="5",font=("Open Sans",13),compound="center", command= lambda : [click_boton(pestaña,entradas,entrada,5),boton_presionado("boton_5")])
    boton_5.place(relx=0.191, rely=0.685, relwidth=0.145, relheight=0.09)

    boton_6 = Button(frame_calculadora, text="6",font=("Open Sans",13),compound="center", command= lambda : [click_boton(pestaña,entradas,entrada,6),boton_presionado("boton_6")])
    boton_6.place(relx=0.347, rely=0.685, relwidth=0.145, relheight=0.09)

    boton_7 = Button(frame_calculadora, text="7",font=("Open Sans",13),compound="center", command= lambda : [click_boton(pestaña,entradas,entrada,7),boton_presionado("boton_7")])
    boton_7.place(relx=0.035, rely=0.5875, relwidth=0.145, relheight=0.09)

    boton_8 = Button(frame_calculadora, text="8",font=("Open Sans",13),compound="center", command= lambda : [click_boton(pestaña,entradas,entrada,8),boton_presionado("boton_8")])
    boton_8.place(relx=0.191, rely=0.5875, relwidth=0.145, relheight=0.09)

    boton_9 = Button(frame_calculadora, text="9",font=("Open Sans",13),compound="center", command= lambda : [click_boton(pestaña,entradas,entrada,9),boton_presionado("boton_9")])
    boton_9.place(relx=0.347, rely=0.5875, relwidth=0.145, relheight=0.09)

    boton_0 = Button(frame_calculadora, text="0",font=("Open Sans",13),compound="center", command= lambda : [click_boton(pestaña,entradas,entrada,0),boton_presionado("boton_0")])
    boton_0.place(relx=0.191, rely=0.88, relwidth=0.145, relheight=0.09)

    boton_punto = Button(frame_calculadora, text=".",font=("Open Sans",13),compound="center", command= lambda : [click_boton(pestaña,entradas,entrada,"."),boton_presionado("boton_punto")])
    boton_punto.place(relx=0.035, rely=0.88, relwidth=0.145, relheight=0.09)

    boton_igual = Button(frame_calculadora, text="=",font=("Open Sans",13),compound="center", command= lambda : [click_boton(pestaña,entradas,entrada,"="),boton_presionado("boton_igual")])
    boton_igual.place(relx=0.347, rely=0.88, relwidth=0.145, relheight=0.09)

    boton_mas = Button(frame_calculadora, text="+",font=("Open Sans",13),compound="center", command= lambda : [click_boton(pestaña,entradas,entrada,"+"),boton_presionado("boton_mas")])
    boton_mas.place(relx=0.503, rely=0.88, relwidth=0.145, relheight=0.09)

    boton_menos = Button(frame_calculadora, text="-",font=("Open Sans",13),compound="center", command= lambda : [click_boton(pestaña,entradas,entrada,"-"),boton_presionado("boton_menos")])
    boton_menos.place(relx=0.503, rely=0.7825,relwidth=0.145, relheight=0.09)

    boton_por = Button(frame_calculadora, text="×",font=("Open Sans",13),compound="center", command= lambda : [click_boton(pestaña,entradas,entrada,"×"),boton_presionado("boton_por")])
    boton_por.place(relx=0.503, rely=0.685,relwidth=0.145, relheight=0.09)

    boton_division = Button(frame_calculadora, text="÷",font=("Open Sans",13),compound="center", command= lambda : [click_boton(pestaña,entradas,entrada,"÷"),boton_presionado("boton_division")])
    boton_division.place(relx=0.503, rely=0.5875,relwidth=0.145, relheight=0.09)

    boton_resultado = Button(frame_calculadora, text="Graficar/Resultado",font=("Open Sans",7),compound="center",command= lambda : [guardar_ans(entrada_result),mostrar_funciones (entrada,frame_funciones,traduccion(fig,ax,entrada,entrada_result,frame_grafica,frame_funciones,color_select)),data(usuario,obtener_fecha_actual(),opciones(),entrada)])
    boton_resultado.place(relx=0.659, rely=0.1975,relwidth=0.30, relheight=0.09)

    boton_izquierda = Button(frame_calculadora, text="˂",font=("Open Sans",13),compound="center", command= lambda : [ cursor_izquierda(pestaña,entradas,entrada)])
    boton_izquierda.place(relx=0.035, rely=0.1975,relwidth=0.145, relheight=0.09)

    boton_arriba = Button(frame_calculadora, text="˄",font=("Open Sans",13),compound="center", command= lambda : [cursor_arriba(entrada,entrada_result)])
    boton_arriba.place(relx=0.191, rely=0.1975, relwidth=0.145, relheight=0.09)

    boton_abajo = Button(frame_calculadora, text="˅",font=("Open Sans",13),compound="center", command= lambda : [cursor_abajo(entrada,entrada_result)])
    boton_abajo.place(relx=0.347, rely=0.1975, relwidth=0.145, relheight=0.09)

    boton_derecha = Button(frame_calculadora, text="˃",font=("Open Sans",13),compound="center", command= lambda : [cursor_derecha(pestaña,entradas,entrada)])
    boton_derecha.place(relx=0.503, rely=0.1975, relwidth=0.145, relheight=0.09)

    boton_sen = Button(frame_calculadora, text="sen",font=("Open Sans",13),compound="center", command= lambda : [click_boton(pestaña,entradas,entrada,"sen("),boton_presionado("boton_sen")])
    boton_sen.place(relx=0.035, rely=0.295, relwidth=0.145, relheight=0.09)

    boton_cos = Button(frame_calculadora, text="cos",font=("Open Sans",13),compound="center", command= lambda : [click_boton(pestaña,entradas,entrada,"cos("),boton_presionado("boton_cos")])
    boton_cos.place(relx=0.191, rely=0.295, relwidth=0.145, relheight=0.09)

    boton_tg = Button(frame_calculadora, text="tg",font=("Open Sans",13),compound="center", command= lambda : [click_boton(pestaña,entradas,entrada,"tg("),boton_presionado("boton_tg")])
    boton_tg.place(relx=0.347, rely=0.295, relwidth=0.145, relheight=0.09)

    boton_asen = Button(frame_calculadora, text="sen-1",font=("Open Sans",11),compound="center", command= lambda : [click_boton(pestaña,entradas,entrada,"sen-1("),boton_presionado("boton_asen")])
    boton_asen.place(relx=0.503, rely=0.295, relwidth=0.145, relheight=0.09)

    boton_acos = Button(frame_calculadora, text="cos-1",font=("Open Sans",11),compound="center", command= lambda : [click_boton(pestaña,entradas,entrada,"cos-1("),boton_presionado("boton_acos")])
    boton_acos.place(relx=0.659, rely=0.295, relwidth=0.145, relheight=0.09)

    boton_atg = Button(frame_calculadora, text="tg-1",font=("Open Sans",11),compound="center", command= lambda : [click_boton(pestaña,entradas,entrada,"tg-1("),boton_presionado("boton_atg")])
    boton_atg.place(relx=0.815, rely=0.295, relwidth=0.145, relheight=0.09)

    boton_pi = Button(frame_calculadora, text="ℼ",font=("Times New Roman",13, "italic"),compound="center", command= lambda : [click_boton(pestaña,entradas,entrada,"ℼ"),boton_presionado("boton_pi")])
    boton_pi.place(relx=0.035, rely=0.3925, relwidth=0.145, relheight=0.09)

    boton_euler = Button(frame_calculadora, text="e",font=("Times New Roman",13, "italic"),compound="center", command= lambda : [click_boton(pestaña,entradas,entrada,"e"),boton_presionado("boton_euler")])
    boton_euler.place(relx=0.191, rely=0.3925, relwidth=0.145, relheight=0.09)

    boton_x = Button(frame_calculadora, text="x",font=("Times New Roman",13, "italic"),compound="center", command= lambda : [click_boton(pestaña,entradas,entrada,"x"),boton_presionado("boton_x")])
    boton_x.place(relx=0.347, rely=0.3925, relwidth=0.145, relheight=0.09)

    boton_y = Button(frame_calculadora, text="y",font=("Times New Roman",13, "italic"),compound="center", command= lambda : [click_boton(pestaña,entradas,entrada,"y"),boton_presionado("boton_y")])
    boton_y.place(relx=0.503, rely=0.3925, relwidth=0.145, relheight=0.09)

    boton_DEL = Button(frame_calculadora, text="DEL",font=("Open Sans",13),compound="center", command= lambda : [DEL(pestaña,entradas,entrada)])
    boton_DEL.place(relx=0.659, rely=0.3925, relwidth=0.145, relheight=0.09)

    boton_AC = Button(frame_calculadora, text="AC",font=("Open Sans",13),compound="center",command= lambda : [AC(pestaña,entradas,entrada,entrada_result)])
    boton_AC.place(relx=0.815, rely=0.3925, relwidth=0.145, relheight=0.09)

    boton_logaritmo = Button(frame_calculadora, text="log",font=("Open Sans",13),compound="center", command= lambda : [click_boton(pestaña,entradas,entrada,"log_()("),boton_presionado("boton_logaritmo")])
    boton_logaritmo.place(relx=0.035, rely=0.49, relwidth=0.145, relheight=0.09)

    boton_ln = Button(frame_calculadora, text="ln",font=("Open Sans",13),compound="center", command= lambda : [click_boton(pestaña,entradas,entrada,"ln("),boton_presionado("boton_ln")])
    boton_ln.place(relx=0.191, rely=0.49, relwidth=0.145, relheight=0.09)

    boton_potencia = Button(frame_calculadora, text="□▫",font=("Open Sans",13),compound="center", command= lambda : [click_boton(pestaña,entradas,entrada,"()^("),boton_presionado("boton_potencia")])
    boton_potencia.place(relx=0.347, rely=0.49, relwidth=0.145, relheight=0.09)

    boton_raiz = Button(frame_calculadora, text="▫√",font=("Open Sans",13),compound="center", command= lambda : [ click_boton(pestaña,entradas,entrada,"()^√("),boton_presionado("boton_raiz")])
    boton_raiz.place(relx=0.503, rely=0.49, relwidth=0.145, relheight=0.09)

    boton_parentesis_a = Button(frame_calculadora, text="(",font=("Open Sans",13),compound="center", command= lambda : [click_boton(pestaña,entradas,entrada,"("),boton_presionado("boton_parentesis_a")])
    boton_parentesis_a.place(relx=0.659, rely=0.49, relwidth=0.145, relheight=0.09)

    boton_parentesis_c = Button(frame_calculadora, text=")",font=("Open Sans",13),compound="center", command= lambda : [click_boton(pestaña,entradas,entrada,")"),boton_presionado("boton_parentesis_c")])
    boton_parentesis_c.place(relx=0.815, rely=0.49, relwidth=0.145, relheight=0.09)

    boton_valor_adsoluto = Button(frame_calculadora, text="|□|",font=("Open Sans",13),compound="center", command= lambda : [click_boton(pestaña,entradas,entrada,"|"),boton_presionado("boton_valor_adsoluto")])
    boton_valor_adsoluto.place(relx=0.659, rely=0.5875, relwidth=0.145, relheight=0.09)

    boton_fraccion = Button(frame_calculadora, text="▫∕▫",font=("Open Sans",13),compound="center", command= lambda : [click_boton(pestaña,entradas,entrada,"() ∕ ("),boton_presionado("boton_fraccion")])
    boton_fraccion.place(relx=0.815, rely=0.5875, relwidth=0.145, relheight=0.09)

    boton_cientifica = Button(frame_calculadora, text="×10▫",font=("Open Sans",13),compound="center", command= lambda : [click_boton(pestaña,entradas,entrada,"()×10^("),boton_presionado("boton_cientifica")])
    boton_cientifica.place(relx=0.659, rely=0.685, relwidth=0.145, relheight=0.09)

    boton_ANS = Button(frame_calculadora, text="ANS",font=("Open Sans",13),compound="center", command= lambda : [ANS(entrada)])
    boton_ANS.place(relx=0.815, rely=0.685, relwidth=0.145, relheight=0.09)

    boton_porcentaje = Button(frame_calculadora, text="%",font=("Open Sans",13),compound="center", command= lambda : [click_boton(pestaña,entradas,entrada,"()%("),boton_presionado("boton_porcentaje")])
    boton_porcentaje.place(relx=0.659, rely=0.7825, relwidth=0.145, relheight=0.09)

    boton_ala_diez = Button(frame_calculadora, text="10▫",font=("Open Sans",13),compound="center", command= lambda : [click_boton(pestaña,entradas,entrada,"10^("),boton_presionado("boton_ala_diez")])
    boton_ala_diez.place(relx=0.815, rely=0.7825, relwidth=0.145, relheight=0.09)

    boton_e = Button(frame_calculadora, text="e▫",font=("Times New Roman",13, "italic"),compound="center", command= lambda : [click_boton(pestaña,entradas,entrada,"e^("),boton_presionado("boton_e") ])
    boton_e.place(relx=0.659, rely=0.88, relwidth=0.145, relheight=0.09)

    boton_factorial = Button(frame_calculadora, text="!",font=("Times New Roman",13),compound="center", command= lambda : [click_boton(pestaña,entradas,entrada,"!("),boton_presionado("boton_factorial")])
    boton_factorial.place(relx=0.815, rely=0.88, relwidth=0.145, relheight=0.09)

    boton_historial = Button(frame_calculadora, text="Historial",font=("Open Sans",8),compound="center", command = lambda : historial(pestaña))
    boton_historial.place(relx= 0.285, rely = 0.002, relwidth=0.330, relheight=0.05 )

    boton_eli_his = Button(frame_calculadora, text="Eliminar Historial",font=("Open Sans",8),compound="center", command = lambda : eliminar_historial(pestaña))
    boton_eli_his.place(relx= 0.622, rely = 0.002, relwidth=0.330, relheight=0.05 )

    boton_conf = Button(frame_calculadora, command= lambda : menu_confi ())
    boton_conf.place(relx= 0.035, rely = 0.002, relwidth=0.093, relheight=0.05 )

    boton_tema = Button(frame_calculadora, command= lambda : modo() )
    boton_tema.place(relx= 0.132, rely = 0.002, relwidth=0.15, relheight=0.05 )

    botones_num = [boton_1,boton_2,boton_3,boton_4,boton_5,boton_6,boton_7,boton_8,boton_9,boton_0]

    botones_oper = [boton_punto,boton_igual,boton_mas,boton_menos,boton_por,boton_division,boton_igual,boton_izquierda,boton_arriba,boton_abajo,boton_derecha,boton_sen,boton_cos,boton_tg,
                    boton_asen,boton_acos,boton_atg,boton_pi,boton_euler,boton_x,boton_y,boton_logaritmo,boton_ln,boton_potencia,boton_raiz,boton_parentesis_a,boton_parentesis_c,
                    boton_valor_adsoluto,boton_fraccion,boton_cientifica,boton_porcentaje,boton_ala_diez,boton_e,boton_factorial,boton_ANS]
    
    botones_res = [boton_resultado,boton_DEL,boton_AC] 

    botones_conf = [boton_historial,boton_eli_his,boton_conf,boton_tema]

    botones_esp =[boton_pi,boton_euler,boton_x,boton_y,boton_e,boton_factorial]

    bot.extend([botones_num,botones_conf,botones_oper,botones_res,botones_esp])

    entrada.bind("<Configure>",diseño )

    monitor_internet_connection()


    pestaña.mainloop()


menu_abierto = False  
menu_abierto_eli = False
menu_conf = False


def historial(pestaña):

    global menu_principal, submenu, submenu_frame, submenu_valores, menu_abierto,us

    if check_internet_connection_tem() == True:

        if menu_abierto:

            us.destroy()
            menu_principal.place_forget()
            submenu_frame.place_forget()
            menu_abierto = False

        else: 

            try:

                us = Label(frame_calculadora, text=f"Usuario Actual: {usuario}")
                us.place(relx=0.035, rely=0.052, relwidth=0.920, relheight=0.04)

                menu_principal = ttk.Combobox(frame_calculadora, values=nodo(usuario))
                menu_principal.place(relx=0.035, rely=0.092, relwidth=0.920, relheight=0.04)
                menu_principal.set(nodo(usuario)[-1])

                submenu_frame = Frame(frame_calculadora)
                submenu = Listbox(submenu_frame, selectmode="single")
                submenu.pack(side="left", fill="both", expand=True)  # Empaqueta la Listbox
                barra_desplazamiento = Scrollbar(submenu_frame, orient="vertical", command=submenu.yview)
                barra_desplazamiento.pack(side="right", fill="y")  # Empaqueta la barra de desplazamiento
                submenu.config(yscrollcommand=barra_desplazamiento.set)  # Configura la barra de desplazamiento
                submenu_frame.place(relx=0.035, rely=0.1322, relwidth=0.920, relheight=0.2)

                submenu_valores = []  # Inicializamos la lista vacía

                menu_principal.bind("<<ComboboxSelected>>", mostrar_submenu)
                mostrar_submenu(None)
                menu_abierto = True

            except Exception as e:

                us.destroy()
                messagebox.showerror("Error", f"No Existe Historial de {usuario}")

    else:

        mostrar_mensaje()


def mostrar_submenu(event):

    global menu_principal, submenu, submenu_frame, submenu_valores, menu_abierto
    
    seleccionar_opcion = menu_principal.get()
    submenu.delete(0, END)
    submenu_valore = subnodos(usuario,seleccionar_opcion)
    sub = len(submenu_valore)
    i = 0
    
    for i in range (i,sub):

        submenu.insert(END,valor(usuario,seleccionar_opcion,submenu_valore[i]) )

    submenu.see(END)
        
    submenu.config(width=300)
    menu_principal.select_clear()
    submenu_frame.place(relx=0.035, rely=0.132, relwidth=0.920, relheight=0.2)

    submenu.bind("<ButtonRelease-1>", lambda event: obtener_opcion_seleccionada())

    submenu.bind("<Button-1>", cerrar_hasta_combobox,)

def cerrar_hasta_combobox(event):

    global menu_principal, submenu, submenu_frame, menu_abierto

    menu_principal.place_forget()
    submenu_frame.place_forget()
    menu_abierto = False

def eliminar_historial (pestaña):

    global menu_principal, submenu, submenu_frame, submenu_valores, menu_abierto,us

    if check_internet_connection_tem() == True:

        if menu_abierto:  

            us.destroy()
            menu_principal.place_forget()
            submenu_frame.place_forget()
            menu_abierto = False

        else:  

            try:

                us = Label(frame_calculadora, text=f"Usuario Actual: {usuario}")
                us.place(relx=0.035, rely=0.052, relwidth=0.920, relheight=0.04)

                menu_principal = ttk.Combobox(frame_calculadora, values=nodo(usuario))
                menu_principal.place(relx=0.035, rely=0.092, relwidth=0.920, relheight=0.04)
                menu_principal.set(nodo(usuario)[-1])

                submenu_frame = Frame(frame_calculadora)
                submenu = Listbox(submenu_frame, selectmode="single")
                submenu.pack(side="left", fill="both", expand=True)  
                barra_desplazamiento = Scrollbar(submenu_frame, orient="vertical", command=submenu.yview)
                barra_desplazamiento.pack(side="right", fill="y")  
                submenu.config(yscrollcommand=barra_desplazamiento.set)  
                submenu_frame.place(relx=0.035, rely=0.132, relwidth=0.920, relheight=0.2)

                submenu_valores = []  

                menu_principal.bind("<<ComboboxSelected>>", eliminar_submenu)
                eliminar_submenu(None)
                menu_abierto = True

            except Exception as e:

                us.destroy()
                messagebox.showerror("Error", f"No Existe Historial de {usuario}")

    else:
        mostrar_mensaje()


def eliminar_submenu(event):

    global menu_principal, submenu, submenu_frame, submenu_valores, menu_abierto,sub

    seleccionar_opcion = menu_principal.get()
    submenu.delete(0, END)
    submenu_valore = subnodos(usuario,seleccionar_opcion)
    sub = len(submenu_valore)
    i = 0
    
    for i in range (i,sub):

        submenu.insert(END,valor(usuario,seleccionar_opcion,submenu_valore[i]) )

    submenu.see(END)
        
    submenu.config(width=300)
    menu_principal.select_clear()
    submenu_frame.place(relx=0.035, rely=0.132, relwidth=0.920, relheight=0.2)

    submenu.bind("<ButtonRelease-1>", lambda event: obtener_opcion_seleccionada_eli(seleccionar_opcion,submenu_valore))
   
    submenu.bind("<Button-1>", cerrar_hasta_combobox_eli)


def cerrar_hasta_combobox_eli(event):

    global menu_principal, submenu, submenu_frame, menu_abierto_eli,us

    menu_principal.place_forget()
    submenu_frame.place_forget()
    us.destroy()
    menu_abierto_eli = False


def obtener_fecha_actual():

    fecha_actual = str(datetime.today().strftime("%Y-%m-%d"))
    return fecha_actual

def data (usuario,fecha,opcion,entrada):

    if entrada_result.get() != "Syntax Error":

        if type(entrada) == str:

            ecuacion = entrada

            if leerBok(usuario,fecha) == "None":
                crear(usuario,fecha,opcion,ecuacion)
                
            else:
                act(usuario,fecha,opcion,ecuacion)
            
        else:

            inline = check_internet_connection_tem()

            if inline == True:

                ecuacion = entrada.get()

                if leerBok(usuario,fecha) == "None":
                    crear(usuario,fecha,opcion,ecuacion)
                
                else:
                    act(usuario,fecha,opcion,ecuacion)

            else:
                
                ecuacion=entrada.get()
                datos = {usuario:{fecha : {opcion: ecuacion}}}
                save_data_locally(datos)


def obtener_opcion_seleccionada():

    global opcion_seleccionada

    color_select = ""

    seleccion_indices = submenu.curselection()

    if seleccion_indices:  

        indice_seleccionado = seleccion_indices[0]  
        opcion_seleccionada = submenu.get(indice_seleccionado)  
        entrada.delete(0,END)
        entrada.insert(0,opcion_seleccionada)

        traduccion(fig,ax,entrada,entrada_result,frame_grafica,frame_funciones,color_select),guardar_ans(entrada_result),mostrar_funciones(entrada, frame_funciones)
            

def obtener_opcion_seleccionada_eli(seleccionar_opcion,submenu_valore):

    global opcion_seleccionada_eli

    seleccion_indices = submenu.curselection()

    if seleccion_indices:  

        indice_seleccionado = seleccion_indices[0]  
        opcion_seleccionada_eli = submenu.get(indice_seleccionado)  

        subno = submenu_valore[indice_seleccionado]

        borrar(usuario,seleccionar_opcion,subno)


def mostrar_funciones (entrada,frame_funciones,si):

    global funciones,j,mi_bool,fun,po_col,po_fil,lista_check

    if si == True:

        glob = globals()
        funcion_c = glob.get("line")
        fun = entrada.get()

        if fun != "":   

            for i in range(0, len(funcion_c)):

                ver = funcion_c[i]

                if ver[0] == fun :

                    color = ver[2]

            funciones.append(entrada.get())
        
            mi_bool= BooleanVar()
            mi_bool.set(True)

            if est_modo == False:

                j = Checkbutton(frame_funciones, text=f"Mostrar Función {fun}",font=("Open Sans", 10),bg="#B2B2B2",selectcolor=color, variable=mi_bool)
                j.place(relx=po_col*0.333333 , rely=po_fil*0.5, relwidth=0.333333, relheight=0.5)
                lista_check.append(j)

            else:

                j = Checkbutton(frame_funciones, text=f"Mostrar Función {fun}",font=("Open Sans", 10),bg="white",selectcolor=color, variable=mi_bool)
                j.place(relx=po_col*0.333333 , rely=po_fil*0.5, relwidth=0.333333, relheight=0.5)
                lista_check.append(j)


            if po_fil == 1:

                po_col +=1
                po_fil = 0

            else:

                po_fil +=1

            mi_bool.nombre = fun
            mi_bool.checkbutton = j
            mi_bool.trace_add("write",  lambda *args, b=mi_bool: eliminar_funcion(ax, fig, frame_grafica,b))


def eliminar_funcion(ax,fig,frame_grafica,mi_bool):

    fun = mi_bool.nombre

    if mi_bool.get():

        color_select = mi_bool.checkbutton.cget("selectcolor")

        traduccion(fig,ax,fun,entrada_result,frame_grafica,frame_funciones,color_select)

    else:

        glob = globals()
        linea = glob.get("line")

        for i in range(0,len(linea)):

            ver = linea[i]

            if ver[0] == fun:

                ver_1 = ver[1]
                line.pop(i)

                ver_1[0].remove()

                canvas = FigureCanvasTkAgg(fig, master=frame_grafica)
                canvas.draw()
                canvas_widget = canvas.get_tk_widget()
                canvas_widget.place(relx=0, rely= 0, relwidth=1, relheight=0.9)
                toolbar = NavigationToolbar2Tk(canvas, frame_grafica)
                toolbar.update()
                toolbar.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)
                break


def diseño (event):

    if est_modo == False :

        frame_calculadora.config(bg="#899aa4")
        frame_funciones.config(bg="#B2B2B2")

        zip_path = 'VIEW_Botones.zip'
        imagen_noche_numeros = 'boton modo noche numeros.png'
        imagen_noche_oper = "boton modo oscuro operaciones.png"
        imagen_noche_res = "boton modo noche res.png"
        imagen_noche_conf = "boton conf noche.png"
        imagen_modo_noche = "modo noche.png"
        imagen_conf = "Component 2.png"

        image_noche_num = extraer_imagen_desde_zip(zip_path, imagen_noche_numeros)
        image_noche_oper = extraer_imagen_desde_zip(zip_path, imagen_noche_oper)
        image_noche_res = extraer_imagen_desde_zip(zip_path, imagen_noche_res)
        image_noche_conf = extraer_imagen_desde_zip(zip_path, imagen_noche_conf)
        image_modo_noche = extraer_imagen_desde_zip(zip_path, imagen_modo_noche)
        image_conf = extraer_imagen_desde_zip(zip_path,imagen_conf)

        for i in botones_num:
            
            aplicar_fondo(i,image_noche_num)
            i.config(bg="#899aa4")
            i.config(fg="white")
            i.config(bd=0)
            i.config(highlightthickness=0)
            

        for i in botones_oper:

            aplicar_fondo(i,image_noche_oper)
            i.config(bg="#899aa4")
            i.config(fg="white")
            i.config(bd=0)
            i.config(highlightthickness=0)

        for i in botones_res:

            aplicar_fondo(i,image_noche_res)
            i.config(bg="#899aa4")
            i.config(fg="white")
            i.config(bd=0)
            i.config(highlightthickness=0)

        for i in botones_conf:

            aplicar_fondo(i,image_noche_conf)
            i.config(bg="#899aa4")
            i.config(fg="white")
            i.config(bd=0)
            i.config(highlightthickness=0)

        aplicar_fondo(boton_tema,image_modo_noche)
        aplicar_fondo(boton_conf,image_conf)

        for i in lista_check:

            i.config(bg="#B2B2B2")
            i.config(bd=0)
            i.config(highlightthickness=0)

        if len(fra_men) > 0 :

            fra_men[0].config(bg="#B2B2B2")
            fra_men[1].config(bg="#B2B2B2")

    else:

        frame_calculadora.config(bg="#F0F0F0")
        frame_funciones.config(bg="white")

        zip_path = 'VIEW_Botones.zip'
        imagen_dia_numeros = 'boton modo dia numero.png'
        imagen_dia_oper = "boton modo dia operaciones.png"
        imagen_dia_res = "boton modo dia res.png"
        imagen_dia_conf = "boton conf dia.png"
        imagen_modo_dia = "modo dia.png"
        image_conf_dia = "Component 1.png"

        image_dia_num = extraer_imagen_desde_zip(zip_path, imagen_dia_numeros)
        image_dia_oper = extraer_imagen_desde_zip(zip_path, imagen_dia_oper)
        image_dia_res = extraer_imagen_desde_zip(zip_path, imagen_dia_res)
        image_dia_conf = extraer_imagen_desde_zip(zip_path, imagen_dia_conf)
        image_modo_dia = extraer_imagen_desde_zip(zip_path, imagen_modo_dia)
        image_conf_dia = extraer_imagen_desde_zip(zip_path,image_conf_dia)

        for i in botones_num:
            
            aplicar_fondo(i,image_dia_num)
            i.config(bg="#F0F0F0")
            i.config(fg="black")
            i.config(bd=0)
            i.config(highlightthickness=0)

        for i in botones_oper:

            aplicar_fondo(i,image_dia_oper)
            i.config(bg="#F0F0F0")
            i.config(fg="black")
            i.config(bd=0)
            i.config(highlightthickness=0)

        for i in botones_res:

            aplicar_fondo(i,image_dia_res)
            i.config(bg="#F0F0F0")
            i.config(fg="black")
            i.config(bd=0)
            i.config(highlightthickness=0)

        for i in botones_conf:

            aplicar_fondo(i,image_dia_conf)
            i.config(bg="#F0F0F0")
            i.config(fg="black")
            i.config(bd=0)
            i.config(highlightthickness=0)

        aplicar_fondo(boton_tema,image_modo_dia)
        aplicar_fondo(boton_conf,image_conf_dia)

        for i in lista_check:

            i.config(bg="white")
            i.config(bd=0)
            i.config(highlightthickness=0)

        if len(fra_men) > 0 :

            fra_men[0].config(bg="white")
            fra_men[1].config(bg="white")


def modo():

    global est_modo

    if est_modo == True :

        est_modo = False
        diseño(None)

    else:

        est_modo = True
        diseño(None)


def extraer_imagen_desde_zip(zip_path, imagen_nombre):
        
        with zipfile.ZipFile(zip_path, 'r') as archivo_zip:

            with archivo_zip.open(imagen_nombre) as archivo_imagen:

                imagen_bytes = archivo_imagen.read() 
                imagen = Image.open(io.BytesIO(imagen_bytes)) 
                return imagen
            

def menu_confi ():

    global  conf_abierto,frame_menu,var,fra_men,menu,boton_tam_fun,boton_tip_fun,menu_tip,boton_inicio_se,us_men

    if conf_abierto:

        frame_menu.destroy()
        us_men.destroy()
        fra_men.pop(0)
        fra_men.pop(0)
        conf_abierto = False

    else:  

        if est_modo == False:

            frame_menu = Frame(pestaña, bg="#B2B2B2")
            fra_men.append(frame_menu)

        else:

            frame_menu = Frame(pestaña)
            fra_men.append(frame_menu)

        frame_menu.place(relx=0.012, rely=0.051, relwidth=0.20, relheight=0.4)
        var = IntVar(value=1)

        if est_modo == False:

            us_men = Label(frame_menu,text=f"Usuario Actual : {usuario}",bg="#B2B2B2")
            us_men.place(relx=0.002, rely=0, relwidth=1)

            checkbutton = Checkbutton(frame_menu, text=" Grilla en el plano cartesiano", bg="#B2B2B2", variable=var, command=toggle_checkbutton)
            checkbutton.place(relx=0.002, rely=0.166)
            fra_men.append(checkbutton)

            zip_path = 'VIEW_Botones.zip'
            imagen_noche_conf = "boton conf noche.png"
            image_noche_conf = extraer_imagen_desde_zip(zip_path, imagen_noche_conf)
            

            boton_tam_fun = Button(frame_menu, text=f"Tamaño de fuente : {tam_act}",bg="#B2B2B2",compound="center",fg="white",bd=0,highlightthickness=0)
            boton_tam_fun.place(relx=0.05, rely=0.332, relwidth=0.9)
            resized_image = redimencionar_imagen(image_noche_conf, 162, 20)
            boton_tam_fun.config(image=resized_image)
            boton_tam_fun.image = resized_image

            pestaña.option_add('*Menu*background', '#B2B2B2')

            menu = Menu(pestaña, tearoff=0)
            menu.add_command(label="+ 2", command=lambda: tamaño_fuente (1))
            menu.add_command(label="Reestablecer", command=lambda: tamaño_fuente (2))
            menu.add_command(label="- 2", command=lambda: tamaño_fuente (3))

            boton_tip_fun = Button(frame_menu, text=f"Tipo de fuente : {tip_act}",bg="#B2B2B2",compound="center",fg="white",bd=0,highlightthickness=0)
            boton_tip_fun.place(relx=0.05, rely=0.498, relwidth=0.9)
            resized_image = redimencionar_imagen(image_noche_conf, 162, 20)
            boton_tip_fun.config(image=resized_image)
            boton_tip_fun.image = resized_image


            menu_tip = Menu(pestaña, tearoff=0)
            menu_tip.add_command(label="Courier New", command=lambda: tip_fuente (1))
            menu_tip.add_command(label="Reestablecer", command=lambda: tip_fuente (2))
            menu_tip.add_command(label="Comic", command=lambda: tip_fuente (3))

            if usuario == "Invitado":

                boton_inicio_se = Button(frame_menu, text="Iniciar sesión",bg="#B2B2B2",compound="center",fg="white",bd=0,highlightthickness=0, command=venta_sesion)
                boton_inicio_se.place(relx=0.05, rely=0.664, relwidth=0.9)
                resized_image = redimencionar_imagen(image_noche_conf, 162, 20)
                boton_inicio_se.config(image=resized_image)
                boton_inicio_se.image = resized_image
            
            else:

                boton_inicio_se = Button(frame_menu, text="Cerrar sesión",bg="#B2B2B2",compound="center",fg="white",bd=0,highlightthickness=0, command= ac_ )
                boton_inicio_se.place(relx=0.05, rely=0.664, relwidth=0.9)
                resized_image = redimencionar_imagen(image_noche_conf, 162, 20)
                boton_inicio_se.config(image=resized_image)
                boton_inicio_se.image = resized_image

            boton_inicio_re = Button(frame_menu, text="Registrarse",bg="#B2B2B2",compound="center",fg="white",bd=0,highlightthickness=0, command=venta_registro)
            boton_inicio_re.place(relx=0.05, rely=0.83, relwidth=0.9)
            resized_image = redimencionar_imagen(image_noche_conf, 162, 20)
            boton_inicio_re.config(image=resized_image)
            boton_inicio_re.image = resized_image

            boton_tam_fun.bind("<Button-1>", show_menu)
            boton_tip_fun.bind("<Button-1>", show_menu_tip)

        else:

            us_men = Label(frame_menu,text=f"Usuario Actual : {usuario}",)
            us_men.place(relx=0.002, rely=0, relwidth=1)

            checkbutton = Checkbutton(frame_menu, text=" Grilla en el plano cartesiano", variable=var, command=toggle_checkbutton)
            checkbutton.place(relx=0.002, rely=0.166)
            fra_men.append(checkbutton)

            zip_path = 'VIEW_Botones.zip'
            imagen_dia_conf = "boton conf dia.png"
            image_dia_conf = extraer_imagen_desde_zip(zip_path, imagen_dia_conf)

            pestaña.option_add('*Menu*background', 'white')

            boton_tam_fun = Button(frame_menu, text=f"Tamaño de fuente : {tam_act}",compound="center",bd=0,highlightthickness=0)
            boton_tam_fun.place(relx=0.05, rely=0.332, relwidth=0.9)
            resized_image = redimencionar_imagen(image_dia_conf, 162, 20)
            boton_tam_fun.config(image=resized_image)
            boton_tam_fun.image = resized_image

            menu = Menu(pestaña, tearoff=0)
            menu.add_command(label="+ 5", command=lambda: tamaño_fuente (1))
            menu.add_command(label="Reestablecer", command=lambda: tamaño_fuente (2))
            menu.add_command(label="- 5", command=lambda: tamaño_fuente (3))

            boton_tip_fun = Button(frame_menu, text=f"Tipo de fuente : {tip_act}",compound="center",bd=0,highlightthickness=0)
            boton_tip_fun.place(relx=0.05, rely=0.498, relwidth=0.9)
            resized_image = redimencionar_imagen(image_dia_conf, 162, 20)
            boton_tip_fun.config(image=resized_image)
            boton_tip_fun.image = resized_image

            menu_tip = Menu(pestaña, tearoff=0)
            menu_tip.add_command(label="Courier New", command=lambda: tip_fuente (1))
            menu_tip.add_command(label="Reestablecer", command=lambda: tip_fuente (2))
            menu_tip.add_command(label="Comic", command=lambda: tip_fuente (3))

            if usuario == "Invitado":

                boton_inicio_se = Button(frame_menu, text="Iniciar sesión",compound="center",bd=0,highlightthickness=0, command= venta_sesion)
                boton_inicio_se.place(relx=0.05, rely=0.664, relwidth=0.9)
                resized_image = redimencionar_imagen(image_dia_conf, 162, 20)
                boton_inicio_se.config(image=resized_image)
                boton_inicio_se.image = resized_image

            else:

                boton_inicio_se = Button(frame_menu, text="Cerrar sesión",compound="center",bd=0,highlightthickness=0, command= ac_ )
                boton_inicio_se.place(relx=0.05, rely=0.664, relwidth=0.9)
                resized_image = redimencionar_imagen(image_dia_conf, 162, 20)
                boton_inicio_se.config(image=resized_image)
                boton_inicio_se.image = resized_image

            boton_inicio_re = Button(frame_menu, text="Registrarse",compound="center",bd=0,highlightthickness=0, command=venta_registro)
            boton_inicio_re.place(relx=0.05, rely=0.83, relwidth=0.9)
            resized_image = redimencionar_imagen(image_dia_conf, 162, 20)
            boton_inicio_re.config(image=resized_image)
            boton_inicio_re.image = resized_image

            boton_tam_fun.bind("<Button-1>", show_menu)
            boton_tip_fun.bind("<Button-1>", show_menu_tip)

        conf_abierto = True


def ac_():

    global usuario,boton_inicio_se,frame_menu,fra_men,conf_abierto

    if usuario != "Invitado":

        usuario = "Invitado"
        boton_inicio_se.config(text="Iniciar sesión")
        frame_menu.destroy()
        fra_men.pop(0)
        fra_men.pop(0)
        conf_abierto = False


def ac ():

    global usuario,boton_inicio_se

    if usuario == "Invitado":

        boton_inicio_se.config(text="Iniciar sesión")

    else:

        boton_inicio_se.config(text="Cerrar sesión")


def eliminar_grid():

    global activar_gird
    
    if activar_gird == True:

        activar_gird = False

        ax.set_title('Plano Cartesiano')
        ax.set_xlabel('Eje X')
        ax.set_ylabel('Eje Y')
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)

        if activar_gird == True:
            ax.grid(True)

        else:
            ax.grid(False)

        canvas = FigureCanvasTkAgg(fig, master=frame_grafica)
        canvas.draw()
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.place(relx=0, rely= 0, relwidth=1, relheight=0.9)
        toolbar = NavigationToolbar2Tk(canvas, frame_grafica)
        toolbar.update()
        toolbar.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)
    
    else:

        activar_gird = True

        ax.set_title('Plano Cartesiano')
        ax.set_xlabel('Eje X')
        ax.set_ylabel('Eje Y')
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)

        if activar_gird == True:
            ax.grid(True)

        else:
            ax.grid(False)
        
        canvas = FigureCanvasTkAgg(fig, master=frame_grafica)
        canvas.draw()
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.place(relx=0, rely= 0, relwidth=1, relheight=0.9)
        toolbar = NavigationToolbar2Tk(canvas, frame_grafica)
        toolbar.update()
        toolbar.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)

    
def toggle_checkbutton():

    if var.get() == 0:  
        eliminar_grid()

    else:
        eliminar_grid()


def tamaño_fuente (op):

    global tam_act,tam

    if op == 1:
        
        for j in bot:

            for i in j:

                current_font_name = i.cget("font")  
                current_font = font.Font(font=current_font_name)
                current_size = current_font.cget("size")       
                nuevo_tamano = current_size + 2
                current_font.configure(size=nuevo_tamano)
                i.config(font=current_font)

        current_font_name = entrada.cget("font")  
        current_font = font.Font(font=current_font_name)
        current_size = current_font.cget("size")       
        nuevo_tamano = current_size + 2
        current_font.configure(size=nuevo_tamano)
        entrada.config(font=current_font)

        current_font_name = entrada_result.cget("font")  
        current_font = font.Font(font=current_font_name)
        current_size = current_font.cget("size")       
        nuevo_tamano = current_size + 2
        current_font.configure(size=nuevo_tamano)
        entrada_result.config(font=current_font)

        for l in lista_check:

            current_font_name = l.cget("font")  
            current_font = font.Font(font=current_font_name)
            current_size = current_font.cget("size")      
            nuevo_tamano = current_size + 2
            current_font.configure(size=nuevo_tamano)
            l.config(font=current_font)

        tam_act = "+ 2"
        tam += 2
        boton_tam_fun.config(text="Tamaño de fuente : + 5") 

    elif op == 3:
        
        for j in bot:

            for i in j:

                current_font_name = i.cget("font") 
                current_font = font.Font(font=current_font_name)
                current_size = current_font.cget("size")      
                nuevo_tamano = current_size - 2
                current_font.configure(size=nuevo_tamano)
                i.config(font=current_font)

        current_font_name = entrada.cget("font") 
        current_font = font.Font(font=current_font_name)
        current_size = current_font.cget("size")       
        nuevo_tamano = current_size + 2
        current_font.configure(size=nuevo_tamano)
        entrada.config(font=current_font)

        current_font_name = entrada_result.cget("font")  
        current_font = font.Font(font=current_font_name)
        current_size = current_font.cget("size")       
        nuevo_tamano = current_size - 2
        current_font.configure(size=nuevo_tamano)
        entrada_result.config(font=current_font)

        for l in lista_check:

            current_font_name = l.cget("font")  
            current_font = font.Font(font=current_font_name)
            current_size = current_font.cget("size")       
            nuevo_tamano = current_size - 2
            current_font.configure(size=nuevo_tamano)
            l.config(font=current_font)

        tam_act = "- 2"
        tam -= 2
        boton_tam_fun.config(text="Tamaño de fuente : - 5") 

    else:
        
        for j in bot:

            for i in j:

                current_font_name = i.cget("font")  
                current_font = font.Font(font=current_font_name)
                current_size = current_font.cget("size")     
                nuevo_tamano = current_size - tam
                current_font.configure(size=nuevo_tamano)
                i.config(font=current_font)

        current_font_name = entrada.cget("font") 
        current_font = font.Font(font=current_font_name)
        current_size = current_font.cget("size")     
        nuevo_tamano = current_size - tam
        current_font.configure(size=nuevo_tamano)
        entrada.config(font=current_font)

        current_font_name = entrada.cget("font") 
        current_font = font.Font(font=current_font_name)
        current_size = current_font.cget("size")       
        nuevo_tamano = current_size - tam
        current_font.configure(size=nuevo_tamano)
        entrada_result.config(font=current_font)

        for l in lista_check:

            current_font_name = l.cget("font")  
            current_font = font.Font(font=current_font_name)
            current_size = current_font.cget("size")       
            nuevo_tamano = current_size - tam
            current_font.configure(size=nuevo_tamano)
            l.config(font=current_font)

        tam_act = "Pre"
        tam = 0
        boton_tam_fun.config(text="Tamaño de fuente : Pre") 
        

def tip_fuente (op):

    global tip_act

    if op == 1:
        
        for j in bot:

            for i in j:

                current_font_name = i.cget("font")  
                current_font = font.Font(font=current_font_name)
                current_font.configure(family="Courier New")
                i.config(font=current_font)

        current_font_name = entrada.cget("font")  
        current_font = font.Font(font=current_font_name)
        current_font.configure(family="Courier New")
        entrada.config(font=current_font)

        current_font_name = entrada_result.cget("font")  
        current_font = font.Font(font=current_font_name)
        current_font.configure(family="Courier New")
        entrada_result.config(font=current_font)

        for l in lista_check:

            current_font_name = l.cget("font")  
            current_font = font.Font(font=current_font_name)
            current_font.configure(family="Courier New")
            l.config(font=current_font)

        tip_act = "Courier New"
        boton_tip_fun.config(text="Tamaño de fuente : Courier New") 

    elif op == 3:
        
        for j in bot:

            for i in j:

                current_font_name = i.cget("font")  
                current_font = font.Font(font=current_font_name)
                current_font.configure(family="Comic Sans MS")
                i.config(font=current_font)

        current_font_name = entrada.cget("font")  
        current_font = font.Font(font=current_font_name)
        current_font.configure(family="Comic Sans MS")
        entrada.config(font=current_font)

        current_font_name = entrada_result.cget("font")  
        current_font = font.Font(font=current_font_name)
        current_font.configure(family="Comic Sans MS")
        entrada_result.config(font=current_font)

        for l in lista_check:

            current_font_name = l.cget("font")  
            current_font = font.Font(font=current_font_name)
            current_font.configure(family="Comic Sans MS")
            l.config(font=current_font)

        tip_act = "Comic Sans MS"
        boton_tip_fun.config(text="Tamaño de fuente : Comic") 

    else:
        
        for j in bot:

            for i in j:

                current_font_name = i.cget("font")  
                current_font = font.Font(font=current_font_name)
                current_font.configure(family="Open Sans")
                i.config(font=current_font)

        current_font_name = entrada.cget("font")  
        current_font = font.Font(font=current_font_name)
        current_font.configure(family="Open Sans")
        entrada.config(font=current_font)

        current_font_name = entrada_result.cget("font")  
        current_font = font.Font(font=current_font_name)
        current_font.configure(family="Open Sans")
        entrada_result.config(font=current_font)

        for l in bot[-1]:

            current_font_name = l.cget("font")  
            current_font = font.Font(font=current_font_name)
            current_font.configure(family="Times New Roman")
            l.config(font=current_font)

        for l in lista_check:

            current_font_name = l.cget("font")  
            current_font = font.Font(font=current_font_name)
            current_font.configure(family="Open Sans")
            l.config(font=current_font)

        tip_act = "Pre"
        boton_tip_fun.config(text="Tamaño de fuente : Pre") 
        

def show_menu(event):

    frame_x = boton_tam_fun.winfo_rootx()
    frame_y = boton_tam_fun.winfo_rooty()
    fixed_x = frame_x + 170   
    fixed_y = frame_y  
    menu.post(fixed_x, fixed_y)


def show_menu_tip(event):

    frame_x = boton_tip_fun.winfo_rootx()
    frame_y = boton_tip_fun.winfo_rooty()
    fixed_x = frame_x + 190  
    fixed_y = frame_y  
    menu_tip.post(fixed_x, fixed_y)


def check_internet_connection():

    while True:

        try:

            requests.get("http://www.google.com", timeout=5)
            sync_data_to_firebase()
            
        except:

            print()
            
        threading.Event().wait(90)
        
    
def check_internet_connection_tem():

    try:

        urllib.request.urlopen('https://www.google.com', timeout=5)
        return True
    except:

        return False  


def save_data_locally(data, file_name='CONTROLLER_base_de_datos_offline.json'):

    try:

        with open(file_name, 'r+') as file:
            local_data = json.load(file)

    except FileNotFoundError:
        local_data = []

    local_data.append(data)

    with open(file_name, 'w') as file:
        json.dump(local_data, file)


def sync_data_to_firebase(file_name='CONTROLLER_base_de_datos_offline.json'):

    try:

        with open(file_name, 'r') as file:
            local_data = json.load(file)

    except FileNotFoundError:
        local_data = []

    for dato in local_data:

        usaa=dato.keys()
        usaa_=list(usaa)
        usa=usaa_[0]
        tracicion_f=dato.get(usaa_[0])
        fecha=tracicion_f.keys()
        fecha_=list(fecha)
        fecha_d = fecha_[0]
        trancision= tracicion_f.get(fecha_[0])
        opcion=trancision.keys()
        opcion_=list(opcion)
        opcion_d=opcion_[0]
        funcion=trancision.get(opcion_[0])
        data(usa,fecha_d,opcion_d,funcion)

    with open(file_name, 'w') as file:

        json.dump([], file)

        with open(file_name, 'r') as file:

            try:
                
                datos = json.load(file)
            except json.JSONDecodeError:

                datos = []


def venta_sesion():
        
    global usuario

    if usuario == "Invitado":

        zip_path = 'VIEW_Botones.zip'
        imagen_noche_conf = "boton conf noche.png"
        image_noche_conf = extraer_imagen_desde_zip(zip_path, imagen_noche_conf)

        vent_sesion = Toplevel(pestaña)
        vent_sesion.title("Inicio de sesión")
        vent_sesion.configure(bg='#B2B2B2')
        vent_sesion.geometry("200x150+230+160")

        vent_sesion.transient(pestaña)
        

        vent_sesion.grab_set()

        Label(vent_sesion, text="Correo:",bg='#B2B2B2').place(relx=0.05,rely=0.05,relwidth=0.9)
        email_entry_sesion = Entry(vent_sesion)
        email_entry_sesion.place(relx=0.05,rely=0.2,relwidth=0.9)
        
        Label(vent_sesion, text="Contraseña:",bg='#B2B2B2').place(relx=0.05,rely=0.35,relwidth=0.9)
        password_entry_sesion = Entry(vent_sesion, show="*")
        password_entry_sesion.place(relx=0.05,rely=0.5,relwidth=0.9)

        login_button = Button(vent_sesion, text="Iniciar sesión",bg="#B2B2B2",compound="center",fg="white",bd=0,highlightthickness=0, command=  lambda: login(email_entry_sesion,password_entry_sesion,vent_sesion))
        login_button.place(relx=0.05,rely=0.75,relwidth=0.9)
        resized_image = redimencionar_imagen(image_noche_conf, 180, 26)
        login_button.config(image=resized_image)
        login_button.image = resized_image

    else:

        ac()


def venta_registro():

    zip_path = 'VIEW_Botones.zip'
    imagen_noche_conf = "boton conf noche.png"
    image_noche_conf = extraer_imagen_desde_zip(zip_path, imagen_noche_conf)

    vent_registro = Toplevel(pestaña)
    vent_registro.title("Registrarse")
    vent_registro.configure(bg='#B2B2B2')
    vent_registro.geometry("200x150+230+160")

    vent_registro.transient(pestaña)

    vent_registro.grab_set()

    Label(vent_registro, text="Correo:",bg='#B2B2B2').place(relx=0.05,rely=0.05,relwidth=0.9)
    email_entry_regis = Entry(vent_registro)
    email_entry_regis.place(relx=0.05,rely=0.2,relwidth=0.9)
    
    Label(vent_registro, text="Contraseña:",bg='#B2B2B2').place(relx=0.05,rely=0.35,relwidth=0.9)
    password_entry_regis = Entry(vent_registro, show="*")
    password_entry_regis.place(relx=0.05,rely=0.5,relwidth=0.9)

    login_button = Button(vent_registro, text="Crear usuario",bg="#B2B2B2",compound="center",fg="white",bd=0,highlightthickness=0, command= lambda: signup(email_entry_regis,password_entry_regis,vent_registro))
    login_button.place(relx=0.05,rely=0.75,relwidth=0.9)
    resized_image = redimencionar_imagen(image_noche_conf, 180, 26)
    login_button.config(image=resized_image)
    login_button.image = resized_image


def login(email_entry_sesion,password_entry_sesion,vent_sesion):

    global usuario,fra_men,conf_abierto,frame_menu,us_men

    email = email_entry_sesion.get()
    password = password_entry_sesion.get()

    try:

        user = auth.sign_in_with_email_and_password(email, password)
        messagebox.showinfo("Éxito", "Has iniciado sesión correctamente")
        posicion = email.find("@")

        if posicion != -1:
            cadena_cortada = email[:posicion]
            
        else:
            cadena_cortada = email

        usuario = cadena_cortada
        vent_sesion.destroy()
        frame_menu.destroy()
        us_men.destroy()
        fra_men.pop(0)
        fra_men.pop(0)
        conf_abierto = False

        
    except:

        messagebox.showerror("Error", "Correo o contraseña incorrectos")


def signup(email_entry_regis,password_entry_regis,vent_registro):

    global usuario,fra_men,conf_abierto,frame_menu,us_men

    email = email_entry_regis.get()
    password = password_entry_regis.get()

    try:

        user = auth.create_user_with_email_and_password(email, password)
        messagebox.showinfo("Éxito", "Usuario creado con éxito")
        posicion = email.find("@")

        if posicion != -1:
            cadena_cortada = email[:posicion]
            
        else:
            cadena_cortada = email

        usuario = cadena_cortada
        vent_registro.destroy()
        us_men.destroy()
        frame_menu.destroy()
        fra_men.pop(0)
        fra_men.pop(0)
        conf_abierto = False

    except:

        messagebox.showerror("Error", "No se pudo crear el usuario")


def redimencionar_imagen(imagen, width, height):
    
    image = imagen.resize((width, height), Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(image)


def aplicar_fondo(boton, imagen):
    
    width = boton.winfo_width()
    height = boton.winfo_height()
    resized_image = redimencionar_imagen(imagen, width, height)
    boton.config(image=resized_image)
    boton.image = resized_image


def monitor_internet_connection():
    threading.Thread(target=check_internet_connection, daemon=True).start()


def mostrar_mensaje():
    messagebox.showinfo("Error de conexion", "En este momento no tienes internet, porfavor conectate a una red de internet para mostrar el historial")