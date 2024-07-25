from tkinter import *
from funciones_operaciones import *
contador = 0000
entradaANS = 0
contador_sen = 0
contador_cos = 0
contador_tg = 0
contador_sen1 = 0
contador_cos1 = 0
contador_tg1= 0
contador_vads = 0
contador_raiz = 0
contador_porcentaje = 0
contador_cientifico = 0
contador_fraccion = 0
contador_potencia = 0
contador_logaritmo = 0 
contador_ln = 0
contador_base_diez = 0
contador_euler = 0
contador_factorial = 0
bo_log = 0
ultimo_boton = ""


def ANS(entrada):

    global entradaANS
    entrada.get()
    entrada.insert(0,entradaANS)



def guardar_ans(resultado):

    global entradaANS
    entradaANS = resultado.get()



def cursor_izquierda(pestaña,entradas,entrada):

    global movidas_izq
    texto=entrada.get()
    contador = len(texto)
    foco = pestaña.focus_get()

    if foco == entrada:

        posicion_actual = entrada.index(INSERT)

        if entrada.get()[posicion_actual-2:posicion_actual] == "!(" or entrada.get()[posicion_actual-2:posicion_actual] == ")(":

            entrada.icursor(posicion_actual - 2)

        elif entrada.get()[posicion_actual-3:posicion_actual] == "e^(" or entrada.get()[posicion_actual-3:posicion_actual] == "tg(" or entrada.get()[posicion_actual-3:posicion_actual] == "ln(" or entrada.get()[posicion_actual-3:posicion_actual] == ")%(" or  entrada.get()[posicion_actual-3:posicion_actual] == ")^(":
            
            entrada.icursor(posicion_actual - 3)

        elif entrada.get()[posicion_actual-6:posicion_actual] == "sin-1(" or entrada.get()[posicion_actual-6:posicion_actual] == "cos-1(" or entrada.get()[posicion_actual-6:posicion_actual] == ")×10^(" :

            entrada.icursor(posicion_actual - 6)

        elif entrada.get()[posicion_actual-4:posicion_actual] == "sen(" or entrada.get()[posicion_actual-4:posicion_actual] == "cos(" or entrada.get()[posicion_actual-4:posicion_actual] == ")^√(" or entrada.get()[posicion_actual-4:posicion_actual] == "10^(" :

            entrada.icursor(posicion_actual - 4)

        elif entrada.get()[posicion_actual-5:posicion_actual] == "tg-1(" or entrada.get()[posicion_actual-5:posicion_actual] == "log_(" or entrada.get()[posicion_actual-5:posicion_actual] == ") ∕ (" :
            
            entrada.icursor(posicion_actual - 5)

        elif contador==posicion_actual:

            elem=ord(entrada.get()[posicion_actual-1])

            if elem >= 48 and elem <= 57 or elem >= 42 and elem <=43 or elem == 45 or elem == 46   or elem == 118 or elem == 47  or elem == 61 or elem == 80 or elem == 113 or elem == 69 or elem == 43 or elem == 120 or elem == 121 or elem >=102 and elem <= 104  or elem == 40 or elem == 41:
                entrada.icursor(posicion_actual - 1)

            elif elem == 82  :
                entrada.icursor(posicion_actual - 3)

        else:

            posicion_actual = entrada.index(INSERT)
            elem=ord(entrada.get()[posicion_actual-1])

            if elem >= 48 and elem <= 57 or elem >= 42 and elem <=45 or elem == 118 or elem == 47  or elem == 61 or elem == 80 or elem == 113 or elem == 69 or elem == 43 or elem == 120 or elem == 121 or elem >=102 and elem <= 104 or elem == 40:
                entrada.icursor(posicion_actual - 1)

            elif elem == 82  :
                entrada.icursor(posicion_actual - 3)


    elif foco == entradas[0]:

        posicion_actual = entradas[0].index(INSERT)
        entradas[0].icursor(posicion_actual - 1)

    elif foco == entradas[1]:

        posicion_actual = entradas[1].index(INSERT)
        entradas[1].icursor(posicion_actual - 1)

    elif foco == entradas[2]:

        posicion_actual = entradas[2].index(INSERT)
        entradas[2].icursor(posicion_actual - 1)

    elif foco == entradas[3]:

        posicion_actual = entradas[3].index(INSERT)
        entradas[3].icursor(posicion_actual - 1)



