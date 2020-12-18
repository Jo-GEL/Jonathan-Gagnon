import argparse
import turtle

import api
from quoridor import Quoridor
from quoridorx import QuoridorX

def analyser_commande():
    """
    TP1
    """
    # Créer un analyseur de ligne de commande
    parser = argparse.ArgumentParser(description="Jeu Quoridor")
    # positional argument for the player's IDUL:
    parser.add_argument('IDUL', metavar='idul', help="IDUL du joueur")
    #Optional argument for auto-mode
    parser.add_argument('-a', dest="mode_auto", action='store_true', help='Activer le mode automatique')
    #Optional argument to activate graphic
    parser.add_argument('-x', dest="mode_graphique", action='store_true', help='Activer le mode graphique')
    #Optional argument to activate automatic graphic mode
    parser.add_argument('-ax', dest="mode_autographique", action='store_true', help='Activer le mode graphique')
    # optional arguments:
    parser.add_argument(
        '-p', '--parties', action='store_true', 
        help='Lister les identifiants de vos 20 dernières parties'
    )
    return parser.parse_args()


def main():
    args = analyser_commande()


def jouer_coup(a, q, partie):
 """
 Main Frame
"""
    #Mode automatic:
    if a.mode_auto:
        #on retourne un coup jouer de api.py
        return api.jouer_coup(id, q.type_coup.upper(), q.position)

    #initalise some variables
    cap = None
    title = "C'est à votre tour!"
    question = "Entrez votre prochain coup (D|MH|MV) (x, y):"

    #loop to determine how graphic mode functions
    while not cap:
        #as long as mode graphic is selected, we ask both questions
        if a.mode_graphique:
            #if nothing happens:
            if entry is None:
                #we pause the game
                turtle.mainloop()
                #raise an error to indicated a problem concerning window
                raise RuntimeError('Le joueur a fermer la fenêtre')
            #if something is entered
            else:
                print(question, end='')
                #the entry is manually entered
                entry = input()

            #we use the re module to separate the values
            #we use ^ to match the pattern at the start of the string
            #we use $ to match the end of the string
            #we use \s to match a single whitespace character like
            #we use \d to match decimal digit 0-9
            #we add them because (position, x, y)
            #we use IGNORECASE to match lower case values
            cap = re.search(r'(D|MH|MV)\s + (\d)\s + (\d)$', entry.split(), re.IGNORECASE)

            #if we enter something
            if cap:
                entry = cap.groups()


if __name__ == "__main__":
  main()
