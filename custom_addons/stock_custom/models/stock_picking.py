# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

# Note to ME: Add Test cases for all tasks
class StockPicking(models.Model):
    _inherit = "stock.picking"

    ##Task-1 : Chatter Message on New DO
    @api.model
    def create(self, vals):
        result = super(StockPicking, self).create(vals)

        if "partner_id" in vals:
            partner = self.env["res.partner"].browse(vals.get("partner_id"))
            message = f"Delivery Order: <b><a href=\"#\" data-oe-model=\"stock.picking\" data-oe-id=\"{result.id}\">{vals['name']}</a></b> is created for {partner.name}"
            partner.message_post(body=_(message))

        return result

    def write(self, vals):

        for record in self:

            ##Task-3 Chatter Message on field change Scheduled Date

            if "scheduled_date" in vals:
                new_scheduled_date = str(vals["scheduled_date"].split()[0])

                # Check if current write is 1st write of scheduled_date
                if record.scheduled_date:
                    old_scheduled_date = record.scheduled_date.strftime("%Y-%m-%d")
                else:
                    old_scheduled_date = "No Date"

                if old_scheduled_date != new_scheduled_date:
                    message = f"Delivery Order: <b><a href=\"#\" data-oe-model=\"stock.picking\" data-oe-id=\"{record.id}\">{record['name']}</a></b> Invoice Date Updated from {old_scheduled_date} to {new_scheduled_date}"
                    record.partner_id.message_post(body=_(message))

        result = super(StockPicking, self).write(vals)
        return result

    ##Task-2 Chatter Message on state change
    def _compute_state(self):
        dictionary = dict(self._fields["state"].selection)
        old_state = self.state
        super(StockPicking, self)._compute_state()
        new_state = self.state
        if old_state and old_state != new_state:
            message = f"Delivery Order: <b><a href=\"#\" data-oe-model=\"stock.picking\" data-oe-id=\"{self.id}\">{self['name']}</a></b> State Updated from {dictionary[old_state]} to {dictionary[new_state]}"
            self.partner_id.message_post(body=_(message))
