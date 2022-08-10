# -*- coding: utf-8 -*-
# from odoo import http


# class Realestate(http.Controller):
#     @http.route('/realestate/realestate', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/realestate/realestate/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('realestate.listing', {
#             'root': '/realestate/realestate',
#             'objects': http.request.env['realestate.realestate'].search([]),
#         })

#     @http.route('/realestate/realestate/objects/<model("realestate.realestate"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('realestate.object', {
#             'object': obj
#         })
