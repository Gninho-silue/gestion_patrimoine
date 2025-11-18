# -*- coding: utf-8 -*-

from odoo import models, fields


class CategoriePersonnel(models.Model):
    _name = 'gestion.patrimoine.categorie.personnel'
    _description = 'Catégorie de Personnel'
    _rec_name = 'libelle'
    _order = 'libelle'

    libelle = fields.Char(string='Libellé', required=True)
    personnel_ids = fields.One2many(
        'gestion.patrimoine.personnel',
        'categorie_id',
        string='Personnel'
    )

    _sql_constraints = [
        ('libelle_unique', 'UNIQUE(libelle)', 'Le libellé doit être unique!')
    ]
