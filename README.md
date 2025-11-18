# Module Gestion du Patrimoine - Odoo 17

## 📦 Structure du Module

```
gestion_patrimoine/
├── __manifest__.py
├── __init__.py
├── models/
│   ├── __init__.py
│   ├── patrimoine_actif.py              # ⭐ Modèle principal
│   ├── etat.py                          # États possibles
│   ├── etat_patrimoine_actif.py         # Historique des états
│   ├── patrimoine_geographique.py       # Localisations
│   ├── unite.py                         # Unités organisationnelles
│   ├── type_unite.py                    # Types d'unités
│   ├── type_patrimoine.py               # Types de patrimoine
│   ├── personnel.py                     # Personnel
│   ├── categorie_personnel.py           # Catégories de personnel
│   ├── categorie_patrim_actif.py        # Catégories de patrimoine
│   ├── fournisseur.py                   # Fournisseurs
│   ├── marque.py                        # Marques
│   ├── famille.py                       # Familles de patrimoine
│   └── sous_famille.py                  # Sous-familles
├── views/
│   ├── patrimoine_actif_views.xml       # Vues principales
│   ├── fournisseur_personnel_unite_views.xml
│   ├── type_unite_views.xml
│   ├── configuration_views.xml          # Toutes les configs
│   └── menu_views.xml                   # Menus
├── security/
│   └── ir.model.access.csv              # Droits d'accès
└── data/
    └── demo_data.xml                    # Données de démonstration
```

---

## 🎯 Modèles et Relations

### 🏆 Modèle Central : **PatrimoineActif**

Le patrimoine actif est le cœur du module. Il représente un bien physique de l'entreprise avec toutes ses caractéristiques.

**Champs principaux** :
- **Identification** : code, désignation
- **Finances** : valeur_acquisition, date_acquisition, date_mise_service
- **Documents** : n_BC, n_BL, n_Facture
- **Sécurité** : image_actif, consigne_securite, degre_importance

**Relations (Many2one - facultatives 0..1)** :
- `etat_id` → **Etat** : État actuel du patrimoine
- `fournisseur_id` → **Fournisseur** : Qui a fourni le bien
- `categorie_id` → **CategoriePatrimActif** : Classification
- `famille_id` → **Famille** : Grande catégorie
- `sous_famille_id` → **SousFamille** : Sous-catégorie (dépend de famille)
- `marque_id` → **Marque** : Marque du bien
- `type_patrimoine_id` → **TypePatrimoine** : Type général
- `patrimoine_geographique_id` → **PatrimoineGeographique** : Localisation physique
- `unite_id` → **Unite** : Service affectataire

**Relation One2many** :
- `etat_patrimoine_actif_ids` → **EtatPatrimoineActif** : Historique complet des états

---

### 📊 Logique des Relations

#### 1️⃣ **Classification Hiérarchique**

```
TypePatrimoine (ex: Informatique)
    └── CategoriePatrimActif (ex: Matériel Info)
            └── Famille (ex: Ordinateurs)
                    └── SousFamille (ex: PC Fixe)
                            └── Marque (ex: Dell)
```

**Contrainte** : La `SousFamille` est filtrée dynamiquement selon la `Famille` choisie (domain dans le champ).

---

#### 2️⃣ **Historique des États**

**Problème** : Un patrimoine change d'état au fil du temps.

**Solution** : Le modèle `EtatPatrimoineActif` enregistre chaque changement avec :
- Date du changement
- Nouvel état
- Commentaire optionnel

**Exemple** :
```
PC-001 :
  - 20/01/2024 : Neuf (Mise en service)
  - 15/06/2024 : Bon (Après 6 mois)
  - 10/12/2024 : Moyen (Usure normale)
```

L'état actuel est stocké dans `patrimoine_actif.etat_id` pour accès rapide.

---

#### 3️⃣ **Localisation et Organisation**

**PatrimoineGeographique** :
- Représente un lieu physique (bâtiment, étage, salle)
- A un responsable (`personnel_id`)
- Contient des documents (fiches, croquis)

**Unite** :
- Service ou département organisationnel
- A un type (`type_unite_id`) : Administratif, Technique, Commercial

**Relation** :
```
PatrimoineActif → est localisé dans → PatrimoineGeographique
                 → appartient à     → Unite
```

---

#### 4️⃣ **Fournisseurs**

Chaque patrimoine peut être lié à son fournisseur d'origine, permettant :
- Traçabilité des achats
- Contact pour garantie/maintenance
- Statistiques par fournisseur

**Informations** :
- Coordonnées complètes
- Responsable commercial
- Documents (BC, BL, Facture) liés au patrimoine

---

#### 5️⃣ **Personnel**

Le personnel a deux rôles :
1. **Responsable de localisation** : Gère un PatrimoineGeographique
2. **Catégorisé** : Appartient à une CategoriePersonnel (Cadre, Technicien, Employé)

---

## 🔄 Workflows Typiques

### Workflow 1 : Acquisition d'un nouveau bien

1. **Configuration** (à faire une fois) :
   - Créer les catégories, familles, marques nécessaires
   - Créer les fournisseurs
   - Définir les états possibles

