# ==========================================
# PROJET MÉDIATHÈQUE - MODELS (Mis à jour Bloc 4 & 6)
# Développé par Wesley & Patrice
# ==========================================

class Media:
    def __init__(self, id, titre, createur, annee, est_disponible=True):
        # On accepte maintenant est_disponible en paramètre pour le rechargement JSON
        self.id = id
        self.titre = titre
        self.createur = createur
        self.annee = annee
        self.est_disponible = est_disponible

    def affiche(self):
        etat = "Disponible" if self.est_disponible else "Emprunté"
        return f"[{self.id}] {self.titre} - {self.createur} ({self.annee}) | Etat: {etat}"

class Livre(Media):
    def __init__(self, id, titre, createur, annee, isbn, nb_pages, est_disponible=True):
        # On passe est_disponible au parent
        super().__init__(id, titre, createur, annee, est_disponible)
        self.isbn = isbn
        self.nb_pages = nb_pages

    def affiche(self):
        base = super().affiche()
        return f"{base} | ISBN: {self.isbn}, Pages: {self.nb_pages}"

class Vinyle(Media):
    def __init__(self, id, titre, createur, annee, label, nb_pistes, est_disponible=True):
        super().__init__(id, titre, createur, annee, est_disponible)
        self.label = label
        self.nb_pistes = nb_pistes

    def affiche(self):
        base = super().affiche()
        return f"{base} | Label: {self.label}, Pistes: {self.nb_pistes}"

class JeuSociete(Media):
    def __init__(self, id, titre, createur, annee, editeur, age_min, est_disponible=True):
        super().__init__(id, titre, createur, annee, est_disponible)
        self.editeur = editeur
        self.age_min = age_min

    def affiche(self):
        base = super().affiche()
        return f"{base} | Editeur: {self.editeur}, Age min: {self.age_min} ans"

class Adherent:
    def __init__(self, id_carte, nom):
        self.id_carte = id_carte
        self.nom = nom
        self.liste_emprunts = []

    def affiche_infos(self):
        return f"Carte N°{self.id_carte} | Nom : {self.nom} ({len(self.liste_emprunts)} emprunts)"
