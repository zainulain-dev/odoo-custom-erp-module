# -*- coding: utf-8 -*-
{
    'name': 'Custom ERP & CRM',
    'version': '18.0.1.0.0',
    'category': 'Services/Custom ERP',
    'summary': 'Custom ERP & CRM Module extending core functionalities for advanced tracking.',
    'description': """
Custom ERP & CRM Module
=======================
Custom ERP & CRM Module extending core functionalities for advanced tracking.
    """,
    'author': 'Muhammad Zain Ul Ain',
    'website': 'https://github.com/zainulain-dev/odoo-custom-erp-module',
    'license': 'LGPL-3',
    'depends': ['base', 'sale', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_actions_server.xml',
        'reports/report_paperformat.xml',
        'reports/sale_order_report_template.xml',
        'views/res_partner_views.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
