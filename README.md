# ListeMaker

ListeMaker est une application de gestion de listes en console écrite en Python.  
Elle permet de créer, charger, modifier, sauvegarder et supprimer des listes personnalisées stockées sous forme de fichiers JSON.  
Chaque liste est enregistrée dans `modules/data`, garantissant une organisation claire et une persistance automatique.

---

## Fonctionnalités principales

- **Création / Chargement**
  - Chargement automatique si la liste existe déjà.
  - Création d’une nouvelle liste sinon.

- **Gestion des éléments**
  - Ajouter un élément
  - Retirer un élément
  - Vider complètement la liste

- **Affichage**
  - Contenu d’une liste
  - Listes disponibles dans `modules/data`

- **Sauvegarde & Suppression**
  - Sauvegarde en JSON
  - Suppression du fichier JSON associé

- **Normalisation des noms**
  - Suppression automatique des espaces
  - Mise en majuscules de chaque mot
  - Exemple : `liste a` → `ListeA`

---

## Structure du projet

```
ListeMaker/
├── main.py                 # Menu principal et logique utilisateur
└── modules/
    ├── constants.py        # Définition des chemins (DATA_DIR)
    ├── lib.py              # Classe Liste : POO + sauvegarde JSON
    └── data/               # Stockage des fichiers JSON
```

---

## Installation

1. Installer Python 3.10+
2. Aucun module externe n'est requis (seulement la librairie standard).

---

## Utilisation

Dans un terminal, exécutez simplement :

```bash
python main.py
```

Le programme :

1. Affiche les listes existantes
2. Demande d’en choisir une ou d’en créer une nouvelle
3. Affiche un menu :
   ```
   1. Ajouter un élément
   2. Retirer un élément
   3. Afficher la liste
   4. Vider la liste
   5. Supprimer la liste
   6. Quitter
   ```

---

## 📄 Licence

MIT License.
