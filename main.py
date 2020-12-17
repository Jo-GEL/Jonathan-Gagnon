import argparse
import turtle

import api
from quoridor import Quoridor
from quoridorx import QuoridorX

def analyser_commande():

    parser = argparse.ArgumentParser(description = 'Jeu Quoridor')
    parser.add_argument('-p', 'lister', action='store_true', help='Lister les identifiants des 20 dernières parties')
    parser.add_agument('idul', help = 'IDUL du joueur')
    parser.add_argument("-a", dest="mode_auto", action="store_true", help="Jouer contre le serveur en mode automatique.")
    parser.add_argument('-x', dest="mode_graphique", action="store_true", help="Jouer contre le serveur en mode manuel avec affichage graphique.")
    parser.add_argument('-ax', dest="mode_graphique", action="store_true", help="Jouer contre le serveur en mode auto avec affichage graphique.")
    return parser.parse_args()


def main():
    args = analyser_commande()


def jouer_coup(a, q, partie):
  pass


if __name__ == "__main__":
  main()