from odoo import fields, models, api

class AmenityTypes(models.Model):
    _name = "amenity.types"
    _description = "Amenity Types"

    amenity_type_id = fields.Many2one("amenity.types", "Types")
    categ_id = fields.Many2one('product.category', "Product Category", delegate=True, copy=False, ondelete="cascade")

    def write(self, vals):
        if "amenity_type_id" in vals:
            amenity_categ = self.env["amenity.type"].browse(vals['amenity_type_id'])
            vals.update({"categ_id": amenity_categ.categ_id.id})
        return super(AmenityTypes, self).write(vals)

    def unlink(self):
        rec = self.env["product.category"].sudo().browse(self.categ_id.id)
        rec.unlink()
        return super(AmenityTypes, self).unlink()

class HotelAmenity(models.Model):
    _name = "hotel.amenity"
    _description = "Hotel Amenities"

    product_id = fields.Many2one('product.product', "Amenities", required=True, delegate=True, ondelete="cascade", )
    type_id = fields.Many2one("amenity.types", "Amenity Type", required=True, ondelete="restrict", )
    manager_id = fields.Many2one("res.users", string='Manager')

    @api.model
    def create(self, vals):
        if "type_id" in vals:
            prod = self.env["amenity.types"].browse(vals["type_id"])
            vals.update({"categ_id": prod.categ_id.id})
        return super(HotelAmenity, self).create(vals)

    def write(self, vals):
        if "type_id" in vals:
            prod = self.env["amenity.types"].browse(vals["type_id"])
            vals.update({"categ_id": prod.categ_id.id})
        return super(HotelAmenity, self).write(vals)

    def unlink(self):
        rec = self.env["product.product"].sudo().browse(self.product_id.id)
        rec.unlink()
        return super(HotelAmenity, self).unlink()
