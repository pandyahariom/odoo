from odoo import models,fields,api,_
from dateutil.relativedelta import relativedelta
import time
from odoo.exceptions import UserError

class realestate(models.Model):
    _name="realestate.property"
    _description="First Real Estate Model"
    _order="id desc"
    name = fields.Char(string="Title",required=True)
    description=fields.Text(string="Description",help="Kindly Describe Your Property in few words!!!")
    postcode= fields.Char(string="Postcode")
    date_availability=fields.Date(string="Date Available",copy=False,default=(fields.Date.today()+ relativedelta(months=+3)))
    expected_price=fields.Float(string="Expected Price",required=True)
    selling_price=fields.Float(string="Selling Price",readonly=True,copy=False)
    bedrooms=fields.Integer(string="Total Badrooms",default=2)
    living_area=fields.Integer(string="Living Area")
    facades=fields.Integer(string="Facades")
    garage=fields.Boolean(string="Has Garage?")
    garden=fields.Boolean(string="Has Garden?")
    garden_area=fields.Integer(string="Garden Area")
    garden_orientation=fields.Selection(selection=[("north","North"),("east","East"),("west","West"),("south","South")],string="Garden Orientatin",help="Select Garden Orientation")
    active=fields.Boolean(default=True)
    state=fields.Selection(selection=[("new","New"),("or","Offer Received"),("oa","Offer Accepted"),("sold","Sold"),("canceled","Canceled")],required=True,copy=False,default='new')

    property_type_id=fields.Many2one(comodel_name="realestate.property.type",string="Property Type", required=True,no_create=True)
    salesman_id=fields.Many2one('res.users', string='Salesperson',  default=lambda self: self.env.user)
    buyer_id=fields.Many2one('res.partner', string='Buyer', copy=False)
    tag_ids=fields.Many2many('realestate.property.tag',string="Property Tag",required=True)
    offer_ids=fields.One2many('realestate.property.offer',inverse_name="property_id",string="Offers")

    total_area=fields.Integer(compute="_compute_total_area",string="Total Area",readonly=True)
    best_price=fields.Float(compute="_compute_best_price",string="Best Offer",readonly=True)

    @api.depends("garden_area","living_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area=record.garden_area+record.living_area

    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for record in self:
            record.best_price=0.0
            for offer in self.offer_ids:
                if(offer.price>record.best_price):
                    record.best_price=offer.price

    @api.onchange("garden")
    def _onchange_garden(self):
        if(self.garden):
            self.garden_area=10
            self.garden_orientation="north"
        else:
            self.garden_area=0
            self.garden_orientation=""
            return {'warning': {
                'title': _("Warning"),
                'message': ('Really !!! No Garden ??')}}
    
    def action_sold(self):
        #("new","New"),("or","Offer Received"),("oa","Offer Accepted"),("sold","Sold"),("canceled","Canceled"
        for record in self:
            if(record.state=="canceled"):
                raise UserError(_('Canceled Property can not be Sold !!'))
            else:
                record.state="sold"
        return True
        
    def action_cancel(self):
        for record in self:
            if(record.state=="sold"):
                raise UserError(_('Sold Property can not be Cancelled !!'))
            else:
                record.state="canceled"
        return True
    
    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price > 0 )',
         'The Expected Price must be strictly positive'),
         ('check_selling_price', 'CHECK(selling_price >= 0 )',
         'The Selling Price must be positive')
    ]

    def unlink(self):
        if not set(self.mapped("state")) <= {"new", "canceled"}:
            raise UserError("Only new and canceled properties can be deleted.")
        return super().unlink()