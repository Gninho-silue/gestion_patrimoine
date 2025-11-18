# -*- coding: utf-8 -*-

from odoo import models, fields


class Famille(models.Model):
    _name = 'gestion.patrimoine.famille'
    _description = 'Famille de Patrimoine'
    _rec_name = 'libelle'
    _order = 'libelle'

    libelle = fields.Char(string='Libellé', required=True)
    sous_famille_ids = fields.One2many(
        'gestion.patrimoine.sous.famille',
        'famille_id',
        string='Sous-Familles'
    )
    patrimoine_actif_ids = fields.One2many(
        'gestion.patrimoine.actif',
        'famille_id',
        string='Patrimoines Actifs'
    )

    _sql_constraints = [
        ('libelle_unique', 'UNIQUE(libelle)', 'Le libellé doit être unique!')
    ]
