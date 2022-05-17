# importation des bibliothèques
from tkinter import Label, Tk
from tkinter import *
from random import *



# 1ère partie de l'algorithme: Jouer au 2048 avec la Console Python


# 1ère étape: Affichage dans la console de la nouvelle partie du 2048

# grille vide du jeu 2048
L=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

# choix aléatoire des coordonnés des 2 nombres de base (j ligne | i colonne)
j12=randint(0,3)
i11=randint(0,3)
j22=randint(0,3)
i21=randint(0,3)

# choix aléatoire des valeurs des 2 nombres
# choix de la valeur(2 ou 4) du premier nombre
n241=randint(0,9)
if n241<5:
    n241=2
if n241>=5:
    n241=4
# choix de la valeur(2 ou 4) du deuxième nombre
n242=randint(0,9)
if n242<5:
    n242=2
if n242>=5:
    n242=4

# placement dans la grille des 2 nombres avec leurs valeurs
for j in range(4):
    for i in range(4):
        if i == i11 and j == j12:
            L[j][i] = n241
        if i == i21 and j == j22:
            L[j][i] = n242



# Affichage dans la console

# de la Séparation décorative entre différents coups du jeu
print("///////////////////////////////////////////////////////////")
print("///////////////////////////////////////////////////////////")

# de la Nouvelle grille
print("Initialisation aléatoire:")
for k in range(4):
    for l in range(1):
        if k==0:
            print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
        if k==1:
            print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
        if k==2:
            print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
        if k==3:
            print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])

# des Règles du jeu et des Commandes
print("Règles du jeu: ")
print("Obtenez le nombre 2048 dans une des cases,")
print("en fusionnant les cases du même nombre,")
print("en déplaçant ces cases une vers l'autre,")
print("par des mouvements à droite, à gauche, en bas ou en haut.")
print(" ")
print("Commandes pour les mouvements: ")
print("mouvement à droite: d()")
print("mouvement à gauche: g()")
print("mouvement à bas: b()")
print("mouvement à haut: h()")

# de la Séparation décorative entre différents coups du jeu encore
print("///////////////////////////////////////////////////////////")
print("///////////////////////////////////////////////////////////")



# 2ème étape: Commandes du 2048 avec la console

