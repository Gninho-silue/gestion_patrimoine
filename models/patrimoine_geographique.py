# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PatrimoineGeographique(models.Model):
    _name = 'gestion.patrimoine.geographique'
    _description = 'Patrimoine Géographique'
    _rec_name = 'code'
    _order = 'code'

    code = fields.Char(string='Code', required=True, copy=False)
    designation = fields.Char(string='Désignation', required=True)
    croquis = fields.Text(string='Croquis')
    fiche_immeuble = fields.Binary(string='Fiche Immeuble')
    fiche_etage = fields.Binary(string='Fiche Étage')
    fiche_local = fields.Binary(string='Fiche Local')

    responsable_id = fields.Many2one(
        'gestion.patrimoine.personnel',
        string='Responsable',
        ondelete='restrict'
    )

    patrimoine_actif_ids = fields.One2many(
        'gestion.patrimoine.actif',
        'patrimoine_geographique_id',
        string='Patrimoines Localisés'
    )

    _sql_constraints = [
        ('code_unique', 'UNIQUE(code)', 'Le code doit être unique!')
    ]

    @api.depends('code', 'designation')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"[{record.code}] {record.designation}"
