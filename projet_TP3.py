"""
Gabriel Claude-Giroux 405
projet tp3: combat des monstres
10 novembre 2022
Dans ce code, le joueur devra affronter des monstres avec des valeurs de dees
jusqu'a ce qu'il perds tout ces vies ou quitte la partie.
"""
import random
niveau_vie = 20
jouer = True
nbr_victoires = 0
while jouer:
    """
    Mise en contexte pour le joueur et menu des choix pour le joueur
    """
    valeur_monstre = random.randint(1, 12)
    print("\n"
          "Vous tombez face à face avec un monstre de difficulté:", valeur_monstre, )
    print("Vous avez un niveau de vie de ", niveau_vie)
    print("Que voulez-vous faire ?")
    print("1- Combattre ce monstre")
    print("2- Contourner ce monstre et aller ouvrir une autre porte")
    print("3- Afficher les règles du jeu")
    print("4- Quitter la partie")
    choix = input()
    """
    Selon le choix du joueur, le code va initier ce que le joueur a choisi
    """
    if choix == "1":
        valeur_dee_1 = random.randint(1, 6)
        valeur_dee_2 = random.randint(1, 6)
        valeur_total = valeur_dee_1 + valeur_dee_2
        print("Si votre dée a une valeur plus grosse que celle du monstre, vous gagnez cette ronde.")
        print("Vous avez rouler une valeur de ", valeur_dee_1, " et ", valeur_dee_2)
        print("Vous avez une valeur totale de ", valeur_total)
        if valeur_total > valeur_monstre:
            print("Vous avez battu le monstre!")
            print("Il vous reste maintenant", niveau_vie)
            print(" vies\n")
            nbr_victoires += 1
            if nbr_victoires == 3:
                """
                Quand le joueur aura 3 victoires, il devra affronter le boss (avec 3 dees)
                """
                print("Felecitation, vous avez gagner 3 fois.")
                print("Vous avez maintenant pas le choix, mais d'affronter le boss")
                valeur_dee_1 = random.randint(1, 6)
                valeur_dee_2 = random.randint(1, 6)
                valeur_dee_3 = random.randint(1, 6)
                valeur_total_2 = valeur_dee_1 + valeur_dee_2 + valeur_dee_3
                valeur_boss = random.randint(14, 17)
                print("Vous roulez maintenant 3 dees. Le boss a  ", valeur_boss, " vies")
                print("Votre premier dee a une valeur de ", valeur_dee_1)
                print("Votre deuxieme a une valeur de ", valeur_dee_2)
                print("Votre troisieme a une valeur de ", valeur_dee_3)
                print("Vous avez une valeur de ", valeur_total_2)
                if valeur_total_2 > valeur_boss:
                    print("Vous avez gagner contre le boss. Felicitation!")
                    niveau_vie -= 3
                elif valeur_total_2 < valeur_boss:
                    print("Vous avez perdu contre le boss. Vous perdez 3 vies.")
                    niveau_vie -= 3
        elif valeur_dee_1 + valeur_dee_2 < valeur_monstre:
            print("Le monstre vous a battu!")
            niveau_vie -= 1
            print("Il vous reste maintenant", niveau_vie, " vies")
    elif choix == "2":
        print("D'accords, cela vous coutera un point de vie")
        niveau_vie -= 1
        print("Il vous reste maintenant", niveau_vie, " vies")
    elif choix == "3":
        print("Vous allez faire face a plusieurs adversaires")
        print("Chacuns des adversaires ont un niveau de difficulte")
        print("Vous devez rouler des dees et si votre valeur est plus grande que la force de l'adversaire, vous gagnez.")
        print("Si vous pensiez que l'adversaire est trop fort, vous pouvez le contourner et aller ouvrir une autre porte.")
        print("Mais cela vous coutera un point de vie")
        print("Vous commencez avec 20 point de vies.")
        print("Lorsque vous perdez contre un monstre, vous en perdez 2.")
        print("Mais, si vous le contourniez, vous en perdez 1.")
        print("Vous allez faire face a un boss a chaques 3 vicoires, si vous perdez contre lui, vous perdez un poit de vie.")
    elif choix == "4":
        jouer = False
        # le joueur quitte la partie volontairement
    if niveau_vie == 0:
        """
        il ne reste plus de vies au joueur, il a perdu
        """
        print("Vous avez perdus toutes vos vies, vous avez perdu")
        jouer = False
