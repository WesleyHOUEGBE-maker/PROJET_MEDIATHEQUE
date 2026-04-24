import tkinter as tk
from tkinter import messagebox, ttk
from gestion import Mediatheque
from models import Livre, Vinyle, JeuSociete, Adherent

class MediathequeGUI:
    def __init__(self, root):
        self.app = Mediatheque()
        self.root = root
        self.root.title("Médiathèque Pro - Wesley & Patrice")
        self.root.geometry("1000x750")
        self.root.configure(bg="#f0f2f5")

        # --- TITRE PRINCIPAL ---
        tk.Label(root, text="📚 GESTION MÉDIATHÈQUE", font=("Helvetica", 22, "bold"), 
                 bg="#1a73e8", fg="white", pady=10).pack(fill="x")

        # --- SYSTÈME D'ONGLETS ---
        self.tabs = ttk.Notebook(root)
        self.tab_media = tk.Frame(self.tabs, bg="#f0f2f5")
        self.tab_adh = tk.Frame(self.tabs, bg="#f0f2f5")
        
        self.tabs.add(self.tab_media, text=" 💿 CATALOGUE & EMPRUNTS ")
        self.tabs.add(self.tab_adh, text=" 👤 GESTION ADHÉRENTS ")
        self.tabs.pack(fill="both", expand=True, padx=10, pady=10)

        self.setup_tab_media()
        self.setup_tab_adherents()
        self.actualiser_tout()

    # ==========================================
    # ONGLET 1 : MÉDIAS
    # ==========================================
    def setup_tab_media(self):
        # Formulaire d'ajout
        self.frame_f = tk.LabelFrame(self.tab_media, text=" AJOUTER MÉDIA ", font=("Arial", 10, "bold"), bg="white", padx=10, pady=10)
        self.frame_f.pack(fill="x", padx=10, pady=5)

        self.combo_type = ttk.Combobox(self.frame_f, values=["Livre", "Vinyle", "JeuSociete"], state="readonly", width=12)
        self.combo_type.grid(row=0, column=0, padx=5); self.combo_type.current(0)
        self.combo_type.bind("<<ComboboxSelected>>", self.maj_labels)

        self.e_id = tk.Entry(self.frame_f, width=10); self.e_id.grid(row=0, column=1, padx=5)
        self.e_tit = tk.Entry(self.frame_f, width=20); self.e_tit.grid(row=0, column=2, padx=5)
        self.e_crea = tk.Entry(self.frame_f, width=20); self.e_crea.grid(row=0, column=3, padx=5)
        
        # Champs dynamiques (Labels changés par maj_labels)
        self.l_s1 = tk.Label(self.frame_f, text="ISBN:", bg="white"); self.l_s1.grid(row=1, column=0)
        self.e_s1 = tk.Entry(self.frame_f, width=15); self.e_s1.grid(row=1, column=1)
        self.l_s2 = tk.Label(self.frame_f, text="Pages:", bg="white"); self.l_s2.grid(row=1, column=2)
        self.e_s2 = tk.Entry(self.frame_f, width=15); self.e_s2.grid(row=1, column=3)

        tk.Button(self.frame_f, text="Ajouter", bg="#34a853", fg="white", command=self.ui_ajouter_media).grid(row=1, column=4, padx=10)

        # Tableau
        self.tree_m = ttk.Treeview(self.tab_media, columns=("ID", "Type", "Titre", "Auteur", "Etat"), show='headings')
        for col in ("ID", "Type", "Titre", "Auteur", "Etat"): self.tree_m.heading(col, text=col)
        self.tree_m.pack(fill="both", expand=True, padx=10, pady=5)

        # Actions Emprunts
        f_act = tk.Frame(self.tab_media, bg="#f0f2f5")
        f_act.pack(fill="x", padx=10, pady=5)
        self.cb_adh = ttk.Combobox(f_act, state="readonly", width=25)
        self.cb_adh.pack(side="left", padx=5)
        tk.Button(f_act, text="EMPRUNTER / RENDRE", bg="#4285f4", fg="white", command=self.ui_action_emprunt).pack(side="left", padx=5)
        tk.Button(f_act, text="SUPPRIMER", bg="#ea4335", fg="white", command=self.ui_suppr_media).pack(side="right", padx=5)

    # ==========================================
    # ONGLET 2 : ADHÉRENTS (NOUVEAU)
    # ==========================================
    def setup_tab_adherents(self):
        f_inscr = tk.LabelFrame(self.tab_adh, text=" NOUVEL ADHÉRENT ", font=("Arial", 10, "bold"), bg="white", padx=20, pady=20)
        f_inscr.pack(fill="x", padx=10, pady=10)

        tk.Label(f_inscr, text="N° Carte (ID) :", bg="white").grid(row=0, column=0)
        self.e_adh_id = tk.Entry(f_inscr, width=15)
        self.e_adh_id.grid(row=0, column=1, padx=10)

        tk.Label(f_inscr, text="Nom Complet :", bg="white").grid(row=0, column=2)
        self.e_adh_nom = tk.Entry(f_inscr, width=30)
        self.e_adh_nom.grid(row=0, column=3, padx=10)

        tk.Button(f_inscr, text="INSCRIPTIION", bg="#1a73e8", fg="white", padx=20, command=self.ui_ajouter_adherent).grid(row=0, column=4, padx=10)

        # Liste des adhérents
        self.tree_a = ttk.Treeview(self.tab_adh, columns=("ID", "Nom", "Emprunts"), show='headings')
        self.tree_a.heading("ID", text="N° CARTE"); self.tree_a.heading("Nom", text="NOM"); self.tree_a.heading("Emprunts", text="NB EMPRUNTS")
        self.tree_a.pack(fill="both", expand=True, padx=10, pady=10)

    # ==========================================
    # LOGIQUE & ACTIONS
    # ==========================================
    def maj_labels(self, e=None):
        t = self.combo_type.get()
        self.l_s1.config(text="ISBN:" if t=="Livre" else "Label:" if t=="Vinyle" else "Editeur:")
        self.l_s2.config(text="Pages:" if t=="Livre" else "Pistes:" if t=="Vinyle" else "Âge Min:")

    def ui_ajouter_adherent(self):
        try:
            id_a, nom = int(self.e_adh_id.get()), self.e_adh_nom.get()
            if not nom: raise ValueError
            self.app.ajouter_adherent(Adherent(id_a, nom))
            self.actualiser_tout()
            self.e_adh_id.delete(0, 'end'); self.e_adh_nom.delete(0, 'end')
        except: messagebox.showerror("Erreur", "Saisie invalide")

    def ui_ajouter_media(self):
        try:
            id_m, t, tit, crea = int(self.e_id.get()), self.combo_type.get(), self.e_tit.get(), self.e_crea.get()
            s1, s2 = self.e_s1.get(), int(self.e_s2.get())
            if t == "Livre": m = Livre(id_m, tit, crea, 2024, s1, s2)
            elif t == "Vinyle": m = Vinyle(id_m, tit, crea, 2024, s1, s2)
            else: m = JeuSociete(id_m, tit, crea, 2024, s1, s2)
            self.app.ajouter_media(m); self.actualiser_tout()
        except: messagebox.showerror("Erreur", "Saisie invalide")

    def ui_action_emprunt(self):
        sel = self.tree_m.selection()
        if not sel: return
        id_m = int(self.tree_m.item(sel)['values'][0])
        media = next((m for m in self.app.catalogue if m.id == id_m), None)
        if media.est_disponible:
            choix = self.cb_adh.get()
            if not choix: return messagebox.showwarning("Info", "Sélectionnez un adhérent")
            id_a = int(choix.split(':')[-1].replace(']', ''))
            self.app.effectuer_emprunt(id_m, id_a)
        else: self.app.effectuer_retour(id_m)
        self.actualiser_tout()

    def ui_suppr_media(self):
        sel = self.tree_m.selection()
        if sel: self.app.supprimer_media(int(self.tree_m.item(sel)['values'][0])); self.actualiser_tout()

    def actualiser_tout(self):
        # Table Médias
        for r in self.tree_m.get_children(): self.tree_m.delete(r)
        for m in self.app.catalogue:
            et = "🟢 Dispo" if m.est_disponible else "🔴 Sorti"
            self.tree_m.insert("", "end", values=(m.id, m.__class__.__name__, m.titre, m.createur, et))
        # Table Adhérents
        for r in self.tree_a.get_children(): self.tree_a.delete(r)
        for a in self.app.adherents:
            self.tree_a.insert("", "end", values=(a.id_carte, a.nom, len(a.liste_emprunts)))
        # Combobox Adhérents
        liste = [f"{a.nom} [ID:{a.id_carte}]" for a in self.app.adherents]
        self.cb_adh['values'] = liste
        if liste: self.cb_adh.current(0)

if __name__ == "__main__":
    root = tk.Tk(); app = MediathequeGUI(root); root.mainloop()
