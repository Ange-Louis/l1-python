"""import tkinter as tk

racine = tk.Tk() # Création de la fenêtre racine
label1 = tk.Label(racine, text="Mon dessin", font = ("algerian", "30")) # création d'un widget
label2 = tk.Label(racine, text="Zoro",font = ("gigi", "30")) # création d'un widget
label1.grid(column=0, row=0, padx=50) # positionnement du premier widget
label2.grid(column=0, row=1, pady=100) # positionnement du premier widget
racine.mainloop() # Lancement de la boucle principale
"""
import tkinter as tk

racine = tk.Tk() # Création de la fenêtre racine
racine.title("Mon dessin")
button1 = tk.Button(text= "Choisir une couleur", font = ("gigi", "20")) # création d'un button
button2 = tk.Button(text= "Choisir une couleur", font = ("gigi", "20"))
button3 = tk.Button(text= "Choisir une couleur", font = ("gigi", "20"))
button4 = tk.Button(text= "Choisir une couleur", font = ("gigi", "20"))
canvas = tk.Canvas(racine, width = 500, height = 500, bg = "black")

# Fin du code 
button1.grid(column = 1, row = 0, padx = 10, pady = 10)
button2.grid(column = 0, row = 1, pady = 10)
button3.grid(column = 0, row = 2, pady = 10)
button4.grid(column = 0, row = 3, pady = 10)
canvas.grid(column = 1, row = 1, padx = 10, pady = 10, rowspan = 3)
racine.mainloop() # Lancement de la boucle principale