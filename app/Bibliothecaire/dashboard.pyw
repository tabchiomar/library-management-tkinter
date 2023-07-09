from tkinter import *
import tkinter.messagebox
import customtkinter
import subprocess
import sqlite3
from datetime import datetime
now = datetime.now()
import customtkinter
import os
from PIL import Image
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
main_path = os.path.join(os.path.dirname(__file__), '..', '..', 'main.pyw')
db_path = os.path.join(os.path.dirname(__file__), '..', '..', 'db', 'app.db')
adh_path = os.path.join(os.path.dirname(__file__), 'Modules', 'adherents.pyw')
exem_path = os.path.join(os.path.dirname(__file__), 'Modules', 'exemplaires.pyw')
livres_path = os.path.join(os.path.dirname(__file__), 'Modules', 'livres.pyw')
prets_path = os.path.join(os.path.dirname(__file__), 'Modules', 'prets.pyw')
sanctions_path = os.path.join(os.path.dirname(__file__), 'Modules', 'sanctions.pyw')
support_path = os.path.join(os.path.dirname(__file__), 'Modules', 'support.pyw')



customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
import sys
if len(sys.argv) > 1:
    valeur = sys.argv[1]
    print("Valeur reçue :", valeur)
else:
    valeur="omar"

def callpage(script_path, user): 
    app.destroy()
    subprocess.call(["pythonw", script_path, user], bufsize=0)

def gomain():
    callpage(main_path, "0")

def golivre():
    callpage(livres_path, str(valeur))

def goadherents():
    callpage(adh_path,str(valeur))

def goprets():
    callpage(prets_path,str(valeur))

def goresa():
    callpage(support_path,str(valeur))

def goexe():
    callpage(exem_path ,str(valeur))

def gosanctions():
    callpage(sanctions_path,str(valeur))


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Bibliothécaire")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(11, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Bienvenu, "+valeur, font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=golivre, text='Gestion de livres')
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=goadherents, text="Gestion d'adherents")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=goprets, text='Gestion de prêts')
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, command=goresa, text='Gestion de support')
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        self.sidebar_button_5 = customtkinter.CTkButton(self.sidebar_frame, command=gosanctions, text='Gestion de sanctions')
        self.sidebar_button_5.grid(row=5, column=0, padx=20, pady=10)
        self.sidebar_button_5 = customtkinter.CTkButton(self.sidebar_frame, command=goexe, text="Gestion d'exemplaires")
        self.sidebar_button_5.grid(row=6, column=0, padx=20, pady=10)
        self.sidebar_button_6 = customtkinter.CTkButton(self.sidebar_frame, command=gomain, text='Se deconnecter')
        self.sidebar_button_6.grid(row=7, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=9, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Dark", "Light", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=10, column=0, padx=20, pady=(10, 10))
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), r"..\..\pics")
        self.librarian_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "librarian.png")), size=(300,500))



  



        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        date = customtkinter.CTkLabel(self, text="Aujourd'hui est le : "+now.strftime("%d/%m/%Y")+"\nIl est : "+now.strftime("%H:%M"), fg_color="transparent")
        date.place(x=550,y=30)

        sqlcontact="SELECT count(*) from contact where etat=0"
        cursor.execute(sqlcontact)
        contact=cursor.fetchone()[0]


        self.list_frame = customtkinter.CTkFrame(self)
        self.list_frame.place(x=700,y=80)
        self.info_frame = customtkinter.CTkFrame(self)
        self.info_frame.place(x=700,y=320)
        labeltache=customtkinter.CTkLabel(self.list_frame, text="Les taches à effectuer aujourd'hui :", fg_color="transparent")
        labeltache.grid(row=0, column=2, sticky="")
        labelcontact=customtkinter.CTkLabel(self.list_frame, text=f"* Vous avez {contact} demande(s) de support à traiter!", fg_color="transparent")
        labelcontact.grid(row=1, column=2, sticky="")
        today=now.strftime("%d/%m/%Y")
        sqlpret="SELECT username, titre from pret p , users u, livre l where p.idadherent=u.id and p.idlivre=l.idlivre and etat=0 and dateretour='"+today+"'"
        cursor.execute(sqlpret)
        retourpret=cursor.fetchall()
        nbr=len(retourpret)
        labelpret=customtkinter.CTkLabel(self.list_frame, text=f" * {nbr} retours de prêts sont prévus pour aujourd'hui :" , fg_color="transparent" )
        textbox = customtkinter.CTkTextbox(self.list_frame, width=350, height=100,  fg_color="transparent", cursor='left_ptr')
        i=0
        for tuple in retourpret:
            textbox.insert("0.0", f"* {retourpret[i][0]} est supposé retourner un exemplaire de {retourpret[i][1]}\n") 
            i=i+1 

        textbox.configure(state="disabled")  
        textbox.grid(row=3, column=2,  sticky="")
        labelpret.grid(row=2, column=2, sticky="")
        labelsanction=customtkinter.CTkLabel(self.list_frame, text="Oubliez pas de sanctionner les retardataires! \n Good luck!" , fg_color="transparent" )
        labelsanction.grid(row=4, column=2,  sticky="")


        labelinfo=customtkinter.CTkLabel(self.info_frame, text="Vos informations:\n\n", fg_color="transparent")
        labelinfo.grid(row=0, column=2, sticky="")
        sqlbiblio="SELECT id from users where username='"+valeur+"'"
        cursor.execute(sqlbiblio)
        idbiblio=cursor.fetchone()[0]
        sqlinfo="SELECT * FROM BIBLIO where iduser='"+str(idbiblio)+"'"
        cursor.execute(sqlinfo)
        result=cursor.fetchone()
        id=result[0]
        cin=result[1]
        nom=result[2]
        prenom=result[4]
        email=result[5]
        datenaissance=result[6]

        labelinfos=customtkinter.CTkLabel(self.info_frame, text=f"Mr/Mme {prenom} {nom} \n\n Votre mail est : {email} \n\n Votre ID est le {id} \n Votre CIN est : {cin} \n\n Vous êtes né(e) le {datenaissance} \n\n Si une information est incorrecte, contactez l'administrateur\n systeme.", fg_color="transparent")
        labelinfos.grid(row=1,column=2, sticky="")
        self.librarianimage = customtkinter.CTkLabel(self, text="", image=self.librarian_image)
        self.librarianimage.place(x=280,y=50)



        # set default values
        self.appearance_mode_optionemenu.set("Dark")

        self.frame_left = customtkinter.CTkFrame(master=self,
                                             width=200,
                                             corner_radius=0)



    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def sidebar_button_event(self):
        print("sidebar_button click")


if __name__ == "__main__":
    app = App()
    app.mainloop()