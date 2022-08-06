from odoo import models,fields
class Estate(models.Model):
    _name="estate.property"
    _description="First Model to store Estate Properties"
    name=fields.Char(string="CustomerName")
    age=fields.Integer(string="Age")
    gender=fields.Selection([('male','Male'),('female','Female')],string="Gender")