import tkinter as tk
import tkinter.font as font


# Fenêtre principale
window = tk.Tk()
window.title("Collection")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

# Menu
menu = tk.Frame(window, relief=tk.FLAT, bd=0, background="orange", width=450, height=50)
menu.pack(side="top", fill="x", expand=0)
# Bouton accueil
bt_accueil = tk.Button(menu, text="Accueil", command="", bg="#5b5b5b", fg="#f87e28")
bt_accueil['font'] = font.Font(size=15)
bt_accueil.pack(side="left", fill="x", expand=1)
# Bouton collection
bt_collection = tk.Button(menu, text="Collection", command="", bg="#5b5b5b", fg="#f87e28")
bt_collection['font'] = font.Font(size=15)
bt_collection.pack(side="left", fill="x", expand=1)

# Page
page = tk.Frame(window, relief=tk.FLAT, bd=0, background="grey")
page.pack(side="bottom", fill="both", expand=1)

# Image
image = tk.PhotoImage(file='./image/fleur.png')
LB_image = tk.Label(page, image=image)
LB_image.pack()

window.mainloop()