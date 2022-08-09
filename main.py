from cProfile import label
from logging import root
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from tkinter import messagebox
from turtle import hideturtle
from PIL import Image,ImageTk
import os
from stegano import lsb

root=Tk()
root.title("Cipher Herold")
root.geometry("700x500+150+180")
root.resizable(False,False)
root.config(bg="#933dbc")

#===========functions==================
def showimg():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select Image File",filetypes=(("PNG file","*.png"),("JPG file","*.jpg"),("All files","*.txt")))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=250,height=250)
    lbl.image=img
    
def hide():
    global secret
    message=txt1.get(1.0,END)
    secret = lsb.hide(str(filename),message)
    messagebox.askyesno("Encrypt","Are you sure?")
    
def show():
    clear_message=lsb.reveal(filename)
    txt1.delete(1.0,END)
    txt1.insert(END,clear_message)
    messagebox.askyesno("Decrypt","Are you sure?")
    
def save():
    secret.save("hidden.png")
    messagebox.showinfo("Saved","Saved Successfully!")            

#====================Icon====================

image_icon=PhotoImage(file="pos.png")
root.iconphoto(False,image_icon)

#===================Logo=======================

logo=PhotoImage(file="icon.png")
Label(root,image=logo,bg="#933dbc").place(x=20,y=20)
Label(root,text="Img Encypt & Decpt",bg="#933dbc",fg="white",font="Helvetica 25 bold").place(x=100,y=20)

#================First frame==========================

f1=Frame(root,bd=3,bg="black",width=340,height=240,relief=SUNKEN)
f1.place(x=15,y=100)
lbl=Label(f1,bg="black")
lbl.place(x=40,y=20)

#=================Second frame======================

f2=Frame(root,bd=3,bg="white",width=340,height=240,relief=SUNKEN)
f2.place(x=350,y=100)
txt1=Text(f2,font="Akzidenz-Grotesk 18 ",bg="white",fg="black",relief=SUNKEN,wrap=WORD)
txt1.place(x=0,y=0,width=320,height=295)

scr1=Scrollbar(f2)
scr1.place(x=320,y=0,height=300)
scr1.configure(command=txt1.yview)
txt1.configure(yscrollcommand=scr1.set)

#=================Third frame======================

f3=Frame(root,bd=3,bg="#933dbc",width=330,height=110,relief=GROOVE)
f3.place(x=15,y=360)
Button(f3,text="Open Image",width=10,height=2,command=showimg,font="Helvetica 14 bold").place(x=20,y=30)
Button(f3,text="Save Image",width=10,height=2,command=save,font="Helvetica 14 bold").place(x=180,y=30)
Label(f3,text="Pic,Img,Photo File..",bg="#933dbc",fg="white").place(x=20,y=5)

#=================Fourth frame======================


f4=Frame(root,bd=3,bg="#933dbc",width=330,height=110,relief=GROOVE)
f4.place(x=360,y=360)
Button(f4,text="Hide Data",width=10,height=2,command=hide,font="Helvetica 14 bold").place(x=20,y=30)
Button(f4,text="Show Data",width=10,height=2,command=show,font="Helvetica 14 bold").place(x=180,y=30)
Label(f4,text="Options available..",bg="#933dbc",fg="white").place(x=20,y=5)



root.mainloop()
