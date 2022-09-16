from odoo import fields, models, api, _


class HotelMeals(models.Model):
    _name = 'hotel.meals'
    _description = 'Meals'

    meal_type_id = fields.Many2one('meal.types', string='Type', required=True, ondelete="cascade")
    product_id = fields.Many2one('product.product', "Meal", required=True, delegate=True, ondelete="cascade")
    manager_id = fields.Many2one("res.users", string='Manager')


    @api.model
    def create(self, vals):
        if "meal_type_id" in vals:
            prod = self.env["meal.types"].browse(vals["meal_type_id"])
            vals.update({"categ_id": prod.product_categ_id.id, 'meals_ok': True})
        return super(HotelMeals, self).create(vals)

    def write(self, vals):
        if "meal_type_id" in vals:
            prod = self.env["meal.types"].browse(vals["meal_type_id"])
            vals.update({"categ_id": prod.product_categ_id.id})
        return super(HotelMeals, self).write(vals)

    def unlink(self):
        rec = self.env["product.product"].sudo().browse(self.product_id.id)
        rec.unlink()
        return super(HotelMeals, self).unlink()
