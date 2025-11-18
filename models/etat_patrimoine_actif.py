# -*- coding: utf-8 -*-

from odoo import models, fields, api


class EtatPatrimoineActif(models.Model):
    _name = 'gestion.patrimoine.etat.patrimoine.actif'
    _description = 'Historique des États du Patrimoine Actif'
    _order = 'date_etat desc'

    date_etat = fields.Date(
        string='Date de l\'État',
        required=True,
        default=fields.Date.context_today
    )

    patrimoine_actif_id = fields.Many2one(
        'gestion.patrimoine.actif',
        string='Patrimoine Actif',
        required=True,
        ondelete='cascade'
    )

    etat_id = fields.Many2one(
        'gestion.patrimoine.etat',
        string='État',
        required=True,
        ondelete='restrict'
    )

    commentaire = fields.Text(string='Commentaire')

    @api.depends('patrimoine_actif_id', 'etat_id', 'date_etat')
    def _compute_display_name(self):
        for record in self:
            pat_name = record.patrimoine_actif_id.code if record.patrimoine_actif_id else 'N/A'
            etat_name = record.etat_id.libelle if record.etat_id else 'N/A'
            date_str = record.date_etat.strftime('%d/%m/%Y') if record.date_etat else 'N/A'
            record.display_name = f"{pat_name} - {etat_name} ({date_str})"
