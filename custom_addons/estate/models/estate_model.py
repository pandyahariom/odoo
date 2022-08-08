from odoo import models,fields
class Estate(models.Model):
    _name="estate.property"
    _inherit='mail.thread','mail.activity.mixin'
    _description="First Model to store Estate Properties"
    name=fields.Char(string="CustomerName",tracking=True)
    age=fields.Integer(string="Age")
    gender=fields.Selection([('male','Male'),('female','Female')],string="Gender",default="male")
    active=fields.Boolean(string="Active or Archive",default=True)