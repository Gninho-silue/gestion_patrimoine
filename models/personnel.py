# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Personnel(models.Model):
    _name = 'gestion.patrimoine.personnel'
    _description = 'Personnel'
    _rec_name = 'matricule'
    _order = 'nom, prenom'

    matricule = fields.Char(string='Matricule', required=True, copy=False)
    nom = fields.Char(string='Nom', required=True)
    prenom = fields.Char(string='Prénom')
    fonction = fields.Char(string='Fonction')
    tel = fields.Char(string='Téléphone')
    fax = fields.Char(string='Fax')
    email = fields.Char(string='Email')

    categorie_id = fields.Many2one(
        'gestion.patrimoine.categorie.personnel',
        string='Catégorie',
        required=True,
        ondelete='restrict'
    )

    patrimoine_geographique_ids = fields.One2many(
        'gestion.patrimoine.geographique',
        'responsable_id',
        string='Localisations Responsables'
    )

    _sql_constraints = [
        ('matricule_unique', 'UNIQUE(matricule)', 'Le matricule doit être unique!')
    ]

    @api.depends('nom', 'prenom', 'matricule')
    def _compute_display_name(self):
        for record in self:
            name = f"{record.nom} {record.prenom or ''}".strip()
            if record.matricule:
                name = f"[{record.matricule}] {name}"
            record.display_name = name
