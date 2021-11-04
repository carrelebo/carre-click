from tkinter import *
import tkinter

#variables
hp_player1 = 200
hp_player2 = 200

damage = 1

#les fonctions

def damage_player1(event):
    global hp_player1
    global hp_player1_label
    hp_player1 = hp_player1 -1

    hp_player1_label.config(text=hp_player1)

    

def damage_player2(event):

    global hp_player2
    global hp_player2_label
    hp_player2 = hp_player2 -1
    hp_player2_label.config(text=hp_player2)

#paramétrage de la fenêtre "widows"
window = Tk()


window.geometry("1920x1080")
window.minsize(720,480)
window.maxsize(1920,1080)

window.title("Click")
window.config(bg="orange")

#les joueurs
player1 = Label(text="joueur1", font=("Arial",75), fg="white", bg='orange')
player2 = Label(text="joueur2", font=("Arial",75), fg='white', bg='orange')
player1.place(x=300, y=300)
player2.place(x=1300, y=300)

#information sur les joeurs
hp_player1_label = Label(font=("Arial",75))
hp_player1_label.config(text=hp_player1)

hp_player2_label = Label(font=("Arial",75))
hp_player2_label.config(text=hp_player2)

hp_player1_label.place(x=300,y=450)
hp_player2_label.place(x=1300,y=450)

#touches des joueurs
player1_keys = Label(text="touches = a", font=("Arial",25), fg="white", bg='orange')


player2_keys = Label(text="touches = m", font=("Arial",25), fg="white", bg='orange')

player1_keys.place(x=300,y=600)
player2_keys.place(x=1300,y=600)
#décoration
vs_label = Label(text="VS", font=("Arial", 200), fg="white", bg='orange')
vs_label.place(x=750,y=300)

#identification et condition des touches

window.bind('<a>', damage_player2)

window.bind('<m>', damage_player1)


#conditions





#fonction pour que la fenêtre ne se ferme pas
window.mainloop()
