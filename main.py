# On importe tout ce qu'on a créé avant
from models import Livre, Vinyle, JeuSociete, Adherent
from gestion import Mediatheque

# ---LES SOUS-MENUS ---

def sous_menu_livre(app):
    while True:
        print("\n" + "-"*10 + " 📚 LISTE DES LIVRES " + "-"*10)
        app.afficher_par_type(Livre)
        print("-" * 41)
        print("A. Ajouter un livre\nB. Supprimer un livre\nC. Rechercher un livre\nR. Retour")
        c = input("Choix : ").upper()
        if c == "A":
            app.ajouter_media(Livre(int(input("ID: ")), input("Titre: "), input("Auteur: "), input("Année: "), input("ISBN: "), int(input("Pages: "))))
        elif c == "B": app.supprimer_media(int(input("ID à supprimer: ")))
        elif c == "C": app.rechercher_media(input("Titre à chercher: "))
        elif c == "R": break

def sous_menu_vinyle(app):
    while True:
        print("\n" + "-"*10 + " 💿 LISTE DES VINYLES " + "-"*10)
        app.afficher_par_type(Vinyle)
        print("-" * 42)
        print("A. Ajouter un vinyle\nB. Supprimer un vinyle\nC. Rechercher un vinyle\nR. Retour")
        c = input("Choix : ").upper()
        if c == "A":
            app.ajouter_media(Vinyle(int(input("ID: ")), input("Titre: "), input("Artiste: "), input("Année: "), input("Label: "), int(input("Pistes: "))))
        elif c == "B": app.supprimer_media(int(input("ID à supprimer: ")))
        elif c == "C": app.rechercher_media(input("Titre à chercher: "))
        elif c == "R": break

def sous_menu_jeu(app):
    while True:
        print("\n" + "-"*10 + " 🎲 LISTE DES JEUX " + "-"*10)
        app.afficher_par_type(JeuSociete)
        print("-" * 39)
        print("A. Ajouter un jeu\nB. Supprimer un jeu\nC. Rechercher un jeu\nR. Retour")
        c = input("Choix : ").upper()
        if c == "A":
            app.ajouter_media(JeuSociete(int(input("ID: ")), input("Nom: "), input("Créateur: "), input("Année: "), input("Editeur: "), int(input("Age min: "))))
        elif c == "B": app.supprimer_media(int(input("ID à supprimer: ")))
        elif c == "C": app.rechercher_media(input("Titre à chercher: "))
        elif c == "R": break

def sous_menu_adherent(app):
    while True:
        print("\n" + "-"*10 + " 👤 LISTE DES ADHÉRENTS " + "-"*10)
        if not app.adherents: print("Aucun adhérent inscrit.")
        for a in app.adherents: print(f"ID:{a.id_carte} | Nom:{a.nom}")
        print("-" * 44)
        print("A. Ajouter un adhérent\nB. Supprimer un adhérent\nR. Retour")
        c = input("Choix : ").upper()
        if c == "A": app.ajouter_adherent(Adherent(int(input("ID Carte: ")), input("Nom: ")))
        elif c == "B": app.supprimer_adherent(int(input("ID à supprimer: ")))
        elif c == "R": break

# --- MENU PRINCIPAL (Le cœur du lancement) ---

def menu_principal():
    app = Mediatheque() # On initialise la médiathèque
    while True:
        print("\n" + "═"*35 + "\n    SYSTÈME GESTION MÉDIATHÈQUE\n" + "═"*35)
        print("1. Gestion des Livres\n2. Gestion des Vinyles\n3. Gestion des Jeux\n4. Voir TOUT le catalogue\n5. Gestion des Adhérents\n6. Faire un Emprunt\nQ. Quitter")
        choix = input("\nAction : ").upper()
        
        if choix == "1": sous_menu_livre(app)
        elif choix == "2": sous_menu_vinyle(app)
        elif choix == "3": sous_menu_jeu(app)
        elif choix == "4": app.rechercher_media("") # Recherche vide = tout afficher
        elif choix == "5": sous_menu_adherent(app)
        elif choix == "6": 
            # 1. On affiche l'état complet du catalogue par catégorie
            print("\n" + "="*15 + " ÉTAT DES DISPONIBILITÉS " + "="*15)
            
            print("\n📚 [LIVRES]")
            app.afficher_par_type(Livre)
            
            print("\n💿 [VINYLES]")
            app.afficher_par_type(Vinyle)
            
            print("\n🎲 [JEUX DE SOCIÉTÉ]")
            app.afficher_par_type(JeuSociete)
            
            print("\n" + "="*45)
            
            # 2. On demande les IDs pour l'emprunt
            id_m = int(input("\nEntrez l'ID du média : "))
            id_a = int(input("Entrez l'ID de l'adhérent : "))
            
            # 3. La logique dans gestion.py s'occupe de vérifier si c'est dispo ou non
            app.effectuer_emprunt(id_m, id_a)

        elif choix == "Q": 
            print("👋 Au revoir !")
            break

if __name__ == "__main__" :
    menu_principal()