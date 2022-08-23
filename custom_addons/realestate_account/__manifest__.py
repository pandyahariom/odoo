# -*- coding: utf-8 -*-
{
    'name': "realestate_account",
    'author': "My Company",
    # any module necessary for this one to work correctly
    'depends': ['base','realestate','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
    "auto_install": True,
}