def cursor_derecha(pestaña,entradas,entrada):

    global contador_vads,contador_raiz,contador_porcentaje,contador_cientifico,contador_fraccion,contador_potencia,contador_logaritmo,contador_ln,contador_base_diez,contador_euler,contador_factorial,contador_sen,contador_cos,contador_tg,contador_sen1,contador_cos1,contador_tg1
    texto=entrada.get()
    contador = len(texto)
    foco = pestaña.focus_get()

    if foco == entrada:

        posicion_actual = entrada.index(INSERT)

        if contador_vads > 0 and len(texto)==posicion_actual:

            entrada.insert(posicion_actual,"|")

        elif contador_raiz == 2 :

            entrada.insert(posicion_actual,")")
            contador_raiz = 0

        elif contador_porcentaje == 2 :
            
            entrada.insert(posicion_actual,")")
            contador_porcentaje = 0

        elif contador_cientifico == 2 :

            entrada.insert(posicion_actual,")")
            contador_cientifico = 0

        elif contador_fraccion == 2 :

            entrada.insert(posicion_actual,")")
            contador_fraccion = 0

        elif contador_potencia == 2 :

            entrada.insert(posicion_actual,")")
            contador_potencia = 0

        elif contador_logaritmo == 2 :

            entrada.insert(posicion_actual,")")
            contador_logaritmo = 0

        elif contador_ln == 1 :

            entrada.insert(posicion_actual,")")
            contador_ln = 0

        elif contador_base_diez == 1 :

            entrada.insert(posicion_actual,")")
            contador_base_diez = 0

        elif contador_euler == 1 :

            entrada.insert(posicion_actual,")")
            contador_euler = 0

        elif contador_factorial == 1 :

            entrada.insert(posicion_actual,")")
            contador_factorial = 0

        elif contador_sen == 1 :

            entrada.insert(posicion_actual,")")
            contador_sen = 0

        elif contador_cos == 1 :

            entrada.insert(posicion_actual,")")
            contador_cos == 0

        elif contador_tg == 1 :

            entrada.insert(posicion_actual,")")
            contador_tg = 0 

        elif contador_sen1 == 1 :

            entrada.insert(posicion_actual,")")
            contador_sen1 == 0

        elif contador_cos1 == 1 :

            entrada.insert(posicion_actual,")")
            contador_cos1 = 0

        elif contador_tg1 == 1 :

            entrada.insert(posicion_actual,")")
            contador_tg1 = 0

        elif contador_vads == 1 :

            entrada.insert(posicion_actual,"|")
            contador_vads = 0

        else:

            if contador==posicion_actual:
                print("error")

            else:

                posicion_actual = entrada.index(INSERT)
                elem=ord(entrada.get()[posicion_actual])

                if elem >= 48 and elem <= 57 or elem >= 42 and elem <=45 or elem == 118 or elem == 47  or elem == 61 or elem == 80 or elem == 113 or elem == 69 or elem == 43 or elem == 120 or elem == 121 or elem >=102 and elem <= 104 :
                    entrada.icursor(posicion_actual + 1)

                elif elem == 82  :
                    entrada.icursor(posicion_actual + 3)

            if contador_logaritmo == 1 and entrada.get()[posicion_actual] == ")" and entrada.get()[posicion_actual + 1] == "(":

                entrada.icursor(posicion_actual + 2)
                contador_logaritmo += 1

            elif entrada.get()[posicion_actual+2] == "√":

                entrada.icursor(posicion_actual + 4)
                contador_raiz += 1

            elif entrada.get()[posicion_actual+1] == "%":

                entrada.icursor(posicion_actual + 3)
                contador_porcentaje += 1

            elif entrada.get()[posicion_actual+1] == "×":

                entrada.icursor(posicion_actual + 6)
                contador_cientifico += 1

            elif entrada.get()[posicion_actual+2] == "∕":

                entrada.icursor(posicion_actual + 5)
                contador_fraccion += 1

            elif entrada.get()[posicion_actual+1] == "^":

                entrada.icursor(posicion_actual + 3)
                contador_potencia += 1


            else:

                posicion_actual = entrada.index(INSERT)

                if entrada.get()[posicion_actual:posicion_actual+2] == "!(" or entrada.get()[posicion_actual:posicion_actual+2] == ")(":

                    entrada.icursor(posicion_actual + 2)

                elif entrada.get()[posicion_actual:posicion_actual+3] == "e^(" or entrada.get()[posicion_actual:posicion_actual+3] == "tg(" or entrada.get()[posicion_actual:posicion_actual+3] == "ln(" or entrada.get()[posicion_actual:posicion_actual+3] == ")%(" or  entrada.get()[posicion_actual:posicion_actual+3] == ")^(":
                    
                    entrada.icursor(posicion_actual + 3)

                elif entrada.get()[posicion_actual:posicion_actual+6] == "sin-1(" or entrada.get()[posicion_actual:posicion_actual+6] == "cos-1(" or entrada.get()[posicion_actual:posicion_actual+6] == ")×10^(" :

                    entrada.icursor(posicion_actual + 6)

                elif entrada.get()[posicion_actual:posicion_actual+4] == "sen(" or entrada.get()[posicion_actual:posicion_actual+4] == "cos(" or entrada.get()[posicion_actual:posicion_actual+4] == ")^√(" or entrada.get()[posicion_actual:posicion_actual+4] == "10^(" :

                    entrada.icursor(posicion_actual + 4)

                elif entrada.get()[posicion_actual:posicion_actual+5] == "tg-1(" or entrada.get()[posicion_actual:posicion_actual+5] == "log_(" or entrada.get()[posicion_actual:posicion_actual+5] == ") ∕ (" :
                    
                    entrada.icursor(posicion_actual + 5)

                elif contador==posicion_actual:

                    elem=ord(entrada.get()[posicion_actual+1])

                    if elem >= 48 and elem <= 57 or elem >= 42 and elem <=43 or elem == 45 or elem == 46   or elem == 118 or elem == 47  or elem == 61 or elem == 80 or elem == 113 or elem == 69 or elem == 43 or elem == 120 or elem == 121 or elem >=102 and elem <= 104  or elem == 40 or elem == 41:
                        entrada.icursor(posicion_actual + 1)

                    elif elem == 82  :
                        entrada.icursor(posicion_actual + 3)


    elif foco == entradas[0]:

        posicion_actual = entradas[0].index(INSERT)
        entradas[0].icursor(posicion_actual + 1)

    elif foco == entradas[1]:

        posicion_actual = entradas[1].index(INSERT)
        entradas[1].icursor(posicion_actual + 1)

    elif foco == entradas[2]:

        posicion_actual = entradas[2].index(INSERT)
        entradas[2].icursor(posicion_actual + 1)

    elif foco == entradas[3]:

        posicion_actual = entradas[3].index(INSERT)
        entradas[3].icursor(posicion_actual + 1)



