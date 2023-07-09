from customtkinter import *
import customtkinter
import sqlite3
import os
from PIL import Image
from CTkMessagebox import CTkMessagebox
import subprocess
import sys
dash_path = os.path.join(os.path.dirname(__file__), '..', 'dashboard.pyw')
db_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'db', 'app.db')
current_dir = os.path.dirname(os.path.abspath(__file__))

if len(sys.argv) > 1:
    valeur = sys.argv[1]
    print("Valeur reçue :", valeur)
else:
    valeur="admin"

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
    query="SELECT * FROM Livre WHERE TITRE='"+name+"' OR idlivre='"+name+"'"
    cursor.execute(query)
    result=cursor.fetchone()
    print(result)
    num_rows = len(result)
    if(num_rows==0):
        CTkMessagebox(title='Erreur',message='Aucun titre de ce nom!', icon="warning")
    else:
        idlivre=result[0]
        titre=result[1]
        categorie=result[2]
        auteur=result[3]
        annee_pub=result[5]
        app.scrollable_label_button_frame.add_item(f"{idlivre} | {titre} | {categorie} | {auteur} | {annee_pub}", image=app.book_image)
    conn.close()

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gestion des livres - Administrateur système")
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
        self.book_image= customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "open_book.png")), dark_image=Image.open(os.path.join(image_path, "open_book_dark.png")))
        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Gestion des livres", 
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
        self.entry = customtkinter.CTkEntry(self, placeholder_text='Chercher', width=650)
        self.entry.place(x=250,y=20)

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text='Chercher', command=chercher)
        self.main_button_1.place(y=20,x=925)

        self.scrollable_label_button_frame = ScrollableLabelButtonFrame(master=self, width=800, height=360, command=self.label_button_frame_event, corner_radius=0)
        self.scrollable_label_button_frame.place(x=250,y=60)
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        sql="SELECT * FROM LIVRE"
        cursor.execute(sql)
        result=cursor.fetchall()
        i=0
        for row in result:
            idlivre=result[i][0]
            titre=result[i][1]
            categorie=result[i][2]
            auteur=result[i][3]
            annee_pub=result[i][5]
            i=i+1
            self.scrollable_label_button_frame.add_item(f"{idlivre} | {titre} | {categorie} | {auteur} | {annee_pub}", image=self.book_image)
        conn.close()
        # create second frame----------------------------------------------------------------------------------------------------------------
        def insert():
            title=entrytitre.get()
            cat=entrycategorie.get()
            aut=entryauteur.get()
            desc=entrydescription.get(1.0,END)
            annee=entryannee.get()
            rayon=entryrayon.get()
            if(title=='' or cat=='' or aut=='' or desc=='' or annee=='' or rayon==''):
                CTkMessagebox(title='Erreur',message="Un ou plusieurs champs sont vide!", icon="warning")
            else:
                conn=sqlite3.connect(db_path)
                sqlcheck="SELECT * FROM LIVRE WHERE TITRE='"+title+"'"
                cursor1=conn.cursor()
                cursor1.execute(sqlcheck)
                numrows=len(cursor1.fetchall())
                if(numrows==0):
                    cursor=conn.cursor()
                    sql="INSERT INTO LIVRE VALUES(NULL, ?,?,?,?,?,?)"
                    cursor.execute(sql,(title,cat,aut,desc,annee,rayon))    
                    idlivre=str(cursor.lastrowid)
                    sql2="INSERT INTO EXEMPLAIRE VALUES(NULL,"+idlivre+", 1)"
                    cursor.execute(sql2)
                    conn.commit()
                    CTkMessagebox(title='Erreur',message='Livre ajouté!', icon="warning")
                else:
                    CTkMessagebox(title='Erreur',message='Titre existant', icon="warning")
  

        self.add_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        labelA = customtkinter.CTkLabel(self.add_frame, text="Ajout de livre:", fg_color="transparent")
        labelA.place(x=50,y=50)
        labeltitre = customtkinter.CTkLabel(self.add_frame, text="Titre du livre :", fg_color="transparent")
        labelcategorie = customtkinter.CTkLabel(self.add_frame, text="Catégorie du livre:", fg_color="transparent")
        labelauteur = customtkinter.CTkLabel(self.add_frame, text="Auteur du livre:", fg_color="transparent")
        labeldescription = customtkinter.CTkLabel(self.add_frame, text="Description du livre:", fg_color="transparent")
        labelrayon = customtkinter.CTkLabel(self.add_frame, text="Rayon:", fg_color="transparent")
        labelannee = customtkinter.CTkLabel(self.add_frame, text="Année de publication:", fg_color="transparent")
        entrytitre = customtkinter.CTkEntry(self.add_frame, placeholder_text="Titre", width=500)
        entrycategorie = customtkinter.CTkEntry(self.add_frame, placeholder_text="Catégorie", width=500)
        entryauteur = customtkinter.CTkEntry(self.add_frame, placeholder_text="Auteur", width=500)
        entrydescription = customtkinter.CTkTextbox(self.add_frame, width=500, height=50, border_width=2)
        entryrayon = customtkinter.CTkEntry(self.add_frame, placeholder_text="Rayon du livre", width=500)
        entryannee = customtkinter.CTkEntry(self.add_frame, placeholder_text="Annee de publication", width=500)

        labeltitre.place(x=75, y=120)
        labelcategorie.place(x=75, y=160)
        labelauteur.place(x=75, y=200)
        labeldescription.place(x=75, y=240)
        labelrayon.place(x=75, y=320)
        labelannee.place(x=75,y=360)
        entrytitre.place(x=210,y=120)
        entrycategorie.place(x=210,y=160)
        entryauteur.place(x=210,y=200)
        entrydescription.place(x=210,y=240)
        entryrayon.place(x=210,y=320)
        entryannee.place(x=210,y=360)

        submit = customtkinter.CTkButton(self.add_frame, text= " Submit " , command=insert)
        submit.place(x=580,y=400)


        # create third frame----------------------------------------------------------------------------------------------------------------
        self.edit_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        labelB = customtkinter.CTkLabel(self.edit_frame, text="Update", fg_color="transparent")
        labelB.place(x=50,y=50)

        labeltitle = customtkinter.CTkLabel(self.edit_frame, text="Titre du livre", fg_color="transparent")
        entrytitle = customtkinter.CTkEntry(self.edit_frame, placeholder_text="Titre", width=300)
        labelid = customtkinter.CTkLabel(self.edit_frame, text="ID du livre", fg_color="transparent")
        entryid = customtkinter.CTkEntry(self.edit_frame, placeholder_text="ID", width=300)



        labtitre = customtkinter.CTkLabel(self.edit_frame, text="Titre du livre :", fg_color="transparent")
        labcategorie = customtkinter.CTkLabel(self.edit_frame, text="Catégorie du livre:", fg_color="transparent")
        labauteur = customtkinter.CTkLabel(self.edit_frame, text="Auteur du livre:", fg_color="transparent")
        labdescription = customtkinter.CTkLabel(self.edit_frame, text="Description du livre:", fg_color="transparent")
        labrayon = customtkinter.CTkLabel(self.edit_frame, text="Rayon:", fg_color="transparent")
        labannee = customtkinter.CTkLabel(self.edit_frame, text="Année de publication:", fg_color="transparent")
        enttitre = customtkinter.CTkEntry(self.edit_frame, placeholder_text="Titre", width=500)
        entcategorie = customtkinter.CTkEntry(self.edit_frame, placeholder_text="Catégorie", width=500)
        entauteur = customtkinter.CTkEntry(self.edit_frame, placeholder_text="Auteur", width=500)
        entdescription = customtkinter.CTkTextbox(self.edit_frame, width=500, height=50, border_width=2)
        entannee = customtkinter.CTkEntry(self.edit_frame, placeholder_text="Annee de publication", width=500)
        entrayon = customtkinter.CTkEntry(self.edit_frame, placeholder_text="Rayon", width=500)

        labtitre.place(x=75, y=120)
        labcategorie.place(x=75, y=160)
        labauteur.place(x=75, y=200)
        labdescription.place(x=75, y=240)
        labannee.place(x=75, y=320)
        labrayon.place(x=75,y=280)
        enttitre.place(x=210,y=120)
        entcategorie.place(x=210,y=160)
        entauteur.place(x=210,y=200)
        entdescription.place(x=210,y=240)
        entrayon.place(x=210,y=280)
        entannee.place(x=210,y=320)
        labeltitle.place(x=50, y=50)
        entrytitle.place(x=130, y=50)
        labelid.place(x=450,y=50)
        entryid.place(x=520, y=50)
        
        def remplirchamps():
            check_id=entryid.get()
            check_entry=entrytitle.get()
            if(check_id=='' and check_entry=='' ):
                CTkMessagebox(title='Erreur',message="Aucun champ de recherche n'a été rempli!", icon="warning")
            else:
                conn=sqlite3.connect(db_path)
                cursor=conn.cursor()
                sql="SELECT * FROM LIVRE WHERE idlivre=? or titre=?"
                cursor.execute(sql,(check_id,check_entry))
                result=cursor.fetchone()

                enttitre.configure(state="normal")
                entcategorie.configure(state="normal")
                entauteur.configure(state="normal")
                entdescription.configure(state="normal")
                entannee.configure(state="normal")
                entrayon.configure(state="normal")

                enttitre.delete(0,END)
                entauteur.delete(0,END)
                entcategorie.delete(0,END)
                entdescription.delete(1.0,END)
                entannee.delete(0,END)
                entrytitre.delete(0,END)
                entrayon.delete(0,END)

                enttitre.insert(END,result[1])
                entcategorie.insert(END,result[2])
                entauteur.insert(END,result[3])
                entdescription.insert(END,result[4])
                entannee.insert(END, result[5])
                entrayon.insert(END,result[6])

                enttitre.configure(state="normal")
                entcategorie.configure(state="normal")
                entauteur.configure(state="normal")
                entdescription.configure(state="normal")
                entannee.configure(state="normal")
                entrayon.configure(state="normal")

                update.configure(state="normal")
                search.configure(state="disabled")
                entrytitle.configure(state="disabled")
                resetall.configure("normal")
                entryid.configure(state="disabled")


        def update_book():
            titre=entrytitle.get()
            id=entryid.get()
            titlevalue=enttitre.get()
            catvalue=entcategorie.get()
            autvalue=entauteur.get()
            descvalue=entdescription.get(1.0,END)
            anneevalue=entannee.get()
            rayon=entrayon.get()

            if(titlevalue=='' or catvalue=='' or autvalue=='' or descvalue=='' or anneevalue=='' or rayon==''):
                CTkMessagebox(title='Erreur',message="Un ou plusieurs champs sont vide!", icon="warning")
            else:
                
                sql="UPDATE LIVRE SET titre=?, categorie=?, auteur=?, description=?, annee_pub=?, rayon=? where titre=? or idlivre=?"
                conn=sqlite3.connect(db_path)
                cursor=conn.cursor()
                cursor.execute(sql, (titlevalue, catvalue, autvalue, descvalue, anneevalue, rayon, titre, id))
                conn.commit()
                cursor.close()
                conn.close()
                CTkMessagebox(title='Erreur',message="Update effectué!", icon="warning")
                resetfunc()

                
        def resetfunc():

            entrytitle.delete(0,END)
            entryid.delete(0,END)
            enttitre.delete(0,END)
            entauteur.delete(0,END)
            entcategorie.delete(0,END)
            entdescription.delete(1.0,END)
            entannee.delete(0,END)
            entrytitre.delete(0,END)
            entrayon.delete(0,END)

            update.configure(state="disabled")
            search.configure(state="normal")
            entrytitle.configure(state="normal")
            entryid.configure(state="normal")

            enttitre.configure(state="disabled")
            entcategorie.configure(state="disabled")
            entauteur.configure(state="disabled")
            entdescription.configure(state="disabled")
            entannee.configure(state="disabled")
            entrayon.configure(state="disabled")
            update.configure("disabled")
            search.configure("normal")
            resetall.configure("normal")



        update = customtkinter.CTkButton(self.edit_frame, text= "Update" , command=update_book)
        update.place(x=400,y=380)

        search = customtkinter.CTkButton(self.edit_frame, text= "Chercher" , command=remplirchamps)
        search.place(x=580,y=380)

        resetall = customtkinter.CTkButton(self.edit_frame, text= "Reset" , command=resetfunc)
        resetall.place(x=220,y=380)
    
        update.configure(state="disabled")
        search.configure(state="normal")
        enttitre.configure(state="disabled")
        entcategorie.configure(state="disabled")
        entauteur.configure(state="disabled")
        entdescription.configure(state="disabled")
        entannee.configure(state="disabled")     

        #create fourth frame----------------------------------------------------------------------------------------------------------------
        self.delete_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        labelD = customtkinter.CTkLabel(self.delete_frame, text="Delete", fg_color="transparent")
        labelD.place(x=50,y=50)

        label_delete_title = customtkinter.CTkLabel(self.delete_frame, text="Titre du livre", fg_color="transparent")
        entry_delete_title = customtkinter.CTkEntry(self.delete_frame, placeholder_text="Titre", width=300)
        label_delete_id = customtkinter.CTkLabel(self.delete_frame, text="ID du livre", fg_color="transparent")
        entry_delete_id = customtkinter.CTkEntry(self.delete_frame, placeholder_text="ID", width=300)


        label_delete_title.place(x=50, y=50)
        entry_delete_title.place(x=130, y=50)
        label_delete_id.place(x=450,y=50)
        entry_delete_id.place(x=520, y=50)

        def delete():
            name_delete = entry_delete_title.get()
            id_delete = entry_delete_id.get()
            conn=sqlite3.connect(db_path)
            cursor2=conn.cursor()
            sql2="DELETE FROM LIVRE WHERE idlivre=? or titre=?"
            cursor2.execute(sql2,(id_delete, name_delete))
            conn.commit()
            count=cursor2.rowcount
            cursor2.close()
            conn.close()
            if(count!=0):
                CTkMessagebox(title='Erreur',message="Supprimé", icon="warning")
            else:
                CTkMessagebox(title='Erreur',message="Aucun livre de ce nom/id", icon="warning")



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
        nom=f"{item}"
        elements=nom.split("|")
        id=elements[0].strip()
        print(id)
        print(f"label button frame clicked: {item}")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        #QUERY DE SELECT LIVRE

        sql="DELETE from LIVRE where idlivre='"+id+"'"
        cursor.execute(sql)
        sqlexemplaires="DELETE FROM EXEMPLAIRE WHERE idlivre='"+id+"'"
        cursor.execute(sqlexemplaires)
        conn.commit()
        conn.close()
        self.scrollable_label_button_frame.clean()
        ListerLivres()
        
def ListerLivres():
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        sql="SELECT * FROM LIVRE"
        cursor.execute(sql)
        result=cursor.fetchall()
        i=0
        for row in result:
            idlivre=result[i][0]
            titre=result[i][1]
            categorie=result[i][2]
            auteur=result[i][3]
            annee_pub=result[i][5]
            i=i+1
            app.scrollable_label_button_frame.add_item(f"{idlivre} | {titre} | {categorie} | {auteur} | {annee_pub}", image=app.book_image)
        conn.close()

if __name__ == "__main__":
    app = App()
    app.mainloop()

