
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from datetime import datetime
from Plano_cartesiano import *
from funciones_calculadora import *
from funciones_operaciones import *
from database import *

menu_abierto = False

def ventana ():

    global entrada,entrada_result,pestaña,entrada_x1,entrada_x2,entrada_y1,entrada_y2

    # Crear la ventana principal de Tkinter
    pestaña = Tk()
    pestaña.title("CALCULADORA GRAFICA")
    pestaña.geometry("900x500+220+100")

    icono = PhotoImage(file="logo.gif")
    pestaña.iconphoto(True, icono)

    # Crear el limite entre la calculadora y la grafica
    canvas= Canvas(pestaña, width=1050, height=650, bg="white")
    canvas.pack()
    canvas.create_line(320, 0,320,500, fill="black")
    canvas.create_line(320, 460, 900, 460, fill="black")

    # Definir el tamaño de la fuente y el tipo
    fuente = tkFont.Font(family="Lucida Grande", size=15)

    # Crear la entrada

    entrada = Entry(pestaña, font=fuente, relief="flat")
    entrada.place(x=10, y=22, width=300, height=25 )
    entrada.bind("<Key>", bloqueo_teclado)
    
    entrada_result= Entry(pestaña, font=fuente, relief="flat", justify="right")
    entrada_result.place(x=10, y=67, width=300, height=25)
    entrada_result.bind("<Key>", bloqueo_teclado)

    
    # Entrada de los rangos de x y Y

    tex_x = Label(pestaña, text="Rango de x =")
    tex_x.place(x=425, y=470, width=70)

    entrada_x1 = Entry(pestaña)
    entrada_x1.place(x=495, y=470, width=30, height=20)
    entrada_x1.bind("<Key>", bloqueo_teclado)

    tex_x_= Label(pestaña, text=",")
    tex_x_.place(x=525, y=470)

    entrada_x2 = Entry(pestaña)
    entrada_x2.place(x=530, y=470, width=30, height=20)
    entrada_x2.bind("<Key>", bloqueo_teclado)

    tex_y = Label(pestaña, text="Rango de y =")
    tex_y.place(x=650, y=470, width=70)

    entrada_y1 = Entry(pestaña)
    entrada_y1.place(x=720, y=470, width=30, height=20)
    entrada_y1.bind("<Key>", bloqueo_teclado)

    tex_y_= Label(pestaña, text=",")
    tex_y_.place(x=750, y=470)

    entrada_y2 = Entry(pestaña)
    entrada_y2.place(x=755, y=470, width=30, height=20)
    entrada_y2.bind("<Key>", bloqueo_teclado)

    # Poner el cursor en la entrada principal
    entrada.focus_set()

    # Crear una plano cartesiano base
    plot_graph(entrada,pestaña,0,0,0,20)

    # CRear una variable que contenga todas las demas entradas
    entradas = [entrada_x1,entrada_x2,entrada_y1,entrada_y2]

    # Botones de la calculadora
    boton_1 = Button(pestaña, text="1", command= lambda : [click_boton(pestaña,entradas,entrada,1),boton_presionado("boton_1")])
    boton_1.place(x=10, y=390, width=50, height=50)

    boton_2 = Button(pestaña, text="2", command= lambda : [click_boton(pestaña,entradas,entrada,2),boton_presionado("boton_2")])
    boton_2.place(x=60, y=390, width=50, height=50)

    boton_3 = Button(pestaña, text="3", command= lambda : [click_boton(pestaña,entradas,entrada,3),boton_presionado("boton_3")])
    boton_3.place(x=110, y=390, width=50, height=50)

    boton_4 = Button(pestaña, text="4", command= lambda : [click_boton(pestaña,entradas,entrada,4),boton_presionado("boton_4")])
    boton_4.place(x=10, y=340, width=50, height=50)

    boton_5 = Button(pestaña, text="5", command= lambda : [click_boton(pestaña,entradas,entrada,5),boton_presionado("boton_5")])
    boton_5.place(x=60, y=340, width=50, height=50)

    boton_6 = Button(pestaña, text="6", command= lambda : [click_boton(pestaña,entradas,entrada,6),boton_presionado("boton_6")])
    boton_6.place(x=110, y=340, width=50, height=50)

    boton_7 = Button(pestaña, text="7", command= lambda : [click_boton(pestaña,entradas,entrada,7),boton_presionado("boton_7")])
    boton_7.place(x=10, y=290, width=50, height=50)

    boton_8 = Button(pestaña, text="8", command= lambda : [click_boton(pestaña,entradas,entrada,8),boton_presionado("boton_8")])
    boton_8.place(x=60, y=290, width=50, height=50)

    boton_9 = Button(pestaña, text="9", command= lambda : [click_boton(pestaña,entradas,entrada,9),boton_presionado("boton_9")])
    boton_9.place(x=110, y=290, width=50, height=50)

    boton_0 = Button(pestaña, text="0", command= lambda : [click_boton(pestaña,entradas,entrada,0),boton_presionado("boton_0")])
    boton_0.place(x=60, y=440, width=50, height=50)

    boton_punto = Button(pestaña, text=".", command= lambda : [click_boton(pestaña,entradas,entrada,"."),boton_presionado("boton_punto")])
    boton_punto.place(x=10, y=440, width=50, height=50)

    boton_igual = Button(pestaña, text="=", command= lambda : [click_boton(pestaña,entradas,entrada,"="),boton_presionado("boton_igual")])
    boton_igual.place(x=110, y=440, width=50, height=50)

    boton_mas = Button(pestaña, text="+", command= lambda : [click_boton(pestaña,entradas,entrada,"+"),boton_presionado("boton_mas")])
    boton_mas.place(x=160, y=440, width=50, height=50)

    boton_menos = Button(pestaña, text="-", command= lambda : [click_boton(pestaña,entradas,entrada,"-"),boton_presionado("boton_menos")])
    boton_menos.place(x=160, y=390, width=50, height=50)

    boton_por = Button(pestaña, text="×", command= lambda : [click_boton(pestaña,entradas,entrada,"×"),boton_presionado("boton_por")])
    boton_por.place(x=160, y=340, width=50, height=50)

    boton_division = Button(pestaña, text="÷", command= lambda : [click_boton(pestaña,entradas,entrada,"÷"),boton_presionado("boton_division")])
    boton_division.place(x=160, y=290, width=50, height=50)

    boton_resultado = Button(pestaña, text="Graficar/Resultado", bg="#0CD765",command= lambda : [traduccion(entrada,entrada_result,pestaña,entrada_x1,entrada_x2,entrada_y1,entrada_y2),guardar_ans(entrada_result),data(obtener_fecha_actual(),opciones(),entrada)])
    boton_resultado.place(x=210, y=90, width=100, height=50)

    boton_izquierda = Button(pestaña, text="˂", command= lambda : [ cursor_izquierda(pestaña,entradas,entrada)])
    boton_izquierda.place(x=10, y=90, width=50, height=50)

    boton_arriba = Button(pestaña, text="˄", command= lambda : [cursor_arriba(entrada,entrada_result)])
    boton_arriba.place(x=60, y=90, width=50, height=50)

    boton_abajo = Button(pestaña, text="˅", command= lambda : [cursor_abajo(entrada,entrada_result)])
    boton_abajo.place(x=110, y=90, width=50, height=50)

    boton_derecha = Button(pestaña, text="˃", command= lambda : [cursor_derecha(pestaña,entradas,entrada)])
    boton_derecha.place(x=160, y=90, width=50, height=50)

    boton_sen = Button(pestaña, text="sen", command= lambda : [click_boton(pestaña,entradas,entrada,"sen("),boton_presionado("boton_sen")])
    boton_sen.place(x=10, y=140, width=50, height=50)

    boton_cos = Button(pestaña, text="cos", command= lambda : [click_boton(pestaña,entradas,entrada,"cos("),boton_presionado("boton_cos")])
    boton_cos.place(x=60, y=140, width=50, height=50)

    boton_tg = Button(pestaña, text="tg", command= lambda : [click_boton(pestaña,entradas,entrada,"tg("),boton_presionado("boton_tg")])
    boton_tg.place(x=110, y=140, width=50, height=50)

    boton_asen = Button(pestaña, text="sen-1", command= lambda : [click_boton(pestaña,entradas,entrada,"sen-1("),boton_presionado("boton_asen")])
    boton_asen.place(x=160, y=140, width=50, height=50)

    boton_acos = Button(pestaña, text="cos-1", command= lambda : [click_boton(pestaña,entradas,entrada,"cos-1("),boton_presionado("boton_acos")])
    boton_acos.place(x=210, y=140, width=50, height=50)

    boton_atg = Button(pestaña, text="tg-1", command= lambda : [click_boton(pestaña,entradas,entrada,"tg-1("),boton_presionado("boton_atg")])
    boton_atg.place(x=260, y=140, width=50, height=50)

    boton_pi = Button(pestaña, text="ℼ", command= lambda : [click_boton(pestaña,entradas,entrada,"ℼ"),boton_presionado("boton_pi")])
    boton_pi.place(x=10, y=190, width=50, height=50)

    boton_euler = Button(pestaña, text="e", command= lambda : [click_boton(pestaña,entradas,entrada,"e"),boton_presionado("boton_euler")])
    boton_euler.place(x=60, y=190, width=50, height=50)

    boton_x = Button(pestaña, text="x", command= lambda : [click_boton(pestaña,entradas,entrada,"x"),boton_presionado("boton_x")])
    boton_x.place(x=110, y=190, width=50, height=50)

    boton_y = Button(pestaña, text="y", command= lambda : [click_boton(pestaña,entradas,entrada,"y"),boton_presionado("boton_y")])
    boton_y.place(x=160, y=190, width=50, height=50)

    boton_DEL = Button(pestaña, text="DEL",bg="#0CD765", command= lambda : [DEL(pestaña,entradas,entrada)])
    boton_DEL.place(x=210, y=190, width=50, height=50)

    boton_AC = Button(pestaña, text="AC", bg="#0CD765",command= lambda : [AC(pestaña,entradas,entrada,entrada_result),plot_graph(entrada,pestaña,0,0,0,20)])
    boton_AC.place(x=260, y=190, width=50, height=50)

    boton_logaritmo = Button(pestaña, text="log", command= lambda : [click_boton(pestaña,entradas,entrada,"log_()("),boton_presionado("boton_logaritmo")])
    boton_logaritmo.place(x=10, y=240, width=50, height=50)

    boton_ln = Button(pestaña, text="ln", command= lambda : [click_boton(pestaña,entradas,entrada,"ln("),boton_presionado("boton_ln")])
    boton_ln.place(x=60, y=240, width=50, height=50)

    boton_potencia = Button(pestaña, text="□▫", command= lambda : [click_boton(pestaña,entradas,entrada,"()^("),boton_presionado("boton_potencia")])
    boton_potencia.place(x=110, y=240, width=50, height=50)

    boton_raiz = Button(pestaña, text="▫√", command= lambda : [ click_boton(pestaña,entradas,entrada,"()^√("),boton_presionado("boton_raiz")])
    boton_raiz.place(x=160, y=240, width=50, height=50)

    boton_parentesis_a = Button(pestaña, text="(", command= lambda : [click_boton(pestaña,entradas,entrada,"("),boton_presionado("boton_parentesis_a")])
    boton_parentesis_a.place(x=210, y=240, width=50, height=50)

    boton_parentesis_c = Button(pestaña, text=")", command= lambda : [click_boton(pestaña,entradas,entrada,")"),boton_presionado("boton_parentesis_c")])
    boton_parentesis_c.place(x=260, y=240, width=50, height=50)

    boton_valor_adsoluto = Button(pestaña, text="|□|", command= lambda : [click_boton(pestaña,entradas,entrada,"|"),boton_presionado("boton_valor_adsoluto")])
    boton_valor_adsoluto.place(x=210, y=290, width=50, height=50)

    boton_fraccion = Button(pestaña, text="▫∕▫", command= lambda : [click_boton(pestaña,entradas,entrada,"() ∕ ("),boton_presionado("boton_fraccion")])
    boton_fraccion.place(x=260, y=290, width=50, height=50)

    boton_cientifica = Button(pestaña, text="×10▫", command= lambda : [click_boton(pestaña,entradas,entrada,"()×10^("),boton_presionado("boton_cientifica")])
    boton_cientifica.place(x=210, y=340, width=50, height=50)

    boton_ANS = Button(pestaña, text="ANS", command= lambda : [ANS(entrada)])
    boton_ANS.place(x=260, y=340, width=50, height=50)

    boton_porcentaje = Button(pestaña, text="%", command= lambda : [click_boton(pestaña,entradas,entrada,"()%("),boton_presionado("boton_porcentaje")])
    boton_porcentaje.place(x=210, y=390, width=50, height=50)

    boton_ala_diez = Button(pestaña, text="10▫", command= lambda : [click_boton(pestaña,entradas,entrada,"10^("),boton_presionado("boton_ala_diez")])
    boton_ala_diez.place(x=260, y=390, width=50, height=50)

    boton_e = Button(pestaña, text="e▫", command= lambda : [click_boton(pestaña,entradas,entrada,"e^("),boton_presionado("boton_e") ])
    boton_e.place(x=210, y=440, width=50, height=50)

    boton_factorial = Button(pestaña, text="!", command= lambda : [click_boton(pestaña,entradas,entrada,"!("),boton_presionado("boton_factorial")])
    boton_factorial.place(x=260, y=440, width=50, height=50)

    boton_historial = Button(pestaña, text="Historial", command = lambda : historial(pestaña))
    boton_historial.place(x= 10, y = 2, width=100, height=15 )

    boton_eli_his = Button(pestaña, text="Eliminar Historial", command = lambda : eliminar_historial(pestaña))
    boton_eli_his.place(x= 110, y = 2, width=100, height=15 )

    # Ejecutar el bucle principal de Tkinter
    pestaña.mainloop()

