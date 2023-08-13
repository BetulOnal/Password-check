# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import json

def create_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    new_letter = [random.choice(letters) for _ in range(nr_letters)]
    new_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    new_symbol = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = new_letter + new_numbers + new_symbol
    random.shuffle(password_list)
    password = "".join(password_list)
    entry_pass.insert(0, password)
    pyperclip.copy(password) #kod u otomotik olarak kopyaladı

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = entry_web.get()
    mail = entry_mail.get()
    password = entry_pass.get()

    new_data = {
        web : {
            "Mail": mail,
            "Password":password
        }
    }

    if web == "" or password == "":
        messagebox.showinfo(title="Ops", message="Please don't leave eny field emty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except:
            with open ("data.json", "w")as data_file:
                json.dump(new_data, data_file)
        else:
            data.update(new_data)
            with open ("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            entry_web.delete(0, END)
            entry_pass.delete(0, END)

#
 # json ile new_data dict. bilgileri(kullanıcının verdiği bilgileri) data_files ile data.json a dic olarak YAZDIK "w" olmalı
            #json.dump(new_data, data_files, indent=2)

            # load ile data.jsondaki önceden yazdığımız verileri OKUDUK. data.jsonda ne varsa onu okuyor. new_data yazdığımızda
            # type hatası alıyoruz. "r " olmalı
            #data = json.load(data_files)

            #data = json.load(data_files)
            #data.update(new_data)

        #with open("data.json", "w") as data_files:

# ---------------------------- FIND PASSWORD------------------------------- #
def find_password():
    web_name = entry_web.get()
    try:
        with open ("data.json","r") as data_files:
            data = json.load(data_files)
            #print(data)
    except FileNotFoundError:
        messagebox.showinfo(title="Opps!", message="No Data File Found")
    else:
        if web_name in data:
            mail = data[web_name]["Mail"]
            password = data[web_name]["Password"]
            messagebox.showinfo(title=web_name, message=f"Email:{mail}\nPassword:{password}")
            entry_pass.insert(0,password)
        else:
            messagebox.showinfo(title="Errorr!", message=f"No details for {web_name} exist.")






# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pasword Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200, )
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(row=0, column=1)

web_site = Label(text="Website:")
web_site.grid(row=1, column=0)

entry_web= Entry(width=21)
entry_web.focus( )
entry_web.grid(row=1, column=1, columnspan=1)

search_button= Button(text="Search", width=10, command=find_password)
search_button.grid(row=1, column=2, )

e_mail= Label(text="E-mail/Username:",)
e_mail.grid(row=2, column=0)

entry_mail= Entry(width=35)
entry_mail.insert(END, "holaalala@gmail.com")
entry_mail.grid(row=2, column=1, columnspan=2)

password = Label(text="Password:")
password.grid(row=3, column=0)

entry_pass= Entry(width=21)
entry_pass.grid(row=3, column=1,)

button_pass = Button(text="Generate Password", width=10, command=create_password)
button_pass.grid(row=3, column=2,)

button_add= Button(text="Add", width=34, command=save)
button_add.grid(row=4, column=1,columnspan=2 )














window.mainloop()