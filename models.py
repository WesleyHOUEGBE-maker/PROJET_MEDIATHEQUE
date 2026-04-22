#==========================================
# PROJET MÉDIATHÈQUE - ARCHITECTURE POO
# Développé par Wesley & Patrice
# ==========================================

# Ici, je crée la classe "Mère". C'est le moule général pour tous nos objets.
class Media:
    def __init__(self, id, titre, createur, annee):
        # On définit les caractéristiques de base que TOUS les médias partagent
        self.id = id
        self.titre = titre
        self.createur = createur
        self.annee = annee
        # Par défaut, quand on ajoute un média, il est disponible
        self.est_disponible = True

    # Ma méthode pour afficher les infos de base proprement
    def affiche(self):
        # Petite condition pour transformer le True/False en texte clair
        etat = "Disponible" if self.est_disponible else "Emprunté"
        return f"[{self.id}] {self.titre} - {self.createur} ({self.annee}) | Etat: {etat}"

# Ici, Livre hérite de Media (on utilise ce que la maman a déjà fait)
class Livre(Media):
    def __init__(self, id, titre, createur, annee, isbn, nb_pages):
        # super() veut dire : "Va chercher le constructeur de Media" 
        # pour ne pas avoir à réécrire id, titre, etc.
        super().__init__(id, titre, createur, annee)
        # On ajoute seulement ce qui est spécifique aux livres
        self.isbn = isbn
        self.nb_pages = nb_pages

    def affiche(self):
        # On appelle l'affichage de base de Media
        base = super().affiche()
        # Et on colle les infos du livre juste à la suite
        return f"{base} | ISBN: {self.isbn}, Pages: {self.nb_pages}"

# Même logique pour les Vinyles
class Vinyle(Media):
    def __init__(self, id, titre, createur, annee, label, nb_pistes):
        super().__init__(id, titre, createur, annee)
        self.label = label
        self.nb_pistes = nb_pistes

    def affiche(self):
        base = super().affiche()
        return f"{base} | Label: {self.label}, Pistes: {self.nb_pistes}"

# Enfin, les Jeux de Société
class JeuSociete(Media):
    def __init__(self, id, titre, createur, annee, editeur, age_min):
        super().__init__(id, titre, createur, annee)
        self.editeur = editeur
        self.age_min = age_min

    def affiche(self):
        base = super().affiche()
        return f"{base} | Editeur: {self.editeur}, Age min: {self.age_min} ans"

class Adherent:
    def __init__(self, id_carte, nom):
        self.id_carte = id_carte
        self.nom = nom
        # On crée une liste vide pour stocker les médias que cet adhérent va emprunter
        self.liste_emprunts = []

    def affiche_infos(self):
        return f"Carte N°{self.id_carte} | Nom : {self.nom} ({len(self.liste_emprunts)} emprunts en cours)"        
