from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title("Banderas de países")
root.geometry("600x400")
root.configure(background="lightblue")

imagen1=ImageTk.PhotoImage(Image.open("India.jpg"))
imagen2=ImageTk.PhotoImage(Image.open("Australia.png"))
imagen3=ImageTk.PhotoImage(Image.open("America.jpg"))
imagen4=ImageTk.PhotoImage(Image.open("Japon.jpg"))
imagen5=ImageTk.PhotoImage(Image.open("Filipinas.png"))


b={"India":imagen1,
   "Australia":imagen2,
   "America":imagen3,
   "Japon":imagen4,
   "Filipinas":imagen5}


def mostras():
    
    try:
        c=input_1.get()
        print(c)
        label_1["image"]=b[c]
    except:messagebox.showinfo("No se encuentra esta bandera")
 

input_1=Entry(root)
input_1.place(relx=0.5 , rely=0.5 , anchor=CENTER)
button_1=Button(root,text="Dame click para mostrar la bandera", command=mostras)
button_1.place(relx=0.5 , rely=0.6 , anchor=CENTER)
label_1=Label(root,text="a")
label_1.place(relx=0.5 , rely=0.9 , anchor=CENTER)
root.mainloop()