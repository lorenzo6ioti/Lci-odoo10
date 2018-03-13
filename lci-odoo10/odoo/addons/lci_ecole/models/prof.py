# -*- coding: utf-8 -*-
# Copyright 2018 lorenzo6ioti
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class Prof(models.Model):
    _name="ecole.prof"
    _inherit = 'ecole.prof'
    salaire=fields.Float(string="Salaire mensuel", compute="_calcSal", store=True)
    nbHeureJour=fields.Integer(string="Nombre d'heures prestées par jour")
    salaireHoraire=fields.Float(string="Salaire par heure")

    @api.depends('salaireHoraire', 'nbHeureJour')
    def _calcSal(self):
        for r in self:
            r.nbHeureTot = r.nbHeureJour * 20
            r.salaire = r.nbHeureTot * r.salaireHoraire
