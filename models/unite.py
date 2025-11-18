# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Unite(models.Model):
    _name = 'gestion.patrimoine.unite'
    _description = 'Unité Organisationnelle'
    _rec_name = 'code'
    _order = 'code'

    code = fields.Char(string='Code', required=True, copy=False)
    designation = fields.Char(string='Désignation', required=True)
    type_unite_id = fields.Many2one(
        'gestion.patrimoine.type.unite',
        string='Type d\'Unité',
        ondelete='restrict'
    )

    patrimoine_actif_ids = fields.One2many(
        'gestion.patrimoine.actif',
        'unite_id',
        string='Patrimoines'
    )

    _sql_constraints = [
        ('code_unique', 'UNIQUE(code)', 'Le code unité doit être unique!')
    ]

    @api.depends('code', 'designation')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"[{record.code}] {record.designation}"
