# -*- coding: utf-8 -*-
# Copyright 2018 lorenzo6ioti
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Lci Ecole',
    'description': """
        custom ecole""",
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'lorenzo6ioti',
    'depends': ['ecole'
    ],
    'data':[

        'views/prof.xml',
        'views/section.xml',
        'views/cours.xml',
        'views/eleve.xml',
        'report/report_cours_temp.xml',
        'report/report_eleve_temp.xml',
        'report/report_prof_temp.xml',
        'report/report_section_temp.xml',
    ],
    'demo': [
    ],
}
