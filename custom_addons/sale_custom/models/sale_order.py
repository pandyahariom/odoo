# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


# Note to ME: Add Test cases for all tasks
class SaleOrder(models.Model):
    _inherit = "sale.order"

    ##Task-1 : Chatter Message on New Order
    @api.model
    def create(self, vals):
        result = super(SaleOrder, self).create(vals)

        if "partner_id" in vals:
            partner = self.env["res.partner"].browse(vals.get("partner_id"))

            message = f"Sales Order: <b><a href=\"#\" data-oe-model=\"sale.order\" data-oe-id=\"{result.id}\">{vals['name']}</a></b> is created for {partner.name}"
            partner.message_post(body=_(message))

        return result

    def write(self, vals):

        dictionary = dict(self._fields["state"].selection)

        for record in self:

            ##Task-2 Chatter Message on state change
            if "state" in vals:

                old_state = record.state
                new_state = vals["state"]

                message = f"Sales Order: <b><a href=\"#\" data-oe-model=\"sale.order\" data-oe-id=\"{record.id}\">{record['name']}</a></b> State Updated from {dictionary[old_state]} to {dictionary[new_state]}"
                record.partner_id.message_post(body=_(message))

            ##Task-3 Chatter Message on field change (Expiration and Pricelist)

            # Task-3(a) : Check on Expiration(validity_date)
            if "validity_date" in vals:
                new_validity = vals["validity_date"]

                # Check if current write is 1st write of validity_date
                if record["validity_date"]:
                    # self['validity_date'] is datetime object.
                    # Fetching Date string similar to format of new_validity
                    old_validity = record.validity_date.strftime("%Y-%m-%d")
                else:
                    old_validity = "No Date"

                if old_validity != new_validity:
                    message = f"Sales Order: <b><a href=\"#\" data-oe-model=\"sale.order\" data-oe-id=\"{record.id}\">{record['name']}</a></b> Expiration Date Updated from {old_validity} to {new_validity}"
                    record.partner_id.message_post(body=_(message))

            # Task-3(b) : Check on Pricelist(pricelist_id)
            if "pricelist_id" in vals:
                new_pricelist = (
                    record.env["product.pricelist"]
                    .browse(vals.get("pricelist_id"))
                    .name
                )

                # Check if current write is 1st write of validity_date
                if record.pricelist_id:
                    old_pricelist = record.pricelist_id.name
                else:
                    old_pricelist = "Empty"

                message = f"Sales Order: <b><a href=\"#\" data-oe-model=\"sale.order\" data-oe-id=\"{record.id}\">{record['name']}</a></b> Pricelist Updated from {old_pricelist} to {new_pricelist}"
                record.partner_id.message_post(body=_(message))

        result = super(SaleOrder, self).write(vals)
        return result
