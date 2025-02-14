from tkinter import *
import tkinter.font as font
root = Tk()
root.geometry("500x500")
root.title("Alachbebsi weather Magic")

Alachbebsi=Label(root,text="Alachbebsi",bg="green",font=font.Font(size=20),fg="Purple")
CandF=Label(root,text="Celsius 👉🏾 Fahrenheit",bg="green",fg="Purple")
CandF.grid(row=0,column=2)
Alachbebsi.grid(row=1,column=2)     
Alachbutton=Button(root,bg="green",text="Use Alachbebsi magic!")
Alachbutton.grid(row=4,column=2)

root.mainloop()





