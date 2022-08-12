from odoo import models,fields,api
class realestate_property_tag(models.Model):
    _name="realestate.property.tag"
    _description="Real Estate Property Tags"
    _order="sequence,name"
    name = fields.Char(string="Property Tag",required=True)
    sequence=fields.Integer('Sequence',default=1, help="Used to order stages. Lower is better.")
    color=fields.Integer()
    _sql_constraints = [
        ('tag_uniq', 'unique (name)', 'Tag must be a unique.'),
    ]