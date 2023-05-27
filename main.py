from tkinter import *
from PIL import ImageTk
import ttkthemes
from tkinter import ttk,messagebox


window=Tk()

def adminis():
    def login():
        if adminnameEntry.get()=='' or adminpswrdEntry.get()=='':
            messagebox.showerror('Error','Fields cannot be empty')
        elif adminnameEntry.get()=='Admin' and adminpswrdEntry.get()=='admin':
            messagebox.showinfo('Success','Welcome')
            window.destroy()
            import admin
        else:
            messagebox.showerror('Error','Enter valid details')


    admin=Toplevel()
    admin.grab_set()
    admin.title('Admin Login')
    admin.geometry('380x140+630+230')


    adminnameLabel=Label(admin,text='Username',font=('times new roman',20,'bold'))
    adminnameLabel.grid(row=0,column=0,padx=10)
    adminnameEntry=Entry(admin,font=('times new roman',15))
    adminnameEntry.grid(row=0,column=1,pady=10,padx=10)

    adminpswrdLabel=Label(admin,text='password',font=('times new roman',20,'bold'))
    adminpswrdLabel.grid(row=1,column=0,padx=10)
    adminpswrdEntry=Entry(admin,font=('times new roman',15))
    adminpswrdEntry.grid(row=1,column=1,pady=10,padx=10)

    loginButton=ttk.Button(admin,text='login',cursor='hand2',command=login)
    loginButton.grid(row=2,columnspan=2)

def user():
    import user

window.geometry('1530x980+200+0')
window.resizable(False,False)
window.title('Agri shop for Farmers')

bg = ImageTk.PhotoImage(file='image.jpg')
bgLabel = Label(window,image=bg)
bgLabel.place(x=0,y=0)

loginframe = Frame(window,bg='navajo white')
loginframe.place(x=500,y=350)

logoimg = PhotoImage(file='admin.png')
logoLabel = Label(loginframe,image=logoimg)
logoLabel.grid(row=0,column=0)

loginframe1 = Frame(window,bg='navajo white')
loginframe1.place(x=900,y=350)

logoimg1 = PhotoImage(file='woman.png')
logoLabel1 = Label(loginframe1,image=logoimg1)
logoLabel1.grid(row=0,column=0)

adminButton = Button(loginframe,text='Admin',compound=CENTER,font=('times new roman',20,'bold'),cursor='hand2',command=adminis)
adminButton.grid(row=1,column=0,pady=10)

userButton = Button(loginframe1,text='User',compound=CENTER,font=('times new roman',20,'bold'),cursor='hand2',command=user)
userButton.grid(row=1,column=0,pady=10)


window.mainloop()

