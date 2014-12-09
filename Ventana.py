#Python
from tkinter import *
import time 

def parpadear():
	ventana.iconify()
	time.sleep(3)
	ventana.deiconify()


ventana = Tk()
ventana.title("Primera ventana en Tkinter")
boton=Button(ventana,text="Evento", command=parpadear)
boton.pack()
ventana.mainloop()