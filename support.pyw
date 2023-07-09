from tkinter import *
from CTkMessagebox import CTkMessagebox
import sqlite3
import customtkinter
from datetime import datetime
now = datetime.now()

customtkinter.set_appearance_mode("Light")


def submit():
    username=user.get()
    cont=contact.get()
    topic=sujetentry.get()
    if(username!='Nom d\'utilisateur' and cont!='Contact (mail, phone..)'):
        conn = sqlite3.connect('./db/app.db')       # IDCONTACT | ETAT | USERNAME | CONTACT
        cursor = conn.cursor()
        date=now.strftime("%d/%m/%Y")
        sql='INSERT INTO CONTACT VALUES (NULL, 0, ?,?, ?, ?, NULL)'
        cursor.execute(sql,(username, cont, topic, date))
        print(date)
        conn.commit()
        conn.close()
        label=Label(frame,text="Nous vous contacterons dans quelques heures!", fg='black', bg='white', font=('Microsoft YaHei UI Light',9))
        label.place(x=35,y=330)
    else:
        CTkMessagebox(title='Erreur',message='Formulaire non completé', icon="warning")


    

root=Tk()
logo=PhotoImage(file = r'C:\Users\Omar\Desktop\Class\PFA\Realisation\pics\logo.png')
root.iconphoto(False,logo)
root.title('Mot de passe oublié')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root. resizable(False,False)


img = PhotoImage(file='./pics/contact.png')
Label(root,image=img,bg='white').place(x=500,y=50)


frame=Frame(root, width=350, height=350, bg='white')
frame.place(x=80,y=70)

heading=Label(frame,text='Formulaire de contact', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=0,y=5)


#-----Zone Username-----

def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Nom d\'utilisateur')

user = Entry(frame,width=25, fg='black', border=0,bg="white", font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Nom d\'utilisateur')

user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=295, height=2, bg="black").place(x=25,y=107)

#-----Zone Contact-----

# PLACEHOLDER FUNCTIONS
def on_enter(e):
    contact.delete(0,'end')

def on_leave(e):
    name=contact.get()
    if name=='':
        contact.insert(0,'Contact (mail, phone..)')

contact = Entry(frame,width=25, fg='black', border=0,bg="white", font=('Microsoft YaHei UI Light',11))
contact.place(x=30,y=150)

contact.insert(0,'Contact (mail, phone..)')

contact.bind('<FocusIn>', on_enter)
contact.bind('<FocusOut>', on_leave)

Frame(frame,width=295, height=2, bg="black").place(x=25,y=177)

#-----Zone Sujet-----

# PLACEHOLDER FUNCTIONS
def on_enter(e):
    sujetentry.delete(0,'end')

def on_leave(e):
    sujet=sujetentry.get()
    if sujet=='':
        sujetentry.insert(0,'Sujet')

sujetentry = Entry(frame,width=25, fg='black', border=0,bg="white", font=('Microsoft YaHei UI Light',11))
sujetentry.place(x=30,y=225)

sujetentry.insert(0,'Sujet')

sujetentry.bind('<FocusIn>', on_enter)
sujetentry.bind('<FocusOut>', on_leave)

Frame(frame,width=295, height=2, bg="black").place(x=25,y=250)

#-----Bouton Login and SIGN UP-----
Button(frame,width=39,pady=7, text='Envoyer', bg='#57a1f8', fg='white', border=0, cursor='hand2',command=submit).place(x=35,y=280)


root.mainloop()