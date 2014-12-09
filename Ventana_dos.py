from tkinter import *

def imprime():
	print("Acbas de presionarl el boton Imprimir")

ventana = Tk()
ventana.title("Segunda Centana")
botonS = Button(ventana, text="Salir", fg="red" ,command=ventana.quit)
botonS.pack(side=LEFT)
botonI = Button(ventana, text="Imprimir", fg="#0000ff",command=imprime)
botonI.pack(side=RIGHT)
ventana.mainloop()