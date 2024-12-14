from tkinter import Tk , Label, Canvas, messagebox  
from PIL import Image, ImageTk
from time import strftime 
flag1, flag2, flag3, flag4 = False, False, False, False

def actualizarHora():
    labelHora.config(text= "Hora: "+ strftime("%H:%M:%S") 
    + " Fecha: " + strftime("%d/%m/%Y"))
    labelHora.after(1000, actualizarHora)

def apagarEncender(event, foco = None):
    global foco1, foco2, foco3, foco4, flag1, flag2, flag3, flag4
    if foco == Canvas1: 
        if flag1 == False:
            foco1 = ImageTk.PhotoImage(Image.open("img/focoOn.png").resize((32,32)))
            canva.itemconfig(Canvas1, image=foco1)
            flag1 = True
        else: 
            foco1 = ImageTk.PhotoImage(focoOff1)
            canva.itemconfig(Canvas1, image=foco1)
            flag1 = False
    elif foco == Canvas2:
        if flag2 == False:
            foco2 = ImageTk.PhotoImage(Image.open("img/focoOn.png").resize((32,32)))
            canva.itemconfig(Canvas2, image=foco2)
            flag2 = True
        else: 
            foco2 = ImageTk.PhotoImage(focoOff2)
            canva.itemconfig(Canvas2, image=foco2)
            flag2 = False
    elif foco == Canvas3:
        if flag3 == False:
            foco3 = ImageTk.PhotoImage(Image.open("img/focoOn.png").resize((32,32)))
            canva.itemconfig(Canvas3, image=foco3)
            flag3 = True
        else: 
            foco3 = ImageTk.PhotoImage(focoOff3)
            canva.itemconfig(Canvas3, image=foco3)
            flag3 = False
    elif foco == Canvas4:
        if flag4 == False:
            foco4 = ImageTk.PhotoImage(Image.open("img/focoOn.png").resize((32,32)))
            canva.itemconfig(Canvas4, image=foco4)
            flag4 = True
        else: 
            foco4 = ImageTk.PhotoImage(focoOff4)
            canva.itemconfig(Canvas4, image=foco4)
            flag4 = False

ventana = Tk()
ventana.geometry("800x600")
ventana.title("GUI Activacion de LEDs")
ventana.iconbitmap("img/led.ico")
titulo = Label(ventana, text="Activacion de LEDs", font=("Arial", 20, "bold"))
titulo.pack()
try:
    imagen = Image.open("img/house1.png")
    fondo = ImageTk.PhotoImage(imagen)
    focoOff1 = Image.open("img/focoOff.png").resize((32,32))
    focoOff2 = Image.open("img/focoOff.png").resize((32,32))
    focoOff3 = Image.open("img/focoOff.png").resize((32,32))
    focoOff4 = Image.open("img/focoOff.png").resize((32,32))
    foco1 = ImageTk.PhotoImage(focoOff1)
    foco2 = ImageTk.PhotoImage(focoOff2)
    foco3 = ImageTk.PhotoImage(focoOff3)
    foco4 = ImageTk.PhotoImage(focoOff4)

except:
    print("Error al cargar la imagen")
    exit()

canva = Canvas(ventana, width=700, height=500)
canva.pack()
canva.create_image(0,0, anchor="nw", image=fondo)
Canvas1 = canva.create_image(120,150, anchor="nw", image=foco1)
canva.tag_bind(Canvas1, "<Button-1>", lambda event: apagarEncender(event, Canvas1))
Canvas2 = canva.create_image(500,100, anchor="nw", image=foco2)
canva.tag_bind(Canvas2, "<Button-1>", lambda event: apagarEncender(event, Canvas2))
Canvas3 = canva.create_image(350,350, anchor="nw", image=foco3)
canva.tag_bind(Canvas3, "<Button-1>", lambda event: apagarEncender(event, Canvas3))
Canvas4 = canva.create_image(550,350, anchor="nw", image=foco4)
canva.tag_bind(Canvas4, "<Button-1>", lambda event: apagarEncender(event, Canvas4))

labelHora = Label(ventana, text="Hora y Fecha ", font=("Arial", 12))
labelHora.place(x=10, y=560)
labelNombre = Label(ventana, text="by Alan Ortiz", font=("Arial", 12))
labelNombre.place(x=630, y=560) 
#La siguiente linea siempre va al final
actualizarHora()
ventana.mainloop()

