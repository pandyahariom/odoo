from odoo import fields,api,models,_
from odoo.exceptions import UserError
from odoo import Command
class realestate(models.Model):
    _inherit="realestate.property"
    def action_sold(self):
        super_call=super().action_sold()

        for property in self:
            journal = self.env["account.move"].with_context(default_move_type="out_invoice")._get_default_journal()
            new_invoice={
                "partner_id": property.buyer_id.id,
                "move_type": "out_invoice",
                "journal_id": journal.id,
                "invoice_line_ids": [
                     Command.create(
                        {
                            "name": property.name,
                            "quantity": 1.0,
                            "price_unit": property.selling_price * 6.0 / 100.0,
                        }
                        ),
                    Command.create(
                        {
                            "name": "Administrative Fees",
                            "quantity": 1.0,
                            "price_unit": 100.0,
                        }
                        )
                    ]
                        
                }
            self.env["account.move"].create(new_invoice) #Create need dictionary as argument
        
        return super_call
       