2. **Enregistrement** :
   - Créer le PatrimoineActif avec toutes les infos
   - Lier au fournisseur
   - Définir la localisation et l'unité
   - État initial = "Neuf"

3. **Historique** :
   - Première entrée dans EtatPatrimoineActif : "Neuf" à la date de mise en service

### Workflow 2 : Suivi de l'état d'un bien

1. **Inspection périodique** :
   - Consulter le patrimoine
   - Évaluer son état actuel
   - Ajouter une ligne dans l'onglet "Historique des États"
   - Mettre à jour `etat_id` si changement significatif

2. **Traçabilité** :
   - L'onglet "Historique" montre toute l'évolution
   - Permet d'identifier les dégradations

### Workflow 3 : Réorganisation

1. **Déplacement physique** :
   - Modifier `patrimoine_geographique_id`
   - Éventuellement changer `unite_id`

2. **Changement de responsabilité** :
   - Modifier le responsable du PatrimoineGeographique

---

## 📈 Vue d'ensemble des Entités

### Entités de **Classification** (Tables de référence)
- TypePatrimoine
- CategoriePatrimActif
- Famille / SousFamille
- Marque
- Etat

### Entités **Organisationnelles**
- Unite / TypeUnite
- PatrimoineGeographique
- Personnel / CategoriePersonnel

### Entités **Transactionnelles**
- Fournisseur
- PatrimoineActif ⭐
- EtatPatrimoineActif (historique)

---

## 🎨 Interface Utilisateur

### Menu Principal : **Gestion Patrimoine**

#### Section 1 : **Patrimoines**
- Patrimoines Actifs (vue Kanban, Tree, Form)
- Historique des États

#### Section 2 : **Ressources**
- Fournisseurs
- Personnel

#### Section 3 : **Organisation**
- Unités
- Localisations

#### Section 4 : **Configuration**
- **Classification** : Types, Catégories, Familles, Sous-Familles, Marques
- **Autres** : États, Types d'Unités, Catégories de Personnel

---

## 🚀 Installation

```bash
# 1. Copier le module dans addons
cp -r gestion_patrimoine/ /path/to/odoo/addons/

# 2. Redémarrer Odoo
./odoo-bin -d votre_base

# 3. Installer le module depuis l'interface
Apps → Rechercher "Gestion du Patrimoine" → Installer
```

---

## 📊 Données de Démonstration

Le module inclut des données de démo réalistes :
- ✅ 3 Types d'unités
- ✅ 3 Types de patrimoine
- ✅ 3 Catégories de personnel
- ✅ 4 Marques (Dell, HP, Lenovo, Canon)
- ✅ 3 Familles avec sous-familles
- ✅ 5 États (Neuf, Bon, Moyen, Mauvais, HS)
- ✅ 2 Fournisseurs
- ✅ 2 Employés
- ✅ 2 Unités
- ✅ 2 Localisations
- ✅ 3 Patrimoines actifs (PC Dell, PC HP, Imprimante Canon)
- ✅ Historique d'états pour PC Dell

---

## 💡 Points Techniques Importants

### 1. Domaine Dynamique (SousFamille)
```python
sous_famille_id = fields.Many2one(
    domain="[('famille_id', '=', famille_id)]"
)

@api.onchange('famille_id')
def _onchange_famille_id(self):
    # Réinitialise la sous-famille si famille change
```

### 2. Display Name Calculé
Plusieurs modèles utilisent `_compute_display_name()` pour un affichage enrichi :
```python
@api.depends('code', 'designation')
def _compute_display_name(self):
    record.display_name = f"[{record.code}] {record.designation}"
```

### 3. Contraintes SQL
```python
_sql_constraints = [
    ('code_unique', 'UNIQUE(code)', 'Le code doit être unique!')
]
```

### 4. Ondelete Cascade vs Restrict
- **cascade** : Supprime les enregistrements liés (EtatPatrimoineActif)
- **restrict** : Empêche la suppression si des liens existent (Fournisseur, Unite)

---

## 🎯 Cas d'Usage Réels

### Exemple 1 : Gestion d'un Parc Informatique
- Créer tous les PC avec Dell/HP
- Les classer par Famille "Ordinateurs" → SousFamille "PC Fixe"
- Les affecter aux unités (Informatique, Comptabilité)
- Suivre leur état au fil du temps
- Identifier les biens à renouveler (état = Mauvais)

### Exemple 2 : Inventaire Physique
- Parcourir les localisations (Bâtiment A, B, C)
- Vérifier la présence de chaque patrimoine
- Mettre à jour les états
- Générer des rapports par localisation

### Exemple 3 : Maintenance Préventive
- Filtrer par degré d'importance = "Critique"
- Consulter l'historique des états
- Planifier les maintenances
- Contacter les fournisseurs si nécessaire

---

## ✅ Vérification Post-Installation

1. Menu **Gestion Patrimoine** visible
2. 3 patrimoines actifs dans les données démo
3. Tous les menus accessibles
4. Création d'un nouveau patrimoine fonctionnelle
5. Ajout d'un état dans l'historique OK

---

**Module développé par SILUE avecOdoo 17 - Compatible et testé** 