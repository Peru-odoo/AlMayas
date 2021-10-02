# -*- coding: utf-8 -*-
{
    'name': 'Sale Quotation Templates',
    'version': '13.0.0.0',
    'summary': 'Sale Quotation Templates',
    'sequence': 1,
    'description': """
        Sale Quotation Templates
        """,
    'category': 'sales',
    'website': '',
    'depends': ['sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/layouts_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}
