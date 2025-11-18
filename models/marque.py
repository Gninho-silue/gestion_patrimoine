# -*- coding: utf-8 -*-

from odoo import models, fields


class Marque(models.Model):
    _name = 'gestion.patrimoine.marque'
    _description = 'Marque'
    _rec_name = 'libelle'
    _order = 'libelle'

    libelle = fields.Char(string='Libellé', required=True)
    patrimoine_actif_ids = fields.One2many(
        'gestion.patrimoine.actif',
        'marque_id',
        string='Patrimoines Actifs'
    )

    _sql_constraints = [
        ('libelle_unique', 'UNIQUE(libelle)', 'Le libellé doit être unique!')
    ]