# 1ère fonction d qui est la commande du mouvement à droite
def d():

    # Chaque coup du jeu va être présenté en 3 parties: "Avant", "Déplacement à droite", "Appartition"
    # Dans le but de facilité le jeu au 2048 dans la console



    # 1ere partie: "Avant" affiche la grille du coup précédent
    print("Avant:")
    for k in range(4):
        for l in range(1):
            if k==0:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
            if k==1:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
            if k==2:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
            if k==3:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])



    # 2ème partie: "Déplacement à droite" affiche la grille après le mouvement à droite

    cond_gain=0
    cond_perte=0
    mouv=1
    fuz=1
    mouv_fuz=0
    comp_1=0

    # boucle qui déplace tout les nombres à droite et les fusionne
    while mouv_fuz==0:

        # Déplacement de tout les nombres à droite d'une case
        for j in range(4):
            for i in range(3,0,-1):
                if L[j][i-1]!=0 and L[j][i]==0:
                    L[j][i]=L[j][i-1]
                    L[j][i-1]=0

        # Vérification si les nombres se sont tous bien collé au côté droit de la grille
        for j in range(4):
            for i in range(3):
                if L[j][i]!=0 and L[j][i+1]==0:
                    mouv=0

        # Fusion de 2 nombres égaux en celui de droite
        for j in range(4):
            for i in range(3,0,-1):
                if L[j][i-1]!=0 and L[j][i]!=0 and L[j][i-1]==L[j][i]:
                    L[j][i-1]=0
                    L[j][i]=L[j][i]*2
                    fuz=0

        # fin de la boucle si lors de ce tour de la boucle il n'y a pas de déplacement ni fusion
        # cela veut dire que tout les nombres sont à doite de la grille et ne sont pas égaux
        if fuz==1 and mouv==1:
            mouv_fuz=1

            # recherce du nombre de cases remplies et d'une case avec la valeur de 2048
            for j in range(4):
                for i in range(4):
                    if L[j][i]!=0:
                        comp_1=comp_1+1
                    if L[j][i]==2048:
                        cond_gain=1
            if comp_1==16:
                cond_perte=1

        # Remise à 1 des temoins de déplacement et de fusion
        mouv=1
        fuz=1

    # Affichage la grille après le mouvement à droite
    print("Déplacement à droite:")
    for k in range(4):
        for l in range(1):
            if k==0:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
            if k==1:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
            if k==2:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
            if k==3:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])



    # 3ème partie: "Apparition" affiche la grille avec un nouveau nombre(2 ou 4) apparu

    i11=0
    j12=0
    comp_0=0
    block=0
    app=17

    # boucle qui compte les cases vides et choisis une case où apparaîtra le nouveau nombre
    for nb_tours in range(2):
        for j in range(4):
            for i in range(4):
                if L[j][i]==0 and block==0:
                    comp_0=comp_0+1
                if nb_tours==1 and block==0 and comp_0!=0:
                    app=randint(1,comp_0)
                    comp_0=0
                    block=1
                if nb_tours==1 and block==1 and L[j][i]==0:
                    comp_0=comp_0+1
                    if comp_0==app:
                        i11=i
                        j12=j

    # choix aléatoire de la valeur du nouveau nombre (2 ou 4)
    n241=randint(0,9)
    if n241<5:
        n241=2
    if n241>=5:
        n241=4

    # placement dans la grille du nouveau nombre avec sa valeur
    if comp_0!=0:
        for j in range(4):
            for i in range(4):
                if i == i11 and j == j12 and L[j][i]==0:
                    L[j][i] = n241

    # Affichage de la grille après l'apparition du nouveau nombre(2 ou 4)
    print("Apparition:")
    if  comp_1!=16:
        print("(",n241,"apparu à |colonne:",i11+1,"|ligne:",j12+1,")")
    for k in range(4):
        for l in range(1):
            if k==0:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
            if k==1:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
            if k==2:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
            if k==3:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
    print(" ")
    print("(nombre minimal de mouvements possibles:",16-comp_1,")")

    # Messages de fin de partie 2048
    if cond_perte==1:
        print(" ")
        print("!!!PERDU!!!")
        print(" ")
    if cond_perte==1:
        # Lien avec les fonctions tkinter pour de l'interface graphique
        fin1()

    if cond_gain==1:
        print(" ")
        print("!!!Gagné!!!")
        print(" ")
    if cond_gain==1:
        # Lien avec les fonctions tkinter pour de l'interface graphique
        fin2()

    print("///////////////////////////////////////////////////////////")
    print("///////////////////////////////////////////////////////////")

    # Lien avec les fonctions tkinter pour de l'interface graphique
    if cond_perte==0 and cond_gain==0:
        grille()



