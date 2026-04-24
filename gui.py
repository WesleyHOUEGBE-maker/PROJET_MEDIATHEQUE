import tkinter as tk
from tkinter import messagebox, ttk
from gestion import Mediatheque
from models import Livre, Vinyle, JeuSociete, Adherent

class MediathequeGUI:
    def __init__(self, root):
        self.app = Mediatheque()
        self.root = root
        self.root.title("Système Gestion Médiathèque - Wesley & Patrice")
        self.root.geometry("1000x800")
        self.root.configure(bg="#f0f2f5")

        # --- TITRE ORIGINAL ---
        header = tk.Frame(root, bg="#1a73e8", pady=15)
        header.pack(fill="x")
        tk.Label(header, text="SYSTÈME GESTION MÉDIATHÈQUE", font=("Helvetica", 20, "bold"), 
                 bg="#1a73e8", fg="white").pack()
       
        # Système d'onglets
        self.tabs = ttk.Notebook(root)
        self.tab_media = tk.Frame(self.tabs, bg="#f0f2f5")
        self.tab_adh = tk.Frame(self.tabs, bg="#f0f2f5")
        self.tabs.add(self.tab_media, text=" 📚 GESTION DU CATALOGUE ")
        self.tabs.add(self.tab_adh, text=" 👤 GESTION DES ADHÉRENTS ")
        self.tabs.pack(fill="both", expand=True, padx=10, pady=10)

        self.setup_tab_media()
        self.setup_tab_adherents()
        self.actualiser_tout()

    def setup_tab_media(self):
        # --- FORMULAIRE D'AJOUT BIEN ALIGNÉ ---
        f_add = tk.LabelFrame(self.tab_media, text=" AJOUTER UN NOUVEAU MÉDIA ", font=("Arial", 10, "bold"), bg="white", padx=15, pady=15)
        f_add.pack(fill="x", padx=15, pady=10)

        # Grille pour les champs
        labels = ["Type:", "ID:", "Titre:", "Créateur:"]
        self.combo_type = ttk.Combobox(f_add, values=["Livre", "Vinyle", "JeuSociete"], state="readonly", width=15)
        self.combo_type.current(0)
        self.combo_type.bind("<<ComboboxSelected>>", self.maj_labels)
        
        self.e_id = ttk.Entry(f_add, width=15)
        self.e_tit = ttk.Entry(f_add, width=25)
        self.e_crea = ttk.Entry(f_add, width=25)

        # Placement Ligne 1
        tk.Label(f_add, text="Type:", bg="white").grid(row=0, column=0, sticky="w")
        self.combo_type.grid(row=0, column=1, padx=5, pady=5)
        tk.Label(f_add, text="ID:", bg="white").grid(row=0, column=2, sticky="w", padx=10)
        self.e_id.grid(row=0, column=3, padx=5)

        # Placement Ligne 2
        tk.Label(f_add, text="Titre:", bg="white").grid(row=1, column=0, sticky="w")
        self.e_tit.grid(row=1, column=1, padx=5, pady=5)
        tk.Label(f_add, text="Créateur:", bg="white").grid(row=1, column=2, sticky="w", padx=10)
        self.e_crea.grid(row=1, column=3, padx=5)

        # Ligne 3 (Dynamique)
        self.l_s1 = tk.Label(f_add, text="ISBN:", bg="white")
        self.l_s1.grid(row=2, column=0, sticky="w")
        self.e_s1 = ttk.Entry(f_add, width=20)
        self.e_s1.grid(row=2, column=1, padx=5, pady=5)

        self.l_s2 = tk.Label(f_add, text="Pages:", bg="white")
        self.l_s2.grid(row=2, column=2, sticky="w", padx=10)
        self.e_s2 = ttk.Entry(f_add, width=20)
        self.e_s2.grid(row=2, column=3, padx=5)

        tk.Button(f_add, text="➕ AJOUTER AU CATALOGUE", bg="#34a853", fg="white", font=("Arial", 10, "bold"), 
                  command=self.ui_ajouter_media, padx=20).grid(row=3, column=0, columnspan=4, pady=10)

        # --- TABLEAU ---
        self.tree_m = ttk.Treeview(self.tab_media, columns=("ID", "Type", "Titre", "Auteur", "Etat"), show='headings')
        for col in ("ID", "Type", "Titre", "Auteur", "Etat"):
            self.tree_m.heading(col, text=col)
            self.tree_m.column(col, anchor="center")
        self.tree_m.pack(fill="both", expand=True, padx=15)

        # --- ACTIONS BAS ---
        f_btns = tk.Frame(self.tab_media, bg="#f0f2f5", pady=10)
        f_btns.pack(fill="x", padx=15)

        tk.Label(f_btns, text="Choisir Adhérent:", bg="#f0f2f5", font=("Arial", 9, "bold")).pack(side="left")
        self.cb_adh = ttk.Combobox(f_btns, state="readonly", width=25)
        self.cb_adh.pack(side="left", padx=10)

        tk.Button(f_btns, text="🤝 EMPRUNTER / RENDRE", bg="#4285f4", fg="white", font=("Arial", 9, "bold"), 
                  command=self.ui_action_emprunt, padx=10).pack(side="left")
        
        tk.Button(f_btns, text="🗑️ SUPPRIMER SÉLECTION", bg="#ea4335", fg="white", font=("Arial", 9, "bold"), 
                  command=self.ui_suppr_media, padx=10).pack(side="right")

    def setup_tab_adherents(self):
        # Section Inscription
        f_adh = tk.LabelFrame(self.tab_adh, text=" INSCRIRE UN NOUVEL ADHÉRENT ", font=("Arial", 10, "bold"), bg="white", padx=15, pady=15)
        f_adh.pack(fill="x", padx=15, pady=10)

        tk.Label(f_adh, text="ID Carte:", bg="white").grid(row=0, column=0)
        self.e_adh_id = ttk.Entry(f_adh, width=15)
        self.e_adh_id.grid(row=0, column=1, padx=5)

        tk.Label(f_adh, text="Nom complet:", bg="white").grid(row=0, column=2, padx=10)
        self.e_adh_nom = ttk.Entry(f_adh, width=30)
        self.e_adh_nom.grid(row=0, column=3, padx=5)

        tk.Button(f_adh, text="👤 CRÉER ADHÉRENT", bg="#1a73e8", fg="white", font=("Arial", 9, "bold"), 
                  command=self.ui_ajouter_adherent, padx=15).grid(row=0, column=4, padx=10)

        # Tableau Adhérents
        self.tree_a = ttk.Treeview(self.tab_adh, columns=("ID", "Nom", "Emprunts"), show='headings')
        for col in ("ID", "Nom", "Emprunts"):
            self.tree_a.heading(col, text=col)
            self.tree_a.column(col, anchor="center")
        self.tree_a.pack(fill="both", expand=True, padx=15, pady=10)

    # --- MÉTHODES LOGIQUES ---
    def maj_labels(self, e=None):
        t = self.combo_type.get()
        self.l_s1.config(text="ISBN:" if t=="Livre" else "Label:" if t=="Vinyle" else "Editeur:")
        self.l_s2.config(text="Pages:" if t=="Livre" else "Pistes:" if t=="Vinyle" else "Âge Min:")

    def actualiser_tout(self):
        for r in self.tree_m.get_children(): self.tree_m.delete(r)
        for m in self.app.catalogue:
            et = "🟢 Dispo" if m.est_disponible else "🔴 Sorti"
            self.tree_m.insert("", "end", values=(m.id, m.__class__.__name__, m.titre, m.createur, et))
        
        for r in self.tree_a.get_children(): self.tree_a.delete(r)
        for a in self.app.adherents:
            self.tree_a.insert("", "end", values=(a.id_carte, a.nom, len(a.liste_emprunts)))
            
        liste = [f"{a.nom} [ID:{a.id_carte}]" for a in self.app.adherents]
        self.cb_adh['values'] = liste
        if liste: self.cb_adh.current(0)

    def ui_ajouter_media(self):
        try:
            id_m = int(self.e_id.get())
            t, tit, crea = self.combo_type.get(), self.e_tit.get(), self.e_crea.get()
            s1, s2 = self.e_s1.get(), int(self.e_s2.get())
            if t == "Livre": m = Livre(id_m, tit, crea, 2024, s1, s2)
            elif t == "Vinyle": m = Vinyle(id_m, tit, crea, 2024, s1, s2)
            else: m = JeuSociete(id_m, tit, crea, 2024, s1, s2)
            self.app.ajouter_media(m); self.actualiser_tout()
        except: messagebox.showerror("Erreur", "Veuillez vérifier les champs numériques.")

    def ui_ajouter_adherent(self):
        try:
            id_a, nom = int(self.e_adh_id.get()), self.e_adh_nom.get()
            if not nom: raise ValueError
            self.app.ajouter_adherent(Adherent(id_a, nom)); self.actualiser_tout()
            self.e_adh_id.delete(0, 'end'); self.e_adh_nom.delete(0, 'end')
        except: messagebox.showerror("Erreur", "Saisie invalide.")

    def ui_action_emprunt(self):
        sel = self.tree_m.selection()
        if not sel: return
        id_m = int(self.tree_m.item(sel)['values'][0])
        media = next((m for m in self.app.catalogue if m.id == id_m), None)
        if media.est_disponible:
            choix = self.cb_adh.get()
            if not choix: return messagebox.showwarning("Info", "Inscrivez un adhérent d'abord.")
            id_a = int(choix.split(':')[-1].replace(']', ''))
            self.app.effectuer_emprunt(id_m, id_a)
        else: self.app.effectuer_retour(id_m)
        self.actualiser_tout()

    def ui_suppr_media(self):
        sel = self.tree_m.selection()
        if sel:
            id_m = int(self.tree_m.item(sel)['values'][0])
            if messagebox.askyesno("Confirmation", f"Supprimer le média {id_m} ?"):
                self.app.supprimer_media(id_m); self.actualiser_tout()

if __name__ == "__main__":
    root = tk.Tk(); gui = MediathequeGUI(root); root.mainloop()
