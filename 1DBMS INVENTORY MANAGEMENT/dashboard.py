from tkinter import*
from PIL import Image,ImageTk
from employee import Employeeclass
class IMS:
    def __init__(self, root):
        self.root =root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.icon_title=PhotoImage(file="images/logo1.gif")
        title=Label(self.root, text="Inventory Management System",image=self.icon_title,compound=LEFT, font=("times new roman",40,"bold"),bg="black",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
        btnlogout=Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1100,y=10,height=50,width=150)
        self.menulogo=Image.open("images/menu.png")
        self.menulogo=self.menulogo.resize((200,200),Image.LANCZOS)
        self.menulogo=ImageTk.PhotoImage(self.menulogo)
        Leftmenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Leftmenu.place(x=0,y=102,width=200,height=565)
        lblmenulogo=Label(Leftmenu,image=self.menulogo)
        lblmenulogo.pack(side=TOP,fill=X) 

        lmenu=Label(Leftmenu,text="Menu",font=("times new roman",20),bg="#009688").pack(side=TOP,fill=X)
        menuemp=Button(Leftmenu,text="Employee",command=self.employee,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        menusupplier=Button(Leftmenu,text="Supplier",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        menucategory=Button(Leftmenu,text="Category",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        menuproduct=Button(Leftmenu,text="Product",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        menusales=Button(Leftmenu,text="Sales",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        menuexit=Button(Leftmenu,text="Exit",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
         
        self.lblemployee=Label(self.root,text="Total Employee\n[ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("times new roman",20,"bold"))
        self.lblemployee.place(x=300,y=120,height=150,width=300)

        self.lblsupplier=Label(self.root,text="Total Supplier\n[ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("times new roman",20,"bold"))
        self.lblsupplier.place(x=650,y=120,height=150,width=300)

        self.lblcategory=Label(self.root,text="Total Category\n[ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("times new roman",20,"bold"))
        self.lblcategory.place(x=1000,y=120,height=150,width=300)

        self.lblproduct=Label(self.root,text="Total Product\n[ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("times new roman",20,"bold"))
        self.lblproduct.place(x=300,y=300,height=150,width=300)

        self.lblsales=Label(self.root,text="Total Sales\n[ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("times new roman",20,"bold"))
        self.lblsales.place(x=650,y=300,height=150,width=300)

    def employee(self):
        self.new_win=Toplevel(self.root)    
        self.new_obj=Employeeclass(self.new_win)
if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop() 
