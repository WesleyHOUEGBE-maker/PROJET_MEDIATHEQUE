import json
import os
from models import Livre, Vinyle, JeuSociete, Adherent

class Mediatheque:
    def __init__(self):
        self.catalogue = []
        self.adherents = []
        self.charger_donnees()

    # --- PERSISTANCE (BLOC 4) ---
    def sauvegarder_donnees(self):
        data = {
            "catalogue": [],
            "adherents": []
        }
        for m in self.catalogue:
            dict_m = vars(m).copy()
            dict_m["type_classe"] = m.__class__.__name__
            data["catalogue"].append(dict_m)
        
        for a in self.adherents:
            data["adherents"].append({
                "id_carte": a.id_carte,
                "nom": a.nom,
                "emprunts_ids": [m.id for m in a.liste_emprunts]
            })

        with open("database.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def charger_donnees(self):
        if not os.path.exists("database.json"):
            return
        try:
            with open("database.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                for m in data["catalogue"]:
                    t = m.pop("type_classe")
                    if t == "Livre": self.catalogue.append(Livre(**m))
                    elif t == "Vinyle": self.catalogue.append(Vinyle(**m))
                    elif t == "JeuSociete": self.catalogue.append(JeuSociete(**m))

                for a_data in data["adherents"]:
                    nouvel_adh = Adherent(a_data["id_carte"], a_data["nom"])
                    for m_id in a_data["emprunts_ids"]:
                        media = next((m for m in self.catalogue if m.id == m_id), None)
                        if media: nouvel_adh.liste_emprunts.append(media)
                    self.adherents.append(nouvel_adh)
        except Exception as e:
            print(f"Erreur chargement: {e}")

    # --- MÉDIAS ---
    def ajouter_media(self, media):
        self.catalogue.append(media)
        self.sauvegarder_donnees()
        print(f"\n✅ '{media.titre}' ajouté.")

    def supprimer_media(self, id_m):
        self.catalogue = [m for m in self.catalogue if m.id != id_m]
        self.sauvegarder_donnees()
        print(f"\n🗑️ Média {id_m} supprimé.")

    def rechercher_media(self, titre):
        resultats = [m for m in self.catalogue if titre.lower() in m.titre.lower()]
        for r in resultats: print(r.affiche())
        if not resultats: print("❌ Aucun résultat.")

    def afficher_par_type(self, type_classe):
        trouve = False
        for m in self.catalogue:
            if isinstance(m, type_classe):
                print(m.affiche()); trouve = True
        if not trouve: print("📂 Vide.")

    # --- ADHÉRENTS ---
    def ajouter_adherent(self, adh):
        self.adherents.append(adh)
        self.sauvegarder_donnees()
        print(f"\n👤 Adhérent '{adh.nom}' inscrit.")

    # --- EMPRUNTS & RETOURS (MANQUANTS) ---
    def effectuer_emprunt(self, id_m, id_a):
        m = next((m for m in self.catalogue if m.id == id_m), None)
        a = next((a for a in self.adherents if a.id_carte == id_a), None)
        if m and a and m.est_disponible:
            m.est_disponible = False
            a.liste_emprunts.append(m)
            self.sauvegarder_donnees()
            print(f"🤝 Emprunt réussi : {m.titre}")
        else:
            print("❌ Impossible d'emprunter (ID incorrect ou déjà pris).")

    def effectuer_retour(self, id_m):
        m = next((m for m in self.catalogue if m.id == id_m), None)
        if m and not m.est_disponible:
            m.est_disponible = True
            for a in self.adherents:
                if m in a.liste_emprunts: a.liste_emprunts.remove(m)
            self.sauvegarder_donnees()
            print(f"✅ Retour réussi : {m.titre}")
        else:
            print("❌ Ce média n'était pas emprunté.")