def g():

    print("Avant:")
    for k in range(4):
        for l in range(1):
            if k==0:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
            if k==1:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
            if k==2:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
            if k==3:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])



    cond_perte=0
    cond_gain=0
    mouv=1
    fuz=1
    mouv_fuz=0
    comp_1=0

    while mouv_fuz==0:

        # Déplacement de tout les nombres à gauche d'une case
        for j in range(4):
            for i in range(3):
                if L[j][i]==0 and L[j][i+1]!=0:
                    L[j][i]=L[j][i+1]
                    L[j][i+1]=0

        # Vérification si les nombres se sont tous collé au côté gauche de la grille
        for j in range(4):
            for i in range(3):
                if L[j][i]==0 and L[j][i+1]!=0:
                    mouv=0

        # Fusion de 2 nombres égaux en celui de gauche
        for j in range(4):
            for i in range(3):
                if L[j][i]!=0 and L[j][i+1]!=0 and L[j][i]==L[j][i+1]:
                    L[j][i]=L[j][i]*2
                    L[j][i+1]=0
                    fuz=0

        if fuz==1 and mouv==1:
            mouv_fuz=1
            for j in range(4):
                for i in range(4):
                    if L[j][i]!=0:
                        comp_1=comp_1+1
            if comp_1==16:
                cond_perte=1
            if L[j][i]==2048:
                cond_gain=1

        mouv=1
        fuz=1

    print("Déplacement à gauche:")
    for k in range(4):
        for l in range(1):
            if k==0:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
            if k==1:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
            if k==2:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
            if k==3:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])



    i11=0
    j12=0
    comp_0=0
    block=0
    app=17

    for nb_tours in range(2):
        for j in range(4):
            for i in range(4):
                if L[j][i]==0 and block==0:
                    comp_0=comp_0+1
                if nb_tours==1 and block==0 and comp_0!=0:
                    app=randint(1,comp_0)
                    comp_0=comp_0-comp_0
                    block=1
                if L[j][i]==0 and nb_tours==1:
                    comp_0=comp_0+1
                    if comp_0==app:
                        i11=i
                        j12=j

    n241=randint(0,9)
    if n241<5:
        n241=2
    if n241>=5:
        n241=4

    if comp_0!=0:
        for j in range(4):
            for i in range(4):
                if i == i11 and j == j12 and L[j][i]==0:
                    L[j][i] = n241

    print("Apparition:")
    if  comp_1!=16:
        print("(",n241,"apparu à |colonne:",i11+1,"|ligne:",j12+1,")")

    for k in range(4):
        for l in range(1):
            if k==0:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
            if k==1:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
            if k==2:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
            if k==3:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
    print(" ")
    print("(nombre minimal de mouvements possibles:",16-comp_1,")")

    if cond_perte==1:
        print(" ")
        print("!!!PERDU!!!")
        print(" ")
    if cond_perte==1:
        fin1()
    if cond_gain==1:
        print(" ")
        print("!!!Gagné!!!")
        print(" ")
    if cond_gain==1:
        fin2()

    print("///////////////////////////////////////////////////////////")
    print("///////////////////////////////////////////////////////////")

    if cond_perte==0 and cond_gain==0:
        grille()



def b():

    print("Avant:")
    for k in range(4):
        for l in range(1):
            if k==0:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
            if k==1:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
            if k==2:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
            if k==3:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])



    cond_perte=0
    cond_gain=0
    mouv=1
    fuz=1
    mouv_fuz=0
    comp_1=0

    while mouv_fuz==0:

        # Déplacement de tout les nombres en bas d'une case
        for j in range(3,0,-1):
            for i in range(4):
                if L[j][i]==0 and L[j-1][i]!=0:
                    L[j][i]=L[j-1][i]
                    L[j-1][i]=0

        # Vérification si les nombres se sont tous collé au côté bas de la grille
        for j in range(3):
            for i in range(4):
                if L[j][i]!=0 and L[j+1][i]==0:
                    mouv=0

        # Fusion de 2 nombres égaux en celui de bas
        for j in range(3,0,-1):
            for i in range(4):
                if L[j][i]!=0 and L[j-1][i]!=0 and L[j][i]==L[j-1][i]:
                    L[j-1][i]=0
                    L[j][i]=L[j][i]*2
                    fuz=0

        if fuz==1 and mouv==1:
            mouv_fuz=1
            for j in range(4):
                for i in range(4):
                    if L[j][i]!=0:
                        comp_1=comp_1+1
            if comp_1==16:
                cond_perte=1
            if L[j][i]==2048:
                cond_gain=1

        mouv=1
        fuz=1

    print("Déplacement en bas:")
    for k in range(4):
        for l in range(1):
            if k==0:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
            if k==1:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
            if k==2:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
            if k==3:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])



    i11=0
    j12=0
    comp_0=0
    block=0
    app=17

    for nb_tours in range(2):
        for j in range(4):
            for i in range(4):
                if L[j][i]==0 and block==0:
                    comp_0=comp_0+1
                if nb_tours==1 and block==0 and comp_0!=0:
                    app=randint(1,comp_0)
                    comp_0=comp_0-comp_0
                    block=1
                if L[j][i]==0 and nb_tours==1:
                    comp_0=comp_0+1
                    if comp_0==app:
                        i11=i
                        j12=j

    n241=randint(0,9)
    if n241<5:
        n241=2
    if n241>=5:
        n241=4

    if comp_0!=0:
        for j in range(4):
            for i in range(4):
                if i == i11 and j == j12 and L[j][i]==0:
                    L[j][i] = n241

    print("Apparition:")
    if  comp_1!=16:
        print("(",n241,"apparu à |colonne:",i11+1,"|ligne:",j12+1,")")

    for k in range(4):
        for l in range(1):
            if k==0:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
            if k==1:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
            if k==2:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
            if k==3:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
    print(" ")
    print("(nombre minimal de mouvements possibles:",16-comp_1,")")

    if cond_perte==1:
        print(" ")
        print("!!!PERDU!!!")
        print(" ")
    if cond_perte==1:
        fin1()
    if cond_gain==1:
        print(" ")
        print("!!!Gagné!!!")
        print(" ")
    if cond_gain==1:
        fin2()

    print("///////////////////////////////////////////////////////////")
    print("///////////////////////////////////////////////////////////")

    if cond_perte==0 and cond_gain==0:
        grille()



