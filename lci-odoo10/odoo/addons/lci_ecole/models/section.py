# -*- coding: utf-8 -*-
# Copyright 2018 lorenzo6ioti
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class Section(models.Model):
    _name="ecole.section"
    _inherit = 'ecole.section'
    description=fields.Integer(string="Description de la section")
