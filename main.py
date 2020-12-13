# -*- coding: utf-8 -*-
"""Jeu Quoridor

Ce programme permet de joueur au jeu Quoridor.

Examples:

    `> python main.py --help`

        usage: main.py [-h] [-p] IDUL

        Quoridor - Phase 1

        positional arguments:
          IDUL          IDUL du joueur

        optional arguments:
          -h, --help    show this help message and exit
          -p, --parties Lister les identifiants de vos 20 dernières parties

    `> python3 main.py josmi42`

        Légende:
           1=josmi42, murs=||||||||||
           2=robot,   murs=||||||||||
           -----------------------------------
        9 | .   .   .   .   2   .   .   .   . |
          |                                   |
        8 | .   .   .   .   .   .   .   .   . |
          |                                   |
        7 | .   .   .   .   .   .   .   .   . |
          |                                   |
        6 | .   .   .   .   .   .   .   .   . |
          |                                   |
        5 | .   .   .   .   .   .   .   .   . |
          |                                   |
        4 | .   .   .   .   .   .   .   .   . |
          |                                   |
        3 | .   .   .   .   .   .   .   .   . |
          |                                   |
        2 | .   .   .   .   .   .   .   .   . |
          |                                   |
        1 | .   .   .   .   1   .   .   .   . |
        --|-----------------------------------
          | 1   2   3   4   5   6   7   8   9

        Type de coup disponible :
        - D : Déplacement
        - MH: Mur Horizontal
        - MV: Mur Vertical

        Choisissez votre type de coup (D, MH ou MV) : D
        Définissez la colonne de votre coup : 5
        Définissez la ligne de votre coup : 2
"""

import argparse
import re
import time
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
  pass

def jouer_coup(a, q, partie):
  pass
  

if __name__ == "__main__":
  main()