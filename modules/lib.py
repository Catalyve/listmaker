"""
Module : lib
------------

Contient la classe Liste, une extension orientée objet de la liste Python.
Chaque instance représente une liste nommée, pouvant être :
- affichée,
- modifiée (ajout/retrait d'éléments),
- sauvegardée dans un fichier JSON,
- supprimée du disque,
- visualisée via l'affichage des listes disponibles.

Les données sont stockées dans /modules/data sous forme de fichiers JSON.
"""
import logging
import json
import os

from modules.constants import DATA_DIR

LOGGER = logging.getLogger()

class Liste(list):
    """
    Classe représentant une liste nommée.

    Hérite de la liste Python classique et ajoute :
    - un nom interne (self.nom),
    - des méthodes d'affichage et de manipulation,
    - la capacité de sauvegarder et charger les données depuis un fichier JSON,
    - la suppression du fichier associé.
    """
    def __init__(self, nom):
        """
        Initialise une nouvelle liste nommée.

        Paramètres :
            nom (str) : nom de la liste (servira aussi au nom du fichier JSON)
        """
        self.nom = nom
    
    def afficher_liste(self):
        """
        Affiche toutes les listes JSON disponibles dans le dossier 'data'.

        Ne retourne rien, se contente d'afficher.
        """
        print("_" * 50)
        print("Liste(s) :")
        dossier = os.path.join(os.path.dirname(__file__), "data")
        json = [f for f in os.listdir(dossier) if f.endswith(".json")]
        for element in json:
            print(element)


    def ajouter(self, element):
        """
        Ajoute un élément à la liste si c'est une chaîne et qu'il n'existe pas déjà.

        Paramètres :
            element (str) : élément à ajouter

        Retour :
            bool : True si ajouté, False si doublon
        """
        if not isinstance(element, str):
            raise ValueError("Vous ne pouvez ajouter que des chaînes de caractères!")
        if element in self:
            LOGGER.error(f"{element} est déjà dans la liste")
            return False
        
        self.append(element)
        return True
    
    def enlever(self, element):
        """
        Retire un élément de la liste s'il existe.

        Paramètres :
            element (str)

        Retour :
            bool : True si retiré, False sinon
        """
        if element in self:
            self.remove(element)
            return True
        return False
    
    def supprimer(self):
        """
        Supprime le fichier JSON associé à la liste.

        Ne supprime pas les données en mémoire, uniquement le fichier physique.
        """
        chemin = os.path.join(DATA_DIR, f"{self.nom}.json")
        if os.path.exists(chemin):
            os.remove(chemin)
            print(f"La liste '{self.nom}' a été supprimée.")
        else:
            print("Aucun fichier à supprimer.")

    def afficher(self):
        """
        Affiche le contenu courant de la liste en mémoire.
        """
        print(f"{self.nom}: ")
        for element in self:
            print(f"- {element}")

    def sauvegarder(self):
        """
        Sauvegarde la liste actuelle dans un fichier JSON situé dans DATA_DIR.

        Retour :
            True (toujours, une fois la sauvegarde terminée)
        """
        chemin = os.path.join(DATA_DIR, f"{self.nom}.json")
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
        with open(chemin, "w") as f:
            json.dump(self, f, indent=4)
        return True
