from odoo import models,fields,api
class realestate_property_tag(models.Model):
    _name="realestate.property.tag"
    _description="Real Estate Property Tags"
    name = fields.Char(string="Property Tag",required=True)
    