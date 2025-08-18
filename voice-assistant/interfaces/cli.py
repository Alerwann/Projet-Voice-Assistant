import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from logique.csv_reader import get_all_information


def afficher_menu():
    """Liste des choix sur l'accueil à des fins de teste"""
    print("=== Assistant Vocal - Test CLI ===")
    print("1. Lire toutes les informations")
    print("2. lire le repas de midi")
    print("3. lire le repas de ce soir")
    print("4. lire le rendez-vous")
    print("q. Quitter")


def mainCli():
    """Affiche les informations demandés"""
    while True:
        afficher_menu()
        choix = input("Votre choix: ")

        if choix=='q': 
            break

        infos = get_all_information()
        
        if choix == "1":
            print(infos)
        elif choix == "2":
            print(infos['midi'])
        elif choix == "3":
            print(infos["soir"])
        elif choix == "4":
            print(infos["rendez-vous"])
        else:
            break


if __name__ == "__main__":
    mainCli()
