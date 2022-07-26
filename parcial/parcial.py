from tkinter import *

# RESPUESTA DE HOLA, NOMBRE, CEDULA, UBICACIÓN 
def consultar():  
    lblsaludar=Label(ventana,text="X1= " + entradaX1.get()
                     + " \n "
                     + entradaCedula.get() + "\nUbicado en: " + entradaubicacion.get(),font=("Arial Black",10),bg="grey68").place(x=50,y=350)


     
#DIMENSIONES DE LA VENTANA
ventana=Tk()
ventana.geometry("600x600+0+0") 

# TITULO  
ventana.title(" parcial #2 ")

# VARIABLES 
lblCedula=Label(text="X1=",font=("Arial",14)).place(x=40,y=400)
entradaCedula=StringVar()
txtCedula=Entry(ventana,textvariable=entradaCedula).place(x=55,y=10)

lblX1=Label(text="Y1=",font=("Arial",14)).place(x=10,y=40)
entradaX1=StringVar()
txtX1=Entry(ventana,textvariable=entradaX1).place(x=115,y=50)

lblAlquiler=Label(text="X2=",font=("Arial",14)).place(x=10,y=100)
entradaAlquiler=IntVar()
txtAlquiler=Entry(ventana,textvariable=entradaAlquiler).place(x=480,y=110)

lblUbicacion=Label(text="Y2=",font=("Arial",14)).place(x=10,y=70)
entradaubicacion=StringVar()
txtUbicacion=Entry(ventana,textvariable=entradaubicacion).place(x=130,y=75)



# BOTON CONSULTAR 
btnSaludar=Button(ventana,text="Graficar",command=consultar,font=("Arial",15)).place(x=95,y=270)
btnSaludar=Button(ventana,text="pendiente",command=consultar,font=("Arial",15)).place(x=95,y=270)

# FIN DEL PROGRAMA 
ventana.mainloop()