# Variable global para rastrear si el menú está abierto o cerrado
menu_abierto = False  
menu_abierto_eli = False

def historial(pestaña):

    global menu_principal, submenu, submenu_frame, submenu_valores, menu_abierto

    if menu_abierto:  # Si el menú está abierto, ciérralo
        menu_principal.place_forget()
        submenu_frame.place_forget()
        menu_abierto = False

    else:  # Si el menú está cerrado, ábrelo

        menu_principal = ttk.Combobox(pestaña, values=nodo())
        menu_principal.place(x=10, y=17, width=300, height=20)
        menu_principal.set(nodo()[-1])

        submenu_frame = Frame(pestaña)
        submenu = Listbox(submenu_frame, selectmode="single")
        submenu.pack(side="left", fill="both", expand=True)  # Empaqueta la Listbox
        barra_desplazamiento = Scrollbar(submenu_frame, orient="vertical", command=submenu.yview)
        barra_desplazamiento.pack(side="right", fill="y")  # Empaqueta la barra de desplazamiento
        submenu.config(yscrollcommand=barra_desplazamiento.set)  # Configura la barra de desplazamiento
        submenu_frame.place(x=10, y=37, width=300, height=100)

        submenu_valores = []  # Inicializamos la lista vacía

        menu_principal.bind("<<ComboboxSelected>>", mostrar_submenu)
        mostrar_submenu(None)
        menu_abierto = True


