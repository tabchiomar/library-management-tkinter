from customtkinter import *
import customtkinter
import sqlite3
from PIL import Image
from CTkMessagebox import CTkMessagebox
import subprocess
import sys
from datetime import datetime
now = datetime.now()
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
dash_path = os.path.join(os.path.dirname(__file__), '..', 'dashboard.pyw')
db_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'db', 'app.db')

if len(sys.argv) > 1:
    valeur = sys.argv[1]
    print("Valeur reçue :", valeur)
else:
    valeur="omar"

def callpage(script_path, user): 
    app.destroy()
    subprocess.call(["pythonw", script_path, user], bufsize=0)

def godashboard():
    callpage(dash_path, str(valeur))




class ScrollableLabelButtonFrame(customtkinter.CTkScrollableFrame):


    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.command = command
        self.radiobutton_variable = customtkinter.StringVar()
        self.label_list = []
        self.button_list = []

    def add_item(self, item, image=None):
        label = customtkinter.CTkLabel(self, text=item, image=image, compound="left", padx=5, anchor="w")
        button = customtkinter.CTkButton(self, text="X", width=50, height=24, fg_color='red')
        if self.command is not None:
            button.configure(command=lambda: self.command(item))
        label.grid(row=len(self.label_list), column=0, pady=(0, 10), sticky="w")
        button.grid(row=len(self.button_list), column=1, pady=(0, 10), padx=5)
        self.label_list.append(label)
        self.button_list.append(button)


    def remove_item(self, item):
        for label, button in zip(self.label_list, self.button_list):
            if item == label.cget("text"):
                label.destroy()
                button.destroy()
                self.label_list.remove(label)
                self.button_list.remove(button)
                return
            
    def clean(self):
        for i in range(10):
            for label, button  in zip(self.label_list, self.button_list):
                    label.destroy()
                    button.destroy()
                    self.label_list.remove(label)
                    self.button_list.remove(button)

    

