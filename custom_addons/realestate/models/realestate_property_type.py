from odoo import models,fields,api
class realestate_property_type(models.Model):
    _name="realestate.property.type"
    _description="Real Estate Property Type"
    name = fields.Char(string="Property Type",required=True)
    _sql_constraints = [
        ('type_uniq', 'unique (name)', 'Property Type must be unique.'),
    ]
    