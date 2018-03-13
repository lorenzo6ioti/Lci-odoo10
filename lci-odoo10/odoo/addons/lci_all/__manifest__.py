# -*- coding: utf-8 -*-
# Copyright 2016 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': "lci-odoo10",
    'description': """
        Odoo aplication for lci-odoo10""",
    'author': 'Metrum',
    'website': "http://metrum.lu",
    'category': 'lci-odoo10',
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'depends': [
        # lci-odoo10 open source addons
        # !!! no odoo enterprise addons dependencies !!!
        # OCA/server-tools
        'base_optional_quick_create',
        'mail_environment',
        'server_environment_ir_config_parameter',
        # OCA/web
        'web_dialog_size',
        'web_environment_ribbon',
        'web_sheet_full_width',
        'lci_ecole'
    ],
    'data': [
    ],
    'application': True,
}
