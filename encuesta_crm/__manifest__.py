# -*- coding: utf-8 -*-
{
    'name': "CMT Models - Encuesta",

    'summary': """
        Modulo para la encuesta de clientes de CMT""",

    'description': """
        Modulo para la encuesta de clientes de CMT
    """,

    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['crm', 'sale'],

    # always loaded
    'data': [
        'view/encuesta_crm_view.xml',
        'view/lead_fields_view.xml',
        'view/term_sale_view.xml',
    ],
    'installable':True,
    'auto_install':False,
}
