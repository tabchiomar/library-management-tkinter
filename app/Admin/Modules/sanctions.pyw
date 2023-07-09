from customtkinter import *
import customtkinter
import sqlite3
import os
from PIL import Image
from CTkMessagebox import CTkMessagebox
import subprocess
import sys
from datetime import datetime

now = datetime.now()
db_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'db', 'app.db')
dash_path = os.path.join(os.path.dirname(__file__), '..', 'dashboard.pyw')

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
        button = customtkinter.CTkButton(self, text="Traiter", width=50, height=24, fg_color='green')
        if self.command is not None:
            button.configure(command=lambda: self.command(item))
        label.grid(row=len(self.label_list), column=0, pady=(0, 10), sticky="w")
        button.grid(row=len(self.button_list), column=1, pady=(0, 10), padx=5)
        self.label_list.append(label)
        self.button_list.append(button)

    def show_item(self, item, image=None):
        label = customtkinter.CTkLabel(self, text=item, image=image, compound="left", padx=5, anchor="w")
        label.grid(row=len(self.label_list), column=0, pady=(0, 10), sticky="w")
        self.label_list.append(label)


    def remove_item_nobutton(self, item):
        for label in self.label_list:
            if item == label.cget("text"):
                label.destroy()
                self.label_list.remove(label)
                return    

    def clean(self):
        for i in range(10):
                for label in self.label_list:
                    label.destroy()
                    self.label_list.remove(label)

    