def h():

    print("Avant:")
    for k in range(4):
        for l in range(1):
            if k==0:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
            if k==1:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
            if k==2:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
            if k==3:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])



    cond_perte=0
    cond_gain=0
    mouv=1
    fuz=1
    mouv_fuz=0
    comp_1=0

    while mouv_fuz==0:

        # Déplacement de tout les nombres en haut d'une case
        for j in range(4):
            for i in range(4):
                if j!=0:
                    if L[j-1][i]==0 and L[j][i]!=0:
                        L[j-1][i]=L[j][i]
                        L[j][i]=0

        # Vérification si les nombres se sont tous collé au côté haut de la grille
        for j in range(4):
            for i in range(4):
                if j!=0:
                    if L[j][i]!=0 and L[j-1][i]==0:
                        mouv=0

        # Fusion de 2 nombres égaux en celui de haut
        for j in range(4):
            for i in range(4):
                if j!=0:
                    if L[j-1][i]!=0 and L[j][i]!=0 and L[j][i]==L[j-1][i]:
                        L[j][i]=0
                        L[j-1][i]=L[j-1][i]*2
                        fuz=0

        if fuz==1 and mouv==1:
            mouv_fuz=1
            for j in range(4):
                for i in range(4):
                    if L[j][i]!=0:
                        comp_1=comp_1+1
            if comp_1==16:
                cond_perte=1
            if L[j][i]==2048:
                cond_gain=1

        mouv=1
        fuz=1

    print("Déplacement en haut:")
    for k in range(4):
        for l in range(1):
            if k==0:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
            if k==1:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
            if k==2:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
            if k==3:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])



    i11=0
    j12=0
    comp_0=0
    block=0
    app=17

    for tour2 in range(2):
        for j in range(4):
            for i in range(4):
                if L[j][i]==0 and block==0:
                    comp_0=comp_0+1
                if tour2==1 and block==0 and comp_0!=0:
                    app=randint(1,comp_0)
                    comp_0=comp_0-comp_0
                    block=1
                if L[j][i]==0 and tour2==1:
                    comp_0=comp_0+1
                    if comp_0==app:
                        i11=i
                        j12=j

    n241=randint(0,9)
    if n241<5:
        n241=2
    if n241>=5:
        n241=4

    if comp_0!=0:
        for j in range(4):
            for i in range(4):
                if i == i11 and j == j12 and L[j][i]==0:
                    L[j][i] = n241

    print("Apparition:")
    if  comp_1!=16:
        print("(",n241,"apparu à |colonne:",i11+1,"|ligne:",j12+1,")")

    for k in range(4):
        for l in range(1):
            if k==0:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
            if k==1:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
            if k==2:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
            if k==3:
                print(L[k][l],"|",L[k][l+1],"|",L[k][l+2],"|",L[k][l+3])
    print(" ")
    print("(nombre minimal de mouvements possibles:",16-comp_1,")")

    if cond_perte==1:
        print(" ")
        print("!!!PERDU!!!")
        print(" ")
    if cond_perte==1:
        fin1()
    if cond_gain==1:
        print(" ")
        print("!!!Gagné!!!")
        print(" ")
    if cond_gain==1:
        fin2()

    print("///////////////////////////////////////////////////////////")
    print("///////////////////////////////////////////////////////////")

    if cond_perte==0 and cond_gain==0:
        grille()



