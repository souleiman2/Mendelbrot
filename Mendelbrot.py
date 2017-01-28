from graphics import *
import math

class complexed:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self, c, d):
        self.a = self.a + c
        self.b = self.b + d
    def carre(self):
        self.a = self.a**2 - self.b**2
        self.b = 2*self.a*self.b


echelle = 50

taille_win = [300,200]
centre = [taille_win[0]//2,taille_win[1]//2]
matrice = []
iteration = 50

for i in range(taille_win[0]):
    for j in range(taille_win[1]):
        
        c = complexed( (i-centre[0])/echelle ,(j-centre[1])/echelle)
        z = complexed(c.a,c.b)
        
        compteur = 0
        while ( (z.a**2 + z.b**2) <= 4) and (compteur <= iteration):
            z.carre()
            print(z.a)
            print(z.b)
            z.add(c.a,c.b)
            compteur +=1
        matrice.append(compteur)


win = GraphWin("Mendelbrot", taille_win[0], taille_win[1])
win.setBackground("white")
compteur = 0
for i in range(taille_win[0]):
    for j in range(taille_win[1]):
        if matrice[compteur] == iteration+1:
            aPoint = Point(i, j)
            aPoint.setFill("black")
            aPoint.draw(win)
        compteur +=1