def chercher():
    app.scrollable_label_button_frame.clean()
    search=app.entrylist.get()
    print(search)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query="SELECT * from sanction where iduser='"+str(search)+"'"
    cursor.execute(query)
    result=cursor.fetchone()
    print(result)
    idsanction=result[0]
    iduser=result[1]
    av1=result[2]
    av2=result[3]
    av3=result[4]
    sql1="SELECT username from users where id='"+str(iduser)+"'"
    cursor.execute(sql1)
    app.scrollable_label_button_frame.show_item(f"{idsanction} | User: {iduser} | AV1 : {av1} | AV2 : {av2} | AV3: {av3} | Username : {cursor.fetchone()[0]}", image=app.adherent_image)
    conn.close()

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gestion des sanctions - Administrateur système")
        self.geometry("1100x450")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


        #images navigation
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), r"..\..\..\pics")
        self.delete_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "delete_light.png")), dark_image=Image.open(os.path.join(image_path, "delete_dark.png")), size=(20, 20))
        self.hammer_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "hammer.png")), dark_image=Image.open(os.path.join(image_path, "hammer_dark.png")), size=(20, 20))
        self.edit_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "edit_light.png")), dark_image=Image.open(os.path.join(image_path, "edit_dark.png")), size=(20, 20))
        self.add_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_light.png")), dark_image=Image.open(os.path.join(image_path, "add_dark.png")), size=(20, 20))
        self.list_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "list_light.png")), dark_image=Image.open(os.path.join(image_path, "list_dark.png")), size=(20, 20))
        self.dashboard_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "dashboard.png")), dark_image=Image.open(os.path.join(image_path, "dashboard_dark.png")), size=(30, 30))
        self.book_image= customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "open_book.png")), dark_image=Image.open(os.path.join(image_path, "open_book_dark.png")))
        self.adherent_image= customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "user.png")), dark_image=Image.open(os.path.join(image_path, "user_dark.png")))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Gestion de sanctions", 
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.list_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Lister", image=self.list_image,
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    anchor="w", command=self.list_button_event)
        self.list_button.grid(row=1, column=0, sticky="ew")

        # self.add_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Ajouter", image=self.add_image,
        #                                               fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
        #                                                anchor="w", command=self.add_button_event)
        # self.add_button.grid(row=2, column=0, sticky="ew")

        # self.edit_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Revoir une sanction", image=self.edit_image,
        #                                                fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
        #                                                 anchor="w", command=self.edit_button_event)
        # self.edit_button.grid(row=3, column=0, sticky="ew")

        self.archive_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Gerer les sanctions", image=self.hammer_image,
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       anchor="w", command=self.archive_button_event)
        self.archive_button.grid(row=2, column=0, sticky="ew")

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
        self.archive_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("list")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.list_button.configure(fg_color=("gray75", "gray25") if name == "list" else "transparent")
        # self.add_button.configure(fg_color=("gray75", "gray25") if name == "add" else "transparent")
        #self.edit_button.configure(fg_color=("gray75", "gray25") if name == "edit" else "transparent")
        self.archive_button.configure(fg_color=("gray75", "gray25") if name == "archive" else "transparent")
    

        #LIST FRAME----------------------------------------------------------------------------------------------------------------
        self.list_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.entrylist = customtkinter.CTkEntry(self, placeholder_text='Chercher par ID user', width=650)
        self.entrylist.place(x=250,y=20)

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text='Chercher', command=chercher)
        self.main_button_1.place(y=20,x=925)

        self.scrollable_label_button_frame = ScrollableLabelButtonFrame(master=self, width=800, height=360, corner_radius=0)
        self.scrollable_label_button_frame.place(x=250,y=60)
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        sql="SELECT * from sanction"
        cursor.execute(sql)
        result=cursor.fetchall()
        i=0
        for row in result:
            idsanction=result[i][0]
            iduser=result[i][1]
            av1=result[i][2]
            av2=result[i][3]
            av3=result[i][4]
            sql1="SELECT username from users where id='"+str(iduser)+"'"
            cursor.execute(sql1)
            username=cursor.fetchone()[0]
            i=i+1
            self.scrollable_label_button_frame.show_item(f"{idsanction} | User: {iduser} | AV1 : {av1} | AV2 : {av2} | AV3: {av3} | Username : {username}", image=self.adherent_image)

        cursor.close()
        conn.close()

        

        #create fourth frame----------------------------------------------------------------------------------------------------------------
 


        def show_user():
                username=entryusername.get()
                print(username) 
                try:
                    sql="SELECT id FROM USERS WHERE username='"+username+"' and rank='Adherent'"
                    conn = sqlite3.connect(db_path)
                    cursor = conn.cursor()
                    cursor.execute(sql)
                    iduser=str(cursor.fetchone()[0])
                    print(iduser)
                    entryusername.configure(state="disabled")

                except:
                    CTkMessagebox(title='Erreur',message='Username inexistant', icon="warning")

                sql2="SELECT * FROM SANCTION WHERE IDUSER = ?"
                cursor.execute(sql2, (iduser,))
                result=cursor.fetchone()
                av1=result[2]
                av2=result[3]
                av3=result[4]
                labelusername = customtkinter.CTkLabel(self.archive_frame, text="Username de l'utilisateur :"+username, fg_color="transparent")
                labelsanctions = customtkinter.CTkLabel(self.archive_frame, text=f"Avertissement 1 : {av1} | Avertissement 2 : {av2} | Avertissement 3 : {av3}", fg_color="transparent")
                labelusername.place(x=350,y=150)
                labelsanctions.place(x=220,y=170)
                avert = customtkinter.CTkButton(self.archive_frame, text= "Avertir" , width=200, command=lambda: avert_user(iduser))
                ban = customtkinter.CTkButton(self.archive_frame, text= "Bannir" ,width=200, command=lambda: ban_user(iduser))
                retirerave = customtkinter.CTkButton(self.archive_frame, text= "Retirer avertissement" ,width=200, command=lambda: retirerav_user(iduser))
                cleanav = customtkinter.CTkButton(self.archive_frame, text= "Retirer tout les avertissements" ,width=200, command=lambda: cleanav_user(iduser))
                reset= customtkinter.CTkButton(self.archive_frame, text= "Reset" ,width=200, command=reseta)
                avert.place(x=200,y=200)
                ban.place(x=450,y=200)
                retirerave.place(x=200,y=250)
                cleanav.place(x=450, y=250)
                reset.place(x=325,y=300)

        def avert_user(id):
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            sql5="SELECT * FROM SANCTION WHERE iduser='"+str(id)+"'"
            cursor.execute(sql5)
            result=cursor.fetchone()
            if(result[2]!='0' and result[3]!='0' and result[4]!='0'):
                ban_user(result[1])
                print('banned')
            elif(result[2]=='0'):
                sql="UPDATE SANCTION SET av1='"+now.strftime("%d/%m/%Y")+"' where iduser='"+str(id)+"'"
                cursor.execute(sql)
                CTkMessagebox(title='Erreur',message="Utilisateur Averti (1er avertissement)!", icon="warning")
            elif(result[2]!='0' and result[3]=='0'):
                sql2="UPDATE SANCTION SET av2='"+now.strftime("%d/%m/%Y")+"' where iduser='"+str(id)+"'"
                cursor.execute(sql2)
                CTkMessagebox(title='Erreur',message="Utilisateur Averti (2eme avertissement)!", icon="warning")
            else:
                sql3="UPDATE SANCTION SET av3='"+now.strftime("%d/%m/%Y")+"' where iduser='"+str(id)+"'"
                cursor.execute(sql3)
                CTkMessagebox(title='Erreur',message="Utilisateur Averti (3eme avertissement)!", icon="warning")
            conn.commit()
            self.select_frame_by_name("list")
            conn.close()
        def reseta():
            self.select_frame_by_name("archive")

                
        def ban_user(id):
            print(id)
            sql="DELETE FROM USERS WHERE id='"+str(id)+"'"
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute(sql)
            sql2="DELETE FROM SANCTION WHERE iduser='"+str(id)+"'"
            conn.execute(sql2)
            CTkMessagebox(title='Erreur',message="Utilisateur Banni!", icon="warning")
            conn.commit()
            self.select_frame_by_name("list")
            conn.close()

        def retirerav_user(id):
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            sql5="SELECT * FROM SANCTION WHERE iduser='"+str(id)+"'"
            cursor.execute(sql5)
            result=cursor.fetchone()
            if(result[2]!='0'):
                sql2="UPDATE SANCTION SET av1='0' WHERE iduser='"+str(id)+"'"
                cursor.execute(sql2)
                CTkMessagebox(title='Erreur',message="Premier avertissement retiré", icon="warning")

            elif(result[3]!='0'):
                sql2="UPDATE SANCTION SET av2='0' WHERE iduser='"+str(id)+"'"
                cursor.execute(sql2)
                CTkMessagebox(title='Erreur',message="Deuxième avertissement retiré!", icon="warning")

            elif(result[4]!='0'):
                sql2="UPDATE SANCTION SET av3='0' WHERE iduser='"+str(id)+"'"
                cursor.execute(sql2)
                CTkMessagebox(title='Erreur',message="Troisième avertissement retiré", icon="warning")

            else:
                CTkMessagebox(title='Erreur',message="Aucun avertissement à retirer!", icon="warning")
            cursor.close()
            conn.commit()
            self.select_frame_by_name("list")
            conn.close()

        def cleanav_user(id):   
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            sql="UPDATE SANCTION SET av1='0', av2='0', av3='0' WHERE iduser='"+str(id)+"'"
            cursor.execute(sql)
            cursor.close()
            conn.commit()
            CTkMessagebox(title='Erreur',message="Avertissements remis à zero", icon="warning")
            self.select_frame_by_name("list")
            conn.close()

        self.archive_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        labelusername = customtkinter.CTkLabel(self.archive_frame, text="Username de l'utilisateur", fg_color="transparent")
        entryusername = customtkinter.CTkEntry(self.archive_frame, placeholder_text="Username", width=300)

        labelusername.place(x=200, y=50)
        entryusername.place(x=345, y=50)

        add = customtkinter.CTkButton(self.archive_frame, text= "Afficher utilisateur" , command=show_user)

        add.place(x=345, y=100)


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

        if name == "archive":
            self.archive_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.archive_frame.grid_forget()

    def list_button_event(self):
        self.select_frame_by_name("list")

    def add_button_event(self):
        self.select_frame_by_name("add")

    def edit_button_event(self):
        self.select_frame_by_name("edit")

    def archive_button_event(self):
        self.select_frame_by_name("archive")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
    
def ListerSanction():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    sql="SELECT * FROM sanction"
    cursor.execute(sql)
    result=cursor.fetchall()
    i=0
    for row in result:
            idsanction=result[i][0]
            iduser=result[i][1]
            av1=result[i][2]
            av2=result[i][3]
            av3=result[i][4]
            sql1="SELECT username from users where id='"+str(iduser)+"'"
            cursor.execute(sql1)
            username=cursor.fetchone()[0]
            i=i+1
            app.scrollable_label_button_frame.show_item(f"{idsanction} | User: {iduser} | AV1 : {av1} | AV2 : {av2} | AV3: {av3} | Username : {username}", image=app.adherent_image)


    cursor.close()



    

if __name__ == "__main__":
    app = App()
    app.protocol("WM_DELETE_WINDOW", app.quit)  # Properly closes the Tk window
    app.mainloop()

