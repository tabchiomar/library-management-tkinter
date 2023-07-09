from tkinter import *
from CTkMessagebox import CTkMessagebox
import customtkinter
import sqlite3
import subprocess
import os
db_path = os.path.join(os.path.dirname(__file__), '.', 'db', 'app.db')
dash_path_bib = os.path.join(os.path.dirname(__file__), 'app', 'Bibliothecaire', 'dashboard.pyw')
dash_path_admin = os.path.join(os.path.dirname(__file__), 'app', 'Admin', 'dashboard.pyw')
dash_path_adh = os.path.join(os.path.dirname(__file__), 'app', 'Adherent', 'dashboard.pyw')
image_path = os.path.join(os.path.dirname(__file__), 'pics',)


customtkinter.set_appearance_mode("Light")

root=Tk()
logo=PhotoImage(file = image_path+'\logo.png')
root.iconphoto(False,logo)
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root. resizable(False,False)

def callpage(script_path, user): 
    root.destroy()
    subprocess.call(["pythonw", script_path, user], bufsize=0)


def seconnecter():
    #FONCTION DE CONNEXION          Table structure : id | username | password | rank
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    username=user.get()
    password=passw.get()
    sql='SELECT * FROM Users WHERE username=? AND password=?'
    cursor.execute(sql, (username, password))
    result = cursor.fetchall()
    num_rows = len(result)
    if(num_rows==1):
        rank=result[0][3] # THE RANK
        if(rank=="admin"):
            callpage(dash_path_admin, username)
        elif(rank=="bibliothecaire"):
            callpage(dash_path_bib, username)
        else:
            callpage(dash_path_adh, username)
    else:
        CTkMessagebox(title='Erreur',message='Nom d\'utilisateur ou mot de passe inconnu!', icon="warning")
    conn.close()


def support():
    callpage(r".\support.pyw", "0")
    
img = PhotoImage(file=image_path+'\login.png')
Label(root,image=img,bg='white').place(x=10,y=50)

frame=Frame(root, width=350, height=350, bg='white')
frame.place(x=480,y=70)

heading=Label(frame,text='Connexion', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

#-----Zone Username-----

# PLACEHOLDER FUNCTIONS
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

#-----Zone Password-----

# PLACEHOLDER FUNCTIONS
def on_enter(e):
    passw.delete(0,'end')

def on_leave(e):
    name=passw.get()
    if name=='':
        passw.insert(0,'Mot de passe')

passw = Entry(frame,width=25, fg='black', border=0,bg="white", font=('Microsoft YaHei UI Light',11),show='•')
passw.place(x=30,y=150)

passw.insert(0,'Mot de passe')

passw.bind('<FocusIn>', on_enter)
passw.bind('<FocusOut>', on_leave)

Frame(frame,width=295, height=2, bg="black").place(x=25,y=177)

#-----Bouton Login and SIGN UP-----
Button(frame,width=39,pady=7, text='Se connecter', bg='#57a1f8', fg='white', border=0, cursor='hand2',command=seconnecter).place(x=35,y=204)
label=Label(frame,text="Besoin d'aide ?", fg='black', bg='white', font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)

contact=Button(frame, width=12, text="Contactez-nous !", border=0, bg='white', cursor='hand2', fg='#57a1f8', command=support).place(x=215, y=270)
root.mainloop()