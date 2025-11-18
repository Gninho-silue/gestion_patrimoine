{
    'name': 'Gestion du Patrimoine',
    'version': '17.0.1.0.0',
    'category': 'Asset Management',
    'summary': 'Module complet de gestion du patrimoine',
    'description': """
        Gestion du Patrimoine
        =====================
        * Gestion des patrimoines actifs
        * Gestion des états et historique
        * Gestion des fournisseurs
        * Gestion du personnel
        * Gestion des unités et localisations
        * Classification par catégories, familles et marques
    """,
    'author': 'SILUE',
    'website': '',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        # Vues de configuration et principales
        'views/type_unite_views.xml',
        'views/configuration_views.xml',
        'views/fournisseur_personnel_unite_views.xml',
        'views/patrimoine_actif_views.xml',
        # Menu
        'views/menu_views.xml',
    ],
    'demo': [
        'data/demo_data.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
