# -*- coding: utf-8 -*-
# from odoo import http


# class RealestateAccount(http.Controller):
#     @http.route('/realestate_account/realestate_account', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/realestate_account/realestate_account/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('realestate_account.listing', {
#             'root': '/realestate_account/realestate_account',
#             'objects': http.request.env['realestate_account.realestate_account'].search([]),
#         })

#     @http.route('/realestate_account/realestate_account/objects/<model("realestate_account.realestate_account"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('realestate_account.object', {
#             'object': obj
#         })
