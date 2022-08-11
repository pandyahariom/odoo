from odoo import models,fields,api
from dateutil.relativedelta import relativedelta
from datetime import datetime
class realestate_property_offer(models.Model):
    _name="realestate.property.offer"
    _description="Real Estate Property Offers"
    price=fields.Float(string="Offer Price")
    status=fields.Selection(selection=[('accepted',"Accepted"),('refused',"Refused")],copy=False)
    partner_id=fields.Many2one(comodel_name='res.partner',required=True)
    property_id=fields.Many2one(comodel_name='realestate.property',required=True)

    validity=fields.Integer(string="Validity(days)",default=7)
    date_deadline=fields.Date(string="Deadline",compute="_compute_deadline",inverse="_inverse_deadline")

    @api.depends("validity","create_date")
    def _compute_deadline(self):
        for record in self:
            if(record.create_date):
                record.date_deadline=record.create_date+relativedelta(days = record.validity)
            else:
                record.date_deadline=fields.Date.today()+relativedelta(days = record.validity)
   
    def _inverse_deadline(self):
        for record in self:
            #create_date is datetime object whereas date_deadline is date object
            #next code will convert create_date object to date object and store it in create
            create=record.create_date.date()
            #print("\n\nCREATE:::",create,type(create),":",record.date_deadline,type(record.date_deadline),"\n")
            
            #difference between two date object will give timedelta. We can extract total days from it using .days
            record.validity=abs((record.date_deadline-create).days)
        
    def action_accept(self):
        for record in self:
            record.status="accepted"
            record.property_id.selling_price=record.price
            record.property_id.buyer_id=record.partner_id
          
        return True
    def action_reject(self):
        for record in self:
            record.status="refused"
        return True
    
    
    _sql_constraints = [
        ('check_offer_price', 'CHECK(price > 0 )',
         'The Offer Price must be strictly positive'),
    ]