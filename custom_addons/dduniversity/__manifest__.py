# -*- coding: utf-8 -*-
{
    'name': "dduniversity",

    'summary': """
        Odoo Module for Dharmsinh Desai University (D.D. University) Management Quota Admission""",

    'description': """
        Module to support various administrative task of the D.D.University admission
    """,

    'author': "Hariom Pandya",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','crm'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
    'installable': True,
    'application': True,
    'license':'LGPL-3'
}
