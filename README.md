# 📚 Projet Médiathèque - IUT Parakou

## 👥 Équipe
* **Wesley HOUEGBE-maker** (@WesleyHOUEGBE-maker) - Chef de projet
* **Patrice AGBODEMAKOU** - Développeur

## 📋 Présentation
Application de gestion de médiathèque développée en Python (POO) dans le cadre de la formation à l'IUT de Parakou sous la direction du **Dr. MOUSSE**.

## 🎯 Objectif du Projet
Développer un système d'inventaire multi-support (Livres, Vinyles, Jeux de société) permettant de gérer efficacement le catalogue, les adhérents et le suivi des emprunts en respectant les principes de la Programmation Orientée Objet.

## 🛠️ Spécifications Techniques
* **Langage** : Python 3.10+
* **Gestionnaire de version** : Git / GitHub
* **Norme de codage** : PEP 8
* **Architecture** : Programmation Orientée Objet (POO) avec modularité (séparation des fichiers)

---

## 🏗️ Architecture Logicielle (Focus POO)

### 📁 Classes de Données (`models.py`)
Le projet suit une hiérarchie d'héritage pour une gestion optimale des médias :
* **Classe Mère : `Media`** (Base commune : id, titre, créateur, année)
* **Classes Filles : `Livre`, `Vinyle`, `JeuSociete`** (Attributs spécifiques et polymorphisme de la méthode `affiche()`)
* **Classe `Adherent`** : Gestion des membres et suivi de leur liste d'emprunts.

### ⚙️ Gestion et Logique (`gestion.py`)
* **Classe `Mediatheque`** : Cœur de l'application gérant le catalogue (ajout/suppression), la recherche et la logique métier des emprunts.

---

## 🚀 État d'avancement (Découpage par Blocs)

### ✅ Bloc 1 : Cahier de charges et spécifications techniques
*Environnement virtuel, Git, types de données de base.*
- [x] **Terminé**

### ✅ Bloc 2 : Workflow & Fondations
*Environnement virtuel, Git, types de données complexes.*
- [x] **Terminé**

### ✅ Bloc 3 : Architecture (POO)
*Classes, héritage, encapsulation, modularité.*
- [x] **Terminé** (Classes créées et fichiers séparés)

### ✅ Bloc 4 : Persistance
*Gestion SQLite ou fichiers JSON/CSV.*
- [x] **Terminé**


### ✅ Bloc 5 : Qualité
*Gestion des exceptions, Tests unitaires avec Pytest.*
- [x] **Terminé**


### ✅ Bloc 6 : Interface & Livraison
*Interface Console avancée (puis GUI Tkinter/PyQt ou Web).*
- [x] **Terminé**
      
