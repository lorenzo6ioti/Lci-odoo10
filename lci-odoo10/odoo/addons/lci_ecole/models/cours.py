# -*- coding: utf-8 -*-
# Copyright 2018 lorenzo6ioti
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class Cours(models.Model):
    _name="ecole.cours"
    _inherit = 'ecole.cours'
    lieu=fields.Char(string="Lieu")
