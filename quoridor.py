import networkx as nx

class Quoridor:
    def __init__(self, joueurs, murs=None):
        if isinstance(joueurs[0], str):
            self.joueur1 = {'nom' : joueurs[0], 'murs' : 10, 'pos' : (5, 1)}
            self.joueur2 = {'nom' : joueurs[1], 'murs' : 10, 'pos' : (5, 9)}
        
        elif isinstance(joueurs[0], dict):
            self.joueur1 = {'nom' : joueurs[0]['nom'], 'murs' : joueurs[0]['murs'], 'pos' : joueurs[0]['pos']}
            self.joueur2 = {'nom' : joueurs[1]['nom'], 'murs' : joueurs[1]['murs'], 'pos' : joueurs[1]['pos']}
        
        if not isinstance(joueurs, list):
            raise QuoridorError("L'argument 'joueurs' n'est pas itérable.")

        if len(joueurs) != 2:
            raise QuoridorError("L'itérable de joueurs en contient un nombre différent de deux.")

        nb_murs = 0
        if murs is not None:
            if not isinstance(murs, dict):
                raise QuoridorError("L'argument 'murs' n'est pas un dictionnaire lorsque présent.")
            self.verticaux = murs['verticaux']
            self.horizontaux = murs['horizontaux']
        else:
            self.verticaux = []
            self.horizontaux = []

        if murs is not None:
            nb_murs += len(self.verticaux) + len(self.horizontaux)
        
        if nb_murs != 20:
            raise QuoridorError("Le total des murs placés et plaçables n'est pas égal à 20.")

        if self.joueur1['murs'] < 0 or self.joueur1['murs'] > 10:
            raise QuoridorError("Le nombre de murs qu'un joueur peut placer est plus grand que 10,ou négatif")
        if self.joueur2['murs'] < 0 or self.joueur2['murs'] > 10:
            raise QuoridorError("Le nombre de murs qu'un joueur peut placer est plus grand que 10,ou négatif")

        if not 1 <= self.joueur1['pos'][0] <= 9 or not 1 <= self.joueur1['pos'][1] <= 9:
            raise QuoridorError("La position d'un joueur est invalide.")

        if not 1 <= self.joueur2['pos'][0] <= 9 or not 1 <= self.joueur2['pos'][1] <= 9:
            raise QuoridorError("La position d'un joueur est invalide.")

        if self.joueur1['murs'] < 0 or self.joueur1['murs'] > 10:
            raise QuoridorError("La position du mur est invalide.")

        if self.joueur2['murs'] < 0 or self.joueur2['murs'] > 1:
            raise QuoridorError("La position du mur est invalide.")



    def __str__(self):
        patron = 3 * [' '] + 35 * ['-'] + [' \n']
        for i in range(9, 0, -1):
            patron += str(i) + ' | ' + 8 * '.   ' + '. |'
            if i != 1:
                patron += '\n  |' + 34 * ' ' + ' |\n'
        patron += '\n--|' + 35 * '-' + '\n  | '

        for i in range(1, 10):
            patron += str(i) + '   '

        for i in self.horizontaux:
            for j in range(7):
                patron[42 + (19 - i[1] * 2) * 40 + 4 * (i[0]-1) + j] = '-'

        for x in self.verticaux:
            for y in range(3):
                patron[35 + (16 - x[1] * 2 + y) * 40 + 4 * (x[0]-1) + 6] = '|'

        patron[37 + (16 - self.joueur1['pos'][1] * 2 + 2) * 40 + 4 * (self.joueur1['pos'][0]-1) + 6] = '1'
        patron[37 + (16 - self.joueur2['pos'][1] * 2 + 2) * 40 + 4 * (self.joueur2['pos'][0]-1) + 6] = '2' 
        patron_final = 'Légende: 1=' + str(self.joueur1['nom'])
        patron_final += ', 2=' + str(self.joueur2['nom'])
        return  patron_final + '\n' + ''.join(patron)

    def déplacer_jeton(self, joueur, position):
        etat = Quoridor.état_partie(self)
        graphe = construire_graphe([joueur['pos'] for joueur in etat['joueurs']], etat['murs']['horizontaux'], etat['murs']['verticaux'])
        if joueur not in (1, 2):
            raise QuoridorError("Le numéro du joueur est autre que 1 ou 2.")

        if not 1 <= position[0] <= 9 or not 1 <= position[1] <= 9:
            raise QuoridorError("La position est invalide (en dehors du damier.")
        
        if not 1 <= position[0] <= 9 or not 1 <= position[1] <= 9:
            raise QuoridorError("La position est invalide (en dehors du damier.")

        if joueur == 1:
            ch = list(graphe.successors(self.joueur1['pos']))
            for i in ch:
                if position == i:
                    self.joueur1['pos'] = position
                else:
                    raise QuoridorError("La position est invalide pour l'état actuel du jeu.")
        
        elif joueur == 2:
            ch2 = list(graphe.successors(self.joueur2['pos']))
            for i in ch2:
                if position == i:
                    self.joueur2['pos'] = position
                else:
                    raise QuoridorError("La position est invalide pour l'état actuel du jeu.")

    def état_partie(self):
        return {'joueurs' : [self.joueur1, self.joueur2], 'murs' : {'horizontaux' : self.horizontaux, 'verticaux' : self.verticaux}}

    def jouer_coup(self, joueur):
        etat = Quoridor.état_partie(self)
        graphe = construire_graphe([joueur['pos'] for joueur in etat['joueurs']], etat['murs']['horizontaux'], etat['murs']['verticaux'])

        if joueur not in [1, 2]:
            raise QuoridorError("Le numéro du joeur est autre que 1 ou 2.")
        if self.partie_terminée():
            raise QuoridorError("La partie est déjà terminée.")
        if joueur == 1 and nx.has_path(graphe, (self.joueur1["pos"][0], self.joueur1["pos"][1]), 'B1'):
            self.joueur1["pos"] = nx.shortest_path(graphe, (self.joueur1["pos"][0], self.joueur1["pos"][1]), 'B1')[1]
        if joueur == 2 and nx.has_path(graphe, (self.joueur2["pos"][0], self.joueur2["pos"][1]), 'B2'):
            self.joueur2["pos"] = nx.shortest_path(graphe, (self.joueur2["pos"][0], self.joueur2["pos"][1]), 'B2')[1]



    def partie_terminée(self):
        if self.joueur1['pos'][1] == 9:
            return self.joueur1['nom']
        
        if self.joueur2['pos'][1] == 1:
            return self.joueur2['nom']
        return False

    def placer_mur(self, joueur, position, orientation):
        if joueur not in (1, 2):
            raise QuoridorError("Le numéro du joueur est autre que 1 ou 2.")
        if position in self.verticaux or self.horizontaux:
            raise QuoridorError("Un mur occupe déjà cette position")
        if orientation not in ("horizontal", "vertical"):
            raise QuoridorError("La position est invalide pour cette orientation.")
        if joueur == 1 and not self.joueur1["murs"]:
            raise QuoridorError("Le jour a déjà placé tous ses murs.")
        if joueur == 2 and not self.joueur2["murs"]:
            raise QuoridorError("Le jour a déjà placé tous ses murs.")
        if joueur == 1:
            self.joueur1["murs"] += -1
        if joueur == 2:
            self.joueur2["murs"] += -1
        if orientation == "vertical":
            self.verticaux.append(position)
        if orientation == "horizontal":
            self.horizontaux.append(position)


