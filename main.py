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
    # optional arguments:
    parser.add_argument(
        '-p', '--parties', action='store_true', 
        help='Lister les identifiants de vos 20 dernières parties'
    )
    return parser.parse_args()


def main():
    args = analyser_commande()


def jouer_coup(a, q, partie):
  pass


if __name__ == "__main__":
  main()
