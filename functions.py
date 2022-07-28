
from tkinter import ttk
import mysql.connector
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from mysql.connector import cursor
import pandas as pd
from pandastable import Table,TableModel

class Mainapp:
    

    def new_window(self):
        global root
        root = tk.Toplevel()
        w = 1000 # width for the Tk root
        h = 500 # height for the Tk root

        ws = root.winfo_screenwidth() # width of the screen
        hs = root.winfo_screenheight() # height of the screen

        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        

        Id = tk.StringVar()
        product = tk.StringVar()
        shop = tk.StringVar()
        price=tk.StringVar()
        table_name = tk.StringVar()
        


        frame = Frame(root,bg="#f4e1d2",highlightbackground="black",highlightthickness=3)
        frame.place(x=0,y=0,width=450,height=250)
        global frame2
        frame2 = Frame(root,bg="#f4e1d2")
        frame2.place(x=450,y=0,width=550,height=500)

        frame3 = Frame(root,bg="#f4e1d2",highlightbackground="black",highlightthickness=3)
        frame3.place(x=0,y=250,width=450,height=250)

        label = Label(frame,text="ID",bg="#f4e1d2")
        label.grid(row=0,column=0,ipadx=2,ipady=2,padx=3,pady=10)
        entry = Entry(frame,font=('Arial 10'),textvariable=Id) 
        entry.grid(row=0,column=1,ipady=5)


        label1 = Label(frame,text="product",bg="#f4e1d2")
        label1.grid(row=1,column=0,ipadx=2,ipady=2,padx=3,pady=10)
        entry1 = Entry(frame,font=('Arial 10'),textvariable=product) 
        entry1.grid(row=1,column=1,ipady=5)

        label2 = Label(frame,text="shop",bg="#f4e1d2")
        label2.grid(row=2,column=0,ipadx=2,ipady=2,padx=3,pady=10)
        entry2 = Entry(frame,font=('Arial 10'),textvariable=shop) 
        entry2.grid(row=2,column=1,ipady=5)

        label3 = Label(frame,text="price",bg="#f4e1d2")
        label3.grid(row=3,column=0,ipadx=1,ipady=1,padx=3,pady=10)
        entry3 = Entry(frame,font=('Arial 10'),textvariable=price) 
        entry3.grid(row=3,column=1,ipady=5)

        
        entry4 = Entry(frame3,font=('Arial 10'),textvariable=table_name) 
        entry4.grid(row=1,column=7,ipady=5)
      

        options = self.tables()
        
        clicked = tk.StringVar()
        clicked.set("options")

        Insert_menu = OptionMenu(frame,clicked,*options) 
        Insert_menu.grid(row=0,column=3,padx=10,pady=10)

        Option_menu = OptionMenu(frame3,clicked,*options) 
        Option_menu.grid(row=1,column=2,padx=10,pady=10)

        delete_menu = OptionMenu(frame3,clicked,*options) 
        delete_menu.grid(row=1,column=5,padx=10,pady=10)

        insert_button = Button(frame,text="Insert",command=lambda:self.insert(clicked.get(),Id.get(),product.get(),shop.get(),price.get()))
        insert_button.grid(row=4,column=1,padx=10,ipadx=20)

        update_button = Button(frame,text="Update",command=lambda:self.Update(clicked.get(),Id.get(),product.get(),shop.get(),price.get()))
        update_button.grid(row=4,column=2,padx=10,ipadx=20)

        option_button = Button(frame3,text="Show records",command=lambda:self.select(clicked.get()))
        option_button.grid(row=0,column=2,padx=10)

        delete_button = Button(frame3,text="Delete",command=lambda:self.drop_table(clicked.get()))
        delete_button.grid(row=0,column=5,padx=10,ipadx=15)

        table_name_button = Button(frame3,text="Create table",command=lambda:self.create_table(table_name.get()))
        table_name_button.grid(row=0,column=7,padx=10,ipadx=15)

        
        

    def show(self,frame3,clicked):
        label = Label(frame3,text=clicked)
        label.place(x=0,y=210)

    def onclick(self):
        tk.messagebox.showwarning("Error","connection failed")
        
    def log(self,x,y,z):
        try:
            
            self.connection = mysql.connector.connect(user = "{}".format(x),password= "{}".format(y),database = "{}".format(z) , auth_plugin = "mysql_native_password")
            self.cursor = self.connection.cursor()
            self.new_window()
        except:
            self.onclick()

    
            
    
    def insert(self,table,id,product,shop,price):
        try:
            rec=[id,product,shop,price]
            cmd = "insert into {} values(%s,%s,%s,%s)".format(table)
            self.cursor.execute(cmd,rec)
            self.connection.commit()
            tk.messagebox.showwarning(":)","Data inserted")
            root.destroy()
            self.new_window()
        except:
            tk.messagebox.showwarning(":)","Error")
        
    def select(self,database):
        query = "select * from {}".format(database)
        
        
        
       
        
        data = pd.read_sql_query(query,self.connection)
        
        
        pt = Table(frame2,showstatusbar=True,showtoolbar=True,enable_menus=True,editable=True,width=550,height=500)
        pt.model.df = data
        pt.show()
        pt.zoomIn()
        

    def drop_table(self,table):
        try:
            self.cursor.execute("drop table {}".format(table))
            tk.messagebox.showwarning(":)","table dropped")
            root.destroy()
            self.new_window()
        except:
            tk.messagebox.showwarning("Error","No such table in database")

    def create_table(self,table_name):
        try:
            self.cursor.execute("create table {}(ID int primary key,product varchar(50),shop varchar(20),price float)".format(table_name))
            
            tk.messagebox.showwarning(":)","table created")
            root.destroy()
            self.new_window()
            
        except:
            tk.messagebox.showwarning("Error","failed to create table")
    
    def Update(self,name,id,product,shop,price):
        try:
            records = [id,product,shop,price]
            upd = "update {} set ID=%s,product=%s,shop=%s,price=%s where ID = '{}' ".format(name,id)
            self.cursor.execute(upd,records)
            self.connection.commit()
            tk.messagebox.showwarning(":)","Data updated")
            root.destroy()
            self.new_window()

        except:
            tk.messagebox.showwarning(":)","Error")
        

    def tables(self):
        global list
        list= []
        self.cursor.execute("show tables")
        for row in self.cursor:
            list.append(row[0])
        return list

    
            
                
      

    
        





   