from odoo import models,fields,api,_
from dateutil.relativedelta import relativedelta
from datetime import datetime
from odoo.exceptions import ValidationError 
from odoo.tools.float_utils import float_compare,float_is_zero
class realestate_property_offer(models.Model):
    _name="realestate.property.offer"
    _description="Real Estate Property Offers"
    _order="price desc"
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

    @api.constrains("price","property_id.expected_price")
    def _check_price_difference(self):
        for record in self:
            if(not float_is_zero(record.price,precision_digits=2)):
                value2=record.property_id.expected_price*0.9
                ans=float_compare(record.price,value2,precision_digits=2)
                if(ans<1):
                    raise ValidationError(_('Selling price (%.2f) cannot be lower than 90 percent of the expected price(%.2f)')%(record.price,value2))
              