from odoo import models,fields,api
from dateutil.relativedelta import relativedelta
import time
class realestate(models.Model):
    _name="realestate.property"
    _description="First Real Estate Model"
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
    garden_orientation=fields.Selection(selection=[("north","North"),("east","East"),("west","West"),("south","South")],string="Garden Orientatin",help="Select Garden Orientation",default='north')
    active=fields.Boolean(default=True)
    state=fields.Selection(selection=[("new","New"),("or","Offer Received"),("oa","Offer Accepted"),("sold","Sold"),("canceled","Canceled")],required=True,copy=False,default='new')
    property_type_id=fields.Many2one(comodel_name="realestate.property.type",string="Property Type")
    salesman_id=fields.Many2one('res.users', string='Salesperson', index=True, tracking=True, default=lambda self: self.env.user)
    buyer_id=fields.Many2one('res.partner', string='Buyer', index=True, tracking=True, copy=False)