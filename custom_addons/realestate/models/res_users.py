from odoo import models,fields
class resUsers(models.Model):
    _inherit="res.users"
    property_ids=fields.One2many(comodel_name="realestate.property",inverse_name="salesman_id")