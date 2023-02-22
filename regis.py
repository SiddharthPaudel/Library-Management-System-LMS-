from tkinter import *
import sqlite3
from tkinter import messagebox
# import Login
# from PIL import image,ImageTk
root = Tk()
root.title('Registration')
#Opening data base
conn=sqlite3.connect('signup.db')
c=conn.cursor()
# Creating a table
c.execute("""CREATE TABLE users (
    fullname text,
    ph_num text,
    email text,
    pass text,
    newpas text
)""")
print('Table created successfully')


# root.iconbitmap('H:\\My Drive\\a\\icon.ico')
root.maxsize(width=1200,height=1000)
root.minsize(width=1200,height=1000)
root.config(bg="SKYBLUE")
# root.configure(bg="GREY")
# image_1=PhotoImage(file='WhatsApp Image 2023-01-29 at 11.27.52.png')
# Label(root,image=image_1,bg='white').place(x=400,y=
photo=PhotoImage(file="working library.png")
Label(root,image=photo,bg="SKY BLUE").place(x=500,y=60)



def register():
    conn=sqlite3.connect('signup.db')
    c=conn.cursor()
    c.execute("INSERT INTO users VALUES(:fullname, :ph_num, :email, :pass, :newpas)",{
        'fullname':FullName.get(),
        'ph_num': phone1.get(),
        'email': email.get(),
        'pass': pas.get(),
        'newpas':newpas.get()
    })

    #clear text box
    FullName.delete(0,END)
    phone1.delete(0,END)
    email.delete(0,END)
    pas.delete(0,END)
    newpas.delete(0,END)

    messagebox.showinfo('Registration Information','Registered Successfully')

    conn.commit()
    conn.close()

    root.destroy()
    import Login

header=Label(root,text=' Please Register Here',fg='Black', bg='sky blue',font=('roboto',23,'bold'))
header.place(x=70,y=50)

#
# para=Label(root,text='Please input your information on fields.',fg='#404040', bg='white',font=('roboto',10,'bold'))
# para.place(x=50,y=100)


fullname=Label(root,text='Full Name*',fg='black',font="bold", bg='skyblue')
fullname.place(x=50,y=170)
FullName=Entry(root,width=25,fg='black',border=2,highlightthickness=1,borderwidth=4,highlightbackground='#F1F0FD',font=('roboto',10))
FullName.place(x=50,y=200,height=25)
#
phonenumber=Label(root,text='Phone Number*',fg='black',bg='skyblue',font="bold",)
phonenumber.place(x=290,y=170)
phone1=Entry(root,width=25,fg='black',border=2,highlightthickness=1,borderwidth=4,highlightbackground='#F1F0FD',font=('roboto',10))
phone1.place(x=290,y=200,height=25)
# para3=Label(root,text='Phone Number*',fg='black', bg='white',font=('roboto',8))
# para3.place(x=50,y=230)
# add=Entry(root,width=25,fg='black',border=0,highlightthickness=1,highlightbackground='#F1F0FD',font=('roboto',9))
# add.place(x=50,y=250,height=25)

para4=Label(root,text='Email*',fg='black', bg='skyblue',font="bold")
para4.place(x=50,y=250)
email=Entry(root,width=25,fg='black',border=2,highlightthickness=1,borderwidth=4,highlightbackground='#F1F0FD',font=('roboto',10))
email.place(x=50,y=280,height=25)

para5=Label(root,text='Create Password*',fg='black', bg='sky blue',font="bold")
para5.place(x=290 ,y=250)

pas=Entry(root,width=25,fg='black',border=2,highlightthickness=1,borderwidth=4,highlightbackground='#F1F0FD',font=('roboto',10),show="*")
pas.place(x=290,y=280,height=25)

para6=Label(root,text='Confirm Password*',fg='black', bg='SKYBLUE',font="bold")
para6.place(x=190,y=350)
newpas=Entry(root,width=25,fg='black',border=2,highlightthickness=1,borderwidth=4,highlightbackground='#F1F0FD',font=('roboto',10),show='*')
newpas.place(x=190,y=380,height=25)
show_pass = IntVar()
def show_pass_check():
    if show_pass.get():
        pas.config(show='')
        newpas.config(show='')
    else:
        pas.config(show='*')
        newpas.config(show='*')

# c = Checkbutton(root,fg='black',border=0,text ="Show",bg='white',font=('roboto',8)).place(x=50,y=395)
c1 = Checkbutton(root,fg='white',border=0,text ="Show",bg='skyblue',font=('roboto',8),command=show_pass_check,variable=show_pass,onvalue=1,offvalue=0).place(x=380,y=380)


button1=Button(root,width=10,pady=7,text='Sign up',bg='#06518d',fg='white',border=0,command=register,font=('roboto',8,'bold')).place(x=250,y=520)

def have_acc():
    root.destroy()
    import Login
para3=Button(root,text='Already have an account? ',fg='grey', bg='white',font=('roboto',8),command=have_acc)
para3.place(x=500,y=590)

# para4=Label(root,text='Login',fg='grey', bg='white',font=('roboto',8))
# para4.place(x=240,y=450)

conn.commit()
conn.close()

root.mainloop()