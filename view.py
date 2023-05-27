from tkinter import *
import pymongo
from tkinter import ttk,messagebox
import ttkthemes
import sys

try:
    client = pymongo.MongoClient("mongodb+srv://Bhavya:Ammulu1906@cluster0.7zd38m0.mongodb.net/?retryWrites=true&w=majority")
    db = client.SoilFarmingAgent
except:
    print("Database connection Error ")
    print("No connection could be made because the target machine actively refused it ")
    messagebox.showerror("Error", "Connection Error")
    sys.exit(1)

def iexit():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass

def viewsand(root,db):
    view=Toplevel()
    view.geometry('1050x480+200+200')
    view.title('Sand Details')
    typeofsoillabel=Label(view,text='Type_of_Soil')
    typeofsoillabel.grid(row=0,column=0,pady=10,padx=10)
    cropsgrownlabel=Label(view,text='Crops_grown')
    cropsgrownlabel.grid(row=0,column=2,pady=10,padx=10)
    nutrientlabel=Label(view,text='Nutrient_content')
    nutrientlabel.grid(row=0,column=4,pady=10,padx=10)
    dryingoutlabel=Label(view,text='Drying_out')
    dryingoutlabel.grid(row=0,column=6,pady=10,padx=10)
    waterretentionlabel=Label(view,text='Water_retention')
    waterretentionlabel.grid(row=0,column=8,pady=10,padx=10)
    difftogrowlabel=Label(view,text='Difficult_to_grow')
    difftogrowlabel.grid(row=0,column=10,pady=10,padx=10)
    i=1
    for x in db.details.find():
        y=len(x)
        print(x)
        typeofsoillabel = Label(view, text=x['Type_of_Soil'])
        typeofsoillabel.grid(row=i, column=0, pady=10, padx=10)
        cropsgrownlabel = Label(view, text=x['Crops_grown'])
        cropsgrownlabel.grid(row=i, column=2, pady=10, padx=10)
        nutrientlabel = Label(view, text=x['Nutrient_Content'])
        nutrientlabel.grid(row=i, column=4, pady=10, padx=10)
        dryingoutlabel = Label(view, text=x['Drying_out'])
        dryingoutlabel.grid(row=i, column=6, pady=10, padx=10)
        waterretentionlabel = Label(view, text=x['Water_retention'])
        waterretentionlabel.grid(row=i, column=8, pady=10, padx=10)
        difftogrowlabel = Label(view, text=x['Difficult_to_grow'])
        difftogrowlabel.grid(row=i, column=10, pady=10, padx=10)
        i += 1

def viewdist(root,db):
    new = Toplevel()
    new.geometry('630x680+200+200')
    new.title('Distributor Details')
    namelabel=Label(new,text='Name')
    namelabel.grid(row=0,column=0,pady=10,padx=10)
    emaillabel=Label(new,text='Email')
    emaillabel.grid(row=0,column=2,pady=10,padx=10)
    phonelabel=Label(new,text='Contact')
    phonelabel.grid(row=0,column=4,pady=10,padx=10)
    genderlabel=Label(new,text='Gender')
    genderlabel.grid(row=0,column=6,pady=10,padx=10)
    placelabel=Label(new,text='Place')
    placelabel.grid(row=0,column=8,pady=10,padx=10)
    l = 1
    for j in db.details1.find():
        k = len(j)
        print(j)
        namelabel = Label(new, text=j['Name'])
        namelabel.grid(row=l, column=0, pady=10, padx=10)
        emaillabel = Label(new, text=j['Email'])
        emaillabel.grid(row=l, column=2, pady=10, padx=10)
        phonelabel = Label(new, text=j['Contact'])
        phonelabel.grid(row=l, column=4, pady=10, padx=10)
        genderlabel = Label(new, text=j['Gender'])
        genderlabel.grid(row=l, column=6, pady=10, padx=10)
        placelabel = Label(new, text=j['Place'])
        placelabel.grid(row=l, column=8, pady=10, padx=10)
        l += 1


root=ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')

root.geometry('300x200+450+300')
root.resizable(0,0)
root.title('User window')


viewButton=ttk.Button(root,text='View Sand Details',width=25,command=lambda: viewsand(root,db))
viewButton.grid(row=2,column=0,pady=15,padx=20)

viewdsButton=ttk.Button(root,text='View Distributor Details',width=25,command=lambda: viewdist(root,db))
viewdsButton.grid(row=3,column=0,pady=15,padx=20)

exitButton=ttk.Button(root,text='Exit',width=25,command=iexit)
exitButton.grid(row=4,column=0,pady=15,padx=20)


root.mainloop()
