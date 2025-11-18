# -*- coding: utf-8 -*-

from odoo import models, fields


class TypeUnite(models.Model):
    _name = 'gestion.patrimoine.type.unite'
    _description = 'Type d\'Unité'
    _rec_name = 'libelle'
    _order = 'libelle'

    libelle = fields.Char(string='Libellé', required=True)
    unite_ids = fields.One2many(
        'gestion.patrimoine.unite',
        'type_unite_id',
        string='Unités'
    )

    _sql_constraints = [
        ('libelle_unique', 'UNIQUE(libelle)', 'Le libellé doit être unique!')
    ]
