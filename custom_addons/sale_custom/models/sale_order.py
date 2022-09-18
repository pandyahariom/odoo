# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit='sale.order'
    
    #Task-1
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
    
    #Task-3
    def write(self,vals):
      if('validity_date' in vals):
        new_validity=vals['validity_date']
        
        #Check if current write is 1st write of validity_date
        if(self['validity_date']):
          #self['validity_date'] is datetime object. 
          #Fetching Date string similar to format of new_validity
          old_validity=self['validity_date'].strftime("%Y-%m-%d")
        else:
          old_validity="No Date"

        if(old_validity != new_validity):
         message="Sales Order:"+self['name']+" Expiration Date Updated from "+old_validity +" to "+new_validity
         self.partner_id.message_post(body=_(message))

      result=super(SaleOrder,self).write(vals)
      return result

    #Task-2: Only update on cancel state
    # def _action_cancel(self):
    #   old_state=self.state
    #   dictionary=dict(self._fields['state'].selection)
    #   result=super(SaleOrder,self)._action_cancel()
    #   for order in self:
    #         partner=order.partner_id
    #         message="Sales Order:"+self['name']+" State Updated from "+dictionary[old_state] +" to "+dictionary[self.state]
    #         partner.message_post(body=_(message))
    #   return result
    
    #Task-2: With Some Bug
    # @api.onchange('state')
    # def _onchange_state(self):
    #   if(self.state != 'draft'):
    #     partner = self.env['res.partner'].browse(self.env.context.get('partner_id'))
    #     message="Sales Order:"+self['name']+"+ State Updated to "+self.state
    #     partner.message_post(body=_(message))
    #   else:
    #     print("Draft State")
    
    def write(self,vals):
      if('state' in vals):
        dictionary=dict(self._fields['state'].selection)

        new_state=vals['state']
        #Check if current write is 1st write of state(i.e. draft)
        if(self['state']):
          old_state=self['state']
        else:
          old_state=""

        message="Sales Order:"+self['name']+" State Updated from "+dictionary[old_state] +" to "+dictionary[new_state]
        self.partner_id.message_post(body=_(message))

      result=super(SaleOrder,self).write(vals)
      return result
