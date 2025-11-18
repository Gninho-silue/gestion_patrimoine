# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Fournisseur(models.Model):
    _name = 'gestion.patrimoine.fournisseur'
    _description = 'Fournisseur'
    _rec_name = 'code'
    _order = 'code'

    code = fields.Char(string='Code', required=True, copy=False)
    denomination = fields.Char(string='Dénomination', required=True)
    adresse = fields.Text(string='Adresse')
    tel = fields.Char(string='Téléphone')
    fax = fields.Char(string='Fax')
    email = fields.Char(string='Email')
    nom_resp = fields.Char(string='Nom Responsable')
    prenom_resp = fields.Char(string='Prénom Responsable')
    gsm1 = fields.Char(string='GSM 1')
    gsm2 = fields.Char(string='GSM 2')

    patrimoine_actif_ids = fields.One2many(
        'gestion.patrimoine.actif',
        'fournisseur_id',
        string='Patrimoines Fournis'
    )

    _sql_constraints = [
        ('code_unique', 'UNIQUE(code)', 'Le code fournisseur doit être unique!')
    ]

    @api.depends('code', 'denomination')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"[{record.code}] {record.denomination}"