def mostrar_submenu(event):

    global menu_principal, submenu, submenu_frame, submenu_valores, menu_abierto
    
    seleccionar_opcion = menu_principal.get()
    submenu.delete(0, END)
    submenu_valore = subnodos(seleccionar_opcion)
    sub = len(submenu_valore)
    i = 0
    
    for i in range (i,sub):
        submenu.insert(END,valor(seleccionar_opcion,submenu_valore[i]) )

    submenu.see(END)
        
    submenu.config(width=300)
    menu_principal.select_clear()
    submenu_frame.place(x=10, y=37, width=300, height=100)

    submenu.bind("<ButtonRelease-1>", lambda event: obtener_opcion_seleccionada())

    # Cerrar hasta la Combobox cuando se selecciona una opción 
    submenu.bind("<Button-1>", cerrar_hasta_combobox,)

def cerrar_hasta_combobox(event):

    global menu_principal, submenu, submenu_frame, menu_abierto
    menu_principal.place_forget()
    submenu_frame.place_forget()
    menu_abierto = False

def eliminar_historial (pestaña):

    global menu_principal, submenu, submenu_frame, submenu_valores, menu_abierto

    if menu_abierto:  # Si el menú está abierto, ciérralo

        menu_principal.place_forget()
        submenu_frame.place_forget()
        menu_abierto = False

    else:  # Si el menú está cerrado, ábrelo

        menu_principal = ttk.Combobox(pestaña, values=nodo())
        menu_principal.place(x=10, y=17, width=300, height=20)
        menu_principal.set(nodo()[-1])

        submenu_frame = Frame(pestaña)
        submenu = Listbox(submenu_frame, selectmode="single")
        submenu.pack(side="left", fill="both", expand=True)  # Empaqueta la Listbox
        barra_desplazamiento = Scrollbar(submenu_frame, orient="vertical", command=submenu.yview)
        barra_desplazamiento.pack(side="right", fill="y")  # Empaqueta la barra de desplazamiento
        submenu.config(yscrollcommand=barra_desplazamiento.set)  # Configura la barra de desplazamiento
        submenu_frame.place(x=10, y=37, width=300, height=100)

        submenu_valores = []  # Inicializamos la lista vacía

        menu_principal.bind("<<ComboboxSelected>>", eliminar_submenu)
        eliminar_submenu(None)
        menu_abierto = True

