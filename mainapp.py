from functions import Mainapp
from tkinter import *
import tkinter as tk
from tkinter import messagebox


log = Mainapp().log

window = Tk()
window.title("database menagment system")
window.configure(background='#f4e1d2')

w = 900 # width for the Tk root
h = 500 # height for the Tk root

ws = window.winfo_screenwidth() # width of the screen
hs = window.winfo_screenheight() # height of the screen

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

window.geometry('%dx%d+%d+%d' % (w, h, x, y))

window.geometry("350x500")

label = tk.Label(window, text="Home budget menager!",font=("Courier",20),height=2,bg="#f4e1d2")
label.pack(padx=0,pady=0)

username = tk.StringVar()
password = tk.StringVar()
databse_2 = tk.StringVar()

signin = tk.Frame(window)
signin.pack(padx=0, pady=0, fill='x', expand=True)

user_name_label = tk.Label(signin, text="Username:",font=("Courier",20),bd=1,pady=10,height=2,bg="#f4e1d2")
user_name_label.pack(fill='x', expand=True)

user_name_entry = tk.Entry(signin, textvariable=username)
user_name_entry.pack(fill='x', expand=True)

# password
password_label = tk.Label(signin, text="Password:",font=("Courier",20),height=2,bg="#f4e1d2")
password_label.pack(fill='x', expand=True)

password_entry = tk.Entry(signin, textvariable=password, show="*")
password_entry.pack(fill='x', expand=True)

database_label = tk.Label(signin, text="database:",font=("Courier",20),height=2,bg="#f4e1d2")
database_label.pack(fill='x', expand=True)

database_entry = tk.Entry(signin, textvariable=databse_2)
database_entry.pack(fill='x', expand=True)




# login button
login_button = tk.Button(signin, text="Login", command=lambda:log(username.get(),password.get(),databse_2.get()),height=5,bg="#f4e1d2")
login_button.pack(fill='x', expand=True, pady=10)





window.mainloop()
