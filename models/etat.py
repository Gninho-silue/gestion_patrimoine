# -*- coding: utf-8 -*-

from odoo import models, fields


class Etat(models.Model):
    _name = 'gestion.patrimoine.etat'
    _description = 'État du Patrimoine'
    _rec_name = 'libelle'
    _order = 'libelle'

    libelle = fields.Char(string='Libellé', required=True)
    patrimoine_actif_ids = fields.One2many(
        'gestion.patrimoine.actif',
        'etat_id',
        string='Patrimoines Actifs'
    )
    etat_patrimoine_actif_ids = fields.One2many(
        'gestion.patrimoine.etat.patrimoine.actif',
        'etat_id',
        string='Historique des États'
    )

    _sql_constraints = [
        ('libelle_unique', 'UNIQUE(libelle)', 'Le libellé doit être unique!')
    ]
