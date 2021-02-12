import tkinter as tk
import tkinter.font as font

def ouvrir_accueil():
    """Ouvre la page accueil"""
    print("Ouverture d'accueil")


def ouvrir_collection():
    """Ouvre la page collection"""
    print("Ouverture de collection")


""" Création de la fenêtre principale de l'UI"""
window = tk.Tk()
window.title("Prototype d'interface")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window)

""" Création d'un "frame" pour contenir les boutons de navigations """
FR_buttons = tk.Frame(window, relief=tk.FLAT, bd=0, background="orange", width=450, height=50)
FR_buttons.pack(side="top", fill="x", expand=0)

""" Création d'un "Frame" pour contenir les images transmises, seulement une image statique actuellement mais plus tard 
aussi le flux de la caméra"""
FR_camera = tk.Frame(window, relief=tk.FLAT, bd=0, background="grey")
FR_camera.pack(side="bottom", fill="both", expand=1)

""" Création d'un "Label" qui contient la photo"""
image = tk.PhotoImage(file='./Images/fleur.png')
LB_Camera = tk.Label(FR_camera, image=image)
LB_Camera.pack()

""" Créations des boutons du menu supérieur, pas encore fonctionnel, le premier servira a aller sur la page accueil
et le deuxième à aller sur la page collection"""

fontBouton = font.Font(size=15)
BTN_open = tk.Button(FR_buttons, text="Accueil", command=ouvrir_accueil, bg="#5b5b5b", fg="#f87e28")
BTN_open['font'] = fontBouton
BTN_open.pack(side="left", fill="x", expand=1)

BTN_save = tk.Button(FR_buttons, text="Collection", command=ouvrir_collection, bg="#5b5b5b", fg="#f87e28")
BTN_save['font'] = fontBouton
BTN_save.pack(side="left", fill="x", expand=1)

window.mainloop()