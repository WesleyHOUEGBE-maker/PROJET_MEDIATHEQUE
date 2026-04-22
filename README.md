# 📚 Projet Médiathèque - IUT Parakou

## 👥 Équipe
* **Wesley HOUEGBE-maker** (Chef de projet)
* **Patrice** (Développeur)

## 📋 Présentation
Application de gestion de médiathèque développée en Python (POO) dans le cadre de la formation à l'IUT de Parakou.

## 🛠️ Spécifications Techniques
* **Langage** : Python 3.10+
* **Gestionnaire de version** : Git / GitHub
* **Environnement** : Virtualenv (`venv`)
* **Architecture** : Programmation Orientée Objet (POO)

## 🏗️ Architecture Logicielle (Modèles)

### 📁 Classes de Données
Le projet suit une hiérarchie d'héritage stricte pour la gestion des médias :

* **Classe Mère : `Media`**
    * Attributs : `id`, `titre`, `createur`, `annee_sortie`, `est_disponible`
* **Classe Fille : `Livre`**
    * Attributs spécifiques : `isbn`, `nb_pages`
* **Classe Fille : `Vinyle`**
    * Attributs spécifiques : `label`, `nb_pistes`
* **Classe Fille : `JeuSociete`**
    * Attributs spécifiques : `editeur`, `age_minimum`

### ⚙️ Gestion et Logique
* **Classe `Adherent`** : Gère les informations des membres et leur liste d'emprunts.
* **Classe `Mediatheque`** : Cœur de l'application gérant le catalogue et la logique métier.
* **Classe `DatabaseManager`** : (Prévue pour le Bloc 5) Assure la persistance des données via SQLite.

## 🚀 État d'avancement
- [x] Bloc 1 : Configuration de l'environnement (Venv, Git)
- [x] Bloc 2 : Cahier des charges et Workflow GitHub
- [ ] Bloc 3 : Architecture POO (En cours)
- [ ] Bloc 4 : Menu Interactif
- [ ] Bloc 5 : Persistance SQLite
      
