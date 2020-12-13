import turtle
from quoridor import Quoridor


class QuoridorX(Quoridor):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.afficher()
    
    grandeur_case = 30
    marge_case = 20
    l_mur = grandeur_case * 2.4 + marge_case
    r_mur = grandeur_case * 0.2
    off_mur = grandeur_case / 2
    off_pion = grandeur_case / 2
    pion = 30
    nb_m = 9
    xy_off = - (grandeur_case * nb_m + marge_case * (nb_m - 1)) / 2 - grandeur_case - marge_case
    xy_up = grandeur_case + marge_case
    police = 18

    def position_damier(self, case):
        return case * self.xy_up + self.xy_off

    def afficher(self):
        turtle.color('silver')
        turtle.pensize(5)
        turtle.clear()
        turtle.penup()
        turtle.setheading(90)
        turtle.Screen().tracer(0, 0)
        
        for i in range(1, self.nb_m + 1):
            for j in range(1, self.nb_m + 1):
                turtle.setpos(self.position_damier(i), self.position_damier(j))
                turtle.pendown()
                turtle.begin_fill()

                for _ in range(4):
                    turtle.right(90)
                    turtle.forward(self.grandeur_case)
                turtle.end_fill()
                turtle.penup()
        
        turtle.color("white")
        for i, j in enumerate(self.etat["joueurs"]):
            turtle.setpos(self.position_damier(["pos"][0]) + self.off_pion, self.position_damier(j["pos"][1]) + self.off_pion)
            turtle.dot(self.pion, "green" if i == 0 else "red")
            turtle.setpos(self.position_damier(j["pos"][0]) + self.off_pion, self.position_damier(j["pos"][1]))
            turtle.write(str(i + 1), font = ("", self.police), align = "center")
            
        id = [f'{i + 1} = {id["nom"]}' for i, id in enumerate(self.etat["joueurs"])]
        turtle.setpos(self.position_damier(1), self.position_damier(10) - self.marge_case / 2)
        turtle.write("Légende: " + ", ".join(id), font = ("", 14))
        for i, j in enumerate(self.etat["joueurs"]):
            id = str(i + 1)
            id.append(f'{id} = {j["nom"]}')
        
        turtle.color("darkblue")
        for i in range(1, self.nb_m + 1):
            turtle.setpos(self.position_damier(i) + self.off_pion, self.position_damier(0) + self.off_pion) 
            turtle.write(str(i), font = ("", self.police), align = "center")
            turtle.setpos(self.position_damier(0) + self.grandeur_case, self.position_damier(i)) 
            turtle.write(str(i), font = ("", self.police), align = "center")

        turtle.color("rosybrown")
        turtle.setheading(0)
        for self.horizontaux in self.etat.get("murs")["horizontaux"]:
            turtle.setpos(self.position_damier(self.horizontaux[0]) - self.r_mur, self.position_damier(self.horizontaux[1]) - self.off_mur)
            turtle.pendown()
            turtle.forward(self.l_mur)
            turtle.penup()

        turtle.setheading(90)
        for self.verticaux in self.etat.get("murs")["verticaux"]:
            turtle.setpos(self.position_damier(self.verticaux[0]) - self.off_mur, self.position_damier(self.verticaux[1]) - self.r_mur)
            turtle.pendown()
            turtle.forward(self.l_mur)
            turtle.penup()
        
        turtle.hideturtle()
        gagnant = self.partie_terminée()
        if gagnant:
            turtle.title(f'{gagnant} a gagné la partie!')
            turtle.bgcolor("green" if gagnant == self.etat["joueurs"][0]["nom"] else "red")
        else:
            turtle.title("QuoridorX")
        turtle.update()