def cursor_abajo(entrada,entrada_result):
    
    if entrada.focus_get() == entrada:
        entrada_result.focus_set()

    else:
        entrada_result.focus_set()

def cursor_arriba(entrada,entrada_result):

    if entrada_result.focus_get() == entrada_result:
        entrada.focus_set()

    else:
        entrada.focus_set()
    


def bloqueo_teclado(evento):
    return "break"



def click_boton(pestaña,entradas,entrada,valor):

    global contador_raiz,contador_porcentaje,contador_cientifico,contador_fraccion,contador_potencia,contador_logaritmo,contador_ln,contador_base_diez,contador_euler,contador_factorial,contador_sen,contador_cos,contador_tg,contador_sen1,contador_cos1,contador_tg1,contador_vads
    foco = pestaña.focus_get()

    
    if foco == entrada:

        posicion_actual = entrada.index(INSERT)
        entrada.insert(posicion_actual,valor)

        if valor == "()^√(" :

            entrada.icursor(posicion_actual+1)
            contador_raiz += 1

        elif valor == "()%(" :

            entrada.icursor(posicion_actual+1)
            contador_porcentaje += 1

        elif valor == "()×10^(" :

            entrada.icursor(posicion_actual+1)
            contador_cientifico += 1

        elif valor == "() ∕ (" :

            entrada.icursor(posicion_actual+1)
            contador_fraccion += 1

        elif valor == "()^(" :

            entrada.icursor(posicion_actual+1)
            contador_potencia += 1

        elif valor == "log_()(" :

            entrada.icursor(posicion_actual+5)
            contador_logaritmo += 1

        elif valor == "ln(" :

            contador_ln += 1

        elif valor == "10^(" :

            contador_base_diez += 1

        elif valor == "e^(" :

            contador_euler += 1

        elif valor == "!(" :

            contador_factorial += 1

        elif valor == "sen(" :
            
            contador_sen += 1

        elif valor == "cos(" :

            contador_cos += 1

        elif valor == "tg(" :

            contador_tg += 1

        elif valor == "sen-1(" :

            contador_sen1 += 1

        elif valor == "cos-1(" :

            contador_cos1 += 1

        elif valor == "tg-1(" :

            contador_tg1 += 1

        elif valor == "|" :

            contador_vads += 1
        
            
    elif foco == entradas[0] :

        valort = type(valor)

        if valort == str:

            if valor == "-" :
                posicion_actual = entradas[0].index(INSERT)
                entradas[0].insert(posicion_actual,valor)
        
        else:

            if valor >= 0 and valor <= 9 :

                posicion_actual = entradas[0].index(INSERT)
                entradas[0].insert(posicion_actual,valor)

    elif foco == entradas[1] :

        valort = type(valor)

        if valort == str:

            if valor == "-":

                posicion_actual = entradas[1].index(INSERT)
                entradas[1].insert(posicion_actual,valor)

        else:
            if valor >= 0 and valor <= 9 :

                posicion_actual = entradas[1].index(INSERT)
                entradas[1].insert(posicion_actual,valor)

    elif foco == entradas[2] :

        valort = type(valor)

        if valort == str:

            if valor == "-":
                posicion_actual = entradas[2].index(INSERT)
                entradas[2].insert(posicion_actual,valor)

        else:

            if valor >= 0 and valor <= 9 :

                posicion_actual = entradas[2].index(INSERT)
                entradas[2].insert(posicion_actual,valor)

    elif foco == entradas[3] :

        valort = type(valor)

        if valort == str:

            if valor == "-":

                posicion_actual = entradas[3].index(INSERT)
                entradas[3].insert(posicion_actual,valor)

        else:

            if valor >= 0 and valor <= 9 :

                posicion_actual = entradas[3].index(INSERT)
                entradas[3].insert(posicion_actual,valor)



