from odoo import models,fields
class Customer(models.Model):
    _name="customer.details"
    _inherit='mail.thread','mail.activity.mixin'
    _description="Model to demonstrate Many2one concept"
    customer_id=fields.Many2one(comodel_name="estate.property", string="Customer Name")