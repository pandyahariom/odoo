# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit='sale.order'

    @api.model
    def create(self, vals):
        result = super(SaleOrder, self).create(vals)
        if 'partner_id' in vals:
          partner = self.env['res.partner'].browse(vals.get('partner_id'))
          order=self.env['sale.order'].browse(vals.get('order_id'))
          print(order)
          message="Sales Order:"+vals['name']+" is created for "+partner.name
          partner.message_post(body=_(message))
        return result