from tkinter import *
from calendar import *


def showcal():
    #global calendarentry
    root2 = Tk()
    root2.geometry("300x300")
    root2.title("Alachbebsi Calendar") 
    
    fetch_year=int(calendarentry.get())
    cal_content=calendar.calendar(fetch_year)
    year_label=Label(root2, text=cal_content)
    year_label.grid(row=5,column=1)
    root2.mainloop()




if __name__=="__main__":
    
    root = Tk()
    root.geometry("300x300")
    root.title("Alachbebsi setup")
    Label(root, text="Alachbebsi.nl", bg="teal").pack()
    Label(root, text="Enter Year", bg="Red").pack()

    calendarentry = Entry(root, width=30)
   
  
    btnenteryear = Button(root, text="Entry", command=showcal)
    exitbtn = Button(root, text="Exit", command=root.destroy)
    calendarentry.pack()
    btnenteryear.pack()
    exitbtn.pack()


    root.mainloop()
