from customtkinter import *
import customtkinter
import sqlite3
import os
from PIL import Image
from CTkMessagebox import CTkMessagebox
import subprocess  
from tkinter import Tk, Canvas, Frame, BOTH 

current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(os.path.dirname(__file__), '..', '..', 'db', 'app.db')
main_path = os.path.join(os.path.dirname(__file__), '..', '..', 'main.pyw')


def callpage(script_path, user): 
    app.destroy()
    subprocess.call(["pythonw", script_path, user], bufsize=0)


customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

import sys
if len(sys.argv) > 1:
    valeur = sys.argv[1]
    print("Valeur reçue :", valeur)
else:
    valeur="Omar"

def chercher():
    app.scrollable_label_button_frame.clean()
    name=app.entry.get()
    print(name)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query="SELECT * FROM LIVRE WHERE TITRE='"+name+"'"
    cursor.execute(query)
    result=cursor.fetchone()
    print(result)
    num_rows = len(result)
    if(num_rows==0):
        CTkMessagebox(title='Erreur',message='Nom d\'utilisateur ou mot de passe inconnu!', icon="warning")
    else:
        titre=result[1]
        app.scrollable_label_button_frame.add_item(f"{titre}", image=app.book_image)


def ListerLivre():
    app.scrollable_label_button_frame.clean()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    sqlcount="SELECT TITRE from LIVRE"
    cursor.execute(sqlcount)
    result=cursor.fetchall()
    i=0
    for row in result:
        titre=result[i][0]
        i=i+1
        app.scrollable_label_button_frame.add_item(f"{titre}", image=app.book_image)


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
        button = customtkinter.CTkButton(self, text="Voir", width=100, height=24)
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
            for label, button in zip(self.label_list, self.button_list):
                    label.destroy()
                    button.destroy()
                    self.label_list.remove(label)
                    self.button_list.remove(button)

def reserver():
    print(1)


def gomain():
    callpage(main_path, "0")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Adherent")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text='Chercher', width=650)
        self.entry.place(x=250,y=20)

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text='Chercher', command=chercher)
        self.main_button_1.place(y=20,x=925)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Bienvenu, "+valeur+"!", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=ListerLivre, text='Lister les livres')
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.entry.focus_set, text='Chercher un livre')
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, command=gomain, text='Se deconnecter')
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.place(x=60,y=515)
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))


        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), r"..\..\pics")
        self.book_image= customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "open_book.png")), dark_image=Image.open(os.path.join(image_path, "open_book_dark.png")))

 
        # create scrollable label and button frame
        self.scrollable_label_button_frame = ScrollableLabelButtonFrame(master=self, width=800, height=500, command=self.label_button_frame_event, corner_radius=0)
        self.scrollable_label_button_frame.place(x=250,y=60)
        
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        sqlcount="SELECT TITRE from LIVRE"
        cursor.execute(sqlcount)
        result=cursor.fetchall()
        i=0
        for row in result:
            titre=result[i][0]
            i=i+1
            self.scrollable_label_button_frame.add_item(f"{titre}", image=self.book_image)
                
    def label_button_frame_event(self, item):
        nom=f"{item}"
        print(f"label button frame clicked: {item}")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        #QUERY DE SELECT LIVRE

        sql="SELECT * from LIVRE where titre='"+nom+"'"
        cursor.execute(sql)
        result=cursor.fetchone()
        print(result)

        #QUERY DE COUNT EXEMPLAIRE

        idliv=result[0]
        sqlexe="SELECT COUNT(*) FROM Exemplaire where idlivre="+str(idliv)
        cursor.execute(sqlexe)
        resultcount=cursor.fetchone()[0]
        print(resultcount)

        #QUERY DE DISPONIBILITE

        sqldispo="SELECT idlivre, disponibilite FROM Exemplaire where idlivre="+str(idliv)
        cursor.execute(sqldispo)
        resultdispo=cursor.fetchall()
        values=[value for _, value in resultdispo] #unzip result and keep values only
        print(values)
        fenetre2 = CTkToplevel(app)
        fenetre2.title("Details de livre")
        fenetre2.attributes("-topmost", True)
        fenetre2.geometry(f"{500}x{500}")
        exit_button = customtkinter.CTkButton(fenetre2,command=fenetre2.withdraw,text="Quitter")
        exit_button.place(x=300,y=450)
        #construction de la deuxième fenetre
        Frame(fenetre2,width=2, height=400, bg="black").place(x=100,y=0)
        Frame(fenetre2,width=500, height=2, bg="black").place(x=0,y=50)
        Frame(fenetre2,width=500, height=2, bg="black").place(x=0,y=100)
        Frame(fenetre2,width=500, height=2, bg="black").place(x=0,y=150)
        Frame(fenetre2,width=500, height=2, bg="black").place(x=0,y=250)
        Frame(fenetre2,width=500, height=2, bg="black").place(x=0,y=300)
        Frame(fenetre2,width=500, height=2, bg="black").place(x=0,y=350)
        Frame(fenetre2,width=500, height=2, bg="black").place(x=0,y=400)
        my_font = customtkinter.CTkFont(weight='bold')
        titretab=customtkinter.CTkLabel(fenetre2, text="Titre", font=my_font)
        cattab=customtkinter.CTkLabel(fenetre2, text="Catégorie", font=my_font)
        auteurtab=customtkinter.CTkLabel(fenetre2, text="Auteur", font=my_font)
        desctab=customtkinter.CTkLabel(fenetre2, text="Description", font=my_font)
        annee_pubtab=customtkinter.CTkLabel(fenetre2, text=f"Année de \npublication", font=my_font)
        dispotab=customtkinter.CTkLabel(fenetre2, text="Disponibilité", font=my_font)
        rayontab=customtkinter.CTkLabel(fenetre2, text="Rayon", font=my_font)

        titretab.place(x=15,y=15)
        cattab.place(x=15,y=65)
        auteurtab.place(x=15,y=115)
        desctab.place(x=15,y=190)
        annee_pubtab.place(x=15,y=265)
        dispotab.place(x=15,y=315)
        rayontab.place(x=15,y=365)


        #VALUES DE LA DEUXIEME FENETRE
        if 1 in values:
            dispo = customtkinter.CTkLabel(fenetre2, text="Disponible !")
            rayon = customtkinter.CTkLabel(fenetre2, text=str(result[6]))


        else:
            dispo = customtkinter.CTkLabel(fenetre2, text="Indisponible")
            rayon = customtkinter.CTkLabel(fenetre2, text="Indisponible")

        
        description = customtkinter.CTkTextbox(fenetre2, width=350, height=75, border_width=2)
            

        titre = customtkinter.CTkLabel(fenetre2, text=result[1])
        cat = customtkinter.CTkLabel(fenetre2, text=result[2])
        auteur = customtkinter.CTkLabel(fenetre2, text=result[3])
        description.insert(END,result[4])
        annee_pub = customtkinter.CTkLabel(fenetre2, text=str(result[5]))
        #placement de la deuxième fenetre


        titre.place(x=120, y=15)
        cat.place(x=120, y=65)
        auteur.place(x=120, y=115)
        description.place(x=120,y=165)
        annee_pub.place(x=120, y=265)
        dispo.place(x=120, y=315)
        rayon.place(x=120, y=365)
        
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