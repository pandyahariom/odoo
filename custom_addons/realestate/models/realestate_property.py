from odoo import models,fields,api
class realestate(models.Model):
    _name="realestate.property"
    _description="First Real Estate Model"
    name = fields.Char(string="Name",required=True)
    description=fields.Text(string="Description")
    postcode= fields.Char(string="Postcode")
    date_availability=fields.Date(string="Date Available")
    expected_price=fields.Float(string="Expected Price",required=True)
    selling_price=fields.Float(string="Selling Price")
    bedrooms=fields.Integer(string="Total Badrooms")
    living_area=fields.Integer(string="Living Area")
    facades=fields.Integer(string="Facades")
    garage=fields.Boolean(string="Has Garage?")
    garden=fields.Boolean(string="Has Garden?")
    garden_area=fields.Integer(string="Garden Area")
    garden_orientation=fields.Selection(string="Garden Orientatin",selection=[('North','north'),('South','south'),('East','east'),('West','west')],help="Select Garden Orientation")