class QuoridorError(Exception):
    """Classe implémentant l'exception QuoridorError"""


def construire_graphe(joueurs, murs_horizontaux, murs_verticaux):
    graphe = nx.DiGraph()

    # pour chaque colonne du damier
    for x in range(1, 10):
        # pour chaque ligne du damier
        for y in range(1, 10):
            # ajouter les arcs de tous les déplacements possibles pour cette tuile
            if x > 1:
                graphe.add_edge((x, y), (x-1, y))
            if x < 9:
                graphe.add_edge((x, y), (x+1, y))
            if y > 1:
                graphe.add_edge((x, y), (x, y-1))
            if y < 9:
                graphe.add_edge((x, y), (x, y+1))

    # retirer tous les arcs qui croisent les murs horizontaux
    for x, y in murs_horizontaux:
        graphe.remove_edge((x, y-1), (x, y))
        graphe.remove_edge((x, y), (x, y-1))
        graphe.remove_edge((x+1, y-1), (x+1, y))
        graphe.remove_edge((x+1, y), (x+1, y-1))

    # retirer tous les arcs qui croisent les murs verticaux
    for x, y in murs_verticaux:
        graphe.remove_edge((x-1, y), (x, y))
        graphe.remove_edge((x, y), (x-1, y))
        graphe.remove_edge((x-1, y+1), (x, y+1))
        graphe.remove_edge((x, y+1), (x-1, y+1))

    # s'assurer que les positions des joueurs sont bien des tuples (et non des listes)
    j1, j2 = tuple(joueurs[0]), tuple(joueurs[1])

    # traiter le cas des joueurs adjacents
    if j2 in graphe.successors(j1) or j1 in graphe.successors(j2):

        # retirer les liens entre les joueurs
        graphe.remove_edge(j1, j2)
        graphe.remove_edge(j2, j1)

        def ajouter_lien_sauteur(noeud, voisin):
            """
            :param noeud: noeud de départ du lien.
            :param voisin: voisin par dessus lequel il faut sauter.
            """
            saut = 2*voisin[0]-noeud[0], 2*voisin[1]-noeud[1]

            if saut in graphe.successors(voisin):
                # ajouter le saut en ligne droite
                graphe.add_edge(noeud, saut)

            else:
                # ajouter les sauts en diagonale
                for saut in graphe.successors(voisin):
                    graphe.add_edge(noeud, saut)

        ajouter_lien_sauteur(j1, j2)
        ajouter_lien_sauteur(j2, j1)

    # ajouter les destinations finales des joueurs
    for x in range(1, 10):
        graphe.add_edge((x, 9), 'B1')
        graphe.add_edge((x, 1), 'B2')

    return graphe