def chercher():
    app.scrollable_label_button_frame.clean()
    name=app.entry.get()
    print(name)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query="SELECT * FROM Adherent WHERE nom='"+name+"' OR prenom='"+name+"' OR idadherent='"+name+"'"
    cursor.execute(query)
    result=cursor.fetchone()
    print(result)
    idadherent=result[0]
    CIN_adherent=result[1]
    nom_adherent=result[2]
    datead=result[3]
    prenom_adherent=result[5]
    id_user=result[7]
    app.scrollable_label_button_frame.add_item(f"{id_user} | Adherent : {idadherent} | {nom_adherent} | {prenom_adherent} | {CIN_adherent} | {datead}", image=app.adherent_image)
    conn.close()

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gestion des adhérents - Bibliothécaire")
        self.geometry("1100x450")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


        #images navigation
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), r"..\..\..\pics")
        self.delete_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "delete_light.png")), dark_image=Image.open(os.path.join(image_path, "delete_dark.png")), size=(20, 20))
        self.edit_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "edit_light.png")), dark_image=Image.open(os.path.join(image_path, "edit_dark.png")), size=(20, 20))
        self.add_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_light.png")), dark_image=Image.open(os.path.join(image_path, "add_dark.png")), size=(20, 20))
        self.list_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "list_light.png")), dark_image=Image.open(os.path.join(image_path, "list_dark.png")), size=(20, 20))
        self.dashboard_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "dashboard.png")), dark_image=Image.open(os.path.join(image_path, "dashboard_dark.png")), size=(30, 30))
        self.adherent_image= customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "user.png")), dark_image=Image.open(os.path.join(image_path, "user_dark.png")))


        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Gestion des Adhérents", 
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.list_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Lister", image=self.list_image,
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    anchor="w", command=self.list_button_event)
        self.list_button.grid(row=1, column=0, sticky="ew")

        self.add_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Ajouter", image=self.add_image,
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       anchor="w", command=self.add_button_event)
        self.add_button.grid(row=2, column=0, sticky="ew")

        self.edit_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Modifier", image=self.edit_image,
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       anchor="w", command=self.edit_button_event)
        self.edit_button.grid(row=3, column=0, sticky="ew")

        self.delete_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Supprimer", image=self.delete_image,
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       anchor="w", command=self.delete_button_event)
        self.delete_button.grid(row=4, column=0, sticky="ew")

        self.dashboard_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Tableau de bord", image=self.dashboard_image,
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       anchor="w", command=godashboard)
        self.dashboard_button.grid(row=5, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Dark", "Light", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create list frame

        # create second frame
        self.add_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create third frame
        self.edit_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create third frame
        self.delete_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("list")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.list_button.configure(fg_color=("gray75", "gray25") if name == "list" else "transparent")
        self.add_button.configure(fg_color=("gray75", "gray25") if name == "add" else "transparent")
        self.edit_button.configure(fg_color=("gray75", "gray25") if name == "edit" else "transparent")
        self.delete_button.configure(fg_color=("gray75", "gray25") if name == "delete" else "transparent")
    

        #LIST FRAME----------------------------------------------------------------------------------------------------------------
        self.list_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.entry = customtkinter.CTkEntry(self, placeholder_text='Chercher par nom adherent', width=650)
        self.entry.place(x=250,y=20)

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text='Chercher', command=chercher)
        self.main_button_1.place(y=20,x=925)

        self.scrollable_label_button_frame = ScrollableLabelButtonFrame(master=self, width=800, height=360, command=self.label_button_frame_event, corner_radius=0)
        self.scrollable_label_button_frame.place(x=250,y=60)
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        sql="SELECT * FROM Adherent"
        cursor.execute(sql)
        result=cursor.fetchall()
        i=0
        for row in result:
            idadherent=result[i][0]
            CIN_adherent=result[i][1]
            nom_adherent=result[i][2]
            datead=result[i][3]
            prenom_adherent=result[i][5]
            id_user=result[i][7]
            i=i+1
            self.scrollable_label_button_frame.add_item(f"{id_user} | Adherent: {idadherent} | {nom_adherent} | {prenom_adherent} | {CIN_adherent} | {datead}", image=self.adherent_image)
        conn.close()
        # create second frame----------------------------------------------------------------------------------------------------------------
        def insert():
            nom=entrynom_adherent.get()
            prenom=entryprenom_adherent.get()
            cin=entryCIN_adherent.get()
            mail=entryemail_adherent.get()
            datenaissance=entrydatenaissance_adherent.get()
            username=entryusername_adherent.get()
            password=entrypassword_adherent.get()
            dateinscription=now.strftime("%d/%m/%Y")
            if(nom=='' or prenom=='' or cin=='' or mail=='' or datenaissance=='' or username=='' or password==''):
                CTkMessagebox(title='Erreur',message="Un ou plusieurs champs sont vide!", icon="warning")
            else:
                conn=sqlite3.connect(db_path)
                sqlcheck="SELECT * FROM Users WHERE username='"+username+"'"
                cursor1=conn.cursor()
                cursor1.execute(sqlcheck)
                numrows=len(cursor1.fetchall())
                if(numrows==0):
                    cursor=conn.cursor()
                    sql="INSERT INTO Users VALUES(NULL, ?,? ,'Adherent')"
                    cursor.execute(sql,(username,password))
                    id=cursor.lastrowid
                    cursor.close()
                    cursor2=conn.cursor()
                    sql2="INSERT INTO ADHERENT VALUES(NULL, ?, ?, ?, ?, ?, ?, ?)"
                    cursor2.execute(sql2,(cin, nom, dateinscription, prenom, mail, datenaissance, id))
                    sql3="INSERT INTO SANCTION VALUES(NULL, "+str(id)+", '0' , '0', '0')"
                    cursor2.execute(sql3)
                    conn.commit()
                    print('done')
                    CTkMessagebox(title='Erreur',message='Adherent ajouté!', icon="warning")
                else:
                    CTkMessagebox(title='Erreur',message="Nom d'utilsiateur existant", icon="warning")
  

        self.add_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        labelA = customtkinter.CTkLabel(self.add_frame, text="Ajout de adherent:", fg_color="transparent")
        labelA.place(x=30,y=30)
        labelnom_adherent = customtkinter.CTkLabel(self.add_frame, text="Nom de l'adherent :", fg_color="transparent")
        labelprenom_adherent = customtkinter.CTkLabel(self.add_frame, text="Prenom de l'adherent:", fg_color="transparent")
        labelCIN_adherent = customtkinter.CTkLabel(self.add_frame, text="CIN de l'adherent:", fg_color="transparent")
        labelemail_adherent = customtkinter.CTkLabel(self.add_frame, text="Mail de l'adherent:", fg_color="transparent")
        labeldatenaissance_adherent = customtkinter.CTkLabel(self.add_frame, text="Date de naissance:", fg_color="transparent")
        labelusername_adherent = customtkinter.CTkLabel(self.add_frame, text="Username:", fg_color="transparent")
        labelpassword_adherent = customtkinter.CTkLabel(self.add_frame, text="Mot de passe:", fg_color="transparent")
        
        entrynom_adherent = customtkinter.CTkEntry(self.add_frame, placeholder_text="Nom", width=500)
        entryprenom_adherent = customtkinter.CTkEntry(self.add_frame, placeholder_text="Prenom", width=500)
        entryCIN_adherent = customtkinter.CTkEntry(self.add_frame, placeholder_text="CIN", width=500)
        entryemail_adherent = customtkinter.CTkEntry(self.add_frame, placeholder_text="Mail", width=500)
        entrydatenaissance_adherent = customtkinter.CTkEntry(self.add_frame, placeholder_text="Date de naissance", width=500)
        entryusername_adherent=customtkinter.CTkEntry(self.add_frame, placeholder_text="Username", width=500)
        entrypassword_adherent=customtkinter.CTkEntry(self.add_frame, placeholder_text="Password", width=500, show='•')

        labelnom_adherent.place(x=75, y=70)
        labelprenom_adherent.place(x=75, y=110)
        labelCIN_adherent.place(x=75, y=150)
        labelemail_adherent.place(x=75, y=190)
        labeldatenaissance_adherent.place(x=75, y=230)
        labelusername_adherent.place(x=75,y=310)
        labelpassword_adherent.place(x=75,y=350)

        entrynom_adherent.place(x=210,y=70)
        entryprenom_adherent.place(x=210,y=110)
        entryCIN_adherent.place(x=210,y=150)
        entryemail_adherent.place(x=210,y=190)
        entrydatenaissance_adherent.place(x=210,y=230)
        entryusername_adherent.place(x=210,y=310)
        entrypassword_adherent.place(x=210,y=350)

        submit = customtkinter.CTkButton(self.add_frame, text= "Submit" , command=insert)
        submit.place(x=580,y=380)


        # create third frame----------------------------------------------------------------------------------------------------------------
        self.edit_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        labelB = customtkinter.CTkLabel(self.edit_frame, text="Update", fg_color="transparent")
        labelB.place(x=50,y=50)

        labelnom_haut = customtkinter.CTkLabel(self.edit_frame, text="Username de l'adherent :", fg_color="transparent") #label
        entrynom_haut = customtkinter.CTkEntry(self.edit_frame, placeholder_text="Nom d'utilisateur", width=300)



        labnom = customtkinter.CTkLabel(self.edit_frame, text="Nom de l'adherent :", fg_color="transparent")
        labprenom = customtkinter.CTkLabel(self.edit_frame, text="Prenom de l'adherent:", fg_color="transparent")
        labCIN = customtkinter.CTkLabel(self.edit_frame, text="CIN de l'adherent:", fg_color="transparent")
        labemail = customtkinter.CTkLabel(self.edit_frame, text="Mail de l'adherent:", fg_color="transparent")
        labdatenaissance = customtkinter.CTkLabel(self.edit_frame, text="Date de naissance :", fg_color="transparent")
        labpassword = customtkinter.CTkLabel(self.edit_frame, text="Nouveau mot de passe :", fg_color="transparent")
        entnom = customtkinter.CTkEntry(self.edit_frame, placeholder_text="Nom", width=500)
        entprenom = customtkinter.CTkEntry(self.edit_frame, placeholder_text="Prenom", width=500)
        entCIN = customtkinter.CTkEntry(self.edit_frame, placeholder_text="CIN", width=500)
        entemail = customtkinter.CTkEntry(self.edit_frame, width=500, placeholder_text="Email")
        entdatenaissance = customtkinter.CTkEntry(self.edit_frame, placeholder_text="Date de naissance", width=500)
        entpassword = customtkinter.CTkEntry(self.edit_frame, placeholder_text="Nouveau password", width=500)

        labnom.place(x=75, y=120)
        labprenom.place(x=75, y=160)
        labCIN.place(x=75, y=200)
        labemail.place(x=75, y=240)
        labdatenaissance.place(x=75, y=280)
        labpassword.place(x=75,y=360)
        entnom.place(x=210,y=120)
        entprenom.place(x=210,y=160)
        entCIN.place(x=210,y=200)
        entemail.place(x=210,y=240)
        entdatenaissance.place(x=210,y=280)
        entpassword.place(x=210,y=360)

        labelnom_haut.place(x=50, y=50)
        entrynom_haut.place(x=200, y=50)

        
        def remplirchamps():
            conn=sqlite3.connect(db_path)
            check_entry=entrynom_haut.get()
            sql2="select id, password from users U, adherent A where username='"+str(check_entry)+"' and U.id=A.iduser"
            cursor1=conn.cursor()
            cursor1.execute(sql2)
            resultat=cursor1.fetchone()
            cursor1.close()
            print(resultat)
            
            if(check_entry=='' ):
                CTkMessagebox(title='Erreur',message="Aucun champ de recherche n'a été rempli!", icon="warning")
            else:
                cursor=conn.cursor()
                sql="SELECT * FROM Adherent WHERE iduser='"+str(resultat[0])+"'"
                cursor.execute(sql)
                result=cursor.fetchone()

                entnom.configure(state="normal")
                entprenom.configure(state="normal")
                entCIN.configure(state="normal")
                entemail.configure(state="normal")
                entdatenaissance.configure(state="normal")
                entpassword.configure(state="normal")

                entnom.delete(0,END)
                entCIN.delete(0,END)
                entprenom.delete(0,END)
                entemail.delete(0,END)
                entdatenaissance.delete(0,END)
                entpassword.delete(0,END)

                entnom.insert(END,result[2])
                entprenom.insert(END,result[4])
                entCIN.insert(END,result[1])
                entemail.insert(END,result[5])
                entdatenaissance.insert(END, result[6])
                entpassword.insert(END, resultat[1]) #jointure

                entnom.configure(state="normal")
                entprenom.configure(state="normal")
                entCIN.configure(state="normal")
                entemail.configure(state="normal")
                entdatenaissance.configure(state="normal")
                entpassword.configure(state="normal")


                update.configure(state="normal")
                search.configure(state="disabled")
                entrynom_haut.configure(state="disabled")
                resetall.configure("normal")


        def update_adherent():
            conn=sqlite3.connect(db_path)
            check_entry=entrynom_haut.get()
            print(check_entry)
            sql2="select id, password from users U, adherent A where username='"+str(check_entry)+"' and U.id=A.iduser"
            cursor1=conn.cursor()
            cursor1.execute(sql2)
            resultat=cursor1.fetchone()
            cursor1.close()
            print(resultat)
            idu=resultat[0]


            nom=entnom.get()
            prenom=entprenom.get()
            cin=entCIN.get()
            email=entemail.get()
            naissance=entdatenaissance.get()
            passw=entpassword.get()
            

            if(nom=='' or prenom=='' or cin=='' or email=='' or naissance=='' or passw==''):
                CTkMessagebox(title='Erreur',message="Un ou plusieurs champs sont vide!", icon="warning")
            else:
                
                sql="UPDATE Adherent SET nom=?, prenom=?, CIN=?, email=?, datenaissance=? where iduser=?"
                cursor=conn.cursor()
                cursor.execute(sql, (nom, prenom, cin, email, naissance, idu))
                sql3="UPDATE USERS SET password='"+passw+"' where id = '"+str(idu)+"'"
                cursor.execute(sql3)
                conn.commit()
                cursor.close()
                conn.close()
                CTkMessagebox(title='Erreur',message="Update effectué!", icon="warning")
                resetfunc()
                
        def resetfunc():
            
            entrynom_haut.delete(0,END)
            entnom.delete(0,END)
            entCIN.delete(0,END)
            entprenom.delete(0,END)
            entemail.delete(0,END)
            entdatenaissance.delete(0,END)
            entpassword.delete(0,END)
            entrynom_haut.delete(0,END)

            update.configure(state="disabled")
            search.configure(state="normal")
            entrynom_haut.configure(state="normal")

            entnom.configure(state="disabled")
            entprenom.configure(state="disabled")
            entCIN.configure(state="disabled")
            entemail.configure(state="disabled")
            entdatenaissance.configure(state="disabled")
            entpassword.configure(state="disabled")
            update.configure("disabled")
            search.configure("normal")
            resetall.configure("normal")



        update = customtkinter.CTkButton(self.edit_frame, text= "Update" , command=update_adherent)
        update.place(x=400,y=400)

        search = customtkinter.CTkButton(self.edit_frame, text= "Chercher" , command=remplirchamps)
        search.place(x=580,y=400)

        resetall = customtkinter.CTkButton(self.edit_frame, text= "Reset" , command=resetfunc)
        resetall.place(x=220,y=400)
    
        update.configure(state="disabled")
        search.configure(state="normal")
        entnom.configure(state="disabled")
        entprenom.configure(state="disabled")
        entCIN.configure(state="disabled")
        entemail.configure(state="disabled")
        entdatenaissance.configure(state="disabled")     
        entpassword.configure(state="disabled")     

        #create fourth frame----------------------------------------------------------------------------------------------------------------
        self.delete_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        labelD = customtkinter.CTkLabel(self.delete_frame, text="Delete", fg_color="transparent")
        labelD.place(x=50,y=50)

        label_delete_name = customtkinter.CTkLabel(self.delete_frame, text="Username de l'adherent", fg_color="transparent")
        entry_delete_name = customtkinter.CTkEntry(self.delete_frame, placeholder_text="Nom d'utilisateur", width=300)



        label_delete_name.place(x=50, y=50)
        entry_delete_name.place(x=190, y=50)


        def delete():
            name_delete = entry_delete_name.get()
            conn=sqlite3.connect(db_path)
            cursor2=conn.cursor()
            sql1="SELECT rank,id FROM USERS WHERE USERNAME='"+name_delete+"'"
            cursor2.execute(sql1)
            res=cursor2.fetchone()
            id=res[1]
            rank=res[0]
            print(id)
            
            if(rank=='Adherent'):
                sql2="DELETE FROM Adherent WHERE iduser='"+str(id)+"'"
                cursor2.execute(sql2)
                sql3="DELETE FROM USERS WHERE id='"+str(id)+"'"
                cursor2.execute(sql3)
                count=cursor2.rowcount
                sql="DELETE FROM SANCTION WHERE iduser='"+str(id)+"'"
                cursor2.execute(sql)
                conn.commit()
            else:
                CTkMessagebox(title="Vous n'êtes pas autorisé!",message="Supprimé", icon="warning")
                
            cursor2.close()
            conn.close()
            if(count!=0):
                CTkMessagebox(title='Erreur',message="Supprimé", icon="warning")
            else:
                CTkMessagebox(title='Erreur',message="Aucun adherent de ce nom/id", icon="warning")



        delete_button = customtkinter.CTkButton(self.delete_frame, text= "Supprimer" , command=delete)
        delete_button.place(x=580,y=100)




        # select default frame



