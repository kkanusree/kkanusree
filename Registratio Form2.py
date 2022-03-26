from tkinter import *
from tkinter import ttk
import mysql.connector as mysql
from tkinter import messagebox
win = Tk()
win.geometry("500x500")
Label(win,text="Registration form", font="arial 20 bold").grid(row=0, column=3)

fname=StringVar()
lname=StringVar()
addname=StringVar()
ename=StringVar()
cno=StringVar()
uname=StringVar()
password=StringVar()
cpassword=StringVar()
gender=StringVar()
country=StringVar()

L1 = Label(win,text="First Name").grid(row=1,column=1)
E2 = Entry(win, bd=5,textvariable=fname).grid(row=1,column=2)
L2 = Label(win,text="Last Name").grid(row=1,column=3)
E2 = Entry(win, bd=5,textvariable=lname).grid(row=1,column=4)
L3 = Label(win,text="Address").grid(row=3,column=1)
E3 = Entry(win, bd=5,textvariable=addname).grid(row=3,column=2)
L4 = Label(win,text="Email").grid(row=4,column=1)
E4 = Entry(win, bd=5,textvariable=ename).grid(row=4,column=2)
L5 = Label(win,text="Gender").grid(row=5,column=1)
R1 = Radiobutton(win, text="Male", value=1,variable=gender).grid(row=5,column=2)
R2 = Radiobutton(win, text="Female", value=2,variable=gender).grid(row=5,column=3)
course = ["India","Russia","Japan","America"]
C1 = Label(win,text="Select your country").grid(row=6,column=1)
cmb=ttk.Combobox(win,value=course,width=20,textvariable=country).grid(row=6,column=2)

L6 = Label(win,text="Contact no").grid(row=11,column=1)
E6 = Entry(win, bd=5,textvariable=cno).grid(row=11,column=2)
L7 = Label(win,text="Username").grid(row=12,column=1)
E7 = Entry(win, bd=5,textvariable=uname).grid(row=12,column=2)
L8 = Label(win,text="Password").grid(row=13,column=1)
E8 = Entry(win, bd=5,textvariable=password).grid(row=13,column=2)
L9 = Label(win,text="Confirm Password").grid(row=13,column=3)
E9 = Entry(win, bd=5,textvariable=cpassword).grid(row=13,column=4)
chk = Checkbutton(win,text="I Agree with the terms and conditions").grid(row=14,column=2)
Button(win,text="Submit",fg="brown",command=register_data).grid(row=16,column=1)
def register_data():
    if fname.get()=="":
        messagebox.showerror("error","Enter first name")
    else:
        conn=mysql.connect(user="root",password="anu_@123",host="localhost",database="anu")
        c=conn.cursor()
        c.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            fname.get(),lname.get(),addname.get(),ename.get(),gender.get(),country.get(),cno.get(),uname.get(),password.get(),cpassword.get(),))
        conn.commit()
        conn.close()
        messagebox.showinfo("login","form registered")
                  
                  
        
        
win.mainloop()
