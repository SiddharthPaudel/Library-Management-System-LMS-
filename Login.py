#Front End
import sqlite3



# import Bill Management
from tkinter import *
a=Tk()
a.title("Login")
a.maxsize(width=1200,height=1000)
a.minsize(width=1200,height=1000)
from tkinter import messagebox
def sign_in():
    conn=sqlite3.connect('signup.db')
    c=conn.cursor()

    c.execute('SELECT *,email, pass FROM users')

    records=c.fetchall()
    # print(records)
    found_username = ''
    found_password=''
    username_check=''
    for record in records:
        username_check=str(record[2])

        if entry1.get() == username_check:
            found_username=username_check
            found_password = str(record[3])
    if found_username==entry1.get() and found_password==pas.get():
        a.destroy()
        import dashboard
    else:
        messagebox.showinfo("CHECK YOUR CREDENTIALS","INVALID CREDENTIALS")
    conn.commit
    conn.close


a.configure(bg='grey')
# a.iconbitmap('H:\\My Drive\\a\\icon.ico')
# canvas=Canvas(a,bg='#06518d',height=1000,width=500).place(x=500,y=0)
photo=PhotoImage(file="nepal.png")
image=Label(a,image=photo,bg='grey').place(x=0,y=40)
label1=Label(a,text=" WELCOME TO LIBRARY MANAGEMENT SYSTEM",font=('Times New Roman',24,'bold'),fg='black',bg='grey').place(x=50,y=40)
# label2=Label(a,text='One place for all your needs.',font=('Calisto MT Bold',18),bg='White',fg='').place(x=100,y=125)
# label4=Label(a,text='_______',font=('Calisto MT Bold',14,'bold'),fg='black',bg="purple").place(x=600,y=195)
label3=Label(a,text='LOGIN',fg='black',font=('Calisto MT Bold',14,'bold'),bg="grey").place(x=700,y=100)
label5=Label(a,text='Email :',font=('Calisto MT Bold',14,'bold'),fg='black',bg="grey").place(x=700,y=150)
entry1=Entry(a,borderwidth=1,bg='White',)
entry1.place(x=780,y=150)
label6=Label(a,text='Password :',font=('Calisto MT Bold',14,'bold'),fg='black',bg="grey").place(x=700,y=200)
pas=Entry(a,borderwidth=1,bg='White',show='*')
pas.place(x=810,y=200)









# C1=Checkbutton(a,text='Show Password',bg='#06518d',fg='White',font=('Calisto MT Bold',10))
# C1.place(x=600,y=310)




def cre():
    email=entry1.get()
    Password=pas.get()




#llogin button
button1=Button(a,text='Login',fg='white',bg='grey',font=('Calisto MT Bold',14,'bold'),height=1,width=7,command=sign_in).place(x=810,y=280)

def forget():
    a.destroy()
    import fpas

label7=Button(a,text='Forgot Password?',bg='grey',fg='white',font=('Roboto ',10),command=forget).place(x=920,y=350)
show_pass=IntVar()
def show_pass_check():
    if show_pass.get():
        pas.config(show='')
    else:
        pas.config(show='*')

# c = Checkbutton(root,fg='black',border=0,text ="Show",bg='white',font=('roboto',8)).place(x=50,y=395)
c1 = Checkbutton(a,fg='white',border=0,text ="Show",bg='grey',font=('roboto',8),command=show_pass_check,variable=show_pass,onvalue=1,offvalue=0).place(x=900,y=230)







a.mainloop()