# show selected frame
        if name == "list":
            self.list_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.list_frame.grid_forget()

        if name == "add":
            self.add_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.add_frame.grid_forget()

        if name == "edit":
            self.edit_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.edit_frame.grid_forget()

        if name == "delete":
            self.delete_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.delete_frame.grid_forget()

    def list_button_event(self):
        self.select_frame_by_name("list")

    def add_button_event(self):
        self.select_frame_by_name("add")

    def edit_button_event(self):
        self.select_frame_by_name("edit")

    def delete_button_event(self):
        self.select_frame_by_name("delete")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def label_button_frame_event(self, item):
        #bouton rouge X
        nom=f"{item}"
        elements=nom.split("|")
        id=elements[0].strip()
        print(id)
        print(f"label button frame clicked: {item}")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        #QUERY DE SELECT LIVRE

        sql="DELETE from ADHERENT where iduser='"+id+"'"
        cursor.execute(sql)
        sqluser="DELETE FROM USERS WHERE id='"+id+"'"
        cursor.execute(sqluser)
        sql2="DELETE FROM SANCTION WHERE iduser='"+id+"'"
        cursor.execute(sql2)
        conn.commit()
        conn.close()
        self.scrollable_label_button_frame.clean()
        ListerAdherents()
        
def ListerAdherents():
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        sql="SELECT * FROM Adherent"
        cursor.execute(sql)
        result=cursor.fetchall()
        i=0
        for row in result:
            idadherent=result[i][0]
            CIN_adherent=result[i][1]
            nom_adherent=result[i][2]
            datead=result[i][3]
            prenom_adherent=result[i][5]
            id_user=result[i][7]
            i=i+1
            app.scrollable_label_button_frame.add_item(f"f{id_user} | Adherent : {idadherent} | {nom_adherent} | {prenom_adherent} | {CIN_adherent} | {datead}", image=app.adherent_image)
        conn.close()

if __name__ == "__main__":
    app = App()
    app.mainloop()

