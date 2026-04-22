from models import Livre, Vinyle, JeuSociete, Adherent

class Mediatheque:
    def __init__(self):
        self.catalogue = []
        self.adherents = []

    # --- GESTION DES MÉDIAS ---
    def ajouter_media(self, media):
        self.catalogue.append(media)
        print(f"\n✅ '{media.titre}' ajouté au catalogue.")

    def supprimer_media(self, id_m):
        avant = len(self.catalogue)
        self.catalogue = [m for m in self.catalogue if m.id != id_m]
        if len(self.catalogue) < avant:
            print(f"\n🗑️ Média avec l'ID {id_m} supprimé avec succès.")
        else:
            print(f"\n⚠️ ID {id_m} introuvable dans le catalogue.")

    def rechercher_media(self, titre):
        print(f"\n🔍 --- Recherche de : '{titre}' ---")
        resultats = [m for m in self.catalogue if titre.lower() in m.titre.lower()]
        for r in resultats: 
            print(r.affiche())
        if not resultats: 
            print("❌ Aucun média trouvé pour cette recherche.")

    def afficher_par_type(self, type_classe):
        """Affiche uniquement les médias d'un certain type"""
        trouve = False
        for m in self.catalogue:
            if isinstance(m, type_classe):
                print(m.affiche())
                trouve = True
        if not trouve: 
            print("📂 Aucun élément enregistré dans cette catégorie.")

    # --- GESTION DES ADHÉRENTS ---
    def ajouter_adherent(self, adh):
        self.adherents.append(adh)
        print(f"\n👤 Adhérent '{adh.nom}' inscrit avec succès.")

    def supprimer_adherent(self, id_a):
        avant = len(self.adherents)
        self.adherents = [a for a in self.adherents if a.id_carte != id_a]
        if len(self.adherents) < avant:
            print(f"\n🗑️ Adhérent avec la carte {id_a} supprimé.")
        else:
            print(f"\n⚠️ ID Adhérent {id_a} introuvable.")

    # --- LOGIQUE D'EMPRUNT ---
    def effectuer_emprunt(self, id_m, id_a):
        m = next((m for m in self.catalogue if m.id == id_m), None)
        a = next((a for a in self.adherents if a.id_carte == id_a), None)
        
        if m and a:
            if m.est_disponible:
                m.est_disponible = False
                a.liste_emprunts.append(m)
                print(f"\n🤝 EMPRUNT : {a.nom} a pris '{m.titre}'.")
            else: 
                print("\n🚫 Ce média est déjà emprunté par quelqu'un d'autre.")
        else: 
            print("\n❌ Erreur : ID Média ou ID Adhérent incorrect.")