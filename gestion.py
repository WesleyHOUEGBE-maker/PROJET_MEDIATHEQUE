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
        """Enregistre tout dans database.json"""
        data = {
            "catalogue": [],
            "adherents": []
        }
        
        # Conversion des médias
        for m in self.catalogue:
            dict_m = vars(m).copy()
            dict_m["type_classe"] = m.__class__.__name__
            data["catalogue"].append(dict_m)
        
        # Conversion des adhérents (on ne stocke que les IDs des emprunts)
        for a in self.adherents:
            data["adherents"].append({
                "id_carte": a.id_carte,
                "nom": a.nom,
                "emprunts_ids": [m.id for m in a.liste_emprunts]
            })

        with open("database.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def charger_donnees(self):
        """Reconstruit les objets et les liens d'emprunt au démarrage"""
        if not os.path.exists("database.json"):
            return
        try:
            with open("database.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                
                # 1. On recrée les objets médias
                self.catalogue = []
                for m in data.get("catalogue", []):
                    t = m.pop("type_classe")
                    if t == "Livre": self.catalogue.append(Livre(**m))
                    elif t == "Vinyle": self.catalogue.append(Vinyle(**m))
                    elif t == "JeuSociete": self.catalogue.append(JeuSociete(**m))

                # 2. On recrée les adhérents et on relie les emprunts
                self.adherents = []
                for a_data in data.get("adherents", []):
                    nouvel_adh = Adherent(a_data["id_carte"], a_data["nom"])
                    for m_id in a_data.get("emprunts_ids", []):
                        # On retrouve l'objet média par son ID
                        media = next((m for m in self.catalogue if m.id == m_id), None)
                        if media:
                            nouvel_adh.liste_emprunts.append(media)
                    self.adherents.append(nouvel_adh)
        except Exception as e:
            print(f"Erreur chargement : {e}")

    # --- GESTION MÉDIAS ---
    def ajouter_media(self, media):
        self.catalogue.append(media)
        self.sauvegarder_donnees()

    def supprimer_media(self, id_m):
        self.catalogue = [m for m in self.catalogue if m.id != id_m]
        self.sauvegarder_donnees()

    def rechercher_media(self, titre):
        return [m for m in self.catalogue if titre.lower() in m.titre.lower()]

    # --- GESTION ADHÉRENTS ---
    def ajouter_adherent(self, adh):
        self.adherents.append(adh)
        self.sauvegarder_donnees()

    # --- LOGIQUE EMPRUNT / RETOUR ---
    def effectuer_emprunt(self, id_m, id_a):
        m = next((m for m in self.catalogue if m.id == id_m), None)
        a = next((a for a in self.adherents if a.id_carte == id_a), None)
        
        if m and a and m.est_disponible:
            m.est_disponible = False
            a.liste_emprunts.append(m)
            self.sauvegarder_donnees()
            return True
        return False

    def effectuer_retour(self, id_m):
        m = next((m for m in self.catalogue if m.id == id_m), None)
        if m and not m.est_disponible:
            m.est_disponible = True
            # On le retire de la liste de l'adhérent
            for a in self.adherents:
                if m in a.liste_emprunts:
                    a.liste_emprunts.remove(m)
            self.sauvegarder_donnees()
            return True
        return False
