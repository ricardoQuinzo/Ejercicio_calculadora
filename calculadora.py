from tkinter import *
import math

def clic(numer):
    global operador
    operador = operador + str(numer)
    num.set(operador)

def igual():
    global operador
    oper = str(eval(operador))
    num.set(oper)
    operador = ""
    
def sen():
    global operador
    oper = int(eval(operador))
    num.set(math.sin(oper))
    operador = ""

def cos():
    global operador
    oper = int(eval(operador))
    num.set(math.cos(oper))
    operador = " "

def tan():
    global operador
    oper = int(eval(operador))
    num.set(math.tan(oper))
    operador = ""

    
ventana = Tk()
frame = Frame(ventana)
ventana.title("CALCULADORA")
ventana.geometry("300x300")
operador = ""
num = StringVar()

##pantalla-----------------------------------------------------------------------------------
display = Entry(ventana, textvariable = num, bd = 20, insertwidth  = 4,
                bg = "white", justify = "right").grid(columnspan = 4)
##-------------------------------------------------------------------------------------------

btn1 = Button(ventana, padx = 15, bd = 5, text = "1",fg = "black", command = lambda: clic(1)).grid(row = 1, column = 0)
btn2 = Button(ventana, padx = 15, bd = 5, text = "2", fg = "black", command = lambda: clic(2)).grid(row = 1, column = 1)
btn3 = Button(ventana, padx = 15, bd = 5, text = "3", fg = "black", command = lambda: clic(3)).grid(row = 1, column = 2)
btn4 = Button(ventana, padx = 15, bd = 5, text = "4", fg = "black", command = lambda: clic(4)).grid(row = 1, column = 3)

btn5 = Button(ventana, padx = 15, bd = 5, text = "5", fg = "black", command = lambda: clic(5)).grid(row = 2, column = 0)
btn6 = Button(ventana, padx = 15, bd = 5, text = "6", fg = "black", command = lambda: clic(6)).grid(row = 2, column = 1)
btn7 = Button(ventana, padx = 15, bd = 5, text = "7", fg = "black", command = lambda: clic(7)).grid(row = 2, column = 2)
btn8 = Button(ventana, padx = 15, bd = 5, text = "8", fg = "black", command = lambda: clic(8)).grid(row = 2, column = 3)

btn9 = Button(ventana, padx = 15, bd = 5, text = "9", fg = "black", command = lambda: clic(9)).grid(row = 3, column = 1)
btn0 = Button(ventana, padx = 15, bd = 5, text = "0", fg = "black", command = lambda: clic(0)).grid(row = 3, column = 2)
##funciones trigonometricas-------------------------------------------------------------------
btnsen = Button(ventana, padx = 10, bd = 5, text = "sen", fg = "black", command = sen).grid(row = 4, column = 0)
btncos = Button(ventana, padx = 10, bd = 5, text = "cos", fg = "black", command = cos).grid(row = 4, column = 1)
btntag = Button(ventana, padx = 10, bd = 5, text = "tan", fg = "black", command = tan).grid(row = 4, column = 2)
btneq = Button(ventana, padx = 10, bd = 5, text = " = ", fg = "black", command = igual).grid(row = 4, column = 3)

btnadd = Button(ventana, padx = 15, bd = 5, text = "+", fg = "black", command = lambda: clic("+")).grid(row = 5, column = 0)
btnsubs = Button(ventana, padx = 15, bd = 5, text = "-", fg = "black", command = lambda: clic("-")).grid(row = 5, column = 1)
btnmul = Button(ventana, padx = 15, bd = 5, text = "*", fg = "black", command = lambda: clic("*")).grid(row = 5, column = 2)
btndiv = Button(ventana, padx = 15, bd = 5, text = "/", fg = "black", command = lambda: clic("/")).grid(row = 5, column = 3)

##funcionamiento-----------------------------------------------------------------------------------


ventana.mainloop()
