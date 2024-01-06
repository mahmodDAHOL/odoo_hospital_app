{
    'name': 'Hospital Management',
    'version': '1.0',
    'description': 'Hospital management system',
    'summary': 'Hospital management system',
    'sequence': '-100',
    'author': 'Mahmod Aldahol',
    'website': '',
    'license': 'LGPL-3',
    'category': 'Hospital',
    'depends': [
        'base',
        'mail',
        'product'
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/cancel_appointment_view.xml',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',
        'views/patient_tag_view.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
    'assets': {
        
    }
}

