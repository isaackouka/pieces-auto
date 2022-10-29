# -*- coding: utf-8 -*-
{
    'name': "TB Auto",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','mail','contacts','product','stock','account','general_means_management'],
    'application': True,

    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/product_template_view.xml',
        'views/product_mark.xml',
        'views/car_engine.xml',
        'views/car_finition.xml',
        'views/car_mark.xml',
        'views/car_model.xml',
        'views/product_position.xml',
        'views/product_family.xml',
        'views/product_packaging_view.xml',
        'views/menu.xml',
        'report/product_report.xml',
    ],
    
    'demo': [

    ],
}