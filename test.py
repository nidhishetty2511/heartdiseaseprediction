# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 09:43:44 2020

@author: Nidhi
"""
import tkinter as tk
import os
from pymongo import MongoClient, ASCENDING 
import pymongo
import tkinter as t
import os
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from tkinter.font import Font


LARGE_FONT= ("Verdana", 18)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)
        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.configure(bg="black")
        frame.tkraise()
        

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        w = tk.Label(self, text ='Welcome!') 
        w.configure(fg='white', bg='black')
        w.config(font=("Courier", 44))
        w.grid(row=1, column=20, padx=(650, 10))
        
        menubutton = tk.Menubutton(self, text = "Signup / Login") 
        	
        menubutton.menu = tk.Menu(menubutton) 
        menubutton["menu"]= menubutton.menu 
        menubutton.configure(fg='white', bg='black')
        menubutton.config(font=("Courier", 30))
        
        var1 = tk.IntVar() 
        var2 = tk.IntVar() 


        menubutton.menu.add_checkbutton(label = "Sign up", 
        								variable = var1,command=lambda: controller.show_frame(PageOne)) 
        menubutton.menu.add_checkbutton(label = "Login", 
        								variable = var2, command=lambda: controller.show_frame(PageTwo)) 
        
        a = tk.Label(self, text = "")
        a.grid(row=2)
        menubutton.grid(row=3, column=20, padx=(630, 10)) 




class PageOne(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        def store():
            client = MongoClient('localhost', 27017) 
        
            name1 = name.get()
            phoneno = phone.get()
            #uname = l3.get()
            password = passw.get()
            hos_id = reg.get()
            
            # Connecting to the database named 
            # GFG 
            mydatabase = client.heart 
            
            
            # Accessing the collection named 
            # gfg_collection 
            mycollection = mydatabase.data 
               
            mycollection.insert_one({'_id': hos_id,
                				    'name': name1, 
                					'Phone No': phoneno, 
                                    
                                    'Password': password}) 
            r = t.Tk()  
            r.title(':D')
            r.geometry('150x100')
            r.configure(bg='black')
            rlbl = t.Label(r , text = '\n[+] Registered Successfully!') 
            rlbl.configure(fg = 'white', bg='black')
            rlbl.pack() 
            rbtn = t.Button(r , text = 'Ok')
            rbtn.bind("<Button-1>", lambda e: controller.show_frame(PageTwo)) 
    
            rbtn.configure(fg = 'white', bg='black')
    
            rbtn.pack()
        
        global name,phoneno,passw,reg
        
        
        tk.Label(self, text="Signup", font=("Courier", 20),bg='black', fg ="white"). grid(row = 0, column = 2, sticky = 'W', pady = 2)
    
        tk.Label(self, text = "Name -",bg='black', fg ="white", font=("Courier", 15)). grid(row = 1, column = 2, sticky = 'W', pady = 2)
        name = tk.Entry(self)
        name. grid(row = 1, column = 3, sticky = 'W', pady = 2)
        name.config(font=("Courier", 15))

        
        tk.Label(self, text = "Phone No - ",bg='black', fg ="white", font=("Courier", 15)). grid(row = 2, column = 2, sticky = 'W', pady = 2)
        phone = tk.Entry(self)
        phone. grid(row = 2, column = 3, sticky = 'W', pady = 2)
        phone.config(font=("Courier", 15))
        
        '''tk.Label(self, text = "Username - ",bg='black', fg ="white", font=("Courier", 15)). grid(row = 3, column = 2, sticky = 'W', pady = 2)
        l3 = tk.Entry(self)
        l3. grid(row = 3, column = 3, sticky = 'W', pady = 2)
        l3.config(font=("Courier", 15))'''

        
    

        
    
        tk.Label(self, text = "Password -",bg='black', fg ="white", font=("Courier", 15)). grid(row = 4, column = 2, sticky = 'W', pady = 2)
        passw = tk.Entry(self)
        passw. grid(row = 4, column = 3, sticky = 'W', pady = 2)
        
        passw.config(show="*")
        passw.config(font=("Courier", 15))

        
        tk.Label(self, text = "Hospital Registration number -",bg='black', fg ="white", font=("Courier", 15)). grid(row = 5, column = 2, sticky = 'W', pady = 2)
        reg = tk.Entry(self)
        reg. grid(row = 5, column = 3, sticky = 'W', pady = 2)
        reg.config(font=("Courier", 15))

        
        
        b1 = tk.Button(self, text = "Submit", command = store, bd='10' ,width = 10, height = 1,bg = 'black', fg ="white")
        b1. grid(row = 6, column = 2, sticky = 'W', pady = 2)
        b1.config(font=("Courier", 15))

        link1 = tk.Label(self, text="Already have an Account?", bg="black",fg="blue", cursor="hand2")
        link1.grid(row = 6, column = 3, sticky = 'W', pady = 2)
        link1.bind("<Button-1>", lambda e: controller.show_frame(PageTwo)) 
        link1.config(font=("Courier", 15))


    
    
class PageTwo(tk.Frame):
    global validate
    
        
    def __init__(self, parent, controller):
        
            tk.Frame.__init__(self, parent)
            def validate():
                id1 = l1.get()
                passd = l2.get()
                myclient = pymongo.MongoClient("mongodb://localhost:27017/")
                db = myclient.heart 
            
                mycollection = db.data 
                #check_id = mycollection.find({'_id' : id1})
                #check_pass = mycollection.find({'password' : passd})
                global a 
                global b
                a = b = False
                for x in mycollection.find({},{"_id":1}):
                    l = dict(x)
                    for key, val in l.items():
                        if val == id1:
                            a = True
                
                    for x in mycollection.find({},{"Password":1}):
                        l=dict(x)
                        for key, val in l.items():
                            if val == passd:
                                b = True
                if not a and b:
                    
                    
                    r = t.Tk()  
                    r.title(':D')
                    r.geometry('150x100')
                    r.configure(bg='black')
                    rlbl = t.Label(r , text = '\n[+] Logged In') 
                    rlbl.configure(fg = 'white', bg='black')
                    rlbl.pack() 
                    rbtn = t.Button(r , text = 'Ok')
                    rbtn.bind('<Button-1>')
                    rbtn.bind("<Button-1>", lambda e: controller.show_frame(PageThree)) 

                    rbtn.configure(fg = 'white', bg='black')
        
                    rbtn.pack()
                    r.mainloop()
                else:
                    r = t.Tk()
                    r.title('D:')
                    r.geometry('150x100')
                    r.configure(bg='black')
                    rlbl = t.Label(r , text = '\nInvalid Login')
                    rlbl.configure(fg = 'white', bg='black')
                    rlbl.pack()
                    rbtn = t.Button(r , text = 'Try again') 
                    #rbtn.bind("<Button-1>", lambda e: controller.show_frame(PageThree)) 

                    rbtn.configure(fg = 'white', bg='black')
                    rbtn.pack()
                    r.mainloop()
                
            
            global l1,l2
            
            tk.Label(self, text="Login", font=("Courier", 20),bg='black', fg ="white"). grid(row = 0, column = 2, sticky = 'W', pady = 2)
        
            tk.Label(self, text = "Registration number", font=("Courier", 15),bg='black', fg ="white"). grid(row = 1, column = 2, sticky = 'W', pady = 2)
            l1 = tk.Entry(self)
            l1.config(font=("Courier", 15))

            l1. grid(row = 1, column = 3, sticky = 'W', pady = 2)
            
            tk.Label(self, text = "Password", font=("Courier", 15),bg='black', fg ="white"). grid(row = 2, column = 2, sticky = 'W', pady = 2)
            l2 = tk.Entry(self)
            l2.config(show="*")
            l2.config(font=("Courier", 15))

            l2. grid(row = 2, column = 3, sticky = 'W', pady = 2)
            b1 = tk.Button(self, text = "Submit", font=("Courier", 15), command = validate, bd='10' ,width = 10, height = 1,bg = 'black', fg ="white")
            b1. grid(row = 3, column = 2, sticky = 'W', pady = 2)
            link1 = tk.Label(self, text="Don't have an Account?", font=("Courier", 15), bg="black",fg="blue", cursor="hand2")
            link1.grid(row =3 , column = 3, sticky = 'W', pady = 2)
            link1.bind("<Button-1>", lambda e: controller.show_frame(PageOne))

          
class PageThree(tk.Frame):
    
               

    def __init__(self, parent, controller):
            def pred():
                a = float(l1.get())
                a1 = float(sex_status.get())
                a3 = float(cp.get())
                a4 = float(l4.get())
                a5 = float(l5.get())
                a6 = float(fbs.get())
                a7 = float(l7.get())
                a8 = float(l8.get())
                a11 = float(smo.get())
                a9 = float(l9.get())
                a10 = float(l10.get())
                a11 = float(l11.get())
                a12 = float(l12.get())
                data = pd.read_csv("heartd.csv")
                Y =data.target.values
                x1=data.drop(["target"],axis=1)
                X = (x1 - np.min(x1))/(np.max(x1)-np.min(x1)).values
                from sklearn.model_selection import train_test_split
                xtrain, xtest, ytrain, ytest = train_test_split(X,Y,test_size=0.2, random_state=37)
                xtrain = xtrain.T
                xtest = xtest.T
                ytrain = ytrain.T
                ytest = ytest.T
                from sklearn.linear_model import LogisticRegression
                LR = LogisticRegression()
                LR.fit(xtrain.T,ytrain.T)
                arry = [[a,a1,a3,a4,a5,a6,a7,a8,a11,a9,a10,a11,a12]]
                ar = LR.predict(arry)
                print(ar)
                return ar
            def alert() :
                r = t.Tk()  
                r.title(':D')
                r.geometry('200x300')  
                r.configure(bg='white')
                a = pred()
                if a == 1:
                    rlbl = t.Label(r , text = "You've a Heart Disease :(",bg='white', fg ="black") 
                    rlbl. pack() 
                elif a == 0:
                    rbtn = t.Label(r , text = "Congratulations !!!\nYou're safe \nYou don't have a Heart Disease :)",bg='white', fg ="black") 
                    rbtn.pack()
                r.mainloop() 
            tk.Frame.__init__(self, parent)
            global l1,sex_status,cp,l4,l5,fbs,l7,l8,l9,l10,l11,l12,smo
                
        
            t.Label(self, text="Please Enter Your Details : ",font=("Helvetica", 16),bg='black', fg ="white"). grid(row = 0, column = 2, sticky = 'W', pady = 2)
            link1 = tk.Label(self, text="Logout", bg="black",fg="red", cursor="hand2")
            link1.grid(row = 0, column = 20, sticky = 'W', pady = 2)
            link1.bind("<Button-1>", lambda e: controller.show_frame(PageTwo)) 
            t.Label(self, text = "Age",bg='black', fg ="white"). grid(row = 1, column = 2, sticky = 'W', pady = 2)
            l1 = t.Entry(self)
            l1. grid(row = 1, column = 3, sticky = 'W', pady = 2)
                
            
            t.Label(self, text="Gender",bg='black', fg ="white"). grid(row = 2, column = 2, sticky = 'W', pady = 2)
            sex_status = t.StringVar()
            sex_false = t.Radiobutton(self, text = "Female",variable = sex_status, value = "0",bg = 'black', fg ="gray")
            sex_false. grid(row = 2, column = 3, sticky = 'W', pady = 2)
            lab4=t.Label(self, text="", bg='black')
            lab4. grid()
            sex_true = t.Radiobutton(self, text = "Male", variable = sex_status, value = "1",bg = 'black', fg ="gray")
            sex_true. grid(row = 2, column = 4, sticky = 'W', pady = 2)
            sex_status.set(0)
                
            
            t.Label(self, text="Chest pain type",bg='black', fg ="white"). grid(row = 3, column = 2, sticky = 'W', pady = 2)
            cp = t.StringVar()
            cp_tan = t.Radiobutton(self, text = "Typical angina", variable = cp, value = "0",bg = 'black', fg ="gray" )
            cp_tan.  grid(row = 3, column = 3, sticky = 'W', pady = 2)
            lab4=t.Label(self, text="", bg='black')
            lab4. grid()
            cp_an = t.Radiobutton(self, text = "Atypical angina", variable = cp, value = "1",bg = 'black', fg ="gray" )
            cp_an.grid(row = 3, column = 4, sticky = 'W', pady = 2)
            lab4=t.Label(self, text="", bg='black')
            lab4. grid()
            cp_nan = t.Radiobutton(self, text = "Non-anginal pain", variable = cp, value = "2",bg = 'black', fg ="gray" )
            cp_nan.grid(row = 4, column = 3, sticky = 'W', pady = 2)
            lab4=t.Label(self, text="", bg='black')
            lab4. grid()
            cp_as = t.Radiobutton(self, text = "Asymptomatic pain", variable = cp, value = "3",bg = 'black', fg ="gray" )
            cp_as.grid(row = 4, column = 4, sticky = 'W', pady = 2)
            cp.set(0)
            
            t.Label(self, text="Resting blood pressure in mm",bg='black', fg ="white"). grid(row = 5, column = 2, sticky = 'W', pady = 2)
            l4 = t.Entry(self)
            l4. grid(row = 5, column = 3, sticky = 'W', pady = 2)
            
            t.Label(self, text="Cholestrol",bg='black', fg ="white"). grid(row = 6, column = 2, sticky = 'W', pady = 2)
            l5 = t.Entry(self)
            l5. grid(row = 6, column = 3, sticky = 'W', pady = 2)
                
            t.Label(self, text="Fasting blood sugar  > 120 mg/dl",bg='black', fg ="white"). grid(row = 7, column = 2, sticky = 'W', pady = 2)
            fbs = t.StringVar()
            fbs_f = t.Radiobutton(self, text = "Yes", variable = fbs, value = "1",bg = 'black', fg ="gray" )
            fbs_f.  grid(row = 7, column = 3, sticky = 'W', pady = 2)
            lab4 = t.Label(self, text="", bg='black')
            lab4. grid()
            fbs_t = t.Radiobutton(self, text = "No", variable = fbs, value = "0",bg = 'black', fg ="gray" )
            fbs_t.  grid(row = 7, column = 4, sticky = 'W', pady = 2)
            fbs.set(0)
                
            t.Label(self, text="Resting electrocardiographic results",bg='black', fg ="white"). grid(row = 8, column = 2, sticky = 'W', pady = 2)
            l7 = t.Entry(self)
            l7. grid(row = 8, column = 3, sticky = 'W', pady = 2)
            
            t.Label(self, text="Thalach(maximum heart rate achieved)",bg='black', fg ="white"). grid(row = 9, column = 2, sticky = 'W', pady = 2)
            l8 = t.Entry(self)
            l8. grid(row = 9, column = 3, sticky = 'W', pady = 2)
            
            t.Label(self, text="Exercise induced angina ",bg='black', fg ="white"). grid(row = 10, column = 2, sticky = 'W', pady = 2)
            smo = t.StringVar()
            smo_f = t.Radiobutton(self, text = "Yes", variable = smo, value = "1",bg = 'black', fg ="gray" )
            smo_f.  grid(row = 10, column = 3, sticky = 'W', pady = 2)
            lab4=t.Label(self, text="", bg='black')
            lab4. grid()
            smo_t = t.Radiobutton(self, text = "No", variable = smo, value = "0",bg = 'black', fg ="gray" )
            smo_t.  grid(row = 10, column = 4, sticky = 'W', pady = 2)
            smo.set(0)
                
            t.Label(self, text="Oldpeak",bg='black', fg ="white"). grid(row = 11, column = 2, sticky = 'W', pady = 2)
            l9 = t.Entry(self)
            l9. grid(row = 11, column = 3, sticky = 'W', pady = 2)
                   
            
            t.Label(self, text="Slope",bg='black', fg ="white"). grid(row = 12, column = 2, sticky = 'W', pady = 2)
            l10 = t.Entry(self)
            l10. grid(row = 12, column = 3, sticky = 'W', pady = 2)
                
            t.Label(self, text="Number of major vessels (0-3) colored by flourosopy",bg='black', fg ="white"). grid(row = 13, column = 2, sticky = 'W', pady = 2)
            l11 = t.Entry(self)
            l11. grid(row = 13, column = 3, sticky = 'W', pady = 2)
            
            t.Label(self, text="Thal",bg='black', fg ="white"). grid(row = 14, column = 2, sticky = 'W', pady = 2)
            l12 = t.Entry(self)
            l12. grid(row = 14, column = 3, sticky = 'W', pady = 2)
            
            b1 = t.Button(self, text = "Submit",bd='10' ,command = alert, width = 10, height = 1,bg = 'black', fg ="white")
            b1. grid(row = 15, column = 2, sticky = 'W', pady = 2)
           

app = SeaofBTCapp()
app.title("Heart Disease Prediction System")
app.geometry("1600x1500")


app.mainloop()