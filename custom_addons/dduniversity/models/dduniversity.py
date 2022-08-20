# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class dduniversity(models.Model):
#     _name = 'dduniversity.dduniversity'
#     _description = 'dduniversity.dduniversity'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
