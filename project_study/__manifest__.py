# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Enmasys Project Study',
    'version': '1.1',
    'category': 'Sales',
    'summary': 'Sales internal machinery',
    'description': """
This module contains all the common features of Sales Management and eCommerce.
    """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/view_study.xml',
        'views/user_view.xml',],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
