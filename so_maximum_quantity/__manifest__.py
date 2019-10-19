# -*- coding: utf-8 -*-

{
    'name': "Sales Order Maximum Quantity",
    'author': "Me",
    'category': 'Sales',
    'summary': """Set maximum sales quantity limit on product""",
    'license': 'AGPL-3',
    'description': """
""",
    'version': '12.0.0.1',
    'depends': ['base','sale_management','product','purchase'],
    'data': ['views/view_maximum_order_quantity.xml'
           ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