def eliminar_submenu(event):

    global menu_principal, submenu, submenu_frame, submenu_valores, menu_abierto,sub
    seleccionar_opcion = menu_principal.get()

    submenu.delete(0, END)
    
    submenu_valore = subnodos(seleccionar_opcion)
    sub = len(submenu_valore)
    i = 0
    
    for i in range (i,sub):
        submenu.insert(END,valor(seleccionar_opcion,submenu_valore[i]) )

    submenu.see(END)
        
    submenu.config(width=300)
    menu_principal.select_clear()
    submenu_frame.place(x=10, y=37, width=300, height=100)

    submenu.bind("<ButtonRelease-1>", lambda event: obtener_opcion_seleccionada_eli(seleccionar_opcion,submenu_valore))

    # Cerrar hasta la Combobox cuando se selecciona una opción A, B o C
    submenu.bind("<Button-1>", cerrar_hasta_combobox_eli)

def cerrar_hasta_combobox_eli(event):

    global menu_principal, submenu, submenu_frame, menu_abierto_eli
    menu_principal.place_forget()
    submenu_frame.place_forget()
    menu_abierto_eli = False


def obtener_fecha_actual():

    fecha_actual = str(datetime.today().strftime("%Y-%m-%d"))
    return fecha_actual

def data (fecha,opcion,entrada):

    ecuacion = entrada.get()

    if leerBok(fecha) == "None":
        crear(fecha,opcion,ecuacion)
    
    else:
        act(fecha,opcion,ecuacion)


def obtener_opcion_seleccionada():

    global opcion_seleccionada

    seleccion_indices = submenu.curselection()

    if seleccion_indices:  # Verifica si se ha seleccionado alguna opción

        indice_seleccionado = seleccion_indices[0]  # Obtiene el índice de la opción seleccionada
        opcion_seleccionada = submenu.get(indice_seleccionado)  # Obtiene el valor de la opción seleccionada
        entrada.delete(0,END)
        entrada.insert(0,opcion_seleccionada)

        traduccion(entrada,entrada_result,pestaña,entrada_x1,entrada_x2,entrada_y1,entrada_y2),guardar_ans(entrada_result)
            

def obtener_opcion_seleccionada_eli(seleccionar_opcion,submenu_valore):

    global opcion_seleccionada_eli

    seleccion_indices = submenu.curselection()

    if seleccion_indices:  # Verifica si se ha seleccionado alguna opción

        indice_seleccionado = seleccion_indices[0]  # Obtiene el índice de la opción seleccionada
        opcion_seleccionada_eli = submenu.get(indice_seleccionado)  # Obtiene el valor de la opción seleccionada

        subno = submenu_valore[indice_seleccionado]

        borrar(seleccionar_opcion,subno)