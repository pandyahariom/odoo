from odoo import fields, models, api, _
from datetime import datetime


class MealsTypes(models.Model):
    _name = "meal.types"
    _description = "Meals Types"

    type_id = fields.Many2one("meal.types", "Types")
    product_categ_id = fields.Many2one('product.category', "Product Category", delegate=True, copy=False,
                                       ondelete="cascade")

    @api.model
    def create(self, vals):
        vals.update({'is_meals_categ': True})
        return super(MealsTypes, self).create(vals)

    def write(self, vals):
        if "type_id" in vals:
            categ = self.env["meal.type"].browse(vals['meal'])
            vals.update({"categ_id": categ.product_categ_id.id})
        return super(MealsTypes, self).write(vals)

    def unlink(self):
        rec = self.env["product.category"].sudo().browse(self.product_categ_id.id)
        rec.unlink()
        return super(MealsTypes, self).unlink()


