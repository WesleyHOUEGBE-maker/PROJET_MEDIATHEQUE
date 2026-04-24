from models import Livre, Vinyle, JeuSociete, Adherent
from gestion import Mediatheque

def saisie_int(message):
    while True:
        try: return int(input(message))
        except ValueError: print("⚠️ Entrez un nombre !")

def sous_menu_livre(app):
    while True:
        print("\n--- 📚 LIVRES ---")
        app.afficher_par_type(Livre)
        print("A. Ajouter | B. Supprimer | R. Retour")
        c = input("Choix : ").upper()
        if c == "A":
            app.ajouter_media(Livre(saisie_int("ID: "), input("Titre: "), input("Auteur: "), input("Année: "), input("ISBN: "), saisie_int("Pages: ")))
        elif c == "B": app.supprimer_media(saisie_int("ID: "))
        elif c == "R": break

def menu_principal():
    app = Mediatheque()
    while True:
        print("\n" + "═"*30 + "\n  GESTION MÉDIATHÈQUE\n" + "═"*30)
        print("1. Livres | 2. Vinyles | 3. Jeux | 4. Catalogue | 5. Adhérents\n6. EMPRUNTER | 7. RENDRE | Q. Quitter")
        choix = input("\nAction : ").upper()
        
        if choix == "1": sous_menu_livre(app)
        # ... (ajoutez ici les autres sous-menus sur le même modèle)
        elif choix == "4": app.rechercher_media("")
        elif choix == "5": 
            print("A. Ajouter Adhérent | B. Liste")
            opt = input("Choix : ").upper()
            if opt == "A": app.ajouter_adherent(Adherent(saisie_int("ID: "), input("Nom: ")))
            else: [print(f"ID:{a.id_carte} | {a.nom}") for a in app.adherents]
        elif choix == "6": app.effectuer_emprunt(saisie_int("ID Média: "), saisie_int("ID Adhérent: "))
        elif choix == "7": app.effectuer_retour(saisie_int("ID Média à rendre: "))
        elif choix == "Q": break

if __name__ == "__main__":
    menu_principal()
