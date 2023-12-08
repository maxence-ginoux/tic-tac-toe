import tkinter

# création de la fenêtre
root = tkinter.Tk()

#stockage
boutons = []
player1 = "X"
win = False

# paramètres fenêtre
root.title("TicTacToe")
root.minsize(500, 500)

def player():
    global player1
    if player1 == "X":
        player1 = "O"
    else:
        player1 = "X"

def winner():
    global win
    if win is False:
        win = True
        print(f"Le joueur {player1} à gagné le jeu !")

#def match_nul():
#    print("MATCH NUL !")

def victoire(clicked_row, clicked_column):

    # victoire horizontale
    count = 0
    for i in range(3):
        current_bouton = boutons[i][clicked_row]
        if current_bouton["text"] == player1:
            count += 1
    if count == 3:
        winner()

    # victoire verticale
    count = 0
    for i in range(3):
        current_bouton = boutons[clicked_column][i]
        if current_bouton["text"] == player1:
            count += 1
    if count == 3:
        winner()

    # victoire diagonale sens 1
    count = 0
    for i in range(3):
        current_bouton = boutons[i][i]
        if current_bouton["text"] == player1:
            count += 1
    if count == 3:
        winner()

    # victoire diagonale sens 2
    count = 0
    for i in range(3):
        current_bouton = boutons[2-i][i]
        if current_bouton["text"] == player1:
            count += 1
    if count == 3:
        winner()

    # match nul
    if win is False:
        count = 0
        for column in range (3):
            for row in range(3):
                current_bouton = boutons[column][row]
            if current_bouton["text"] == "X" or current_bouton == "O":
                count += 1
                #print(count)
        if count == 9:
            print("MATCH NUL !")

def symbole(row, column):
    clique_bouton = boutons[column][row]
    if clique_bouton["text"] == "":
        clique_bouton.config(text=player1)

    victoire(row, column)
    player()

#grille
def grille():
    for column in range (3):
        boutons_liste = []
        for row in range (3):
            bouton = tkinter.Button(root, font=("arial", 50), width=4, height=2, command=lambda r=row, c=column: symbole(r, c))
            bouton.grid(row=row, column=column)
            boutons_liste.append(bouton)
        boutons.append(boutons_liste)


grille()
root.mainloop()
