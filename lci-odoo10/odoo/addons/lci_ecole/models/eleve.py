# -*- coding: utf-8 -*-
# Copyright 2018 lorenzo6ioti
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class Eleve(models.Model):
    
    _inherit = 'ecole.eleve'
    surname = fields.Char(string="Surnom")
    nbCredObt = fields.Integer(string="Nombre de crédits validés")
    nbCredTot = fields.Integer(string="Nombre de crédits total du cursus")
    nbCredRest = fields.Integer(string="Nombre de crédits restants", compute="_nbCRest", store=True)
    voiture = fields.Boolean(string="Possession d'une voiture", default=False)

    @api.depends('nbCredObt', 'nbCredTot')
    def _nbCRest(self):
        for r in self:
            r.nbCredRest = r.nbCredTot - r.nbCredObt
