from tkinter import *
import tkinter.messagebox
import customtkinter
import subprocess
import sqlite3
from datetime import datetime
now = datetime.now()
import os
from PIL import Image
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


current_dir = os.path.dirname(os.path.abspath(__file__))
main_path = os.path.join(os.path.dirname(__file__), '..', '..', 'main.pyw')
db_path = os.path.join(os.path.dirname(__file__), '..', '..', 'db', 'app.db')
adh_path = os.path.join(os.path.dirname(__file__), 'Modules', 'adherents.pyw')
exem_path = os.path.join(os.path.dirname(__file__), 'Modules', 'exemplaires.pyw')
livres_path = os.path.join(os.path.dirname(__file__), 'Modules', 'livres.pyw')
prets_path = os.path.join(os.path.dirname(__file__), 'Modules', 'prets.pyw')
sanctions_path = os.path.join(os.path.dirname(__file__), 'Modules', 'sanctions.pyw')
support_path = os.path.join(os.path.dirname(__file__), 'Modules', 'support.pyw')
biblio_path = os.path.join(os.path.dirname(__file__), 'Modules', 'biblio.pyw')




customtkinter.set_appearance_mode("light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
import sys
if len(sys.argv) > 1:
    valeur = sys.argv[1]
    print("Valeur reçue :", valeur)
else:
    valeur="admin"




def callpage(script_path, user): 
    plt.close('all')
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

def gobiblio():
    callpage(biblio_path,str(valeur))

    

def create_plot(num_loaned, num_not_loaned, titre1, titre2, titrecomplet):
        fig = Figure(figsize=(3, 2), dpi=85, facecolor='none')
        ax = fig.add_subplot(111)
        labels = [titre1, titre2]
        values = [num_loaned, num_not_loaned]
        ax.pie(values, labels=labels, autopct='%1.1f%%')
        ax.set_title(titrecomplet)
        return fig

def create_plot_num(listcat, nbliv, titrecomplet):
        fig = Figure(figsize=(3, 2), dpi=85, facecolor='none')
        ax = fig.add_subplot(111)
        labels = listcat
        values = nbliv
        ax.pie(values, labels=labels, autopct='%1.1f%%')
        ax.set_title(titrecomplet)
        return fig

def create_line_chart(mois, nbr_adherent_parmois):
    fig3 = plt.figure(figsize=(10, 3.5), dpi=80)
    plt.plot(mois, nbr_adherent_parmois, marker='o', linestyle='-', color='b')
    plt.title('Nombre d\'adhérents par mois')
    plt.xlabel('Mois')
    plt.ylabel('Nombre d\'adhérents')
    return fig3

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Administrateur système")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(12, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Bienvenu, "+valeur, font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=golivre, text='Gestion de livres')
        self.sidebar_button_1.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=goadherents, text="Gestion d'adherents")
        self.sidebar_button_2.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=goprets, text='Gestion de prêts')
        self.sidebar_button_3.grid(row=4, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, command=goresa, text='Gestion de support')
        self.sidebar_button_4.grid(row=5, column=0, padx=20, pady=10)
        self.sidebar_button_5 = customtkinter.CTkButton(self.sidebar_frame, command=gosanctions, text='Gestion de sanctions')
        self.sidebar_button_5.grid(row=6, column=0, padx=20, pady=10)
        self.sidebar_button_5 = customtkinter.CTkButton(self.sidebar_frame, command=goexe, text="Gestion d'exemplaires")
        self.sidebar_button_5.grid(row=7, column=0, padx=20, pady=10)
        self.sidebar_button_5 = customtkinter.CTkButton(self.sidebar_frame, command=gobiblio, text="Gestion de bibliothécaires")
        self.sidebar_button_5.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_6 = customtkinter.CTkButton(self.sidebar_frame, command=gomain, text='Se deconnecter')
        self.sidebar_button_6.grid(row=8, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=10, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Dark", "Light", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=11, column=0, padx=20, pady=(10, 10))
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), r"..\..\pics")
        self.librarian_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "librarian.png")), size=(300,500))



        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        sqlexemplaire_indispo="SELECT count(*) from exemplaire where disponibilite=0"
        sqlexemplaire_dispo="SELECT count(*) from exemplaire where disponibilite=1"
        sqladherent="SELECT count(*) from users where rank='Adherent'"
        sqlbiblio="SELECT count(*) from users where rank='bibliothecaire'"
        sqladh_parmois="""SELECT COUNT(adherent.idadherent) AS nombre_adherents
                        FROM (
                            SELECT '01' AS mois UNION ALL SELECT '02' AS mois UNION ALL SELECT '03' AS mois UNION ALL
                            SELECT '04' AS mois UNION ALL SELECT '05' AS mois UNION ALL SELECT '06' AS mois UNION ALL
                            SELECT '07' AS mois UNION ALL SELECT '08' AS mois UNION ALL SELECT '09' AS mois UNION ALL
                            SELECT '10' AS mois UNION ALL SELECT '11' AS mois UNION ALL SELECT '12' AS mois
                        ) AS mois
                        LEFT JOIN ADHERENT ON SUBSTR(ADHERENT.datead, 4, 2) = mois.mois
                        GROUP BY mois.mois
                        """
        mois = ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Juin', 'Juil', 'Août', 'Sep', 'Oct', 'Nov', 'Déc']

        conn=sqlite3.connect(db_path)
        cursor=conn.cursor()
        cursor.execute(sqladh_parmois)
        nbr_adherent_parmois=[element for tuple in cursor.fetchall() for element in tuple]
        print(nbr_adherent_parmois)


        cursor.execute(sqlexemplaire_dispo)
        nbr_dispo=cursor.fetchone()[0]
        cursor.execute(sqlexemplaire_indispo)
        nbr_indispo=cursor.fetchone()[0]
        cursor.execute(sqladherent)
        nbr_adherent=cursor.fetchone()[0]
        cursor.execute(sqlbiblio)
        nbr_biblio=cursor.fetchone()[0]
        

        date = customtkinter.CTkLabel(self, text="Aujourd'hui est le : "+now.strftime("%d/%m/%Y")+"\nIl est : "+now.strftime("%H:%M"), fg_color="transparent")
        date.place(x=550,y=30)

        fig = create_plot(nbr_dispo, nbr_indispo, 'Non prétés', 'Prétés', 'Statue des exemplaires')
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().place(x=250,y=100)


        fig2 = create_plot(nbr_adherent, nbr_biblio, 'Adherents', 'Bibliothécaires', 'Etat des users')
        canvas2 = FigureCanvasTkAgg(fig2, master=self)
        canvas2.draw()
        canvas2.get_tk_widget().place(x=520,y=100)


        sqlcat="select categorie from livre group by categorie"
        cursor.execute(sqlcat)
        res_cat=[element for tuple in cursor.fetchall() for element in tuple]
        print(res_cat)

        sqlnum_cat="select count(*) from livre group by categorie"
        cursor.execute(sqlnum_cat)
        res_num_cat=[element for tuple in cursor.fetchall() for element in tuple]

        fig4 = create_plot_num(res_cat, res_num_cat, 'Nombre de livre par catégorie')
        canvas4 = FigureCanvasTkAgg(fig4, master=self)
        canvas4.draw()
        canvas4.get_tk_widget().place(x=792,y=100)




        fig3=create_line_chart(mois, nbr_adherent_parmois)
        canvas3=FigureCanvasTkAgg(fig3, master=self)
        canvas3.draw()
        canvas3.get_tk_widget().place(x=250,y=280)

        cursor.close()
        conn.close()



        # set default values
        self.appearance_mode_optionemenu.set("Light")

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
    app.protocol("WM_DELETE_WINDOW", app.quit)  # Properly closes the Tk window
    app.mainloop()
    
    # Properly closes the matplotlib figures
    plt.close('all')

    