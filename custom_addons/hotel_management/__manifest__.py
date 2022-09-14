
{
    'name': 'Hotel Management',
    'version': '1.0',
    'summary': 'Hotel Management odoo 15',
    'description': """The module manage rooms,amenities,services,restaurants.""",
    'category': 'Sales',
    'depends': ['sale_management', 'account', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/room_reservation.xml',
        'views/hotel_meals.xml',
        'views/hotel_restaurant.xml',
        'views/res_settings.xml',
        'views/hotel_amenity.xml',
        'views/hotel_services.xml',
        'views/room_checkin_in_out.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
