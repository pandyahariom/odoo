from odoo import fields,api,models
class realestate(models.Model):
    _inherit="realestate.property"
    def action_sold(self):
        return super().action_sold()