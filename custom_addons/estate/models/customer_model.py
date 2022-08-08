from odoo import models,fields
from datetime import date

class Customer(models.Model):
    _name="customer.details"
    _inherit='mail.thread','mail.activity.mixin'
    _description="Model to demonstrate Many2one concept"
    customer_id=fields.Many2one(comodel_name="estate.property", string="Customer Name")
    gender=fields.Selection([('male','Male'),('female','Female')],string="Gender",related="customer_id.gender")
    appointment_time=fields.Datetime(string="Appointment Time",default=fields.Datetime.now)
    birth_date=fields.Date(string="Birth Date",default=fields.Date.today)
    age=fields.Integer(string="Age",compute="_compute_age")

    def _compute_age(self):
        today = date.today()
        for record in self:
            try:
                birthday = record.birth_date.replace(year = today.year)
            # raised when birth date is February 29
            # and the current year is not a leap year
            except ValueError:
                birthday = record.birth_date.replace(year = today.year,
                        month = record.birth_date.month + 1, day = 1)
        
            if birthday > today:
                return today.year - record.birth_date.year - 1
            else:
                return today.year - record.birth_date.year
