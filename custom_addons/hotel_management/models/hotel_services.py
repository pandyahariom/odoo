from odoo import fields, models, api


class ServiceCategories(models.Model):
    _name = "service.category"
    _description = "Service Categories"

    service_categ_id = fields.Many2one("service.category", "Types")
    product_categ_id = fields.Many2one('product.category', " Category", delegate=True, copy=False,
                                       ondelete="cascade", )

    def write(self, vals):
        if "service_categ_id" in vals:
            categ = self.env["service.category"].browse(vals['service.category'])
            vals.update({"categ_id": categ.product_categ_id.id})
        return super(ServiceCategories, self).write(vals)

    def unlink(self):
        rec = self.env["product.category"].sudo().browse(self.product_categ_id.id)
        rec.unlink()
        return super(ServiceCategories, self).unlink()


class HotelService(models.Model):
    _name = "hotel.service"
    _description = "Hotel Service"

    product_id = fields.Many2one('product.product', "Services", required=True, delegate=True, ondelete="cascade", )
    category_id = fields.Many2one("service.category", "Category", required=True, ondelete="restrict", )
    manager_id = fields.Many2one("res.users", string='Manager')

    @api.model
    def create(self, vals):
        if "category_id" in vals:
            prod = self.env["service.category"].browse(vals["category_id"])
            vals.update({"categ_id": prod.product_categ_id.id, 'service_ok': True})
        return super(HotelService, self).create(vals)

    def write(self, vals):
        if "category_id" in vals:
            prod = self.env["service.category"].browse(vals["category_id"])
            vals.update({"categ_id": prod.product_categ_id.id,'service_ok': True})
        return super(HotelService, self).write(vals)

    def unlink(self):
        rec = self.env["product.product"].sudo().browse(self.product_id.id)
        rec.unlink()
        return super(HotelService, self).unlink()
