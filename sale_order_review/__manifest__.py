# -*- coding: utf-8 -*-
{
    'name': 'Sale Order Review',
    'version': '13.0.0.1',
    'summary': 'Sale Order Review',
    'sequence': 1,
    'description': """
        Sale Order Review
        """,
    'category': 'sales',
    'website': '',
    'depends': ['sale_management'],
    'data': [
        'security/revise_security.xml',
        'views/sale_order_views.xml',
        'views/sale_report_template.xml',
        'views/res_users_view.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}
