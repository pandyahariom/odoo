from odoo import models,fields
class Customer(models.Model):
    _name="customer.details"
    _inherit='mail.thread','mail.activity.mixin'
    _description="Model to demonstrate Many2one concept"
    customer_id=fields.Many2one(comodel_name="estate.property", string="Customer Name")
    gender=fields.Selection([('male','Male'),('female','Female')],string="Gender",related="customer_id.gender")
    appointment_time=fields.Datetime(string="Appointment Time",default=fields.Datetime.now)
    appointment_date=fields.Date(string="Appointment Date",default=fields.Date.today)