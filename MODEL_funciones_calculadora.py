from tkinter import *
from MODEL_funciones_operaciones import *

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
        

def traduccion (fig,ax,entrada,entrada_result,frame,frame_funciones,color_select):

    

    if type(entrada) == str:
        ecuacion = entrada

    else:
        ecuacion = entrada.get()

    can_par = ecuacion.count("(")
    con_par_c = ecuacion.count(")")

    if can_par == con_par_c or ecuacion != "":

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

            elif ecuacion[i] == "÷" :
                ecua.append("/")
                i += 1

            else:
                ecua.append(ecuacion[i])
                i += 1

        si = operacion_principal(fig,ax,entrada,entrada_result,ecua,frame,frame_funciones,color_select)
        return si
    
    else:
        entrada_result.delete(0,"end")
        entrada_result.insert(0,"Syntax Error")


def opciones ():
    global contador

    contador += 1

    return f"Opcion_{contador:04d}"