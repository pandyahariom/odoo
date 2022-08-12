from odoo import models,fields,api
class realestate_property_type(models.Model):
    _name="realestate.property.type"
    _description="Real Estate Property Type"
    _order="name"
    name = fields.Char(string="Property Type",required=True)
    property_ids=fields.One2many(comodel_name="realestate.property",inverse_name="property_type_id")
    _sql_constraints = [
        ('type_uniq', 'unique (name)', 'Property Type must be unique.'),
    ]