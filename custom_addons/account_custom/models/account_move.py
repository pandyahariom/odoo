# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

# Note to ME: Add Test cases for all tasks
class AccountMove(models.Model):
    _inherit = "account.move"

    ##Task-1 : Chatter Message on New Invoice
    @api.model
    def create(self, vals):
        result = super(AccountMove, self).create(vals)

        if "partner_id" in vals:
            partner = self.env["res.partner"].browse(vals.get("partner_id"))
            message = f"Invoice: <b><a href=\"#\" data-oe-model=\"account.move\" data-oe-id=\"{result.id}\">{vals['name']}</a></b>{vals['name']} is created for {partner.name}"
            partner.message_post(body=_(message))

        return result

    def write(self, vals):

        dictionary = dict(self._fields["state"].selection)

        for record in self:

            ##Task-2 Chatter Message on state change
            if "state" in vals:

                old_state = record.state
                new_state = vals["state"]

                message = f"Invoice: <b><a href=\"#\" data-oe-model=\"account.move\" data-oe-id=\"{record.id}\">{record['name']}</a></b> State Updated from {dictionary[old_state]} to {dictionary[new_state]}"
                record.partner_id.message_post(body=_(message))

            ##Task-3 Chatter Message on field change (Invoice Date and Currency Type)

            # Task-3(a) : Check on Invoice Date
            if "invoice_date" in vals:
                new_invoice_date = vals["invoice_date"]

                # Check if current write is 1st write of invoice_date
                if record["invoice_date"]:
                    old_invoice_date = record.invoice_date.strftime("%Y-%m-%d")
                else:
                    old_invoice_date = "No Date"

                if old_invoice_date != new_invoice_date:
                    message = f"Invoice: <b><a href=\"#\" data-oe-model=\"account.move\" data-oe-id=\"{record.id}\">{record['name']}</a></b> Invoice Date Updated from {old_invoice_date} to {new_invoice_date}"
                    record.partner_id.message_post(body=_(message))

            # Task-3(b) : Check on Currency(currency_id)
            if "currency_id" in vals:
                new_currency = (
                    record.env["res.currency"].browse(vals.get("currency_id")).name
                )

                # Check if current write is 1st write of currency_id
                if record.currency_id:
                    old_currency = record.currency_id.name
                else:
                    old_currency = "Empty"

                message = f"Invoice: <b><a href=\"#\" data-oe-model=\"account.move\" data-oe-id=\"{record.id}\">{record['name']}</a></b> Currency Updated from {old_currency} to {new_currency}"
                record.partner_id.message_post(body=_(message))

        result = super(AccountMove, self).write(vals)
        return result
