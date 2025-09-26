import time
import random as rd
import turtle as t

screen=t.Screen()
screen.title("Lièvre et Tortue")

def ligne_depart():
    lignes.speed(0)
    lignes.hideturtle()
    lignes.pensize(10)
    lignes.penup()
    lignes.goto(-150,50)
    lignes.pendown()
    lignes.goto(-150,-100)
    lignes.penup()

def dessin_rounded_square():
        centre_x, centre_y = 250, 200
        taille = 50
        diametre = 10

        carre.speed(0)
        carre.hideturtle()
        carre.penup()
        carre.goto(centre_x - taille/2 + diametre, centre_y - taille/2)
        carre.pendown()

        for _ in range(4):
            carre.forward(taille - 2*diametre)
            carre.circle(diametre, 90)

def dessiner_arrivee(lignes):
    lignes.pensize(1)
    lignes.speed(0)

    def dessiner_carre(lignes):
        lignes.pendown()
        lignes.fillcolor("black")
        lignes.begin_fill()
        for _ in range(4):
            lignes.forward(10)
            lignes.right(90)
        lignes.end_fill()
        lignes.penup()

    def dessiner_ligne(lignes):
        for _ in range(7):
            dessiner_carre(lignes)
            lignes.penup()
            lignes.right(90)
            lignes.forward(20)
            lignes.left(90)

    lignes.penup()
    lignes.setposition(180, 50)
    dessiner_ligne(lignes)
    lignes.setposition(190, 40)
    lignes.penup()
    dessiner_ligne(lignes)


def tortue():
    image_tortue = "tortue_lievre/images/voiture_2cv.gif"
    screen.addshape(image_tortue)

    tt.speed(0)
    tt.shape(image_tortue)
    tt.color("blue")
    tt.penup()
    tt.setpos(-100,0)
    tt.speed(1)

def lievre():
    image_lievre = "tortue_lievre/images/voiture_sport.gif"
    screen.addshape(image_lievre)

    tl.speed(0)
    tl.shape(image_lievre)
    tl.color("red")
    tl.penup()
    tl.setpos(-100,-75)
    tl.speed(2)

def victoire_lievre():
    d.color("red")
    d.penup()
    d.hideturtle()
    d.goto(-60,80)
    d.pendown()

    d.write("Victoire du Lièvre", font=("Arial", 24))

def victoire_tortue():
    tt.forward(40)

    d.color("blue")
    d.penup()
    d.hideturtle()
    d.goto(-60,80)
    d.pendown()

    d.write("Victoire de le Tortue", font=("Arial", 24))

def des(chiffre_obtenu):
    centre_x, centre_y = 250, 200
    taille = 50
    diametre = 10

    point.hideturtle()
    point.speed(0)
    point.pensize(3)
    point.clear()

    def dessin_point(x, y):
        point.penup()
        point.goto(x, y - 4)  # Ajustement pour centrer le cercle
        point.pendown()
        point.begin_fill()
        point.circle(4)
        point.end_fill()

    def face_1():
        dessin_point(centre_x, centre_y)

    def face_2():
        dessin_point(centre_x - 10, centre_y - 10)
        dessin_point(centre_x + 10, centre_y + 10)

    def face_3():
        face_1()
        face_2()
    def face_4():
        dessin_point(centre_x - 10, centre_y - 10)
        dessin_point(centre_x + 10, centre_y - 10)
        dessin_point(centre_x - 10, centre_y + 10)
        dessin_point(centre_x + 10, centre_y + 10)
    def face_5():
        face_4()
        face_1()
    def face_6():
        dessin_point(centre_x - 10, centre_y - 15)
        dessin_point(centre_x + 10, centre_y - 15)
        dessin_point(centre_x - 10, centre_y)
        dessin_point(centre_x + 10, centre_y)
        dessin_point(centre_x - 10, centre_y + 15)
        dessin_point(centre_x + 10, centre_y + 15)

    if chiffre_obtenu == 1:
        face_1()
    elif chiffre_obtenu == 2:
        face_2()
    elif chiffre_obtenu == 3:
        face_3()
    elif chiffre_obtenu == 4:
        face_4()
    elif chiffre_obtenu == 5:
        face_5()
    elif chiffre_obtenu == 6:
        face_6()

def des_images(chiffre_obtenu):
    de.speed(0)
    de.pensize(3)
    de.clear()
    de.penup()
    de.goto(0,200)

    def face_1():
        de1 = "tortue_lievre/images/1.gif"
        screen.addshape(de1)
        de.shape(de1)
    def face_2():
        de2 = "tortue_lievre/images/2.gif"
        screen.addshape(de2)
        de.shape(de2)
    def face_3():
        de3 = "tortue_lievre/images/3.gif"
        screen.addshape(de3)
        de.shape(de3)
    def face_4():
        de4 = "tortue_lievre/images/4.gif"
        screen.addshape(de4)
        de.shape(de4)
    def face_5():
        de5 = "tortue_lievre/images/5.gif"
        screen.addshape(de5)
        de.shape(de5)
    def face_6():
        de6 = "tortue_lievre/images/6.gif"
        screen.addshape(de6)
        de.shape(de6)
    if chiffre_obtenu == 1:
        face_1()
    elif chiffre_obtenu == 2:
        face_2()
    elif chiffre_obtenu == 3:
        face_3()
    elif chiffre_obtenu == 4:
        face_4()
    elif chiffre_obtenu == 5:
        face_5()
    elif chiffre_obtenu == 6:
        face_6()

def restart():
    r = t.Turtle()
    restart = "tortue_lievre/images/restart.gif"
    screen.addshape(restart)
    r.shape(restart)
    r.penup()
    r.goto(200, -200)

def click_image(x=None, y=None):
        if 170 < x < 200  and -180 < y < -200:
            jeu()

def jeu():
    tt.clear()
    tl.clear()
    de.clear()
    point.clear()
    d.clear()

    tortue()
    lievre()

    score_tortue = 0
    score_lievre = 0

    while score_tortue < 6 and score_lievre < 1:
        de_val = rd.randint(1, 6)
        des(de_val)
        des_images(de_val)
        time.sleep(2)
        if de_val == 6:
            score_lievre = 1
            tl.forward(340)
            victoire_lievre()
        else:
            score_tortue += 1
            tt.forward(50)

    if score_tortue == 6:
        victoire_tortue()


lignes = t.Turtle()
d = t.Turtle()
carre = t.Turtle()
point = t.Turtle()
de = t.Turtle()
tl = t.Turtle()
tt = t.Turtle()

dessin_rounded_square()
dessiner_arrivee(lignes)
ligne_depart()
restart()
jeu()


t.onscreenclick(click_image)
t.mainloop()
