# -*- coding: utf-8 -*-
{
    'name': 'Add Sucursal',
    
    'summary': """
        Modulo para Elegir Lugar de Expedicion """,
    
    'description': """
        Segun el Usuario loggeado se podra definir una Sucursal """,
    
    'author': "GBA Tecnologías",
    'website': "http://www.gba.com.mx",
    
    'category': 'Invoice',
    'version': '0.1',
    
    'depends': 'acount_invoicing',
    
    'data': [
        'view/expplace_view.xml',
    ],
    'installable': True,
    'auto_install': False,    
}