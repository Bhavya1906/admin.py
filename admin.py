from tkinter import *
import pymongo
from tkinter import ttk, messagebox
import ttkthemes
import sys
from random import randint

try:
    client = pymongo.MongoClient(
        "mongodb+srv://Bhavya:Ammulu1906@cluster0.7zd38m0.mongodb.net/?retryWrites=true&w=majority")
    db = client.SoilFarmingAgent
except:
    print("Database connection Error ")
    print("No connection could be made because the target machine actively refused it ")
    messagebox.showerror("Error", "Connection Error")
    sys.exit(1)


def iexit():
    result = messagebox.askyesno('Confirm', 'Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass


def soil_det(root, db):
    def post_data():
        global root
        ToS = typeofsoilEntry.get()
        CRE = cropsgrownEntry.get()
        DTG = difftogrowEntry.get()
        NE = nutrientEntry.get()
        DOE = dryingoutEntry.get()
        WRE = waterretentionEntry.get()
        Type_of_Soil = [ToS]
        Crops_grown = [CRE]
        Difficult_to_grow = [DTG]
        Nutrient_Content = [NE]
        Drying_out = [DOE]
        Water_retention = [WRE]
        SoilFarmingAgent = {
            'Type_of_Soil': Type_of_Soil[randint(0, (len(Type_of_Soil) - 1))],
            'Crops_grown': Crops_grown[randint(0, (len(Crops_grown) - 1))],
            'Difficult_to_grow': Difficult_to_grow[randint(0, (len(Difficult_to_grow) - 1))],
            'Nutrient_Content': Nutrient_Content[randint(0, (len(Nutrient_Content) - 1))],
            'Drying_out': Drying_out[randint(0, len(Drying_out) - 1)],
            'Water_retention': Water_retention[randint(0, len(Water_retention) - 1)]
        }
        if (len(Type_of_Soil) == 0):
            messagebox.showwarning('Warning', 'Fields cannot be empty(Except:When_to_grow)')
            return
        if (len(Crops_grown) == 0):
            messagebox.showwarning('Warning', 'Fields cannot be empty(Except:When_to_grow)')
            return
        if (len(Nutrient_Content) == 0):
            messagebox.showwarning('Warning', 'Fields cannot be empty(Except:When_to_grow)')
            return
        if (len(Drying_out) == 0):
            messagebox.showwarning('Warning', 'Fields cannot be empty(Except:When_to_grow)')
            return
        if (len(Water_retention) == 0):
            messagebox.showwarning('Warning', 'Fields cannot be empty(Except:When_to_grow)')
            return
        if len(Difficult_to_grow) == 0 and db.details.count_documents({'Type_of_Soil': ToS}, limit=1) == 0:
            result = db.details.insert_one(
                {'Type_of_soil': ToS, 'Crops_grown': CRE, 'Difficult_to_grow': DTG, 'Nutrient_Content': NE,
                 'Drying_out': DOE, 'Water_retention': WRE})
        elif len(Difficult_to_grow) != 0 and db.details.count_documents({'Type_of_Soil': ToS}, limit=1) == 0:
            result = db.details.insert_one(SoilFarmingAgent)
            messagebox.showinfo('Success', 'Data added successfully')
            new.destroy()
        else:
            messagebox.showerror('Error', 'All details are required')
            return

    new = Toplevel(root)
    new.geometry('530x450')
    new.resizable(0, 0)
    new.title('Soil info')

    typeofsoillabel = Label(new, text='Type_of_Soil', font=('times new roman', 20, 'bold'))
    typeofsoillabel.grid(row=0, column=0, pady=10, padx=10)
    typeofsoilEntry = Entry(new, font=('calibri', 15))
    typeofsoilEntry.grid(row=0, column=1, pady=10, padx=10)

    cropsgrownlabel = Label(new, text='Crops_grown', font=('times new roman', 20, 'bold'))
    cropsgrownlabel.grid(row=1, column=0, pady=10, padx=10)
    cropsgrownEntry = Entry(new, font=('calibri', 15))
    cropsgrownEntry.grid(row=1, column=1, pady=10, padx=10)

    nutrientlabel = Label(new, text='Nutrient_content', font=('times new roman', 20, 'bold'))
    nutrientlabel.grid(row=2, column=0, pady=10, padx=10)
    nutrientEntry = Entry(new, font=('calibri', 15))
    nutrientEntry.grid(row=2, column=1, pady=10, padx=10)

    dryingoutlabel = Label(new, text='Drying_out', font=('times new roman', 20, 'bold'))
    dryingoutlabel.grid(row=3, column=0, pady=10, padx=10)
    dryingoutEntry = Entry(new, font=('calibri', 15))
    dryingoutEntry.grid(row=3, column=1, pady=10, padx=10)

    waterretentionlabel = Label(new, text='Water_retention', font=('times new roman', 20, 'bold'))
    waterretentionlabel.grid(row=4, column=0, pady=10, padx=10)
    waterretentionEntry = Entry(new, font=('calibri', 15))
    waterretentionEntry.grid(row=4, column=1, pady=10, padx=10)

    difftogrowlabel = Label(new, text='Difficult_to_grow', font=('times new roman', 20, 'bold'))
    difftogrowlabel.grid(row=5, column=0, pady=10, padx=10)
    difftogrowEntry = Entry(new, font=('calibri', 15))
    difftogrowEntry.grid(row=5, column=1, pady=10, padx=10)

    submitButton = ttk.Button(new, text='Submit', command=post_data)
    submitButton.grid(row=6, columnspan=2, pady=10)


def update_soil(root, db):
    def update_data():
        global root
        ToS = typeofsoilEntry.get()
        CRE = cropsgrownEntry.get()
        DTG = difftogrowEntry.get()
        NE = nutrientEntry.get()
        DOE = dryingoutEntry.get()
        WRE = waterretentionEntry.get()
        if db.details.count_documents({'Type_of_Soil': ToS}, limit=1) == 0:
            messagebox.showwarning('Error', 'Serial does not exist')
            return
        if len(ToS) != 0:
            db.details.update_one({'Type_of_Soil': ToS}, {'$set': {'Type_of_soil': ToS}})
        if len(CRE) != 0:
            db.details.update_one({'Type_of_Soil': ToS}, {'$set': {'Crops_grown': CRE}})
        if len(DTG) != 0:
            db.details.update_one({'Type_of_Soil': ToS}, {'$set': {'Difficult_to_grow': DTG}})
        if len(NE) != 0:
            db.details.update_one({'Type_of_Soil': ToS}, {'$set': {'Nutrient_Content': NE}})
        if len(DOE) != 0:
            db.details.update_one({'Type_of_Soil': ToS}, {'$set': {'Drying_out': DOE}})
        if len(WRE) != 0:
            db.details.update_one({'Type_of_Soil': ToS}, {'$set': {'Water_retention': WRE}})
            messagebox.showinfo("Success", 'Info updated successfully')
            new1.destroy()

    new1 = Toplevel(root)
    new1.geometry('530x450')
    new1.resizable(0, 0)
    new1.title('Update info')

    typeofsoillabel = Label(new1, text='Type_of_Soil', font=('times new roman', 20, 'bold'))
    typeofsoillabel.grid(row=1, column=0, pady=10, padx=10)
    typeofsoilEntry = Entry(new1, font=('calibri', 15))
    typeofsoilEntry.grid(row=1, column=1, pady=10, padx=10)

    cropsgrownlabel = Label(new1, text='Crops_grown', font=('times new roman', 20, 'bold'))
    cropsgrownlabel.grid(row=2, column=0, pady=10, padx=10)
    cropsgrownEntry = Entry(new1, font=('calibri', 15))
    cropsgrownEntry.grid(row=2, column=1, pady=10, padx=10)

    nutrientlabel = Label(new1, text='Nutrient_content', font=('times new roman', 20, 'bold'))
    nutrientlabel.grid(row=3, column=0, pady=10, padx=10)
    nutrientEntry = Entry(new1, font=('calibri', 15))
    nutrientEntry.grid(row=3, column=1, pady=10, padx=10)

    dryingoutlabel = Label(new1, text='Drying_out', font=('times new roman', 20, 'bold'))
    dryingoutlabel.grid(row=4, column=0, pady=10, padx=10)
    dryingoutEntry = Entry(new1, font=('calibri', 15))
    dryingoutEntry.grid(row=4, column=1, pady=10, padx=10)

    waterretentionlabel = Label(new1, text='Water_retention', font=('times new roman', 20, 'bold'))
    waterretentionlabel.grid(row=5, column=0, pady=10, padx=10)
    waterretentionEntry = Entry(new1, font=('calibri', 15))
    waterretentionEntry.grid(row=5, column=1, pady=10, padx=10)

    difftogrowlabel = Label(new1, text='Difficult_to_grow', font=('times new roman', 20, 'bold'))
    difftogrowlabel.grid(row=6, column=0, pady=10, padx=10)
    difftogrowEntry = Entry(new1, font=('calibri', 15))
    difftogrowEntry.grid(row=6, column=1, pady=10, padx=10)

    submitButton = ttk.Button(new1, text='Update', command=update_data)
    submitButton.grid(row=7, columnspan=2, pady=10)


def dist_det(root, db):
    def dist_data():
        global root
        name = nameEntry.get()
        email = emailEntry.get()
        contact = phoneEntry.get()
        gender = genderEntry.get()
        place = placeEntry.get()
        Name = [name]
        Email = [email]
        Contact = [contact]
        Gender = [gender]
        Place = [place]
        SoilFarmingAgent = {
            'Name': Name[randint(0, (len(Name) - 1))],
            'Email': Email[randint(0, (len(Email) - 1))],
            'Contact': Contact[randint(0, (len(Contact) - 1))],
            'Gender': Gender[randint(0, (len(Gender) - 1))],
            'Place': Place[randint(0, (len(Place) - 1))]
        }
        if (len(name) == 0):
            messagebox.showwarning('warning', 'Fields cannot be empty(Except:Email)')
            return
        if (len(contact) == 0):
            messagebox.showwarning('warning', 'Fields cannot be empty(Except:Email)')
            return
        if (len(gender) == 0):
            messagebox.showwarning('warning', 'Fields cannot be empty(Except:Email)')
            return
        if (len(place) == 0):
            messagebox.showwarning('warning', 'Fields cannot be empty(Except:Email)')
            return
        if len(email) == 0 and db.details1.count_documents({'Id': id}, limit=1) == 0:
            result = db.details1.insert_one({'Name': name, 'Place': place, 'Gender': gender, 'Contact': contact})
        elif len(email) != 0 and db.details1.count_documents({'Name': name}, limit=1) == 0:
            result = db.details1.insert_one(SoilFarmingAgent)
            messagebox.showinfo('Success', 'Data added successfully')
            new2.destroy()
        else:
            messagebox.showerror('Error', 'All details are required')
            return

    new2 = Toplevel(root)
    new2.geometry('450x400')
    new2.resizable(0, 0)
    new2.title('Distributive details')

    namelabel = Label(new2, text='Name', font=('times new roman', 20, 'bold'))
    namelabel.grid(row=0, column=0, pady=10, padx=10)
    nameEntry = Entry(new2, font=('calibri', 15))
    nameEntry.grid(row=0, column=1, pady=10, padx=10)

    emaillabel = Label(new2, text='Email', font=('times new roman', 20, 'bold'))
    emaillabel.grid(row=1, column=0, pady=10, padx=10)
    emailEntry = Entry(new2, font=('calibri', 15))
    emailEntry.grid(row=1, column=1, pady=10, padx=10)

    phonelabel = Label(new2, text='Contact', font=('times new roman', 20, 'bold'))
    phonelabel.grid(row=2, column=0, pady=10, padx=10)
    phoneEntry = Entry(new2, font=('calibri', 15))
    phoneEntry.grid(row=2, column=1, pady=10, padx=10)

    genderlabel = Label(new2, text='Gender', font=('times new roman', 20, 'bold'))
    genderlabel.grid(row=3, column=0, pady=10, padx=10)
    genderEntry = Entry(new2, font=('calibri', 15))
    genderEntry.grid(row=3, column=1, pady=10, padx=10)

    placelabel = Label(new2, text='Place', font=('times new roman', 20, 'bold'))
    placelabel.grid(row=4, column=0, pady=10, padx=10)
    placeEntry = Entry(new2, font=('calibri', 15))
    placeEntry.grid(row=4, column=1, pady=10, padx=10)

    submitButton = ttk.Button(new2, text='Submit', command=dist_data)
    submitButton.grid(row=5, columnspan=2, pady=10)


def update_dist(rrot, db):
    def update():
        global root
        name = nameEntry.get()
        email = emailEntry.get()
        contact = phoneEntry.get()
        gender = genderEntry.get()
        place = placeEntry.get()
        if len(name) == 0:
            messagebox.showwarning('Warning', 'Enter valid id')
            return
        if db.details1.count_documents({'Name': name}, limit=1) == 0:
            messagebox.showwarning('Warning', 'Name does not match')
            return
        if len(email) != 0:
            db.details1.update_one({'Name': name}, {'$set': {'Email': email}})
        if len(contact) != 0:
            db.details1.update_one({'Name': name}, {'$set': {'Contact': contact}})
        if len(gender) != 0:
            db.details1.update_one({'Name': name}, {'$set': {'Gender': gender}})
        if len(place) != 0:
            db.details1.update_one({'Name': name}, {'$set': {'Place': place}})
            messagebox.showinfo("Success", 'Details updated successfully')
            new3.destroy()

    new3 = Toplevel(root)
    new3.geometry('450x400')
    new3.resizable(0, 0)
    new3.title('Distributive details')

    namelabel = Label(new3, text='Name', font=('times new roman', 20, 'bold'))
    namelabel.grid(row=0, column=0, pady=10, padx=10)
    nameEntry = Entry(new3, font=('calibri', 15))
    nameEntry.grid(row=0, column=1, pady=10, padx=10)

    emaillabel = Label(new3, text='Email', font=('times new roman', 20, 'bold'))
    emaillabel.grid(row=1, column=0, pady=10, padx=10)
    emailEntry = Entry(new3, font=('calibri', 15))
    emailEntry.grid(row=1, column=1, pady=10, padx=10)

    phonelabel = Label(new3, text='Contact', font=('times new roman', 20, 'bold'))
    phonelabel.grid(row=2, column=0, pady=10, padx=10)
    phoneEntry = Entry(new3, font=('calibri', 15))
    phoneEntry.grid(row=2, column=1, pady=10, padx=10)

    genderlabel = Label(new3, text='Gender', font=('times new roman', 20, 'bold'))
    genderlabel.grid(row=3, column=0, pady=10, padx=10)
    genderEntry = Entry(new3, font=('calibri', 15))
    genderEntry.grid(row=3, column=1, pady=10, padx=10)

    placelabel = Label(new3, text='Place', font=('times new roman', 20, 'bold'))
    placelabel.grid(row=4, column=0, pady=10, padx=10)
    placeEntry = Entry(new3, font=('calibri', 15))
    placeEntry.grid(row=4, column=1, pady=10, padx=10)

    submitButton = ttk.Button(new3, text='Update', command=update)
    submitButton.grid(row=5, columnspan=2, pady=10)


root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')

root.geometry('300x450+150+150')
root.resizable(0, 0)
root.title('Admin window')

postButton = ttk.Button(root, text='Post soil details', width=25, compound=CENTER, command=lambda: soil_det(root, db))
postButton.grid(row=0, column=0, pady=20, padx=10)

updateButton = ttk.Button(root, text='Update soil details', width=25, compound=CENTER,
                          command=lambda: update_soil(root, db))
updateButton.grid(row=1, column=0, pady=20, padx=10)

postdisButton = ttk.Button(root, text='Post distributor det', width=25, compound=CENTER,
                           command=lambda: dist_det(root, db))
postdisButton.grid(row=2, column=0, pady=20, padx=10)

updatedisButton = ttk.Button(root, text='Update dist details', width=25, compound=CENTER,
                             command=lambda: update_dist(root, db))
updatedisButton.grid(row=3, column=0, pady=20, padx=10)

exitButton = ttk.Button(root, text='Exit', width=25, compound=CENTER, command=iexit)
exitButton.grid(row=4, column=0, pady=20, padx=10)

root.mainloop()