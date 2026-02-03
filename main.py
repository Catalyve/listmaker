"""
Programme ListeMaker
--------------------

Ce programme permet de créer, charger, afficher, modifier, vider,
sauvegarder et supprimer des listes personnalisées stockées en JSON.

Fonctionnement général :
- L'utilisateur choisit un nom de liste (espaces supprimés, majuscules automatiques)
- Le programme charge la liste si elle existe, sinon en crée une nouvelle
- L'utilisateur interagit avec un menu en console
- Chaque liste est sauvegardée dans /modules/data sous forme de fichier JSON

Classes utilisées :
- Liste (définie dans modules.lib)
"""

from modules.lib import Liste  
import os
import json

def charger_liste(nom):
    """Charge la liste depuis un fichier JSON s'il existe"""
    chemin = os.path.join(os.path.dirname(__file__), "modules", "data", f"{nom}.json")
    if os.path.exists(chemin):
        with open(chemin, "r", encoding="utf-8") as f:
            elements = json.load(f)
        liste = Liste(nom)
        for e in elements:
            liste.ajouter(e)
        print("Liste chargée depuis le fichier.")
        return liste
    print(f"Nouvelle liste crée : {nom}")
    return Liste(nom)

def normaliser_nom(nom):
    """
    Transforme un nom fourni par l'utilisateur en format valide :
    - Espaces supprimés
    - Première lettre de chaque mot en majuscule
    - Mots collés ensemble

    Exemples :
        "liste a" -> "ListeA"
        "  ma liste 3 test " -> "MaListe3Test"
    """
    nom = nom.strip()
    words = nom.split()
    words = [w.capitalize() for w in words]
    nom_final = "".join(words)
    return nom_final

def menu():
    """Affiche le menu principal à l'écran."""
    print("_" * 50)
    print("\nChoisissez parmi les options suivantes :")
    print("| 1: Ajouter un élément")
    print("| 2: Retirer un élément")
    print("| 3: Afficher la liste")
    print("| 4: Vider la liste")
    print("| 5: Supprimer la liste")
    print("| 6: Quitter")
    print("_" * 50)

def main():
    """
    Fonction principale :
    - Affiche les listes existantes
    - Demande le nom de la liste à charger ou créer
    - Exécute les actions choisies par l'utilisateur via le menu
    """
    init = Liste("liste")
    init.afficher_liste()
    nom_brut = input("\nCharger ou créer une liste : ")
    nom = normaliser_nom(nom_brut)

    liste = charger_liste(nom)

    while True:
        menu()
        choix = input("\nVotre choix : ").strip()

        if choix == "1":
            item = input("Entrez un élément à ajouter : ")
            liste.ajouter(item)
            print(f"L'élément {item} à été ajouté.")
        elif choix == "2":
            item = input("Entrez un élément à retirer : ")
            liste.enlever(item)
        elif choix == "3":
            liste.afficher()
        elif choix == "4":
            liste.clear()
            print("Liste vidée.")
        elif choix == "5":
            liste.supprimer()
            print("Liste supprimée.")
            break    
        elif choix == "6":
            liste.sauvegarder()
            print("Liste sauvegardée. À bientôt !")
            break
        else:
            print("Option invalide.")

if __name__ == "__main__":
    main()
