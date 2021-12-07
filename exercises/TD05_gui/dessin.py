"""import tkinter as tk

racine = tk.Tk() # Création de la fenêtre racine
label1 = tk.Label(racine, text="Mon dessin", font = ("algerian", "30")) # création d'un widget
label2 = tk.Label(racine, text="Zoro",font = ("gigi", "30")) # création d'un widget
label1.grid(column=0, row=0, padx=50) # positionnement du premier widget
label2.grid(column=0, row=1, pady=100) # positionnement du premier widget
racine.mainloop() # Lancement de la boucle principale
"""
import tkinter as tk
import random

racine = tk.Tk() # Création de la fenêtre racine
racine.title("Mon dessin")

canvas = tk.Canvas(racine, width = 500, height = 500, bg = "white")
def choisir_une_couleur():
    
    def red():
        c = "red"
        return c
    def orange():
        c = "orange"
        return c
    def yellow():
        c = "yellow"
        return c
    def black():
        c = "blue"
        return c

    racinecolor = tk.Tk()
    racinecolor.title("Choisir une couleur")

    buttonred = tk.Button(racinecolor, bg="red", width= 10, height= 5, command= red)
    buttonorange = tk.Button(racinecolor, bg="orange", width= 10, height= 5, command=orange)
    buttonyellow = tk.Button(racinecolor, bg="yellow", width= 10, height= 5, command=yellow)
    buttonblack = tk.Button(racinecolor, bg="black", width= 10, height= 5, command= black)

    buttonred.grid(column= 0, row= 0, padx = 1, pady = 1)
    buttonorange.grid(column= 1, row= 0, padx = 1, pady = 1)
    buttonyellow.grid(column= 0, row= 1, padx = 1, pady = 1)
    buttonblack.grid(column= 1, row= 1, padx = 1, pady = 1)

    racinecolor.mainloop()
    
def cercle():
    x = random.randint(1,501)
    y = random.randint(1,501)
    size = random.randint(1,201)
    canvas.create_oval(x - size, y + size, x + size, y - size)
def croix():
    x = random.randint(1,501)
    y = random.randint(1,501)
    size = random.randint(1, 201)
    canvas.create_line(x + size, y - size, x - size, y + size)
    canvas.create_line(x - size, y - size, x + size, y + size)
def carré():
    x = random.randint(1,501)
    y = random.randint(1,501)
    size = random.randint(1, 201)
    canvas.create_rectangle(x + size, y - size, x - size, y + size)

button1 = tk.Button(text= "Choisir une couleur", font = ("gigi", "20"), command=choisir_une_couleur) # création d'un button
button2 = tk.Button(text= "Cercle", font = ("gigi", "20"), command=cercle)
button3 = tk.Button(text= "Carré", font = ("gigi", "20"), command=carré)
button4 = tk.Button(text= "Croix", font = ("gigi", "20"),command=croix)


# Fin du code 
button1.grid(column = 1, row = 0, padx = 10, pady = 10)
button2.grid(column = 0, row = 1, pady = 10)
button3.grid(column = 0, row = 2, pady = 10)
button4.grid(column = 0, row = 3, pady = 10)
canvas.grid(column = 1, row = 1, padx = 10, pady = 10, rowspan = 3)
racine.mainloop() # Lancement de la boucle principale