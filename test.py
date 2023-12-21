import tkinter

# Création de la fenêtre
root = tkinter.Tk()

# Stockage
boutons = []
player1 = "X"
win = False

# Paramètres fenêtre
root.title("TicTacToe")
root.minsize(500, 500)

# Définition du joueur
def player():
    global player1
    if player1 == "X":
        player1 = "O"
    else:
        player1 = "X"

def victoire(clicked_row, clicked_column, count):
    # Victoire horizontale
    count = 0
    for i in range(3):
        current_bouton = boutons[i][clicked_row]
        if current_bouton["text"] == player1:
            count += 1
    if count == 3:
        winner()
    
    # Victoire verticale
    count = 0
    for i in range(3):
        current_bouton = boutons[clicked_column][i]
        if current_bouton["text"] == player1:
            count += 1
    if count == 3:
        winner()

    # Victoire diagonale sens 1
    count = 0
    for i in range(3):
        current_bouton = boutons[i][i]
        if current_bouton["text"] == player1:
            count += 1
    if count == 3:
        winner()

    # Victoire diagonale sens 2
    count = 0
    for i in range(3):
        current_bouton = boutons[2-i][i]
        if current_bouton["text"] == player1:
            count += 1
    if count == 3:
        winner()

    # Match nul
    count = 0
    for i in range(3):
        for j in range(3):
            current_bouton = boutons[j][i]
            if current_bouton["text"] == "X" or current_bouton["text"] == "O":
                count += 1
    if count == 9:
        print("Match nul !")
        rejouer()

def symbole(row, column, count2):
    clique_bouton = boutons[column][row]
    if clique_bouton["text"] == "":
        clique_bouton.config(text=player1)
    victoire(row, column, count2)
    player()

def grille(count2):
    for column in range(3):
        boutons_liste = []
        for row in range(3):
            bouton = tkinter.Button(root, font=("arial", 50), width=4, height=2, command=lambda r=row, c=column: symbole(r, c, count2))
            bouton.grid(row=row, column=column)
            boutons_liste.append(bouton)
        boutons.append(boutons_liste)

def winner():
    global win
    if win is False:
        win = True
        print(f"Le joueur {player1} a gagné le jeu !")
        rejouer()

def rejouer():
    choice = input("Souhaitez-vous rejouer ? (oui/non) : ")
    if choice.lower() == "oui":
        raz_jeu()
    else:
        quit()

def raz_jeu():
    global boutons, player1, win
    for column in range(3):
        for row in range(3):
            boutons[column][row].config(text="")
    player1 = "X"
    win = False

count2 = 0
grille(count2)
count2 += 1
root.mainloop()
