# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SousFamille(models.Model):
    _name = 'gestion.patrimoine.sous.famille'
    _description = 'Sous-Famille de Patrimoine'
    _rec_name = 'libelle'
    _order = 'famille_id, libelle'

    libelle = fields.Char(string='Libellé', required=True)
    famille_id = fields.Many2one(
        'gestion.patrimoine.famille',
        string='Famille',
        required=True,
        ondelete='cascade'
    )
    patrimoine_actif_ids = fields.One2many(
        'gestion.patrimoine.actif',
        'sous_famille_id',
        string='Patrimoines Actifs'
    )

    _sql_constraints = [
        ('libelle_famille_unique', 'UNIQUE(libelle, famille_id)',
         'Le libellé doit être unique par famille!')
    ]

    @api.depends('libelle', 'famille_id')
    def _compute_display_name(self):
        for record in self:
            if record.famille_id:
                record.display_name = f"{record.famille_id.libelle} / {record.libelle}"
            else:
                record.display_name = record.libelle
