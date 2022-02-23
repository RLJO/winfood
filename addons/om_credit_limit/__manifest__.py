{
    'name': 'Odoo 13 Credit Limit',
    'author': 'Odoo Mates',
    'category': 'Accounting',
    'version': '1.1.0',
    'description': """Customer Credit Limit""",
    'summary': """Customer Credit Limit""",
    'sequence': 11,
    'website': 'https://www.odoomates.tech',
    'depends': ['sale'],
    'license': 'LGPL-3',
    'data': [
        'wizard/warning.xml',
        'views/res_partner.xml',
        'views/sale_order.xml'
    ],
    'images': ['static/description/banner.png'],

}
