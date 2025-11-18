# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PatrimoineActif(models.Model):
    _name = 'gestion.patrimoine.actif'
    _description = 'Patrimoine Actif'
    _rec_name = 'code'
    _order = 'code'

    # Informations de base
    code = fields.Char(string='Code', required=True, copy=False)
    designation = fields.Char(string='Désignation', required=True)

    # Informations financières et administratives
    valeur_acquisition = fields.Float(string='Valeur d\'Acquisition')
    date_acquisition = fields.Date(string='Date d\'Acquisition')
    date_mise_service = fields.Date(string='Date de Mise en Service')

    # Documents administratifs
    n_bc = fields.Char(string='N° BC')
    n_bl = fields.Char(string='N° BL')
    n_facture = fields.Char(string='N° Facture')

    # État et sécurité
    etat_actuelle = fields.Char(string='État Actuelle')
    image_actif = fields.Binary(string='Image Actif')
    consigne_securite = fields.Text(string='Consigne de Sécurité')
    degre_importance = fields.Selection([
        ('faible', 'Faible'),
        ('moyen', 'Moyen'),
        ('eleve', 'Élevé'),
        ('critique', 'Critique')
    ], string='Degré d\'Importance')

    # Relations Many2one (0..1)
    etat_id = fields.Many2one(
        'gestion.patrimoine.etat',
        string='État',
        ondelete='restrict'
    )

    fournisseur_id = fields.Many2one(
        'gestion.patrimoine.fournisseur',
        string='Fournisseur',
        ondelete='restrict'
    )

    categorie_id = fields.Many2one(
        'gestion.patrimoine.categorie.patrim.actif',
        string='Catégorie',
        ondelete='restrict'
    )

    famille_id = fields.Many2one(
        'gestion.patrimoine.famille',
        string='Famille',
        ondelete='restrict'
    )

    sous_famille_id = fields.Many2one(
        'gestion.patrimoine.sous.famille',
        string='Sous-Famille',
        ondelete='restrict',
        domain="[('famille_id', '=', famille_id)]"
    )

    marque_id = fields.Many2one(
        'gestion.patrimoine.marque',
        string='Marque',
        ondelete='restrict'
    )

    type_patrimoine_id = fields.Many2one(
        'gestion.patrimoine.type.patrimoine',
        string='Type de Patrimoine',
        ondelete='restrict'
    )

    patrimoine_geographique_id = fields.Many2one(
        'gestion.patrimoine.geographique',
        string='Localisation',
        ondelete='restrict'
    )

    unite_id = fields.Many2one(
        'gestion.patrimoine.unite',
        string='Unité',
        ondelete='restrict'
    )

    # Relations One2many
    etat_patrimoine_actif_ids = fields.One2many(
        'gestion.patrimoine.etat.patrimoine.actif',
        'patrimoine_actif_id',
        string='Historique des États'
    )

    _sql_constraints = [
        ('code_unique', 'UNIQUE(code)', 'Le code du patrimoine doit être unique!')
    ]

    @api.depends('code', 'designation')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"[{record.code}] {record.designation}"

    @api.onchange('famille_id')
    def _onchange_famille_id(self):
        """Réinitialiser la sous-famille si la famille change"""
        if self.famille_id:
            return {'domain': {'sous_famille_id': [('famille_id', '=', self.famille_id.id)]}}
        else:
            self.sous_famille_id = False
            return {'domain': {'sous_famille_id': []}}
