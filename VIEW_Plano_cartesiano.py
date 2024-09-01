from matplotlib.backends.backend_tkagg import *
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np

line = []


def plot_graph(fig,ax,frame,x,y,entrada,frame_funciones,color_select,hay_tn=0):
    
    global line

    glo = globals()
    grid = glo.get("activar_gird")

    if hay_tn > 0:

        if y != 0:

            for i in range(len(y)):
                if abs(y[i]) >= 8:
                    y[i] = float('nan')

    else:
        if y != 0:

            for i in range(len(y)):
                if abs(y[i]) >= 50:
                    y[i] = float('nan')

    if color_select == "":

        linea = ax.plot(x, y, linestyle='-')
        color_l = linea[0].get_color()

    else:

        linea = ax.plot(x, y, linestyle='-',color=color_select)
        color_l = linea[0].get_color()

    if type(entrada) == str:
        funcion = (entrada,linea,color_l)

    else:
        funcion = (entrada.get(),linea,color_l)

    line.append(funcion)
    ax.set_title('Plano Cartesiano')
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    if grid == True or grid == None:
        ax.grid(True)
    

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.place(relx=0, rely= 0, relwidth=1, relheight=0.9)
    toolbar = NavigationToolbar2Tk(canvas, frame)
    toolbar.update()
    toolbar.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)

    if type(entrada) != str:
        entrada.focus_set()