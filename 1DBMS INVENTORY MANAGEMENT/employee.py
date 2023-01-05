from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
class Employeeclass:
    def __init__(self, root):
        self.root =root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()

        searchframe=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        searchframe.place(x=250,y=20,width=600,height=70)

        cmb_search=ttk.Combobox(searchframe,values=("select","email","name","contact"),state='readonly',justify=CENTER,font=("times new roman",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(searchframe,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        searchbutton=Button(searchframe,text="Search",font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=440,y=9,width=150,height=30)

if __name__=="__main__":
    root=Tk()
    obj=Employeeclass(root)
    root.mainloop()         