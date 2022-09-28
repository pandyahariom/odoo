from email.policy import default
from odoo import models, fields, api, _
from dateutil.relativedelta import relativedelta
from datetime import datetime
from odoo.exceptions import ValidationError, UserError
from odoo.tools.float_utils import float_compare, float_is_zero


class realestate_property_offer(models.Model):
    _name = "realestate.property.offer"
    _description = "Real Estate Property Offers"
    _order = "price desc"
    price = fields.Float(string="Offer Price")
    status = fields.Selection(
        selection=[("accepted", "Accepted"), ("refused", "Refused")], copy=False
    )
    partner_id = fields.Many2one(comodel_name="res.partner", required=True)
    property_id = fields.Many2one(comodel_name="realestate.property", required=True)
    disable_button = fields.Boolean(default=True)
    disable_accept_button = fields.Boolean(default=False)
    validity = fields.Integer(string="Validity(days)", default=7)
    date_deadline = fields.Date(
        string="Deadline", compute="_compute_deadline", inverse="_inverse_deadline"
    )

    @api.depends("validity", "create_date")
    def _compute_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date + relativedelta(
                    days=record.validity
                )
            else:
                record.date_deadline = fields.Date.today() + relativedelta(
                    days=record.validity
                )

    def _inverse_deadline(self):
        for record in self:
            # create_date is datetime object whereas date_deadline is date object
            # next code will convert create_date object to date object and store it in create
            create = record.create_date.date()
            # print("\n\nCREATE:::",create,type(create),":",record.date_deadline,type(record.date_deadline),"\n")

            # difference between two date object will give timedelta. We can extract total days from it using .days
            record.validity = abs((record.date_deadline - create).days)

    def action_accept(self):
        for record in self:
            record.status = "accepted"
            record.property_id.state = "oa"
            record.disable_button = False
            record.disable_accept_button = True
            record.property_id.selling_price = record.price
            record.property_id.buyer_id = record.partner_id
            message = f'Congratulations {record.partner_id.name}!! Your Offer for property <b><a href="#" data-oe-model="realestate.property" data-oe-id="{record.property_id.id}">{record.property_id.name}</a></b> is accepted.'
            record.partner_id.message_post(body=_(message))
        # Disable accept and reject buttons for all records
        record_set = self.env["realestate.property.offer"].search(
            [("property_id", "=", self.property_id.id)]
        )
        for record in record_set:
            if record.id != self.id:
                record.disable_accept_button = True
                message = f'Sorry {record.partner_id.name}!! Your Offer for property <b><a href="#" data-oe-model="realestate.property" data-oe-id="{self.property_id.id}">{self.property_id.name}</a></b> is not under consideration.'
                record.partner_id.message_post(body=_(message))
        return True

    def action_reject(self):
        for record in self:
            record.status = "refused"
            record.property_id.state = "or"
            record.property_id.selling_price = False
            record.property_id.buyer_id = False
            record.disable_button = True
        record_set = self.env["realestate.property.offer"].search([])
        for record in record_set:
            record.disable_accept_button = False
            # record.disable_button = True
            # if record.id != self.id:
            #    record.status=False
        return True

    _sql_constraints = [
        (
            "check_offer_price",
            "CHECK(price > 0 )",
            "The Offer Price must be strictly positive",
        ),
    ]

    @api.constrains("price", "property_id.expected_price")
    def _check_price_difference(self):
        for record in self:
            if not float_is_zero(record.price, precision_digits=2):
                value2 = record.property_id.expected_price * 0.9
                ans = float_compare(record.price, value2, precision_digits=2)
                if ans < 1:
                    raise ValidationError(
                        _(
                            "Selling price (%.2f) cannot be lower than 90 percent of the expected price(%.2f)"
                        )
                        % (record.price, value2)
                    )

    @api.model
    def create(self, vals):
        if vals.get("property_id") and vals.get("price"):
            prop = self.env["realestate.property"].browse(vals["property_id"])
            # Check if the offer is higher than all existing offers
            if prop.offer_ids:
                max_offer = max(prop.mapped("offer_ids.price"))
                if (
                    float_compare(vals["price"], max_offer, precision_rounding=0.01)
                    <= 0
                ):
                    raise UserError("The offer must be higher than %.2f" % max_offer)

            # There is no previous offer and the current offer is the first one
            else:
                prop.state = "or"
        return super().create(vals)