# 2ème partie de l'algorithme: Jouer au 2048 avec l'interface graphique tkinter

# fonction appart car pas le droit grid et pack en même temps
def grille():



    #définition de tout les cases de la grille

    lab1 = Label(can, text=L[0][0])
    lab2 = Label(can, text=L[0][1])
    lab3 = Label(can, text=L[0][2])
    lab4 = Label(can, text=L[0][3])

    lab5 = Label(can, text=L[1][0])
    lab6 = Label(can, text=L[1][1])
    lab7 = Label(can, text=L[1][2])
    lab8 = Label(can, text=L[1][3])

    lab9 = Label(can, text=L[2][0])
    lab10 = Label(can, text=L[2][1])
    lab11 = Label(can, text=L[2][2])
    lab12 = Label(can, text=L[2][3])

    lab13 = Label(can, text=L[3][0])
    lab14 = Label(can, text=L[3][1])
    lab15 = Label(can, text=L[3][2])
    lab16 = Label(can, text=L[3][3])



    #placement de cases dans un tableau = grille

    lab1.grid(column=1, row=0,padx =15,pady =10)
    lab2.grid(column=2, row=0,padx =15,pady =10)
    lab3.grid(column=3, row=0,padx =15,pady =10)
    lab4.grid(column=4, row=0,padx =15,pady =10)

    lab5.grid(column=1, row=1,padx =15,pady =10)
    lab6.grid(column=2, row=1,padx =15,pady =10)
    lab7.grid(column=3, row=1,padx =15,pady =10)
    lab8.grid(column=4, row=1,padx =15,pady =10)

    lab9.grid(column=1, row=2,padx =15,pady =10)
    lab10.grid(column=2, row=2,padx =15,pady =10)
    lab11.grid(column=3, row=2,padx =15,pady =10)
    lab12.grid(column=4, row=2,padx =15,pady =10)

    lab13.grid(column=1, row=3,padx =15,pady =10)
    lab14.grid(column=2, row=3,padx =15,pady =10)
    lab15.grid(column=3, row=3,padx =15,pady =10)
    lab16.grid(column=4, row=3,padx =15,pady =10)



# Fin du jeu n°1: Gain
def fin2():
    fenetre.destroy()
    fenetrefin = Tk()
    fenetrefin.title("Jeu 2048")
    messagefin=Label(fenetrefin, text="!!!Gagné!!! Vous avez obtenu: 2048")
    messagefin.pack()
    bouton=Button(fenetrefin, text="Quitter le jeu", command=fenetrefin.destroy)
    bouton.pack()
    fenetrefin.mainloop()



# Fin du jeu n°2: Perte
def fin1():
    fenetre.destroy()
    fenetrefin = Tk()
    fenetrefin.title("Jeu 2048")
    messagefin=Label(fenetrefin, text="!!!PERDU!!!")
    bouton=Button(fenetrefin, text="Quitter le jeu", command=fenetrefin.destroy)
    bouton.pack()
    messagefin.pack()
    fenetrefin.mainloop()



# Création de la première et principale fenêtre

fenetre = Tk()
fenetre.title('Jeu 2048')

bouton1=Button(fenetre, text="droite", command=d)
bouton2=Button(fenetre, text="gauche", command=g)
bouton3=Button(fenetre, text="haut", command=h)
bouton4=Button(fenetre, text="bas ", command=b)

can=Canvas(fenetre,height=250,width=250, bg="orange")
can.pack()
grille()

bouton1.pack(side=RIGHT)
bouton2.pack(side=LEFT)
bouton3.pack(side=TOP)
bouton4.pack(side=BOTTOM)

fenetre.mainloop()