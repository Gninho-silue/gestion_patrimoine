# -*- coding: utf-8 -*-

from odoo import models, fields


class TypePatrimoine(models.Model):
    _name = 'gestion.patrimoine.type.patrimoine'
    _description = 'Type de Patrimoine'
    _rec_name = 'libelle'
    _order = 'libelle'

    libelle = fields.Char(string='Libellé', required=True)
    patrimoine_actif_ids = fields.One2many(
        'gestion.patrimoine.actif',
        'type_patrimoine_id',
        string='Patrimoines Actifs'
    )

    _sql_constraints = [
        ('libelle_unique', 'UNIQUE(libelle)', 'Le libellé doit être unique!')
    ]
