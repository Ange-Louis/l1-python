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
label = tk.Label(racine, text= "Mon Dessin", font = ("algerian", "30"), bg = "black", fg = "white") # création d'un widget
button1 = tk.Button(text= "Choisir une couleur", font = ("gigi", "20")) # création d'un button
canvas = tk.Canvas(racine, width = 500, height = 500, bg = "black")
label.grid(column=0, row=0, padx= "0cm") # positionnement du premier widget
button1.grid(column=1, row=1, pady= "0cm") # positionnement du premier widget
label.grid()
button1.grid()
racine.mainloop() # Lancement de la boucle principale