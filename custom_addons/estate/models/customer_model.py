from odoo import models,fields,api
from datetime import date


class Customer(models.Model):
    _name="customer.details"
    _inherit='mail.thread','mail.activity.mixin'
    _description="Model to demonstrate Many2one concept"
    customer_id=fields.Many2one(comodel_name="estate.property", string="Customer Name")

    #in the breadcrumb bydefault model name and ID will be displayed if the field with name as "name" is missing
    #we can add _rec_name to add any field value in breadcrumb
    _rec_name='customer_id' 

    html_field_demo=fields.Html(string="HTML Text Field")
    
    gender=fields.Selection([('male','Male'),('female','Female')],string="Gender",related="customer_id.gender")
    appointment_time=fields.Datetime(string="Appointment Time",default=fields.Datetime.now)
    birth_date=fields.Date(string="Birth Date",default=fields.Date.today)
    age=fields.Integer(string="Age",compute="_compute_age") #Demo of depends
    
    name2=fields.Char(string="OnChangeDemo") #Retrive the name while name is changed
    @api.onchange('customer_id')
    def onchange_customer_id(self):
        self.name2=self.customer_id.name
#Mentioning api.depends will update the Age as soon as user select birth_date. 
# If not specified it will get updated on save and not on birth_date selection.
    @api.depends('birth_date')
    def _compute_age(self):
        today = date.today()
        for record in self:
            try:
                birthday = record.birth_date.replace(year = today.year)
                #print("Brithdate:",birthday)
            # raised when birth date is February 29
            # and the current year is not a leap year
            except ValueError:
                birthday = record.birth_date.replace(year = today.year,
                        month = record.birth_date.month + 1, day = 1)
                #print("Brithdate:",birthday)
            #print("ANS:",today.year - record.birth_date.year)
            if birthday > today:
                self.age= today.year - record.birth_date.year - 1
            else:
                self.age= today.year - record.birth_date.year
