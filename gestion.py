import json
import os
from models import Livre, Vinyle, JeuSociete, Adherent

class Mediatheque:
    def __init__(self):
        self.catalogue = []
        self.adherents = []
        self.charger_donnees()  # Charge les données au lancement

    # --- PERSISTANCE (BLOC 4) ---
    def sauvegarder_donnees(self):
        """Enregistre le catalogue et les adhérents dans un fichier JSON"""
        data = {
            "catalogue": [],
            "adherents": []
        }
        
        # On convertit les objets médias en dictionnaires avec une clé "type"
        for m in self.catalogue:
            dict_m = vars(m).copy()
            dict_m["type_classe"] = m.__class__.__name__
            data["catalogue"].append(dict_m)
        
        # On convertit les adhérents
        for a in self.adherents:
            dict_a = {
                "id_carte": a.id_carte,
                "nom": a.nom,
                "emprunts_ids": [m.id for m in a.liste_emprunts] # On ne stocke que les IDs
            }
            data["adherents"].append(dict_a)

        with open("database.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def charger_donnees(self):
        """Récupère les données du fichier JSON au démarrage"""
        if not os.path.exists("database.json"):
            return

        try:
            with open("database.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                
                # Reconstruction du catalogue
                for m in data["catalogue"]:
                    t = m.pop("type_classe")
                    if t == "Livre": self.catalogue.append(Livre(**m))
                    elif t == "Vinyle": self.catalogue.append(Vinyle(**m))
                    elif t == "JeuSociete": self.catalogue.append(JeuSociete(**m))

                # Reconstruction des adhérents
                for a_data in data["adherents"]:
                    nouvel_adh = Adherent(a_data["id_carte"], a_data["nom"])
                    # On relie les emprunts par ID
                    for m_id in a_data["emprunts_ids"]:
                        media = next((m for m in self.catalogue if m.id == m_id), None)
                        if media:
                            nouvel_adh.liste_emprunts.append(media)
                    self.adherents.append(nouvel_adh)
        except Exception as e:
            print(f"Erreur lors du chargement : {e}")

    # --- GESTION DES MÉDIAS ---
    def ajouter_media(self, media):
        self.catalogue.append(media)
        self.sauvegarder_donnees()
        print(f"\n✅ '{media.titre}' ajouté au catalogue.")

    def supprimer_media(self, id_m):
        avant = len(self.catalogue)
        self.catalogue = [m for m in self.catalogue if m.id != id_m]
        if len(self.catalogue) < avant:
            self.sauvegarder_donnees()
            print(f"\n🗑️ Média avec l'ID {id_m} supprimé avec succès.")
        else:
            print(f"\n⚠️ ID {id_m} introuvable.")

    def rechercher_media(self, titre):
        print(f"\n🔍 --- Recherche de : '{titre}' ---")
        resultats = [m for m in self.catalogue if titre.lower() in m.titre.lower()]
        for r in resultats: 
            print(r.affiche())
        if not resultats: 
            print("❌ Aucun média trouvé.")

    def afficher_par_type(self, type_classe):
        trouve = False
        for m in self.catalogue:
            if isinstance(m, type_classe):
                print(m.affiche())
                trouve = True
        if not trouve: 
            print("📂 Aucun élément dans cette catégorie.")

    # --- GESTION DES ADHÉRENTS ---
    def ajouter_adherent(self, adh):
        self.adherents.append(adh)
        self.sauvegarder_donnees()
        print(f"\n👤 Adhérent '{adh.nom}' inscrit.")

    def supprimer_adherent(self, id_a):
        avant = len(self.adherents)
        self.adherents = [a for a in self.adherents if a.id_carte != id_a]
        if len(self.adherents) < avant:
            self.sauvegarder_donnees()
            print(f"\n🗑️ Adhérent {id_a} supprimé.")
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
                self.sauvegarder_donnees()
                print(f"\n🤝 EMPRUNT : {a.nom} a pris '{m.titre}'.")
            else: 
                print("\n🚫 Déjà emprunté.")
        else: 
            print("\n❌ Erreur ID.")