def AC(pestaña,entradas,entrada,entrada_result):

    global contador_vads,contador_raiz,contador_porcentaje,contador_cientifico,contador_fraccion,contador_potencia,contador_logaritmo,contador_ln,contador_base_diez,contador_euler,contador_factorial
    contador_vads = 0
    contador_raiz = 0
    contador_porcentaje = 0
    contador_cientifico = 0
    contador_fraccion = 0
    contador_potencia = 0
    contador_logaritmo = 0
    contador_ln = 0
    contador_base_diez = 0
    contador_euler = 0
    contador_factorial = 0
    foco = pestaña.focus_get()

    if foco == entrada:

        entrada.delete(0, END)

    elif foco == entradas[0] :

        entradas[0].delete(0, END)

    elif foco == entradas[1]:
        
        entradas[1].delete(0, END)

    elif foco == entradas[2]:
        
        entradas[2].delete(0, END)

    elif foco == entradas[3]:
        
        entrada[3].delete(0, END)

    entrada_result.delete(0,"end")



def DEL(pestaña,entradas,entrada):

    foco = pestaña.focus_get()
    global movidas_izq
    texto=entrada.get()
    contador = len(texto)

    if foco == entrada:

        posicion_actual = entrada.index(INSERT)

        if contador==posicion_actual:

            posicion_actual = entrada.index(INSERT)


            if entrada.get()[posicion_actual-6:posicion_actual] == ")×10^(" :

                n_ent = entrada.get()[:posicion_actual-6] + entrada.get()[posicion_actual:]
                entrada.delete(0,"end")
                entrada.insert(0,n_ent)
                entrada.icursor(posicion_actual-6)

            elif entrada.get()[posicion_actual-2:posicion_actual] == "!(" :

                n_ent = entrada.get()[:posicion_actual-2] + entrada.get()[posicion_actual:]
                entrada.delete(0,"end")
                entrada.insert(0,n_ent)
                entrada.icursor(posicion_actual-2)

            elif entrada.get()[posicion_actual-2:posicion_actual] == ")(" :

                n_ent = entrada.get()[:posicion_actual-2] + entrada.get()[posicion_actual:]
                entrada.delete(0,"end")
                entrada.insert(0,n_ent)
                entrada.icursor(posicion_actual-2)

            elif entrada.get()[posicion_actual-3:posicion_actual] == "tg(" :

                n_ent = entrada.get()[:posicion_actual-3] + entrada.get()[posicion_actual:]
                entrada.delete(0,"end")
                entrada.insert(0,n_ent)
                entrada.icursor(posicion_actual-3)

            elif entrada.get()[posicion_actual-3:posicion_actual] == "ln(" :

                n_ent = entrada.get()[:posicion_actual-3] + entrada.get()[posicion_actual:]
                entrada.delete(0,"end")
                entrada.insert(0,n_ent)
                entrada.icursor(posicion_actual-3)

            elif entrada.get()[posicion_actual-3:posicion_actual] == ")^(" :

                n_ent = entrada.get()[:posicion_actual-3] + entrada.get()[posicion_actual:]
                entrada.delete(0,"end")
                entrada.insert(0,n_ent)
                entrada.icursor(posicion_actual-3)

            elif entrada.get()[posicion_actual-3:posicion_actual] == ")%(" :

                n_ent = entrada.get()[:posicion_actual-3] + entrada.get()[posicion_actual:]
                entrada.delete(0,"end")
                entrada.insert(0,n_ent)
                entrada.icursor(posicion_actual-3)

            elif entrada.get()[posicion_actual-3:posicion_actual] == "e^(" :

                n_ent = entrada.get()[:posicion_actual-3] + entrada.get()[posicion_actual:]
                entrada.delete(0,"end")
                entrada.insert(0,n_ent)
                entrada.icursor(posicion_actual-3)

            elif entrada.get()[posicion_actual-4:posicion_actual] == "sen(" :

                n_ent = entrada.get()[:posicion_actual-4] + entrada.get()[posicion_actual:]
                entrada.delete(0,"end")
                entrada.insert(0,n_ent)
                entrada.icursor(posicion_actual-4)

            elif entrada.get()[posicion_actual-4:posicion_actual] == "cos(" :

                n_ent = entrada.get()[:posicion_actual-4] + entrada.get()[posicion_actual:]
                entrada.delete(0,"end")
                entrada.insert(0,n_ent)
                entrada.icursor(posicion_actual-4)

            elif entrada.get()[posicion_actual-4:posicion_actual] == ")^√(" :

                n_ent = entrada.get()[:posicion_actual-4] + entrada.get()[posicion_actual:]
                entrada.delete(0,"end")
                entrada.insert(0,n_ent)
                entrada.icursor(posicion_actual-4)

            if entrada.get()[posicion_actual-4:posicion_actual] == "10^(" :

                n_ent = entrada.get()[:posicion_actual-4] + entrada.get()[posicion_actual:]
                entrada.delete(0,"end")
                entrada.insert(0,n_ent)
                entrada.icursor(posicion_actual-4)

            elif entrada.get()[posicion_actual-5:posicion_actual] == "tg-1(" :

                n_ent = entrada.get()[:posicion_actual-5] + entrada.get()[posicion_actual:]
                entrada.delete(0,"end")
                entrada.insert(0,n_ent)
                entrada.icursor(posicion_actual-5)

            elif entrada.get()[posicion_actual-5:posicion_actual] == "log_(" :

                n_ent = entrada.get()[:posicion_actual-5] + entrada.get()[posicion_actual:]
                entrada.delete(0,"end")
                entrada.insert(0,n_ent)
                entrada.icursor(posicion_actual-5)

            elif entrada.get()[posicion_actual-5:posicion_actual] == ") ∕ (" :

                n_ent = entrada.get()[:posicion_actual-5] + entrada.get()[posicion_actual:]
                entrada.delete(0,"end")
                entrada.insert(0,n_ent)
                entrada.icursor(posicion_actual-5)

            elif entrada.get()[posicion_actual-6:posicion_actual] ==  "sen-1(" :

                n_ent = entrada.get()[:posicion_actual-6] + entrada.get()[posicion_actual:]
                entrada.delete(0,"end")
                entrada.insert(0,n_ent)
                entrada.icursor(posicion_actual-6)

            elif entrada.get()[posicion_actual-6:posicion_actual] ==  "cos-1(" :

                n_ent = entrada.get()[:posicion_actual-6] + entrada.get()[posicion_actual:]
                entrada.delete(0,"end")
                entrada.insert(0,n_ent)
                entrada.icursor(posicion_actual-6)
            
            elem=ord(entrada.get()[posicion_actual-1])

            if elem >= 48 and elem <= 57 or elem >= 42 and elem <=43 or elem == 45 or elem == 46   or elem == 118 or elem == 47  or elem == 61 or elem == 80 or elem == 113 or elem == 69 or elem == 43 or elem == 120 or elem == 121 or elem >=102 and elem <= 104  or elem == 40 or elem == 41 or 215:
                
                ac_entrada=entrada.get()
                n_entrada=ac_entrada[:-1]
                entrada.delete(0,"end")
                entrada.insert(0,n_entrada)

            elif  elem == 82 :

                ac_entrada=entrada.get()
                n_entrada=ac_entrada[:-3]
                entrada.delete(0,"end")
                entrada.insert(0,n_entrada)


        else:

            posicion_actual = entrada.index(INSERT)


            if entrada.get()[posicion_actual-6:posicion_actual] == ")×10^(" :

                n_ent = entrada.get()[:posicion_actual-6] + entrada.get()[posicion_actual:]
                entrada.delete(0,"end")
                entrada.insert(0,n_ent)
                entrada.icursor(posicion_actual-6)

            elif entrada.get()[posicion_actual-2:posicion_actual] == "!(" :

                n_ent = entrada.get()[:posicion_actual-2] + entrada.get()[posicion_actual:]
                entrada.delete(0,"end")
                entrada.insert(0,n_ent)
                entrada.icursor(posicion_actual-2)

            elif entrada.get()[posicion_actual-2:posicion_actual] == ")(" :

                n_ent = entrada.get()[:posicion_actual-2] + entrada.get()[posicion_actual:]
                entrada.delete(0,"end")
                entrada.insert(0,n_ent)
                entrada.icursor(posicion_actual-2)

            elif entrada.get()[posicion_actual-3:posicion_actual] == "tg(" :

                n_ent = entrada.get()[:posicion_actual-3] + entrada.get()[posicion_actual:]
                entrada.delete(0,"end")
                entrada.insert(0,n_ent)
                entrada.icursor(posicion_actual-3)

            elif entrada.get()[posicion_actual-3:posicion_actual] == "ln(" :

                n_ent = entrada.get()[:posicion_actual-3] + entrada.get()[posicion_actual:]
                entrada.delete(0,"end")
                entrada.insert(0,n_ent)
                entrada.icursor(posicion_actual-3)

            elif entrada.get()[posicion_actual-3:posicion_actual] == ")^(" :

                n_ent = entrada.get()[:posicion_actual-3] + entrada.get()[posicion_actual:]
                entrada.delete(0,"end")
                entrada.insert(0,n_ent)
                entrada.icursor(posicion_actual-3)

            elif entrada.get()[posicion_actual-3:posicion_actual] == ")%(" :

                n_ent = entrada.get()[:posicion_actual-3] + entrada.get()[posicion_actual:]
                entrada.delete(0,"end")
                entrada.insert(0,n_ent)
                entrada.icursor(posicion_actual-3)

            elif entrada.get()[posicion_actual-3:posicion_actual] == "e^(" :

                n_ent = entrada.get()[:posicion_actual-3] + entrada.get()[posicion_actual:]
                entrada.delete(0,"end")
                entrada.insert(0,n_ent)
                entrada.icursor(posicion_actual-3)

            elif entrada.get()[posicion_actual-4:posicion_actual] == "sen(" :

                n_ent = entrada.get()[:posicion_actual-4] + entrada.get()[posicion_actual:]
                entrada.delete(0,"end")
                entrada.insert(0,n_ent)
                entrada.icursor(posicion_actual-4)

            elif entrada.get()[posicion_actual-4:posicion_actual] == "cos(" :

                n_ent = entrada.get()[:posicion_actual-4] + entrada.get()[posicion_actual:]
                entrada.delete(0,"end")
                entrada.insert(0,n_ent)
                entrada.icursor(posicion_actual-4)

            elif entrada.get()[posicion_actual-4:posicion_actual] == ")^√(" :

                n_ent = entrada.get()[:posicion_actual-4] + entrada.get()[posicion_actual:]
                entrada.delete(0,"end")
                entrada.insert(0,n_ent)
                entrada.icursor(posicion_actual-4)

            if entrada.get()[posicion_actual-4:posicion_actual] == "10^(" :

                n_ent = entrada.get()[:posicion_actual-4] + entrada.get()[posicion_actual:]
                entrada.delete(0,"end")
                entrada.insert(0,n_ent)
                entrada.icursor(posicion_actual-4)

            elif entrada.get()[posicion_actual-5:posicion_actual] == "tg-1(" :

                n_ent = entrada.get()[:posicion_actual-5] + entrada.get()[posicion_actual:]
                entrada.delete(0,"end")
                entrada.insert(0,n_ent)
                entrada.icursor(posicion_actual-5)

            elif entrada.get()[posicion_actual-5:posicion_actual] == "log_(" :

                n_ent = entrada.get()[:posicion_actual-5] + entrada.get()[posicion_actual:]
                entrada.delete(0,"end")
                entrada.insert(0,n_ent)
                entrada.icursor(posicion_actual-5)

            elif entrada.get()[posicion_actual-5:posicion_actual] == ") ∕ (" :

                n_ent = entrada.get()[:posicion_actual-5] + entrada.get()[posicion_actual:]
                entrada.delete(0,"end")
                entrada.insert(0,n_ent)
                entrada.icursor(posicion_actual-5)

            elif entrada.get()[posicion_actual-6:posicion_actual] ==  "sen-1(" :

                n_ent = entrada.get()[:posicion_actual-6] + entrada.get()[posicion_actual:]
                entrada.delete(0,"end")
                entrada.insert(0,n_ent)
                entrada.icursor(posicion_actual-6)

            elif entrada.get()[posicion_actual-6:posicion_actual] ==  "cos-1(" :

                n_ent = entrada.get()[:posicion_actual-6] + entrada.get()[posicion_actual:]
                entrada.delete(0,"end")
                entrada.insert(0,n_ent)
                entrada.icursor(posicion_actual-6)

            elem=ord(entrada.get()[posicion_actual-1])

            if elem >= 48 and elem <= 57 or elem >= 42 and elem <=43 or elem == 45 or elem == 46   or elem == 118 or elem == 47  or elem == 61 or elem == 80 or elem == 113 or elem == 69 or elem == 43 or elem == 120 or elem == 121 or elem >=102 and elem <= 104  or elem == 40 or elem == 41:
                
                posicion_actual -= 1
                ac_entrada=entrada.get()
                n_entrada=ac_entrada[:posicion_actual] + ac_entrada[posicion_actual + 1:]
                entrada.delete(0,"end")
                entrada.insert(0,n_entrada)
                entrada.icursor( posicion_actual)

            elif  elem == 82 :

                posicion_actual -= 3
                ac_entrada=entrada.get()
                n_entrada=ac_entrada[:posicion_actual] + ac_entrada[posicion_actual + 3:]
                entrada.delete(0,"end")
                entrada.insert(0,n_entrada)
                entrada.icursor( posicion_actual)


    elif foco == entradas[0]:

        posicion_actual = entradas[0].index(INSERT)
        entradas[0].delete(posicion_actual-1, posicion_actual )

    elif foco == entradas[1]:

        posicion_actual = entradas[1].index(INSERT)
        entradas[1].delete(posicion_actual-1, posicion_actual )

    elif foco == entradas[2]:

        posicion_actual = entradas[2].index(INSERT)
        entradas[2].delete(posicion_actual-1, posicion_actual )

    elif foco == entradas[3]:

        posicion_actual = entradas[3].index(INSERT)
        entradas[3].delete(posicion_actual-1, posicion_actual )



