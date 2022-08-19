from odoo import models,fields,api
class realestate(models.Model):
    _inherit="realestate.property"
     
    def action_sold(self):
        print("My Message")
        return super().action_sold()