def boton_presionado(boton):
    global ultimo_boton
    ultimo_boton = boton
        


def traduccion (entrada,entrada_result,pestaña,entrada_x1,entrada_x2,entrada_y1,entrada_y2):

    ecuacion = entrada.get()
    l_ecuacion = len(ecuacion)
    ecua = [ ]
    i  = 0

    while i < l_ecuacion:

        if ecuacion[i] == "×" and ecuacion[i+1] == "1" and ecuacion[i+2] == "0" and ecuacion[i+3] == "^" :
            ecua.append("j")
            i += 4

        elif ecuacion[i] == "s" and ecuacion[i+1] == "e" and ecuacion[i+2] == "n" and ecuacion[i+3] == "-" and ecuacion[i+4] == "1":
            ecua.append("s")
            i +=5

        elif ecuacion[i] == "c" and ecuacion[i+1] == "o" and ecuacion[i+2] == "s" and ecuacion[i+3] == "-" and ecuacion[i+4] == "1":
            ecua.append("u")
            i +=5

        elif ecuacion[i] == "t" and ecuacion[i+1] == "g" and ecuacion[i+2] == "-" and ecuacion[i+3] == "1" :
            ecua.append("t")
            i +=4

        elif ecuacion[i] == "s" and ecuacion[i+1] == "e" and ecuacion[i+2] == "n" :
            ecua.append("S")
            i +=3

        elif ecuacion[i] == "c" and ecuacion[i+1] == "o" and ecuacion[i+2] == "s" :
            ecua.append("C")
            i +=3

        elif ecuacion[i] == "t" and ecuacion[i+1] == "g" :
            ecua.append("T")
            i +=2

        elif ecuacion[i] == "l" and ecuacion[i+1] == "o" :
            ecua.append("L")
            i +=3

        elif ecuacion[i] == "l" and ecuacion[i+1] == "n" :
            ecua.append("l")
            i +=2

        elif ecuacion[i] == "^" and ecuacion[i+1] == "√" :
            ecua.append("r")
            i +=2

        elif ecuacion[i] == "e" and l_ecuacion-i > 1 and ecuacion[i+1] == "^" :
            ecua.append("e")
            i +=2

        elif ecuacion[i] == "e" :
            ecua.append("E")
            i +=1

        elif ecuacion[i] == "^" :
            ecua.append("p")
            i +=1

        elif ecuacion[i] == "∕" :
            ecua.append("F")
            i +=1

        elif ecuacion[i] == " " :
            i +=1

        elif ecuacion[i] == "%" :
            ecua.append("o")
            i +=1

        elif ecuacion[i] == "1" and ecuacion[i+1] == "0" and ecuacion[i+2] == "^":
            ecua.append("B")
            i +=3

        elif ecuacion[i] == "!" :
            ecua.append("w")
            i +=1

        elif ecuacion[i] == "ℼ" :
            ecua.append("P")
            i +=1

        else:
            ecua.append(ecuacion[i])
            i += 1

    operacion_principal(entrada,entrada_result,ecua,pestaña,entrada_x1,entrada_x2,entrada_y1,entrada_y2)



def opciones ():
    global contador

    contador += 1

    return f"Opcion_{contador:04d}"